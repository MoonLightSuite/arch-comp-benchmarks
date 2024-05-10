Aircraft Ground Collision Avoidance System - F16

Model name: AeroBenchVV-develop/src/main/Simulink/AeroBenchSim_2019a.slx
Matlab version >= 2019a

Initial Conditions:
- x_01: Roll angle
- x_02: Pitch angle
- x_03: Yaw angle

Outputs:
- y_1: F16 altitude

Requirements in STL:
F16: □_[0, 15] y_1 > 0

Minimum simulation time: 15s

Initial Condition range:
- x_01: pi/4-pi/20 <= x_01 <= pi/4+pi/30
- x_02: -2/5*pi+0 <= x_02 <= -2/5*pi+pi/20
- x_03: -pi/4-pi/8 <= x_03 <= -pi/4+pi/8

Instance 1: The system has no inputs. Any combination of roll, pitch, and yaw within their respective ranges is acceptable.

Instance 2: Not Available

Running the model: To run the model use the function 'runF16.m'.
Please note the following instructions:
1. Before running, make sure that the folder 'AeroBenchVV-develop' is in the current working directory.
2. Run 'initF16.m' once before running 'runF16.m'. The init function should load all the necessary configuration parameters for the model. This function also set the initial altitude and simulation time for the model, so set them accordingly.