from typing import TypeVar, Generic

from arch_comp_moonlight.experiment.iteration import Iteration
from ..utils import nested_loops_from_dict_of_lists
from abc import ABC, abstractmethod
from typing import Any
from arch_comp_moonlight.experiment.configuration import Configuration
import logging
from .store import Store
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
        params = self._hyper_params_to_string(config.hyper_params)
        output_file = f"{config.formula_name}{params}_results.csv"
        self.store = Store(f"{output_dir}/{output_file}")

        logger.info(
            f"Running {config.exp_name} experiment for {config.exp_repetitions} repetitions.")

    def _hyper_params_to_string(self, params: dict[str, Any]) -> str:
        """Converts the hyper parameters to a string."""
        return '_'.join([f"_{k}-{v}" for k, v in params.items()])

    def run_batch(self) -> None:
        """Runs the experiment for all the parameters combinations."""
        last_iteration = self.config.exp_repetitions + 1
        self.config.hyper_params['n'] = list(range(1, last_iteration))

        params = self.config.hyper_params
        nested_loops_from_dict_of_lists(
            params, self.optimizer_run)  # type: ignore

    @abstractmethod
    def single_run(self, params: dict[str, np.float64]) -> np.float64:
        """Abstract: Runs the simulator and monitor for a single parameter combination."""
        raise NotImplementedError

    @abstractmethod
    def optimizer_run(self, iteration: Iteration[T]) -> None:
        """Runs the optimizer for a single parameter combination.
        The optimizer will call the single_run method to run the simulator and monitor as much as needed.
        """
        raise NotImplementedError
