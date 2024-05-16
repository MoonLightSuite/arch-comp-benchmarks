from experiments.nn.runner import NNRunner
from experiments.main import nn_config_1


def test_nn():
    runner = NNRunner(nn_config_1)
    assert nn_config_1 == runner.config

    assert runner.run_batch() is None
