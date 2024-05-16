from os import path
from arch_comp_moonlight.experiment.configuration import Configuration
from experiments.nn.runner import NNRunner
from logging import basicConfig, getLogger, INFO

basicConfig(
    level=INFO, format="[%(levelname)s] %(asctime)s - %(message)s", datefmt="%H:%M:%S")
logger = getLogger(__name__)

dir = path.dirname(path.realpath(__file__))
EXP_DIR = f"{dir}/../models/NN - Magnet"

nn_config = Configuration(
    exp_name="NN",
    exp_batch_name="TURBO",
    exp_instance_number=1,
    exp_repetitions=10,
    optimization_iterations=28,
    simulator_model_path=EXP_DIR,
    simulator_repetitions=1,
    # Experiment-specific
    monitor_spec=f"{dir}/nn/spec_nn.mls",
    monitor_formula_name="NN",
    simulator_hyper_params={
        'length': [13],
    },
    optimization_lower_bounds=1.0,
    optimization_upper_bounds=3.0,
)


def main():
    logger.info(f"Running experiment {nn_config.exp_name}")

    nn = NNRunner(nn_config)
    nn.run_batch()


if __name__ == "__main__":
    main()
