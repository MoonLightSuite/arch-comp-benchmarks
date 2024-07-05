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

### Project structure
The project is organized in the following way:
- `arch_comp_moonlight` contains the core implementation of the benchmarking suite.
- `experiments` contains the code for running the specific benchmark problems.
- `models` contains the models of the benchmark problems, as provided by the ARCH-Comp team.
- `output` contains the results of the benchmarks.

### Updating the changelog
- Refresh the changelog by running `poetry run git-changelog`
- Then commit following the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) standard.
- Add a tag to the commit, named as the last item of the changelog (e.g. for `v0.3.0`: `git tag -a v0.3.0 -m "v0.3.0"`).
- Finally, push the changes to the repository.

### Adding a new benchmark
To add the new benchmark, create a new directory for it in the `experiments` directory.
In order to have it ready, one needs to:
- Implement the `Simulator` abstract class for the specific benchmark.
- Implement the `Runner` class for the specific benchmark.

These two classes are responsible for, respectively, passing the data to the simulator, and passing the results back to the monitor and to the optimizer. 

### Adding a new monitor
To add a new monitor, create a new file (or directory) for it in the `arch_comp_moonlight/monitors` directory.
It is sufficient that it implements the `Monitor` abstract class, to make it usable by the benchmarks.

### Adding a new optimizer
To add a new optimizer, create a new file (or directory) for it in the `arch_comp_moonlight/optimizers` directory.
It is sufficient that it implements the `Optimizer` abstract class, to make it usable by the benchmarks.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

