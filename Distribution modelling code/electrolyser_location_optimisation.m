% 3YP electrolyser location optimisation code
close all
clc

n = 5;                    % number of clients (depots)

xc = [-1.21726,-1.19719,-1.19285,-1.4946,-1.24657,-1.26362];  % x coordinates 
yc = [51.71164,51.72743,51.73705,51.78529,51.6224,51.74548];  % y coordinates
xc_range = linspace(-1.5,-1.1,100); % 100 different x coordinates will be tried
yc_range = linspace(51,52,100); % 100 different y coordinates will be tried
coord = [xc;        
         yc];
 
electrolyser = coord(:,1);                                    % Initial suggested location for electrolyser

Iterations = zeros(1);
for k = 1:length(xc_range)                                   % For every x possiblility
    for q = 1:length(yc_range) 
        d1_prev = sqrt((coord(1,1)-coord(1,2))^2 + (coord(2,1)-coord(2,2))^2);
        d2_prev = sqrt((coord(1,1)-coord(1,3))^2 + (coord(2,1)-coord(2,3))^2);
        d3_prev = sqrt((coord(1,1)-coord(1,4))^2 + (coord(2,1)-coord(2,4))^2);
        d4_prev = sqrt((coord(1,1)-coord(1,5))^2 + (coord(2,1)-coord(2,5))^2);
        d5_prev = sqrt((coord(1,1)-coord(1,6))^2 + (coord(2,1)-coord(2,6))^2);
        d_total_prev = d1_prev+d2_prev+d3_prev+d4_prev+d5_prev;
        d1 = sqrt((xc_range(k)-coord(1,2))^2 + (yc_range(q)-coord(2,2))^2);      % Distance between electrolyser and first depot
        d2 = sqrt((xc_range(k)-coord(1,3))^2 + (yc_range(q)-coord(2,3))^2);
        d3 = sqrt((xc_range(k)-coord(1,4))^2 + (yc_range(q)-coord(2,4))^2);
        d4 = sqrt((xc_range(k)-coord(1,5))^2 + (yc_range(q)-coord(2,5))^2);
        d5 = sqrt((xc_range(k)-coord(1,6))^2 + (yc_range(q)-coord(2,6))^2);
        d_total_now = d1+d2+d3+d4+d5; 
        if d_total_now < d_total_prev
            coord(1,1) = xc_range(k);
            coord(2,1) = yc_range(q);
            Iterations = [Iterations d_total_now]    % Used to test program, to see if distances get smaller
        end
    end
end

set(gca,'color','none')     % Removing background
scatter(coord(1,1),coord(2,1),10,'r')   % Plot the suggested electrolyser location
hold on
scatter(coord(1,2:end),coord(2,2:end),10,'b')   % 2 = marker size

plot([coord(1,1),coord(1,2)],[coord(2,1),coord(2,2)],'g')
hold on
plot([coord(1,1),coord(1,3)],[coord(2,1),coord(2,3)],'g')
plot([coord(1,1),coord(1,4)],[coord(2,1),coord(2,4)],'g')
plot([coord(1,1),coord(1,5)],[coord(2,1),coord(2,5)],'g')
plot([coord(1,1),coord(1,6)],[coord(2,1),coord(2,6)],'g')
% Removing tick labels
set(gca,'YTickLabel',[]); 
set(gca,'YTick',[]); 
set(gca,'XTickLabel',[]);
set(gca,'XTick',[]); 
coord(:,1)
set(gca,'color','none') % Removing background