from abc import ABC, abstractmethod
from typing import Callable, Any, Union
import numpy as np

import os


class Optimizer(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def optimize(self, simulator: Callable[[dict[str, np.float64]], Any]) -> Union[dict, None]:
        """Runs an instance of the monitor on a trace."""
        pass

    def store(self, header: str, line: str) -> None:
        """Stores the data of the optimization."""
        print(f"Printing to file: {self.filename}")

        if not os.path.isfile(self.filename):
            with open(self.filename, 'w') as f:
                f.write(header + '\n')

        with open(self.filename, 'a') as f:
            f.write(line + '\n')
