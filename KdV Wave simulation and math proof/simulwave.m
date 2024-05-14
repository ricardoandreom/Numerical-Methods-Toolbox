c=0.20; %velocidade do soliton

% Simulação do soliton
x=0:0.5:100;
y=0:0.5:100;

[xx,yy]=meshgrid(x,y);

figure
for t=0:1:300
    u=3*c*sech(sqrt(c)/(-2)*(xx-c*t)).^2;
    surf(u);
    axis([0 50 0 100 0 0.7])
    pause(0.01);
end
