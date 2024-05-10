
from typing import Generic, TypeVar, TypedDict
import numpy as np


T = TypeVar("T")


class Trace(TypedDict, Generic[T]):
    times: list[np.float64]
    values: list[T]
