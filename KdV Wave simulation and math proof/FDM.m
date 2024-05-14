function FDM

N=16;
h=1/(N+1);
T=10;
M=40;
dt=T/M;

t=linspace(0,T,M);
x=linspace(0,N,N/h);

u=zeros(length(x),length(t)); 

c=0.20;%velocidade da onda


%CONDIÇÕES INICIAIS
u0=3*c*sech(sqrt(c)/(-2)*x).^2;
for n=2:length(x)-1
    u(n,1)=u0(n);%U_j^0
end


for m=1:length(t)-1
    u(1,m)=3*c*sech(-sqrt(c)/(-2)*c*m)^2; %U0^m
    %u(N,m)=3*c*sech(-sqrt(c)/(-2)*(1-c*m))^2; %U_N^m
end


for m=1:length(t)-1
    for n=3:length(x)-2
         u(n,m+1)= u(n,m)*(1-(dt/h)*(u(n+1,m))-u(n,m))-(dt/(2*h^3))*(-u(n-2,m)+2*u(n-1,m)-2*u(n+1,m)+u(n+2,m));
         plot(x,u(:,m+1));
         pause(0.01);
    end
    %u(length(x),m)=3c*sech(sqrt(c)/(-2)*(1-c*m))^2;
end
    
end
