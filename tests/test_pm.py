from experiments.pm.runner import PMRunner
from experiments.main import pm_config


def test_pm():
    runner = PMRunner(pm_config)
    assert pm_config == runner.config

    print("Running PMRunner")

    assert runner.run_batch() is None
