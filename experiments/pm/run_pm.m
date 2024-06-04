function [tout, yout, xin] = run_pm(u, T)
ts = u(:,1);
us = u(:,2:end);

tin = 0:0.01:T;
xin = interp1(ts, us, tin, 'previous');
u = [tin' xin'];

assignin('base','u',u);
assignin('base','T',T);

load_system('Model1_Scenario1_Correct');

result = sim('Model1_Scenario1_Correct', ...
    'StopTime', 'T', ...
    'LoadExternalInput', 'on', 'ExternalInput', 'u', ...
    'SaveTime', 'on', 'TimeSaveName', 'tout', ...
    'SaveOutput', 'on', 'OutputSaveName', 'yout', ...
    'SaveFormat', 'Array');
tout = result.tout;
yout = result.yout;
end