# This is the main program of GB parameter fitter

import sys
import os
import math
from scipy.optimize import minimize 
import Mean-Sqare-Diff  # call Mean-Square-Diff.py


# Define input parameters
# AMD_data is a list containing file names of PES data from AMD
# Fill in initial guess here 
# I just put in 0.0 for convenience
# shape matrix 1 shape_1[s1a,s1b,s1c]
# GB coefficient GB_coeff[epsilon,sigma,e1a,e1b,e1c,e2a,e2b,e2c,nu,mu,gamma]
global AMD_data
AMD_data = ["face2face.dat","end2end.dat","face2end.dat"]


shape_1 = [1.0,1.0,1.0] # shape matrix of ellipsoid 1
shape_2 = [1.0,1.0,1.0] # shape matrix of ellipsoid 2
GB_coeff = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1,1,1]

parameter = []

for i in range(len(shape_1)):
    parameter.append(shape_1[i])

for i in range(len(shape_2)):
    parameter.append(shape_2[i])

for i in range(len(GB_coeff)):
    parameter.append(GB_coeff[i])

# start to call subroutine computing mean 
# squared difference between AMD PES and 
# PES from GB parameter set
# simplex optimization can only be done with one
# single list of variables, namely, "parameter"

psi = 0.0 # value of mean square difference
psi =  Mean-Sqr-compute(parameter)


