# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 10:21:35 2017

@author: zcao

This code is from Wikipedia Euler–Maruyama method
Url https://en.wikipedia.org/wiki/Euler%E2%80%93Maruyama_method#Computer_implementation

"""

import numpy as np
import matplotlib.pyplot as plt

num_sims = 5
N        = 1000

y_init   = 0
t_init   = 3
t_end    = 7

c_theta  = 0.7
c_mu     = 1.5
c_sigma  = 0.06

def mu(y, t): 
    return c_theta * (c_mu - y)
        
def sigma(y, t): 
    return c_sigma

dt   = float(t_end - t_init) / N
dW   = lambda dt: np.random.normal(loc = 0.0, scale = np.sqrt(dt))

t    = np.arange(t_init, t_end, dt)
y    = np.zeros(N)
y[0] = y_init

for i_sim in range(num_sims):
    for i in range(1, t.size):
        a = mu(y[i-1], (i-1) * dt)
        b = sigma(y[i-1], (i-1) * dt)
        y[i] = y[i-1] + a * dt + b * dW(dt)
    plt.plot(t, y)
#plt.savefig("UO.pdf")
plt.show()


#### OU MCMC  ####
import matplotlib.pyplot as plt

np.random.seed(2017)
n  = 100
s  = np.linspace(0,1,n)
x  = np.zeros(n)
y  = np.zeros(n)
x0 = np.random.uniform(1,-1,1)
#dt = [1/n] * n   ## equal space dt
sm = 1/np.random.choice(range(1,n+1),n,replace = True)
dt = sm / sum(sm)  ## NOT equal space dt
gam     = 1
trueTau = 1
trueSig = 1

x[0] = x0 + np.random.normal(scale = trueTau, size =  1)
for k in range(1,n):
    x[k] = np.exp(-gam*dt[k]) * x[k-1] + np.random.normal(scale = np.exp(-2*gam*dt[k]),size=1)

y = x + np.random.normal(scale = trueSig, size = n)

plt.plot(s,x, 'r-',label = 'x' )
plt.scatter(s,x, color = 'red')
plt.plot(s,y, 'b-', label = 'y')
plt.scatter(s,y, color = 'blue')
plt.title('OU process')
plt.legend(loc = 'upper left')
plt.show()








