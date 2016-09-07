# This is the main program of GB parameter fitter

import sys
import os
import math
import Mean-Sqare-Diff  # call Mean-Square-Diff.py


# Define input parameters
# AMD_data is a list containing file names of PES data from AMD
# Fill in initial guess here 
# I just put in 0.0 for convenience
# shape matrix 1 shape_1[s1a,s1b,s1c]
# GB coefficient GB_coeff[epsilon,sigma,e1a,e1b,e1c,e2a,e2b,e2c,nu,mu,gamma]

AMD_data = ["face2face.dat","end2end.dat","face2end.dat"]
shape_1 = [1.0,1.0,1.0] # shape matrix of ellipsoid 1
shape_2 = [1.0,1.0,1.0] # shape matrix of ellipsoid 2
GB_coeff = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1,1,1]


# start to call subroutine computing mean 
# squared difference between AMD PES and 
# PES from GB parameter set

psi = 0.0 # value of mean square difference
psi =  Mean-Square-Diff.compute(AMD_data,shape_1,shape_2,GB_coeff)


