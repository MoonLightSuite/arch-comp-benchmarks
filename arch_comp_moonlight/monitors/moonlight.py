
from ..experiment.trace import Trace
from moonlight import ScriptLoader  # type: ignore
import numpy as np
from logging import getLogger
from numpy.typing import NDArray
from typing import TypeVar

from ..baseline.monitor import Monitor

logger = getLogger(__name__)

T = TypeVar('T')


class Moonlight(Monitor[T]):
    def __init__(self, spec: str) -> None:
        super().__init__()
        file = f"{spec}"
        logger.info(f"Loading moonlight script from {file}")
        self.moonlight = ScriptLoader.loadFromFile(file)  # type: ignore

    def run(self, trace: Trace[T], formula: str) \
            -> NDArray[np.float64]:
        monitor = self.moonlight.getMonitor(formula)  # type: ignore
        logger.info(f"Monitor values: {trace['values']}")
        res = monitor.monitor(trace['times'], trace['values'])  # type: ignore
        return np.array(res)  # type: ignore
