from enum import Enum, auto
import os
from logging import getLogger
from typing import Any, Self
from numpy import float64
from functools import total_ordering


@total_ordering
class LineKey(Enum):
    system = auto()
    property = auto()
    simulations = auto()
    time = auto()
    robustness = auto()
    falsified = auto()
    input = auto()
    instance = auto()

    def __lt__(self, other: Self) -> bool:
        if self.__class__ is other.__class__:
            return self.value < other.value
        return False

    def __str__(self):
        return str(self.value)


Line = dict[LineKey, str | float64 | int]

logger = getLogger(__name__)


class Store:
    def __init__(self):
        self.last_line: Line | None = None

    def _sort_line(self, line: Line) -> Line:
        keys = list(line.keys())
        keys.sort()
        return {key: line[key] for key in keys}

    def _print_line(self, line: Line) -> str:
        # return f'"{line[LineKey.system]}","{line[LineKey.property]}",{line[LineKey.simulations]},{line[LineKey.time]},{line[LineKey.robustness]},"{line[LineKey.falsified]}","{line[LineKey.input]}",{line[LineKey.instance]}'
        # output = ""
        # for key in line:
        #     if(line[key].isnumeric()):
        #         output += f'{line[key]},'
        #     else:
        #         output += f'"{line[key]}",'
        # return output
        line = self._sort_line(line)

        return ",".join([self._print_value(line[key]) for key in line])

    def _print_value(self, value: Any) -> str:
        if isinstance(value, str):
            return f'"{value}"'
        return str(value)

    def _print_header(self) -> str:
        header = list(LineKey.__members__.keys())
        return '"' + '","'.join(header) + '"'

    def store(self, key: LineKey, value: str | float64 | int) -> None:
        """Stores the data of the optimization."""
        if (self.last_line is None):
            self.last_line = {}
        self.last_line[key] = value

    def _create_file(self, filename: str) -> None:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        if not os.path.isfile(filename):
            with open(filename, 'w') as f:
                f.write(self._print_header() + '\n')
                logger.debug(f"Created file: {filename}.")
        logger.debug(f"File '{filename}' already exists, skipping creation.")

    def save(self, destination: str) -> None:
        """Saves the data to the file."""
        logger.info(f"Saving to file: {destination}")
        self._create_file(destination)
        if (self.last_line is not None):
            with open(destination, 'a') as f:
                f.write(self._print_line(self.last_line) + '\n')
        else:
            logger.warning("No data to save.")
