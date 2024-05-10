from abc import ABC, abstractmethod
from numpy.typing import NDArray
import numpy as np
from ..experiment.trace import Trace
from typing import TypeVar, Generic

T = TypeVar("T")

class Monitor(ABC, Generic[T]):

    @abstractmethod
    def run(self, trace: Trace[T], formula: str) -> NDArray[np.float64]:
        """Runs an instance of the monitor on a trace."""
        pass
