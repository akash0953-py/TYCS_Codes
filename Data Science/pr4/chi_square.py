import numpy as np 
from scipy import stats   

observed = np.array([12,10,8,10,11,9]) 
print("Observed frequency : ",observed) 

faces = 6 

expected = np.array([observed.sum()/faces]*faces) 
print("Expected frequency : ",expected) 

dof = faces-1   

chi2 = sum(((observed-expected)**2)/expected) 
print("Chisquare Value : ",chi2) 

p_value = stats.chi2.sf(chi2,dof) 
print("Probability : ",p_value)   

chi2,p_value = stats.chisquare(observed,expected) 
print("Built-In Formula ",p_value)