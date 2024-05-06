
from typing import TypedDict
from moonlight import ScriptLoader
import numpy as np

from ..baseline.monitor import Monitor

Trace = TypedDict('Trace', {'times': list[float], 'values': list[float]})


class NNMonitor(Monitor):
    def run(self, trace: Trace, formula: str) -> np.ndarray[float]:

        moonlightScript = ScriptLoader.loadFromFile("spec.txt")
        monitor = moonlightScript.getMonitor(formula)

        res = monitor.monitor(trace['times'], trace['values'])

        return np.array(res)
