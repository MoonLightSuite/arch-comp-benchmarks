Automatic Transmission - AT

Model name: Autotrans_shift.mdl
Matlab version >= 2018b

Inputs:
- u_1: Throttle percentage
- u_2: Brake torque

Outputs:
- y_1: Vehicle speed
- y_2: Engine speed
- y_3: Gear

Requirements in STL:
AT1:    □_[0, 20] y_1 < 120
AT2:    □_[0, 10] y_2 < 4750
AT51:   □_[0, 30] ((!(y_3 ~= 1) /\ ◇_[0.001, 0.1] (y_3 == 1)) -> ◇_[0.001, 0.1] □_[0.0, 2.5] (y_3 == 1))
AT52:   □_[0, 30] ((!(y_3 ~= 2) /\ ◇_[0.001, 0.1] (y_3 == 2)) -> ◇_[0.001, 0.1] □_[0.0, 2.5] (y_3 == 2))
AT53:   □_[0, 30] ((!(y_3 ~= 3) /\ ◇_[0.001, 0.1] (y_3 == 3)) -> ◇_[0.001, 0.1] □_[0.0, 2.5] (y_3 == 3))
AT54:   □_[0, 30] ((!(y_3 ~= 4) /\ ◇_[0.001, 0.1] (y_3 == 4)) -> ◇_[0.001, 0.1] □_[0.0, 2.5] (y_3 == 4))
AT6a:   (□_[0, 30] y_2 < 3000) -> (□_[0, 4] y_1 < 35)
AT6b:   (□_[0, 30] y_2 < 3000) -> (□_[0, 8] y_1 < 50)
AT6c:   (□_[0, 30] y_2 < 3000) -> (□_[0, 20] y_1 < 65)
AT6abc: (□_[0, 30] y_2 < 3000) -> ((□_[0, 4] y_1 < 35) /\ (□_[0, 8] y_1 < 50) /\ (□_[0, 20] y_1 < 65))

Minimum simulation time: 33s

Input range:
- u_1: 0 <= u_1 <= 100
- u_2: 0 <= u_2 <= 325

Instance 1: Both input signals must be piecewise continuous with a finite number of discontinuities.

Instance 2: Both input signals must be piecewise constant functions, but consecutive discontinuities must be at least 5s apart.