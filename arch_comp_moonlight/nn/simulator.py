
from ..utils import unpack
from ..matlab import Matlab
from ..baseline.simulator import Simulator
import os
import numpy as np
from typing import TypedDict
from logging import getLogger

logger = getLogger(__name__)

dir = os.path.dirname(os.path.realpath(__file__))

SimulationParams = TypedDict(
    'SimulationParams', {'length': int, 'inputs': list[float]}
)


class NNSimulator(Simulator):

    def __init__(self, model_path: str) -> None:
        self.matlab = Matlab()
        self.matlab.eval(f"addpath('{model_path}');")

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

    def pass_input(self, params: SimulationParams) -> None:
        length = params.pop('length')

        inputs = {}
        for (key, value) in enumerate(params['inputs']):
            inputs["u" + str(key + 1)] = value

        logger.info(f"Length: {length}")
        self.matlab.eval(f"t__ = linspace(0, 40, {length})';")
        self.matlab.eval(f"u__ = {unpack(inputs)};")
        self.matlab.eval("u = [t__, u__];")

    def prepare_output(self) -> dict:
        yout = self.matlab.eval("yout;", 1)
        tout = self.matlab.eval("tout;", 1)

        times = np.asarray(tout).transpose().tolist()[0]
        error = np.asarray(yout).transpose().tolist()[0]
        pos = np.asarray(yout).transpose().tolist()[1]

        return {'times': times, 'values': list(zip(error, pos))}

    def reset_engine(self) -> None:
        self.eval("clear all")
