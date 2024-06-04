
from arch_comp_moonlight.experiment.configuration import Configuration
from arch_comp_moonlight.experiment.store import LineKey, Store
from arch_comp_moonlight.experiment.trace import Trace
from arch_comp_moonlight.matlab import Matlab
from arch_comp_moonlight.baseline.simulator import Simulator
import os
import numpy as np
from logging import getLogger

logger = getLogger(__name__)

dir = os.path.dirname(os.path.realpath(__file__))

TraceValue = tuple[np.float64, np.float64, np.float64]


class PMSimulator(Simulator[TraceValue]):
    def __init__(self, config: Configuration, store: Store) -> None:
        super().__init__(config=config, store=store)
        self.matlab = Matlab()
        self.matlab.eval(f"addpath('{config.simulator_model_path}');")
        self._init()

    def run(self, params: dict[str, np.float64]) -> Trace[TraceValue]:
        self._pass_input(params)
        self.matlab.eval("[tout, yout] = run_pm(u_1);")
        return self._prepare_output()

    def _init(self) -> None:
        self.matlab.eval(f"addpath('{dir}');")

    def _pass_input(self, params: dict[str, np.float64]) -> None:
        logger.info("Params: ", params)
        self.matlab.eval(f"u_1 = {params['u1']};")
        # self.matlab.eval(f"T = 15;")
        # self.matlab.eval(f"u = [0' u_1'];")

    def _prepare_output(self) -> Trace[TraceValue]:
        tout = self.matlab.eval("tout;", outputs=1)
        u1 = self.matlab.eval("u_1;", outputs=1)
        y = self.matlab.eval("yout;", outputs=1)

        times = np.asarray(tout).transpose().tolist()[0]
        [y1, y2, y3] = np.asarray(y).transpose().tolist()
        values = list(zip(y1, y2, y3))

        self.store.store(LineKey.time, times[-1])
        self.store.store(LineKey.input, f"{u1}")

        return {'times': times, 'values': values}
