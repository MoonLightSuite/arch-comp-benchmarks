from dataclasses import dataclass
from typing import Callable, Any
from ..baseline.optimizer import Optimizer


@dataclass
class Configuration:
    """
    Holds the configuration for an experiment.

    Attributes:
    -   exp_name: the name of the experiment
    -   exp_batch_name: the name of the batch of experiments (typically the optimizer or the specific configuration of the optimizer)
    -   exp_repetitions: the number of repetitions for each experiment
    -   random_samples: the number of random samples to take
    -   optimization_iterations: the number of optimization iterations before stopping
    -   other_params: a dictionary with the parameters to optimize
    -   formula_name: the name of the formula to monitor
    -   simulator_repetitions: the number of repetitions for each simulation
    """
    exp_name: str
    exp_batch_name: str
    random_samples: int
    optimization_iterations: int
    other_params: dict[str, list[Any]]
    formula_name: str
    simulator_repetitions: int = 1
    exp_repetitions: int = 1
