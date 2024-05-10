
from typing import TypedDict
from moonlight import ScriptLoader
import numpy as np
from logging import getLogger
from os import path
from numpy.typing import NDArray

from ..baseline.monitor import Monitor

logger = getLogger(__name__)

Trace = TypedDict(
    'Trace', {
        'times': list[float], 
        'values': list[tuple[np.float64, np.float64]]
    }
)


class NNMonitor(Monitor):
    def run(self, trace: Trace, formula: str) -> NDArray[np.float64]:
        dir = path.dirname(path.realpath(__file__))
        moonlightScript = ScriptLoader.loadFromFile(
            f"{dir}/spec_{formula}.mls")

        monitor = moonlightScript.getMonitor(formula)

        res = monitor.monitor(trace['times'], trace['values']) # type: ignore

        return np.array(res)
