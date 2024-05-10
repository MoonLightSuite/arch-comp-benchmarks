from abc import ABC, abstractmethod
from typing import Callable, Any, Union
import numpy as np


class Optimizer(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def optimize(self, simulator: Callable[[dict[str, np.float64]], Any]) -> Union[dict[Any, Any], None]:
        """Runs an instance of the monitor on a trace."""
        pass
