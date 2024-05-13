from enum import Enum, auto
import os
from logging import getLogger


class LineKey(Enum):
    system = auto()
    property = auto()
    simulations = auto()
    time = auto()
    robustness = auto()
    falsified = auto()
    input = auto()
    instance = auto()


Line = dict[LineKey, str]

logger = getLogger(__name__)


class Store:
    def __init__(self, filename: str):
        if not os.path.isfile(filename):
            with open(filename, 'w') as f:
                f.write(self._print_header() + '\n')
                logger.debug(f"Created file: {filename}.")
        self.filename = filename
        self.last_line: Line | None = None

    def _print_line(self, line: Line) -> str:
        return f'"{line[LineKey.system]}","{line[LineKey.property]}","{line[LineKey.simulations]}","{line[LineKey.time]}","{line[LineKey.robustness]}","{line[LineKey.falsified]}","{line[LineKey.input]}"'

    def _print_header(self) -> str:
        header = list(LineKey.__members__.keys())
        return '"' + '","'.join(header) + '"'

    def store(self, key: LineKey, value: str) -> None:
        """Stores the data of the optimization."""
        if (self.last_line is None):
            self.last_line = {}
        self.last_line[key] = value

    def save(self) -> None:
        """Saves the data to the file."""
        print(f"Saving to file: {self.filename}")
        if (self.last_line is not None):
            with open(self.filename, 'a') as f:
                f.write(self._print_line(self.last_line) + '\n')
        else:
            logger.warning("No data to save.")
