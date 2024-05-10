function [tout, yout, xin] = run_neural(u, T)
    ts = u(:,1);
    us = u(:,2:end);
    
    tin = 0:0.01:T;
    xin = interp1(ts, us, tin, 'previous');
    % disp(size(xin))
    % disp(size(tin))
    u = [tin' xin'];

    % disp(u)
    % plot(u)

    assignin('base','u',u);
    assignin('base','T',T);


    load_system('narmamaglev_v1');
    
    result = sim('narmamaglev_v1', ...
        'StopTime', 'T', ...
        'LoadExternalInput', 'on', 'ExternalInput', 'u', ...
        'SaveTime', 'on', 'TimeSaveName', 'tout', ...
        'SaveOutput', 'on', 'OutputSaveName', 'yout', ...
        'SaveFormat', 'Array');
    tout = result.tout;
    yout = result.yout;
end