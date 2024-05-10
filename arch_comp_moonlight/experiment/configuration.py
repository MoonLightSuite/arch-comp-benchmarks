from dataclasses import dataclass
from typing import Any


@dataclass
class Configuration:
    """
    Holds the configuration for an experiment.

    Attributes:
    -   exp_name: the name of the experiment
    -   exp_batch_name: the name of the batch of experiments (typically the optimizer or the specific configuration of the optimizer)
    -   exp_repetitions: the number of repetitions for each experiment
    -   optimization_iterations: the number of optimization iterations before stopping
    -   optimization_lower_bounds: the lower bound for the optimization
    -   optimization_upper_bounds: the upper bound for the optimization
    -   other_params: a dictionary with the parameters to optimize
    -   formula_name: the name of the formula to monitor
    -   simulator_repetitions: the number of repetitions for each simulation
    """
    exp_name: str
    exp_batch_name: str
    optimization_iterations: int
    optimization_lower_bounds: float
    optimization_upper_bounds: float
    monitor_spec: str
    monitor_formula_name: str
    simulator_hyper_params: dict[str, list[Any]]
    simulator_repetitions: int = 1
    exp_repetitions: int = 1
