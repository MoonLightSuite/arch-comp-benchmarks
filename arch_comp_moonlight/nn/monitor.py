
from typing import TypedDict
from moonlight import ScriptLoader
import numpy as np
from logging import getLogger
from os import path

from ..baseline.monitor import Monitor

logger = getLogger(__name__)

Trace = TypedDict('Trace', {'times': list[float], 'values': list[float]})


class NNMonitor(Monitor):
    def run(self, trace: Trace, formula: str) -> np.ndarray[float]:
        dir = path.dirname(path.realpath(__file__))
        moonlightScript = ScriptLoader.loadFromFile(
            f"{dir}/spec_{formula}.mls")
        monitor = moonlightScript.getMonitor(formula)

        logger.info(f"Trace: ${trace.keys()}")
        logger.info(f"Times: {len(trace['times'])}")
        logger.info(f"Values: {len(trace['values'])}")
        logger.info(f"Values[0]: {len(trace['values'][0])}")

        res = monitor.monitor(trace['times'], trace['values'])

        return np.array(res)
