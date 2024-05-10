
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T   = TypeVar("T")

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

    def __init__(self) -> None:
        # hook for simulation initialization
        pass

    @abstractmethod
    def run(self, params: T) -> Trace:
        """Runs an instance of the simulation."""
        raise NotImplementedError()

    def __del__(self) -> None:
        # hook for simulation cleanup
        pass