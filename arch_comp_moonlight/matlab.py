from typing import Any
import matlab.engine


class Matlab:
    def __init__(self) -> None:
        self.engine = matlab.engine.start_matlab()
        self.reset_engine()

    def reset_engine(self) -> None:
        self.eval("clear all")

    def eval(self, command: str, outputs: int = 0) -> Any:
        return self.engine.eval(command, nargout=outputs)

    def exec(self, script: str, output_args: int = 0) -> Any:
        script = getattr(self.engine, script)
        return script(nargout=output_args)  # type: ignore

    def __del__(self) -> None:
        self.engine.quit()  # type: ignore
