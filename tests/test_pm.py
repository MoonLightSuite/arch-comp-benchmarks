from experiments.pm.runner import PMRunner
from experiments.main import pm_config_2


def test_pm():
    runner = PMRunner(pm_config_2)
    assert pm_config_2 == runner.config

    print("Running PMRunner")

    assert runner.run_batch() is None
