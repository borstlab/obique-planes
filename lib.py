# -*- coding: utf-8 -*-
"""
Created on Sun May 17 18:52:14 2020

@author: schuetzenberger
"""


import numpy as np

# general data analysis library

def LPF(data, axis, tau, dt):
    """ takes data (array), axis (integer), tau (float) and dt (float).
    returns LP-filtered data with time constant tau along axis using np.apply_along_axis.
    """ 
    def LPF_1axis(d):
    
        filter_alpha = dt/(tau+dt)
        o = np.zeros(d.shape)
        o[0] = d[0]
    
        for i in range(1,len(d)):
            o[i] = o[i-1]*(1.-filter_alpha) + filter_alpha*d[i]
        
        return o
    
    return np.apply_along_axis(LPF_1axis, axis, data)

