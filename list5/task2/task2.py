import matplotlib.pyplot as plt
import numpy as np 
from scipy.integrate import odeint

def SIR(u,t=0):
    S = u[0]
    I = u[1]
    R = u[2]
    dsdt = -beta * S *I
    didt = beta *S *I - r*I
    drdt = r*I
    return np.array([dsdt, didt, drdt])

def simple_SIR(u,t=0): #SI model
    S = u[0]
    I = u[1]
    dsdt = -beta * S *I
    didt = beta *S *I - r*I
    return np.array([dsdt, didt])

def phase_plane(init):
    u = odeint(simple_SIR,init,t)  
    plt.plot(u[:,0], u[:,1])
    ymax = plt.ylim(bottom=0)[1]                    
    xmax = plt.xlim(left=0)[1]
    nb_points = 20
    x = np.linspace(0, xmax, nb_points)
    y = np.linspace(0, ymax, nb_points)
    X1 , Y1  = np.meshgrid(x, y)
    DX1, DY1 = simple_SIR([X1, Y1])
    M = (np.hypot(DX1, DY1))
    M[ M == 0] = 1.
    DX1 /= M
    DY1 /= M
    plt.quiver(X1, Y1, DX1, DY1, M)
    plt.xlabel('susceptible')
    plt.ylabel('infected')

N = 1000
I0 = 1
R0 = 0
S0 = N - I0 -R0
t = np.linspace(0,10,1000)

# R_0 > 1

figure1 = plt.subplots(1, 2, figsize=(10,5))
plt.subplot(1, 2, 1)
beta = 0.05
r = 4
R_0 = beta*N/r
initial = [S0,I0,R_0]
u = odeint(SIR,initial,t)
plt.plot(t,u[:,0],'green')      # susceptible
plt.plot(t,u[:,1],'red')        # infected
plt.plot(t,u[:,2],'blue')      # recovered
plt.legend(('susceptible','infected','recovered'))
plt.title(r"$R_0 = $" + str(R_0) + r"$, \beta = $" + str(beta) + r"$, r = $" + str(r))
plt.subplot(1, 2, 2)
beta = 0.01
r = 9
R_0 = (beta*N)/r
initial = [S0,I0,R_0]
u = odeint(SIR,initial,t)
plt.plot(t,u[:,0],'green')      # susceptible
plt.plot(t,u[:,1],'red')        # infected
plt.plot(t,u[:,2],'blue')      # recovered
plt.legend(('susceptible','infected','recovered'))
plt.title(r"$R_0 = $" + str(R_0) + r"$, \beta = $" + str(beta) + r"$, r = $" + str(r))
plt.show()


# R_0 < 1

figure2 = plt.subplots(1, 2, figsize=(10,5))
plt.subplot(1, 2, 1)
beta = 0.015
r = 20
R_0 = (beta*N)/r
initial = [S0,I0,R_0]
u = odeint(SIR,initial,t)
plt.plot(t,u[:,0],'green')      # susceptible
plt.plot(t,u[:,1],'red')        # infected
plt.plot(t,u[:,2],'blue')      # recovered
plt.legend(('susceptible','infected','recovered'))
plt.title(r"$R_0 = $" + str(R_0) + r"$, \beta = $" + str(beta) + r"$, r = $" + str(r))
plt.subplot(1, 2, 2)
beta = 0.001
r = 10
R_0 = (beta*N)/r
initial = [S0,I0,R_0]
u = odeint(SIR,initial,t)
plt.plot(t,u[:,0],'green')      # susceptible
plt.plot(t,u[:,1],'red')        # infected
plt.plot(t,u[:,2],'blue')      # recovered
plt.legend(('susceptible','infected','recovered'))
plt.title(r"$R_0 = $" + str(R_0) + r"$, \beta = $" + str(beta) + r"$, r = $" + str(r))
plt.show()


# simple SIR
figure3 = plt.figure(figsize=(15,5))
N = 1000
beta = 0.02
r = 5
R0 = (N*beta)/r

plt.subplot(1, 3, 1)
I0 = 1
S0 = 999
phase_plane([S0, I0])
plt.title(r"$S_0 = $" + str(S0) + r"$, I_0 = $" + str(I0))

plt.subplot(1, 3, 2)
I0 = 50
S0 = 950
phase_plane([S0, I0])
plt.title(r"$S_0 = $" + str(S0) + r"$, I_0 = $" + str(I0))

plt.subplot(1, 3, 3)
I0 = 250
S0 = 750
phase_plane([S0, I0])
plt.title(r"$S_0 = $" + str(S0) + r"$, I_0 = $" + str(I0))

plt.show()

# total number of individuals infected

N = 1000
beta_list = np.linspace(0,1,10)
r_list = np.linspace(11,1,10)

R_0 = []
I0 = 1
S0 = 999
infected =[]

for i in range(len(r_list)):
    beta = beta_list[i]
    r = r_list[i]
    u = odeint(simple_SIR,[S0,I0],t)
    S,I=u.T
    infected = infected + [max(I)]
    R_0 = R_0 + [beta*N/r]

figure4 = plt.figure()
plt.plot(R_0,infected)
plt.xlabel("R_0")
plt.ylabel("infected")
plt.title("$I(R_0)$")
plt.show()

