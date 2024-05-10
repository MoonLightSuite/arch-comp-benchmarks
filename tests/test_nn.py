from arch_comp_moonlight.nn.runner import NNRunner, Params, nn_config, Iteration


def test_nn():
    runner = NNRunner(nn_config)
    assert nn_config == runner.config

    iteration = Iteration[Params](n=1,
                                  params={
                                      "length": 3
                                  })
    assert runner.optimizer_run(iteration) is None
