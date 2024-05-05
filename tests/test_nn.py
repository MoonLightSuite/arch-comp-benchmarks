from arch_comp_moonlight.nn import NNRunner, nn_config


def test_nn():
    runner = NNRunner(nn_config)
    assert nn_config == runner.config

    assert runner.optimizer_run({}) is None
