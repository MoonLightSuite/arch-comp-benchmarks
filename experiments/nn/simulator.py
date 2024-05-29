
from arch_comp_moonlight.experiment.configuration import Configuration
from arch_comp_moonlight.experiment.store import LineKey, Store
from arch_comp_moonlight.experiment.trace import Trace
from arch_comp_moonlight.utils import unpack
from arch_comp_moonlight.matlab import Matlab
from arch_comp_moonlight.baseline.simulator import Simulator
import os
import numpy as np
from logging import getLogger

logger = getLogger(__name__)

dir = os.path.dirname(os.path.realpath(__file__))

TraceValue = tuple[np.float64, np.float64]


class NNSimulator(Simulator[TraceValue]):
    def __init__(self, config: Configuration, store: Store) -> None:
        super().__init__(config=config, store=store)
        self.matlab = Matlab()
        self.matlab.eval(f"addpath('{config.simulator_model_path}');")

    def run(self, params: dict[str, np.float64]) -> Trace[TraceValue]:
        self.init()
        self.pass_input(params)

        self.matlab.eval("[tout, yout, xin] = run_neural(u, T);")

        return self.prepare_output()

    def init(self) -> None:
        self.matlab.eval(f"addpath('{dir}');")
        self.matlab.eval("u_ts = 0.001;")
        self.matlab.eval("alpha = 0.005;")
        self.matlab.eval("beta = 0.03;")
        self.matlab.eval("T = 40;")

    def pass_input(self, params: dict[str, np.float64]) -> None:
        length = len(params.keys())
        self.matlab.eval(f"t__ = linspace(0, 40, {length})';")
        self.matlab.eval(f"u__ = {unpack(params)};")
        self.matlab.eval("u = [t__, u__];")

    def prepare_output(self) -> Trace[TraceValue]:
        yout = self.matlab.eval("yout;", outputs=1)
        tout = self.matlab.eval("tout;", outputs=1)

        times = np.asarray(tout).transpose().tolist()[0]
        [error, pos] = np.asarray(yout).transpose().tolist()
        values = list(zip(error, pos))

        self.store.store(LineKey.time, times[-1])

        u = self.matlab.eval("u;", outputs=1)
        self.store.store(LineKey.input, f"{u}")

        return {'times': times, 'values': values}
