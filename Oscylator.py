# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:43:29 2018

@author: Michał
"""

import numpy as n
import matplotlib.pyplot as plt
k=2
m=1

def oscilator(state,time):
    k=2
    v0=state[1]
    a=-k*state[0]
    return(n.array([v0,a]))

def Euler(y,t,dt,derivative):
    y_next=y+derivative(y,t)*dt
    return (y_next)

def f(y,t,dt,derivative):
    
    fo=derivative(y,t)*dt
    f1=derivative(y+dt/2,t+(dt/2))*dt
    f2=derivative(y+dt/2,t+(dt/2))*dt
    f3=derivative(y+dt,t+(dt))*dt
    y_next=y+1/6*(fo+2*f1+2*f2+f3)
    return(y_next)

xo=10
vo=0
dt=0.1
to=0
te=40
t=n.arange(to,te,dt)
N=len(t)
y=n.zeros([N,2])
y[0,0]=xo
y[0,1]=vo
for i in range(N-1):
    y[i+1]=f(y[i],t[i],dt,oscilator)


positions=[y[j,0] for j in range(N)]
velocity=[y[j,1] for j in range(N)]

fig, ax1= plt.subplots()
ax1.plot(t, positions)

fig, ax2= plt.subplots()
ax2.plot(t, velocity)
