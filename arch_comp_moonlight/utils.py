from typing import Callable, Any
from itertools import product
import logging

logger = logging.getLogger(__name__)


def nested_loops_from_dict_of_lists(param_dict: dict[str, list[Any]],
                                    action: Callable[[dict[str, Any]], None]):
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
        logger.info(f"Experiment parameters: {combo_dict} ##################")
        action(combo_dict)
