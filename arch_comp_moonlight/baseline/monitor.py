from typing import Union
from abc import ABC, abstractmethod
from numpy.typing import NDArray
import numpy as np


class Monitor(ABC):

    @abstractmethod
    def run(self, trace: dict, formula: str) -> NDArray[np.float64]:
        """Runs an instance of the monitor on a trace."""
        pass
