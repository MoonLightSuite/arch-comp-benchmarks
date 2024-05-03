Pacemaker - PM

Model name: Model1_Scenario1_Correct.slx
Matlab version >= 2022a

Inputs:
- u_1: Lower Heart Rate Limit

Outputs:
- y_1: Heart Rate Period
- y_2: Lower Heart Rate Limit
- y_3: Pace count

Requirements in STL:
PM: (□_[0,10]  y_3 <= 15) /\ (◇_[0,10]  y_3 >= 8)

Minimum simulation time: 10s

Input range:
- u_1: 50 <= u_1 <= 90

Instance 1: The input signal must be piecewise continuous with a finite number of discontinuities.

Instance 2: Piecewise constant function with 5 intervals of uniform length.