from typing import Any, Callable
from os import path


class Store:
    header = """\
"system","property","simulations","time","robustness","falsified","input"\
"""

    def __init__(self, filename: str):
        if not path.isfile(filename):
            with open(filename, 'w') as f:
                f.write(self.header + '\n')

    def do_store(self, store: Callable, params: dict[str, Any], robustness: float) -> None:
        input_params_str = ','.join([str(v) for v in params.values()])
        data_line = f"{input_params_str},{robustness},-1"
        ln = range(1, len(params) + 1)
        header_line = ','.join(
            [f'u{str(j)}' for j in ln]) + ',value,Timestamp'
        store(header_line, data_line)
