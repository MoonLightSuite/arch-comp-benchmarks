from typing import Callable, Any, Mapping, TypeVar
from itertools import product
import logging

from arch_comp_moonlight.experiment.iteration import Iteration

logger = logging.getLogger(__name__)

T = TypeVar("T")


def nested_loops_from_dict_of_lists(param_dict: Mapping[str, list[Any]],
                                    action: Callable[[Mapping[str, object]], Any]):
    """
    Given a dictionary of lists, we perform a nested loop over all the lists and call the given action with the current combination of values.

    Parameters:
    - `param_dict`: dictionary of lists
    - `action`: function to call with the current combination of values

    Example usage:
    ```
    param_dict = {
        'var1': [1, 2, 3],
        'var2': ['a', 'b'],
        'var3': [10, 20]
    }
    nested_loops_from_dict_of_lists(param_dict,  print)
    ```
    """
    keys, lists = zip(*param_dict.items())

    for combination in product(*lists):
        combo_dict = dict(zip(keys, combination))
        structured_combo_dict = _prepare_iteration(combo_dict)
        action(structured_combo_dict)


def _prepare_iteration(params: dict[str, Any]) -> Iteration[object]:
    """
    Prepare the iteration for the optimizer
    """
    iter_keys = list(Iteration.__annotations__.keys())
    iter_keys.remove('params')

    iter_basic = {key: params[key] for key in iter_keys if key in params}
    iter_params = {key: params[key]
                   for key in params.keys() if key not in iter_keys}

    return {**iter_basic, 'params': iter_params}  # type: ignore


def unpack(params: dict[Any, Any]) -> str:
    """
    Iterate over params keys and concatenate to a string
    the values of the dictionary
    e.g. {'u1': 1, 'u2': 2, 'u3': 2} -> '[1; 2; 2]'
    """
    return f"[ {'; '.join([str(params[key]) for key in params.keys()])} ]"
