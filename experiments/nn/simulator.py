
from arch_comp_moonlight.experiment.configuration import Configuration
from arch_comp_moonlight.experiment.store import LineKey, Store
from arch_comp_moonlight.experiment.trace import Trace
from arch_comp_moonlight.utils import unpack, list_of_lists_to_matlab_matrix
from arch_comp_moonlight.matlab import Matlab
from arch_comp_moonlight.baseline.simulator import Simulator
import os
import numpy as np
from logging import getLogger
from typing import Any

logger = getLogger(__name__)

dir = os.path.dirname(os.path.realpath(__file__))

TraceValue = tuple[np.float64, np.float64]


class NNSimulator(Simulator[TraceValue]):
    t_end = 40

    def __init__(self, config: Configuration, store: Store) -> None:
        super().__init__(config=config, store=store)
        self.matlab = Matlab()
        self.matlab.eval(f"addpath('{config.simulator_model_path}');")
        self._init()

    def raw_run(self, params: dict[str, np.float64]) -> Trace[TraceValue]:
        self._pass_input(params)
        self.matlab.eval("[tout, yout, xin] = run_neural(u, T);")
        return self._prepare_output()

    def _init(self) -> None:
        self.matlab.eval(f"addpath('{dir}');")
        self.matlab.eval("u_ts = 0.001;")
        self.matlab.eval("alpha = 0.005;")
        self.matlab.eval("beta = 0.03;")
        self.matlab.eval(f"T = {self.t_end};")

    def _pass_input(self, params: dict[str, np.float64]) -> None:
        length = len(params.keys())
        self.matlab.eval(f"t__ = linspace(0, {self.t_end}, {length})';")
        self.matlab.eval(f"u__ = {unpack(params)};")
        self.matlab.eval("u = [t__, u__];")

    def _prepare_output(self) -> Trace[TraceValue]:
        u = self.matlab.eval("u;", outputs=1)
        tout = self.matlab.eval("tout;", outputs=1)
        yout = self.matlab.eval("yout;", outputs=1)

        times = np.asarray(tout).transpose().tolist()[0]
        [error, pos] = np.asarray(yout).transpose().tolist()
        values: list[tuple[Any, Any]] = list(zip(error, pos))

        self.store.store(LineKey.stop_time, times[-1])
        self.store.store(LineKey.input, f"{list_of_lists_to_matlab_matrix(u)}")

        return {'times': times, 'values': values}
