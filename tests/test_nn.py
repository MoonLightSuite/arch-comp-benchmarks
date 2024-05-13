from experiments.nn.runner import NNRunner, nn_config


def test_nn():
    runner = NNRunner(nn_config)
    assert nn_config == runner.config

    # iteration = Iteration[Params](n=1,
    #                               params={
    #                                   "length": 3
    #                               })
    # assert runner.optimizer_run(iteration) is None
    assert runner.run_batch() is None
