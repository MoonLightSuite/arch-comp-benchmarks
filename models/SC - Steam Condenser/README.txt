Steam condenser with Recurrent Neural Network Controller - SC

Model name: steamcondense_RNN_22.slx
Matlab version >= 2018a

Inputs:
- u_1: Steam flow rate

Outputs:
- y_1: Steam temperature
- y_2: Cooling water flow rate
- y_3: Heat transferred
- y_4: Steam pressure

Requirements in STL:
SC: □_[30,35] 87 <= y_4 <= 87.5

Minimum simulation time: 35s

Input range:
- u_1: 3.99 <= u_1 <= 4.01

Instance 1: The input signal must be piecewise continuous with a finite number of discontinuities.

Instance 2: Piecewise constant function with 20 intervals of uniform length.