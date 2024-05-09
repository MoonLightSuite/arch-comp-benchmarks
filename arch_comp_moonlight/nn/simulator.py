
from ..utils import unpack
from ..matlab import Matlab
from ..baseline.simulator import Simulator
import os
import numpy as np
from typing import TypedDict

dir = os.path.dirname(os.path.realpath(__file__))

SimulationParams = TypedDict(
    'SimulationParams', {'length': int, 'input': list[float]}
)


class NNSimulator(Simulator):

    def __init__(self, model_path: str) -> None:
        os.chdir(model_path)
        self.matlab = Matlab()

    def run(self, params: SimulationParams) -> dict:
        print(f"Params: {params}")
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

    def pass_input(self, params: dict) -> None:
        # self.matlab.eval("t__ = linspace(0, 40, 10)';", nargout=0)
        length = params.pop('length')
        PARAMS = {'u1': 1.7371798557979203,
                  'u2': 2.0007661359736426, 'u3': 1.8324732072952215}

        self.matlab.eval(f"t__ = linspace(0, 40, {length})';")
        self.matlab.eval(f"u__ = {unpack(PARAMS )};")
        self.matlab.eval("u = [t__, u__];")

        # t = self.matlab.eval("u;", nargout=1)
        # print(t)

    def prepare_output(self) -> dict:
        yout = self.matlab.eval("yout;", 1)  # type: ignore
        tout = self.matlab.eval("tout;", 1)  # type: ignore
        xin = self.matlab.eval("xin;", 1)  # type: ignore
        # tout = self.eval("tout", outputs=1)

        times = np.asarray(tout).transpose().tolist()[0]

        pos = np.asarray(yout).transpose()[0].tolist()  # 40005
        ref = np.asarray(xin)[0]  # 4001
        ref = np.repeat(ref, 10)[:-5].tolist()  # 40010

        return {'times': times, 'values': list(zip(pos, ref))}

    def reset_engine(self) -> None:
        self.eval("clear all")
