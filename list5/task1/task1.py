import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

def rhs(u,t = 0):
    S = u[0]
    I = u[1]
    dsdt = b * S - beta * I *S
    didt = beta * I * S - k * I
    return np.array([dsdt, didt])

def phase_plane(init):
    u = odeint(rhs,init,t)  
    plt.plot(u[:,0], u[:,1])
    ymax = plt.ylim(bottom=0)[1]                    
    xmax = plt.xlim(left=0)[1]
    nb_points = 20
    x = np.linspace(0, xmax, nb_points)
    y = np.linspace(0, ymax, nb_points)
    X1 , Y1  = np.meshgrid(x, y)
    DX1, DY1 = rhs([X1, Y1])
    M = (np.hypot(DX1, DY1))
    M[ M == 0] = 1.
    DX1 /= M
    DY1 /= M
    plt.quiver(X1, Y1, DX1, DY1, M)
    plt.xlabel('susceptible')
    plt.ylabel('infected')

b = 3
beta = 3
k = 3
S0 = 1
t = np.linspace(0,10,1000)

I0 = 0.1
initial = [S0,I0]
u = odeint(rhs,initial,t)
figure1 = plt.subplots(1, 2, figsize=(10,5))
plt.subplot(1, 2, 1)
plt.title(r"$I_0 = $" + str(I0))
plt.plot(t,u[:,0],'g')      # susceptible
plt.plot(t,u[:,1],'r')      # infected
plt.legend(('susceptible','infected'))
plt.xlabel('t')
plt.subplot(1, 2, 2)
plt.title(r"$I_0 = $" + str(I0))
phase_plane([S0, I0])
plt.show()

I0 = 0.5
initial = [S0,I0]
u = odeint(rhs,initial,t)
figure2 = plt.subplots(1, 2, figsize=(10,5))
plt.subplot(1, 2, 1)
plt.title(r"$I_0 = $" + str(I0))
plt.plot(t,u[:,0],'g')      # susceptible
plt.plot(t,u[:,1],'r')      # infected
plt.legend(('susceptible','infected'))
plt.xlabel('t')
plt.subplot(1, 2, 2)
plt.title(r"$I_0 = $" + str(I0))
phase_plane([S0, I0])
plt.show()

I0 = 1.3
initial = [S0,I0]
u = odeint(rhs,initial,t)
figure3 = plt.subplots(1, 2, figsize=(10,5))
plt.subplot(1, 2, 1)
plt.title(r"$I_0 = $" + str(I0))
plt.plot(t,u[:,0],'g')      # susceptible
plt.plot(t,u[:,1],'r')      # infected
plt.legend(('susceptible','infected'))
plt.xlabel('t')
plt.subplot(1, 2, 2)
plt.title(r"$I_0 = $" + str(I0))
phase_plane([S0, I0])
plt.show()