from arch_comp_moonlight.nn.runner import NNRunner, nn_config, Iteration


def test_nn():
    runner = NNRunner(nn_config)
    assert nn_config == runner.config

    iteration = Iteration(n=1,
                          params={
                              "length": 3,
                              "inputs": [1.7371798557979203,
                                         2.0007661359736426,
                                         1.8324732072952215
                                         ]
                          })

    assert runner.optimizer_run(iteration) is None
