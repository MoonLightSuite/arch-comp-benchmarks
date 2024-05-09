from os import path
from logging import getLogger
from typing import Any, Callable

from .simulator import NNSimulator
from ..nn.monitor import NNMonitor, Trace
from ..baseline.optimizer import Optimizer
from ..experiment.configuration import Configuration
from ..experiment.runner import Runner

dir = path.dirname(path.realpath(__file__))

EXP_DIR = f"{dir}/../../benchmarks/NN - Magnet"

logger = getLogger(__name__)


nn_config = Configuration(
    exp_name="NN",
    exp_batch_name="TURBO",
    random_samples=10,  # TODO: check the goal of this parameter
    optimization_iterations=1,
    other_params={
        'i': [1]
    },
    formula_name="nnx",
    simulator_repetitions=1
)


class NNRunner(Runner):
    def __init__(self, config: Configuration):
        super().__init__(config)
        logger.debug(config)
        self.simulator = NNSimulator(model_path=EXP_DIR)
        self.monitor = NNMonitor()
        self.optimizer = DumbOptimizer({})

    def single_run(self, params: dict[str, Any]) -> float:
        trace: Trace = self.simulator.run(params)

        robustness = self.monitor.run(trace, self.config.formula_name)
        value = robustness.transpose()[1][0]
        return value

    def optimizer_run(self, iter_params) -> None:
        self.optimizer.optimize(iter_params, self.single_run)
        # n = iter_params['n']
        # i = iter_params['input_size']
        # a = iter_params['alpha']
        # b = iter_params['beta']
        # print(f"Repetition n.: {n}")
        # opt = self.config.optimizer({**vars(self.config), **iter_params})
        # opt.optimize(self.single_run({}))


class DumbOptimizer(Optimizer):
    def __init__(self, params: dict[str, Any]):
        super().__init__("test.txt")

    def optimize(self, params: Any,
                 single_run: Callable[[dict], float]) -> None:
        logger.info("Optimizer RUN")
        single_run(params)
