function [tout, yout, xin] = run_pm(u_1)
    T = 10;
    u = [0' u_1'];

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