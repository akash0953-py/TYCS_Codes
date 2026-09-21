import numpy as np 
from scipy import stats   

# GOODNESS OF FIT :-  CHI_SQUARE 
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

# Practice Question 
# A dice is rolled 60 times. The observed frequencies are:

# Face	1	2	3	4	5	6
# Observed	8	12	11	9	10	10

# Test at the 5% significance level whether the dice can be considered fair.

a = 0.05
observed = np.array([8,12,11,9,10,10])
faces = 6
expected = np.array([sum(observed) / faces] * faces)
dof = faces - 1
chi2 = sum(((observed - expected) ** 2) /expected)
p_value = stats.chi2.sf(chi2,dof)
if p_value > a:
    print("Accept Null Hypothesis")
else:
    print("Reject Null Hypothesis")

# Q1. A lottery machine has marbles with red, green, yellow and bluecolor.
# 20 marbels were drawn at random. The observations were as follows:[3,7,4,6]
# Find out if the machine is fair using Chi Square Test.

a = 0.05
observed = np.array([3,7,4,6])
categ = 4
dof = categ - 1
expected = np.array([observed.sum() / categ] * categ)
chi2 = sum(((observed - expected) ** 2 )/ expected)
p_value = stats.chi2.sf(chi2,dof)
if p_value > a:
    print("Fail to Reject Null Hypothesis")
else:
    print("Reject Null Hypothesis")

