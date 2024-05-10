
from ..experiment.trace import Trace
from ..utils import unpack
from ..matlab import Matlab
from ..baseline.simulator import Simulator
import os
import numpy as np
from logging import getLogger

logger = getLogger(__name__)

dir = os.path.dirname(os.path.realpath(__file__))

TraceValue = tuple[np.float64, np.float64]


class NNSimulator(Simulator[TraceValue]):
    def __init__(self, model_path: str) -> None:
        self.matlab = Matlab()
        self.matlab.eval(f"addpath('{model_path}');")

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

        return {'times': times, 'values': list(zip(error, pos))}
