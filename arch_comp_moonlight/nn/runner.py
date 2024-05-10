from os import path
from logging import getLogger
from typing import TypedDict

from ..experiment.iteration import Iteration


from .simulator import NNSimulator
from ..nn.monitor import NNMonitor, Trace
from ..baseline.optimizer import Optimizer
from ..experiment.configuration import Configuration
from ..experiment.runner import Runner
from ..optimizer.turbo import Turbo
import numpy as np

dir = path.dirname(path.realpath(__file__))

EXP_DIR = f"{dir}/../../benchmarks/NN - Magnet"

logger = getLogger(__name__)


nn_config = Configuration(
    exp_name="NN",
    exp_batch_name="TURBO",
    optimization_iterations=7,
    hyper_params={
        'i': [3]
    },
    simulator_repetitions=1,
    # Experiment-specific
    formula_name="nn",
    optimization_lower_bounds=0.0,
    optimization_upper_bounds=1.0,
)


Params = TypedDict('Params', {'length': int})

class NNRunner(Runner[Params]):
    def __init__(self, config: Configuration):
        super().__init__(config)
        logger.debug(config)
        self.simulator = NNSimulator(model_path=EXP_DIR)
        self.monitor = NNMonitor()

    def single_run(self, params: dict[str, np.float64]) -> np.float64:
        logger.info(f"Running simulator with params: {params}")
        trace: Trace = self.simulator.run(params)
        logger.info
        robustness = self.monitor.run(trace, self.config.formula_name)
        value = robustness.transpose()[1][0]
        logger.info(f"Robustness: {value}")
        return value

    def optimizer_run(self, iteration: Iteration[Params]) -> None:
        logger.info(f"Repetition n.: {iteration['n']}")
        length = iteration["params"]["length"]
        lower_bounds = self.config.optimization_lower_bounds * np.ones(length)
        upper_bounds = self.config.optimization_upper_bounds * np.ones(length)
        self.optimizer = Turbo(
            optimization_iters=self.config.optimization_iterations,
            lower_bounds=lower_bounds,
            upper_bounds=upper_bounds
        )
        value = self.optimizer.optimize(self.single_run)
        return value
