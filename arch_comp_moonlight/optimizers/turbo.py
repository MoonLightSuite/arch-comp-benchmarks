

from ..baseline.optimizer import Optimizer
from typing import Callable
import numpy as np
from numpy.typing import NDArray
from logging import getLogger
import warnings
from turbo import Turbo1  # type: ignore

logger = getLogger(__name__)


class Turbo(Optimizer):
    def __init__(self,
                 optimization_iters: int,
                 lower_bounds: NDArray[np.float64],
                 upper_bounds: NDArray[np.float64]) -> None:
        super().__init__()

        _check_bounds(lower_bounds, upper_bounds)

        INPUT_DIMENSIONS = upper_bounds.size
        SAMPLES = 2 * INPUT_DIMENSIONS
        PYTORCH_BATCH_SIZE = 1

        self.turbo: Callable[
            [Callable[[NDArray[np.float64]], np.float64]],
            Turbo1]
        self.turbo = lambda f: Turbo1(
            f=f,  # Handle to objective function
            lb=lower_bounds,  # Numpy array specifying lower bounds
            ub=upper_bounds,  # Numpy array specifying upper bounds
            n_init=SAMPLES,  # Number of initial points from an Latin hypercube design
            max_evals=optimization_iters,  # Maximum number of evaluations
            batch_size=PYTORCH_BATCH_SIZE,  # Optimizes TuRBO's computations
            verbose=False,  # Print information from each batch
            use_ard=False,  # Set to true if you want to use ARD for the GP kernel
            max_cholesky_size=2000,  # When we switch from Cholesky to Lanczos
            n_training_steps=50,  # Number of steps of ADAM to learn the hypers
            min_cuda=1024,  # Run on the CPU for small datasets
            device="cpu",  # "cpu" or "cuda"
            dtype="float32",  # float64 or float32
        )  # type: ignore

    def optimize(self, simulator:
                 Callable[[dict[str, np.float64]], np.float64]) -> None:
        self.simulator = simulator
        opt = self.turbo(self._simulation)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=UserWarning)
            warnings.simplefilter("ignore", category=DeprecationWarning)
            opt.optimize()

    def _simulation(self, params: NDArray[np.float64]) -> np.float64:
        return self.simulator(self.__array_to_dict(params))

    def __array_to_dict(self, raw_params: NDArray[np.float64]) \
            -> dict[str, np.float64]:
        params = {f"u{i+1}": raw_params[i] for i in range(len(raw_params))}
        return params


def _check_bounds(lower_bounds: NDArray[np.float64],
                  upper_bounds: NDArray[np.float64]) -> None:
    if (lower_bounds.shape != upper_bounds.shape):
        raise Exception("Lower and upper bounds must have the same shape")

    if (lower_bounds.size != upper_bounds.size):
        raise Exception("Lower and upper bounds must have the same size")

    if (len(lower_bounds.shape) != 1):
        raise Exception("Lower and upper bounds must be 1-dimensional")

    if (lower_bounds.dtype != np.float64
            or upper_bounds.dtype != np.float64):
        raise Exception("Lower and upper bounds must be of type float64")
