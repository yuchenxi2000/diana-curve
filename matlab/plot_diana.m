s=0:0.01:134.33236086148722;

x = diana_x(s);
y = diana_y(s);

% 去掉间断点连线（置nan）
% 参数的s步长需要足够小，不然间断点连线不会全部被去除，而且会导致不是间断点的地方间断
for t=1:size(s, 2)-1
    if (x(t+1) - x(t)) ^ 2 + (y(t+1) - y(t)) ^ 2 > 100
        x(t+1) = nan;
        y(t+1) = nan;
    end
end

plot(x, y)
axis equal

