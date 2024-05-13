from typing import TypeVar, Generic

from ..baseline.optimizer import Optimizer
from ..experiment.iteration import Iteration
from ..utils import nested_loops_from_dict_of_lists
from abc import ABC, abstractmethod
from typing import Any
from ..experiment.configuration import Configuration
import logging
from .store import LineKey, Store
import numpy as np
import os

logger = logging.getLogger(__name__)

T = TypeVar("T")


class Runner(ABC, Generic[T]):
    """
    Runner is an abstract class that defines the interface for running an experiment.

    Attributes:
    -   config: the configuration for the experiment
    """

    def __init__(self, config: Configuration):
        """Sets the input parameters for running an experiment."""
        self.config = config
        output_dir = f"output/{config.exp_name}/{config.exp_batch_name}"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        params = self._hyper_params_to_string(config.simulator_hyper_params)
        output_file = f"{config.monitor_formula_name}{params}_results.csv"
        self.store = Store(f"{output_dir}/{output_file}")

        logger.info(
            f"Running {config.exp_name} experiment for {config.exp_repetitions} repetitions.""")

        self.store.store(LineKey.system, config.exp_name)
        self.store.store(LineKey.instance, config.exp_instance_number)

    def _hyper_params_to_string(self, params: dict[str, Any]) -> str:
        """Converts the hyper parameters to a string."""
        return '_'.join([f"_{k}-{v}" for k, v in params.items()])

    def run_batch(self) -> None:
        """Runs the experiment for all the parameters combinations."""
        last_iteration = self.config.exp_repetitions + 1
        self.config.simulator_hyper_params['n'] = list(
            range(1, last_iteration))

        params = self.config.simulator_hyper_params
        nested_loops_from_dict_of_lists(
            params, self.optimizer_run)  # type: ignore

    @abstractmethod
    def single_run(self, params: dict[str, np.float64]) -> np.float64:
        """Abstract: Runs the simulator and monitor for a single parameter combination."""
        raise NotImplementedError

    @abstractmethod
    def prepare_optimizer(self, iteration: Iteration[T]) -> None:
        """Prepares the optimizer to run for a single parameter combination.
        The optimizer will call the single_run method to run the simulator and monitor as much as needed.
        """
        raise NotImplementedError

    def optimizer_run(self, iteration: Iteration[T]) -> None:
        """Runs the optimizer for a single parameter combination."""
        self.optimizer: Optimizer
        self.prepare_optimizer(iteration)
        self.optimizer.optimize(self._simulator)
        self.store.save()

    def _simulator(self, params: dict[str, np.float64]) -> np.float64:
        """Runs the simulator and monitor for a single parameter combination."""
        robustness = self.single_run(params)
        self.store.store(LineKey.robustness, robustness)
        if robustness < 0:
            self.store.store(LineKey.falsified, "yes")
        else:
            self.store.store(LineKey.falsified, "no")
        return robustness
