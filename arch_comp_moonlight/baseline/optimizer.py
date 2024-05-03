from typing import Callable, Any, Union

import os

class Optimizer:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        pass

    def optimize(self, simulator: Callable[[dict[str, float]], Any]) -> Union[dict, None]:
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
