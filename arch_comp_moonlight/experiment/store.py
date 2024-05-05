from typing import Any, Callable


class Store:
    def __init__(self):
        pass

    def do_store(self, store: Callable, params: dict[str, Any], robustness: float) -> None:
        input_params_str = ','.join([str(v) for v in params.values()])
        data_line = f"{input_params_str},{robustness},-1"
        ln = range(1, len(params) + 1)
        header_line = ','.join(
            [f'u{str(j)}' for j in ln]) + ',value,Timestamp'
        store(header_line, data_line)
