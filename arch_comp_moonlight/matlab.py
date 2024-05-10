from typing import Any
import matlab.engine  # type: ignore


class Matlab:
    def __init__(self) -> None:
        self.engine = matlab.engine.start_matlab()  # type: ignore
        self.reset_engine()

    def reset_engine(self) -> None:
        self.eval("clear all")

    def eval(self, command: str, outputs: int = 0) -> Any:
        return self.engine.eval(command, nargout=outputs)  # type: ignore

    def exec(self, script: str, output_args: int = 0) -> Any:
        script = getattr(self.engine, script)  # type: ignore
        return script(nargout=output_args)  # type: ignore

    def __del__(self) -> None:
        self.engine.quit()  # type: ignore
