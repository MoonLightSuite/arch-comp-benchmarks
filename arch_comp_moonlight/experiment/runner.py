from ..utils import nested_loops_from_dict_of_lists
from abc import ABC, abstractmethod
from typing import Any
from arch_comp_moonlight.experiment.configuration import Configuration
import logging
from .store import Store

logger = logging.getLogger(__name__)


class Runner(ABC):
    """
    Runner is an abstract class that defines the interface for running an experiment.

    Attributes:
    -   config: the configuration for the experiment
    """

    def __init__(self, config: Configuration):
        """Sets the input parameters for running an experiment."""
        self.config = config
        self.store = Store()

        logger.info(
            f"Running {config.exp_name} experiment for {config.exp_repetitions} repetitions.")

    def run_batch(self) -> None:
        """Runs the experiment for all the parameters combinations."""
        last_iteration = self.config.exp_repetitions + 1
        self.config.other_params['n'] = list(range(1, last_iteration))

        params = self.config.other_params
        nested_loops_from_dict_of_lists(params, self.optimizer_run)

    @abstractmethod
    def single_run(self, params: dict[str, Any]) -> None:
        """Abstract: Runs the simulator and monitor for a single parameter combination."""
        raise NotImplementedError

    @abstractmethod
    def optimizer_run(self, iter_params) -> None:
        """Runs the optimizer for a single parameter combination.
        The optimizer will call the single_run method to run the simulator and monitor as much as needed.
        """
        raise NotImplementedError
