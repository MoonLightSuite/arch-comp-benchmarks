
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from arch_comp_moonlight.experiment.configuration import Configuration
from arch_comp_moonlight.experiment.store import LineKey, Store

from ..experiment.trace import Trace
import numpy as np

T = TypeVar("T")


class Simulator(ABC, Generic[T]):
    """
    Simulator is an abstract class that defines the interface for a simulation.

    Methods to implement:
    - run: Runs an instance of the simulation.

    Example:
    ```
    class MySimulator(Simulator):
        def run(self, params: dict) -> dict:
            return 1 # a very dumb simulator that always returns 1
    ```
    """

    def __init__(self, config: Configuration, store: Store) -> None:
        self.store = store
        self.config = config
        store.store(LineKey.property, config.monitor_formula_name)

    @abstractmethod
    def run(self, params: dict[str, np.float64]) -> Trace[T]:
        """Runs an instance of the simulation."""
        raise NotImplementedError()

    def __del__(self) -> None:
        # hook for simulation cleanup
        pass
