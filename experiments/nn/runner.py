from os import path
from logging import getLogger
from typing import TypedDict
import numpy as np

from arch_comp_moonlight.experiment.iteration import Iteration
from arch_comp_moonlight.monitors.moonlight import Moonlight
from arch_comp_moonlight.experiment.trace import Trace
from arch_comp_moonlight.experiment.configuration import Configuration
from arch_comp_moonlight.experiment.runner import Runner
from arch_comp_moonlight.optimizers.turbo import Turbo
from .simulator import NNSimulator, TraceValue

logger = getLogger(__name__)


# TODO: change simulations to report the first falsifying one


Params = TypedDict('Params', {'length': int})


class NNRunner(Runner[Params]):
    def __init__(self, config: Configuration):
        super().__init__(config)
        logger.debug(config)
        self.simulator = NNSimulator(config, self.store)
        self.monitor = Moonlight[TraceValue](spec=config.monitor_spec)

    def single_run(self, params: dict[str, np.float64]) -> np.float64:
        logger.info(f"Running simulator with params: {params}")
        trace: Trace[TraceValue] = self.simulator.run(params)
        robustness = self.monitor.run(trace, self.config.monitor_formula_name)
        value = robustness.transpose()[1][0]
        logger.info(f"Robustness: {value}")
        return value

    def prepare_optimizer(self, iteration: Iteration[Params]) -> None:
        logger.info(f"Repetition n.: {iteration['n']}")
        logger.info(f"Iteration params: {iteration}")
        length = iteration["params"]["length"]
        lower_bounds = self.config.optimization_lower_bounds * np.ones(length)
        upper_bounds = self.config.optimization_upper_bounds * np.ones(length)

        self.optimizer = Turbo(
            config=self.config,
            store=self.store,
            lower_bounds=lower_bounds,
            upper_bounds=upper_bounds
        )
