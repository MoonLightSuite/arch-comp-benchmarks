Fuel Control of an Automotive Powertrain - AFC

Model name: AbstractFuelControl_M1.slx
Matlab version >= 2017b

Inputs:
- u_1: Throttle pedal angle
- u_2: Engine speed

Outputs:
- y_1: Air-to-Fuel ratio error
- y_2: Controller Mode

Requirements in STL:
AFC27: □_[11, 50] (((u_1 < 8.8 /\ ◇_[0, 0.05] u_1 > 40.0) \/ (u_1 > 40.0 /\ ◇_[0, 0.05] u_1 < 8.8)) -> (□_[1, 5] |y_1| < 0.008))
AFC29: □_[11, 50] |y_1| < 0.007
AFC33: □_[11, 50] |y_1| < 0.007

Minimum simulation time: 55s

Input range:
- u_1:
    * For AFC27 and AFC29, 0.0 <= u_1 < 61.2
    * For AFC33, 61.2 <= u_1 <= 81.2
- u_2: 900 <= u_2 < 1100

Instance 1: Not Available

Instance 2:
- u_1: Piecewise constant function with 10 intervals of uniform length.
- u_2: Constant value.

Model parameters:

    simTime        = 55;
    measureTime    =  1;
    fault_time     = 60;
    spec_num       =  1;
    fuel_inj_tol   =  1;
    MAF_sensor_tol =  1;
    AF_sensor_tol  =  1;
