
from abc import ABC, abstractmethod
from typing import TypeVar, Generic, cast

from arch_comp_moonlight.experiment.configuration import Configuration
from arch_comp_moonlight.experiment.store import LineKey, Store

from ..experiment.trace import Trace
import numpy as np
import time


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

    def run(self, params: dict[str, np.float64]) -> Trace[T]:
        """Runs an instance of the simulation and keeps track of the time."""
        start = time.time()
        result = self.raw_run(params)
        end = time.time()
        currentTime = np.float64(end - start)

        # print(f"Simulation time is: {self.store[LineKey.simulation_time]}")
        if (self.store[LineKey.simulation_time]):
            previousTime = cast(
                np.float64, self.store[LineKey.simulation_time])
            currentTime += previousTime

        self.store.store(LineKey.simulation_time, currentTime)
        return result

    @abstractmethod
    def raw_run(self, params: dict[str, np.float64]) -> Trace[T]:
        """Runs an instance of the simulation."""
        raise NotImplementedError()

    def __del__(self) -> None:
        # hook for simulation cleanup
        pass
