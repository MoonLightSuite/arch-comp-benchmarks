from arch_comp_moonlight.baseline.monitor import Monitor

def test_monitor():

    monitor = Monitor()
    assert monitor.run({}) is None