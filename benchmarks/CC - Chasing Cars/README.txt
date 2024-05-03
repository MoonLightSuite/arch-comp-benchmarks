Chasing Cars simulation - CC

Model name: cars.mdl
Matlab version >= 2018b

Inputs:
- u_1: Car 1 throttle
- u_2: Car 1 brake

Outputs:
- y_1: Position of car 1
- y_2: Position of car 2
- y_3: Position of car 3
- y_4: Position of car 4
- y_5: Position of car 5

Requirements in STL:
CC1: □_[0, 100] y_5-y_4 <= 40
CC2: □_[0, 70] ◇_[0, 30] y_5-y_4 <= 40
CC3: □_[0, 80] ((□_[0, 20] y_2-y_1 <= 20) \/ (◇_[0, 20] y_5-y_4 >= 40))
CC4: □_[0, 65] ◇_[0, 30] □_[0, 5] y_5-y_4 >= 8
CC5: □_[0, 72] ◇_[0, 8] ((□_[0, 5] y_2-y_1 >= 9) -> (□_[5, 20] y_5-y_4 >= 9))
CCx: (□_[0, 50] y_2-y_1 > 7.5) /\ (□_[0, 50] y_3-y_2 > 7.5) /\ (□_[0, 50] y_4-y_3 > 7.5) /\ (□_[0, 50] y_5-y_4 > 7.5)

Minimum simulation time: 100s

Input range:
- u_1: 0.0 <= u_1 <= 1.0
- u_2: 0.0 <= u_2 <= 1.0

Instance 1: Both input signals must be piecewise continuous with a finite number of discontinuities.

Instance 2: Both input signals must be piecewise constant functions, but consecutive discontinuities must be 5s apart.