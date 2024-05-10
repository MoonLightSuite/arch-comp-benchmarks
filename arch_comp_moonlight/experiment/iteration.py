from typing import Generic, TypeVar, TypedDict

T = TypeVar("T")


class Iteration(TypedDict, Generic[T]):
    """
    Iteration is a generic TypedDict that represents a single iteration of the experiment.
    `n:` the iteration number
    `params:` the parameters to pass to the simulator for the iteration
    """
    n: int
    params: T
