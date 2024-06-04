import os
from arch_comp_moonlight.experiment.configuration import Configuration
from experiments.f16.runner import F16Runner
from experiments.nn.runner import NNRunner
from experiments.pm.runner import PMRunner
from numpy import pi
from logging import basicConfig, getLogger, INFO


basicConfig(
    level=INFO, format="[%(levelname)s] %(asctime)s - %(message)s", datefmt="%H:%M:%S")
logger = getLogger(__name__)

dir = os.path.dirname(os.path.realpath(__file__))
EXP_DIR = f"{dir}/../models/"

nn_config_1 = Configuration(
    exp_name="NN",
    exp_batch_name="TURBO",
    exp_instance_number=1,
    exp_repetitions=10,
    optimization_iterations=28,
    simulator_model_path=f"{EXP_DIR}/NN - Magnet",
    simulator_repetitions=1,
    # Experiment-specific
    monitor_spec=f"{dir}/nn/spec_nn.mls",
    monitor_formula_name="NN",
    simulator_hyper_params={
        'length': [13],
    },
    optimization_lower_bounds=[1.0],
    optimization_upper_bounds=[3.0],
)

nnx_config_1 = Configuration(
    exp_name="NN",
    exp_batch_name="TURBO",
    exp_instance_number=1,
    exp_repetitions=10,
    optimization_iterations=72,
    simulator_model_path=f"{EXP_DIR}/NN - Magnet",
    simulator_repetitions=1,
    # Experiment-specific
    monitor_spec=f"{dir}/nn/spec_nnx.mls",
    monitor_formula_name="NNx",
    simulator_hyper_params={
        'length': [35],
    },
    optimization_lower_bounds=[1.95],
    optimization_upper_bounds=[2.05],
)

nn_config_2 = Configuration(
    exp_name="NN",
    exp_batch_name="TURBO",
    exp_instance_number=2,
    exp_repetitions=10,
    optimization_iterations=10,
    simulator_model_path=f"{EXP_DIR}/NN - Magnet",
    simulator_repetitions=1,
    # Experiment-specific
    monitor_spec=f"{dir}/nn/spec_nn.mls",
    monitor_formula_name="NN",
    simulator_hyper_params={
        'length': [3],
    },
    optimization_lower_bounds=[1.0],
    optimization_upper_bounds=[3.0],
)

nnx_config_2 = Configuration(
    exp_name="NN",
    exp_batch_name="TURBO",
    exp_instance_number=2,
    exp_repetitions=10,
    optimization_iterations=10,
    simulator_model_path=f"{EXP_DIR}/NN - Magnet",
    simulator_repetitions=1,
    # Experiment-specific
    monitor_spec=f"{dir}/nn/spec_nnx.mls",
    monitor_formula_name="NNx",
    simulator_hyper_params={
        'length': [3],
    },
    optimization_lower_bounds=[1.95],
    optimization_upper_bounds=[2.05],
)

f16_config = Configuration(
    exp_name="F16",
    exp_batch_name="TURBO",
    exp_instance_number=1,
    exp_repetitions=10,
    optimization_iterations=10,
    simulator_model_path=f"{EXP_DIR}/F16",
    simulator_repetitions=1,
    # Experiment-specific
    monitor_spec=f"{dir}/f16/spec.mls",
    monitor_formula_name="F16",
    simulator_hyper_params={},
    optimization_lower_bounds=[pi/4-pi/20, -2/5*pi+0, -pi/4-pi/8],
    optimization_upper_bounds=[pi/4+pi/30, -2/5*pi+pi/20, -pi/4+pi/8],
)

pm_config = Configuration(
    exp_name="PM",
    exp_batch_name="TURBO",
    exp_instance_number=1,
    exp_repetitions=10,
    optimization_iterations=10,
    simulator_model_path=f"{EXP_DIR}/PM - Pacemaker",
    simulator_repetitions=1,
    # Experiment-specific
    monitor_spec=f"{dir}/pm/spec.mls",
    monitor_formula_name="PM",
    simulator_hyper_params={},
    optimization_lower_bounds=[50.0],
    optimization_upper_bounds=[90.0],
)


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    # nn = NNRunner(nn_config_2)
    # nn.run_batch()
    # f16 = F16Runner(f16_config)
    # f16.run_batch()
    pm = PMRunner(pm_config)
    pm.run_batch()


if __name__ == "__main__":
    main()
