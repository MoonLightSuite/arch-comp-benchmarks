from abc import ABC, abstractmethod
from typing import Callable, Any, Union
import numpy as np

from arch_comp_moonlight.experiment.configuration import Configuration
from arch_comp_moonlight.experiment.store import Store


class Optimizer(ABC):
    def __init__(self, config: Configuration, store: Store) -> None:
        pass

    @abstractmethod
    def optimize(self, simulator: Callable[[dict[str, np.float64]], Any]) -> Union[dict[Any, Any], None]:
        """Runs an instance of the monitor on a trace."""
        pass
