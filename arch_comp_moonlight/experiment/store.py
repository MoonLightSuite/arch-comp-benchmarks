from typing import Any, Callable
import os


class Store:
    header = """\
"system","property","simulations","time","robustness","falsified","input"\
"""

    def __init__(self, filename: str):
        if not os.path.isfile(filename):
            with open(filename, 'w') as f:
                f.write(self.header + '\n')
        self.filename = filename

    def do_store(self, store: Callable[[str, str], None], params: dict[str, Any], robustness: float) -> None:
        input_params_str = ','.join([str(v) for v in params.values()])
        data_line = f"{input_params_str},{robustness},-1"
        ln = range(1, len(params) + 1)
        header_line = ','.join(
            [f'u{str(j)}' for j in ln]) + ',value,Timestamp'
        store(header_line, data_line)

    def store(self, header: str, line: str) -> None:
        """Stores the data of the optimization."""
        print(f"Printing to file: {self.filename}")

        if not os.path.isfile(self.filename):
            with open(self.filename, 'w') as f:
                f.write(header + '\n')

        with open(self.filename, 'a') as f:
            f.write(line + '\n')
