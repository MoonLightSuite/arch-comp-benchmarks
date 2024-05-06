from arch_comp_moonlight.nn.runner import NNRunner, nn_config


def test_nn():
    runner = NNRunner(nn_config)
    assert nn_config == runner.config

    assert runner.single_run({"length": [3]}) is None
