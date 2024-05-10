Neural Network Controller for Levitating Magnet - NN

Model name: narmamaglev_v1.slx
Matlab version >= 2018b

Inputs:
- u_1: Reference position

Outputs:
- y_1: Position error
- y_2: Magnet position

Requirements in STL:
NN:  □_[1,37] ((y_1 > 0)->(◇_[0,2] (□_[0,1] (y_1 < 0))))
NNx: (◇_[0,1] y_2 > 3.2) /\ (◇_[1,1.5] (□_[0,0.5] 1.75 < y_2 < 2.25)) /\ (□_[2,3] 1.825 < y_2 < 2.175)
where: y_1 = |Pos-Ref|-(alpha+beta*|Ref|) = |y_2-u_1|-(alpha+beta*|u_1|)

Minimum simulation time: 40s

Input range:
- For NN:  1 <= u_1 <= 3
- For NNx: 1.95 <= u_1 <= 2.05

Instance 1:
- For NN: The input signal must be piecewise continuous with consecutive discontinuities (steps) at least 3 seconds apart.
- For NNx: The input signal must be piecewise continuous with consecutive discontinuities (steps) at least 1 second apart.

Instance 2: Piecewise constant function with 3 intervals of uniform length.

Model parameters:
    u_ts = 0.001;
    alpha = 0.005;
    beta = 0.03;

