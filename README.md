# ARCH-COMP Moonlight

This repository contains the models and scripts for reproducing the ARCH-COMP Moonlight benchmarks.

## Prerequisites
The benchmarks have been implemented via python 3.11 and [Poetry](https://python-poetry.org/docs/#installation).
Moreover, since the benchmarks are based on the classical ARCH-COMP problems, Matlab must be available in the running environment (the suite has been tested with [Matlab R2024a](https://www.mathworks.com/help/install/ug/install-products-with-internet-connection.html)).


## Installation
```bash
poetry install
```

## Running the benchmarks
```bash
poetry run experiments
```

## Results
The results of the benchmarks are stored in the `output` directory. They can also be visualized by looking at the `paper_table.ipynb` Jupyter notebook.

## Contributing
The project is organized in the following way:
- `arch_comp_moonlight` contains the core implementation of the benchmarking suite.
- `experiments` contains the code for running the specific benchmark problems.
- `models` contains the models of the benchmark problems, as provided by the ARCH-Comp team.
- `output` contains the results of the benchmarks.