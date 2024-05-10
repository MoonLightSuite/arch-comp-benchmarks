
from ..experiment.trace import Trace
from moonlight import ScriptLoader  # type: ignore
import numpy as np
from logging import getLogger
from os import path
from numpy.typing import NDArray
from typing import TypeVar

from ..baseline.monitor import Monitor

logger = getLogger(__name__)

T = TypeVar('T')


class Moonlight(Monitor[T]):
    def __init__(self, spec: str) -> None:
        super().__init__()
        dir = path.dirname(path.realpath(__file__))
        file = f"{dir}/{spec}"
        self.moonlight = ScriptLoader.loadFromFile(file)  # type: ignore

    def run(self, trace: Trace[T], formula: str) \
            -> NDArray[np.float64]:
        monitor = self.moonlight.getMonitor(formula)  # type: ignore
        res = monitor.monitor(trace['times'], trace['values'])  # type: ignore
        return np.array(res)  # type: ignore
