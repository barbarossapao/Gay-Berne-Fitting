# This is the main program of GB parameter fitter

import sys
import os
import math
import Mean-Sqare-Diff  # call Mean-Square-Diff.py


# Define input parameters
# Fill in initial guess here 
# I just put in 0.0 for convenience

epsilon = 0.0
sigma = 0.0
Sa = 0.0 # shape_a
Sb = 0.0 # shape_b
Sc = 0.0 # shape_c
eia = 0.0 #epsilon_a
eib = 0.0 #epsilon_b
eic = 0.0 #epsilon_c

# I suggest not to change default setting of 
# nu, mu, and gamma
nu = 1.0 
mu = 1.0
gamma = 1.0


# start to call subroutine computing mean 
# squared difference between AMD PES and 
# PES from GB parameter set

psi = 0.0 # value of mean square difference
psi =  Mean-Square-Diff.compute(epsilon,sigma,Sa,Sb,Sc,eia,eib,eic,nu,mu,gamma)


