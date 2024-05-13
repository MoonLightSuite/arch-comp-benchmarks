from sympy import Line
from arch_comp_moonlight.experiment.store import LineKey, Line


def test_store():
    # line = LineKey
    line: Line = {
        LineKey.system: 'a',
        LineKey.property: 'b',
    }
    print(line)
    for key in line:
        print(key)
        print("Value: ", line[key])
    assert True
