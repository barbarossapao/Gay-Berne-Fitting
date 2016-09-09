import numpy as np
from scipy.optimize import minimize

	
def compute(x):
	print string
	return (x[0]-1)*(x[0]-1)+(x[1]-1)*(x[1]-1)+(x[2]-1)*(x[2]-1)
	

x0 = [0.7,1.2,1.1]

global string 
string = ['test','fuck','duck']

compute(x0)
res = minimize(compute,x0,method='nelder-mead',options={'xtol': 1e-8, 'disp': True})

print res.x


