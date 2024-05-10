
from ..nn.simulator import TraceValue
from ..experiment.trace import Trace
from moonlight import ScriptLoader  # type: ignore
import numpy as np
from logging import getLogger
from os import path
from numpy.typing import NDArray

from ..baseline.monitor import Monitor

logger = getLogger(__name__)


class NNMonitor(Monitor[TraceValue]):
    def run(self, trace: Trace[TraceValue], formula: str) -> NDArray[np.float64]:
        dir = path.dirname(path.realpath(__file__))
        moonlightScript = ScriptLoader.loadFromFile(  # type: ignore
            f"{dir}/spec_{formula}.mls")  # type: ignore

        monitor = moonlightScript.getMonitor(formula)  # type: ignore

        res = monitor.monitor(trace['times'], trace['values'])  # type: ignore

        return np.array(res)  # type: ignore
