from arch_comp_moonlight.baseline.optimizer import Optimizer
from arch_comp_moonlight.experiment.configuration import Configuration
from arch_comp_moonlight.experiment.runner import Runner

from typing import Any


class NNOptimizer(Optimizer):
    def __init__(self, params: dict[str, Any]):
        super().__init__(params)

    def optimize(self, single_run: Any) -> None:
        print(self.params)


nn_config = Configuration(
    exp_name="NN",
    exp_batch_name="TURBO",
    random_samples=10,  # TODO: check the goal of this parameter
    optimization_iterations=1,
    other_params={
        'i': [1]
    },
    optimizer=lambda params: NNOptimizer(params)
)


class NNRunner(Runner):
    def __init__(self, config: Configuration):
        super().__init__(config)
        print(config)

    def single_run(self, params: dict[str, Any]) -> None:
        pass

    def optimizer_run(self, iter_params) -> None:
        # n = iter_params['n']
        # i = iter_params['input_size']
        # a = iter_params['alpha']
        # b = iter_params['beta']

        # print(f"Repetition n.: {n}")

        opt = self.config.optimizer({**vars(self.config), **iter_params})
        opt.optimize(self.single_run({}))
