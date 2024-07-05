from typing import Callable, Any, Mapping, TypeVar
from itertools import product
import logging
import zlib
import base64
from glob import glob
from pandas import DataFrame, read_csv, concat

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


def compress_string(input_string: str):
    """
    Compress a string using zlib and encode it with Base64
    """
    compressed_data = zlib.compress(input_string.encode('utf-8'))
    compressed_string = base64.b64encode(compressed_data).decode('utf-8')
    return compressed_string


def decompress_string(compressed_string: str):
    """
    Decode a compressed string using Base64 and decompress it using zlib
    """
    compressed_data = base64.b64decode(compressed_string)
    decompressed_data = zlib.decompress(compressed_data)
    return decompressed_data.decode('utf-8')


def list_of_lists_to_matlab_matrix(matrix: list[list[Any]]) -> str:
    """
    Given a list of lists, we convert it to a string that represents a matrix in MATLAB
    e.g. [[1, 2, 3], [4, 5, 6]] -> '[1 2 3; 4 5 6]'
    """
    return '[' + '; '.join([' '.join(map(str, row)) for row in matrix]) + ']'


def merge_results(path: str, to_file: str | None = None) -> DataFrame:
    """
    Merge all the CSV files in the provided directory and its subdirectories into a single CSV file, and optionally saves it.
    """

    dfs: list[DataFrame] = []

    # Get a list of all CSV files in the output directory and its subdirectories
    csv_files = glob(path, recursive=True)

    # Loop through the list of CSV files
    for csv_file in csv_files:
        logger.info(f'Reading {csv_file}')
        dfs.append(read_csv(csv_file, sep=',', quotechar='"',  # type: ignore
                            skipinitialspace=True))

    merged_df: DataFrame = concat(dfs, ignore_index=True)  # type: ignore

    if (to_file):
        merged_df.to_csv(to_file, index=False)  # type: ignore

    return merged_df  # type: ignore
