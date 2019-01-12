# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 11:08:19 2019

@author: Michał
"""

import numpy as np

d=3.844*10**5
m_e=5.9742*10**24
m_M=7.35*10**22
T=27.322*86400
G=6.6726*10**(-11)

def force(m,M,r):

    F=-G*(m*M/r**2)
    return F


def r_E(m_M,m_E,d):

    r=(m_M/(m_M+m_E))*d
    return r


def r_M(m_M,m_E,d):

    r=(m_E/(m_M+m_E))*d
    return r

ro=2*np.pi/T
#R orbity 6800 km
#y=np.zeros([n,4])

##################################Zadanie 1 ###################################
#Policzyć prędkosc dla R=6800








