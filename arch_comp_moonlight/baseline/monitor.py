from typing import Union
from abc import ABC, abstractmethod


class Monitor(ABC):

    @abstractmethod
    def run(self, trace: dict, formula: str) -> Union[list[float], None]:
        """Runs an instance of the monitor on a trace."""
        pass
