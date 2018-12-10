# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 09:48:33 2018

@author: mmazurek
"""

X5=[0.906179845938664,-0.906179845938664, 0.538469310105683, 
-0.538469310105683,
0.000000000000000]
W5=[ 0.236926885056189, 0.236926885056189, 0.478628670499367, 
0.478628670499367, 0.568888888888889]

import numpy as np
import matplotlib.pylab as plt

def fi(x,y,xp,yp):
    ro=1.
    
    fi=ro*((x-xp)**2+(y-yp)**2)**-0.5
    return fi

def int1(x,xp,yp):
    i=0
    calka1=0
    for y in X5:
        calka1+=W5[i]*fi(x,y,xp,yp)
        i+=1
    return calka1

def int2(xp,yp):  
    i=0
    calka2=0
    for x in X5:
        calka2+=W5[i]*int1(x,xp,yp)
        i+=1
    return calka2
    
print("Potencjal: ", int2(2,2))

from mpl_toolkits.mplot3d import Axes3D

x = np.arange(1.1, 5, 0.1)
y = np.arange(1.1, 5, 0.2)
xx, yy = np.meshgrid(x, y, sparse=True)
z=int2(xx,yy)

fig=plt.figure()
ax3=fig.add_subplot(111,projection='3d')
ax3.plot_surface(xx,yy,z)
plt.show()

#Axes3D.plot_surface(x, y, z)
