function [ PL_dB ] = Path_loss_model(d_Km, f_MHz, varargin)
% Path_Loss_model function
% Input: 
% d_Km is the distance between transmitter and reciever in Km.
% f_MHz is the frequency in MHz
% nargin is varibale number of inputs 

% Path_loss_model(d_Km, f_MHz, Env,h_GW, h_ED ) for Outdoor
% Path_loss_model(d_Km, f_MHz, Env,wall, floor ) for Indoor
% Env : environement types (rural, urban, indoor, campus)
% h_GW : antenna height of the gateway
% h_ED : antenna height of the end-device
% wall : number of wall in case of indoor
% floor : number of floor in case of indoor

%% Read input or assign default values
switch nargin   
    case 2
        h_ED = 1; % Default value
        h_GW = 200;  % Default value
        Env = 'urban'; % Default value
    case 3
        Env = varargin{1};
        if (strcmp( Env, 'indoor')==1);
            wall = 1;
            floor = 0;
        elseif (strcmp( Env, 'out_in')==1);
            wall = 1;
            floor = 0;
        else
            h_ED = 1; % Default value
            h_GW = 200;  % Default value
        end
    case 4
        Env = varargin{1};
        if (strcmp( Env, 'indoor')==1);
            wall = varargin{2};
            floor = 0;
        else
            h_GW = varargin{2}; % Default value
            h_ED = 200;  % Default value
        end
    case 5
        Env = varargin{1};
        if (strcmp( Env, 'indoor')==1)
            wall = varargin{2};
            floor = varargin{3};
        elseif (strcmp( Env, 'out_in')==1);
            wall = varargin{2};
            floor = varargin{3};
        else
            h_GW = varargin{2}; % Default value
            h_ED = varargin{3} ; % Default value
        end
end

%% Compute the path-loss value according to the Env Types
switch Env
    case 'rural' % rural
        PL_dB = 30.33*log10(d_Km)+111.75-6.685*log10(h_ED);
        
    case 'urban' % Urban
        PL_dB = 41.79*log10(d_Km)+102.86-6.3*log10(h_ED);
    case 'indoor' % Indoor building
        Lf = 10; % Lf  = 12; cst = 113.3 n = 26.47 Lw =1.42 sigma = 8.29
        Lw  = 1.412;
        n = 28.51;
        cst = 120.4;
        Af = floor.^((floor + 2)./(floor + 1) -0.46).*Lf;
        Aw = Lw.*wall;
        PL_dB = n*log10(d_Km)+Af +Aw+cst;
    case 'out_in' % Indoor building
        Lf = 10; % Lf  = 12; cst = 113.3 n = 26.47 Lw =1.42 sigma = 8.29
        Lw  = 1.412;
        Af = floor.^((floor + 2)./(floor + 1) -0.46).*Lf;
        Aw = Lw.*wall;
        PL_dB = 41.79*log10(d_Km)+102.86+Af +Aw;
    case 'usj_campus'  % usj campus
        PL_dB = 31.19*log10(d_Km) + 140.7-4.7*log10(h_ED);
end

end

