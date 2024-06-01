from logging import getLogger
from typing import TypedDict
import numpy as np

from arch_comp_moonlight.experiment.configuration import Configuration
from arch_comp_moonlight.experiment.iteration import Iteration
from arch_comp_moonlight.experiment.runner import Runner
from arch_comp_moonlight.experiment.trace import Trace
from arch_comp_moonlight.monitors.moonlight import Moonlight
from arch_comp_moonlight.optimizers.turbo import Turbo
from experiments.f16.simulator import F16Simulator, TraceValue

logger = getLogger(__name__)

Params = TypedDict('Params', {
    'roll': float,
    'pitch': float,
    'yaw': float,
})

# - x_01: pi/4-pi/20 <= x_01 <= pi/4+pi/30
# - x_02: -2/5*pi+0 <= x_02 <= -2/5*pi+pi/20
# - x_03: -pi/4-pi/8 <= x_03 <= -pi/4+pi/8


class F16Runner(Runner[Params]):
    def __init__(self, config: Configuration):
        super().__init__(config)
        self.simulator = F16Simulator(config, self.store)
        self.monitor = Moonlight[TraceValue](spec=config.monitor_spec)

    def single_run(self, params: dict[str, np.float64]) -> np.float64:
        trace: Trace[TraceValue] = self.simulator.run(params)
        robustness = self.monitor.run(trace, self.config.monitor_formula_name)
        value = robustness.transpose()[1][0]
        return value

    def prepare_optimizer(self, iteration: Iteration[Params]) -> None:
        self.optimizer = Turbo(
            config=self.config,
            store=self.store,
            lower_bounds=np.array(self.config.optimization_lower_bounds),
            upper_bounds=np.array(self.config.optimization_upper_bounds)
        )
