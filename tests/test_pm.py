from experiments.pm.runner import PMRunner
from experiments.main import pm_config_1


def test_pm():
    runner = PMRunner(pm_config_1)
    assert pm_config_1 == runner.config

    print("Running PMRunner")

    assert runner.run_batch() is None
