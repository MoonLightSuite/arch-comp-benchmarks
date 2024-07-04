import numpy as np

from arch_comp_moonlight.baseline.simulator import Simulator
from arch_comp_moonlight.experiment.configuration import Configuration
from arch_comp_moonlight.experiment.store import LineKey, Store
from arch_comp_moonlight.experiment.trace import Trace
from arch_comp_moonlight.matlab import Matlab
from arch_comp_moonlight.utils import list_of_lists_to_matlab_matrix

from logging import getLogger

logger = getLogger(__name__)

TraceValue = list[np.float64]


class F16Simulator(Simulator[TraceValue]):
    def __init__(self, config: Configuration, store: Store) -> None:
        super().__init__(config=config, store=store)
        self.matlab = Matlab()
        self.model_path = config.simulator_model_path

    def raw_run(self, params: dict[str, np.float64]) -> Trace[TraceValue]:
        self.matlab.cd(self.model_path)
        self._init()
        self._pass_input(params)
        self.matlab.eval("[T, XT, YT] = runF16(roll, pitch, yaw);")
        return self._prepare_output()

    def _pass_input(self, params: dict[str, np.float64]) -> None:
        self.matlab.eval(f"roll = {params['u1']};")
        self.matlab.eval(f"pitch = {params['u2']};")
        self.matlab.eval(f"yaw = {params['u3']};")

    def _init(self) -> None:
        self.matlab.eval("initF16;")

    def _prepare_output(self) -> Trace[TraceValue]:
        tout = self.matlab.eval("T;", outputs=1)
        u = self.matlab.eval("XT;", outputs=1)
        yout = self.matlab.eval("YT;", outputs=1)

        times = np.asarray(tout).transpose().tolist()[0]
        altitude = np.asarray(yout).transpose().tolist()[0]

        values = [[v] for v in altitude]

        # logger.info(f"Times: {len(times)}")
        # logger.info(f"Altitude: {len(altitude)}")

        self.store.store(LineKey.stop_time, times[-1])
        self.store.store(LineKey.input, f"{list_of_lists_to_matlab_matrix(u)}")

        return {'times': times, 'values': values}
