import numpy as np
from scipy import stats

observed = np.array([[25, 30, 15],
                     [30, 25, 40]])
row_sum = observed.sum(axis=1)
col_sum = observed.sum(axis=0)
grand_total = observed.sum()

expected = np.outer(row_sum, col_sum) / grand_total
dof = (observed.shape[0]-1) * (observed.shape[1]-1)

chi2 = (((observed - expected) ** 2) / expected).sum()
p_value = stats.chi2.sf(chi2, dof)
print("Chisquare Value:", chi2)
print("Probability:", p_value)

# Built-in:
chi2, p_value, dof, expected = stats.chi2_contingency(observed)
print("Built-In Formula", p_value)

# 🧪 Chi-Square Test of Independence — Practice
# A college wants to find out whether gender and preferred mode of transport are related.
# A survey of 120 students gave the following results:
# 	Bus	Train	Bike
# Male	25	20	15
# Female	15	25	20

observed = np.array([[25,20,15],
                    [15,25,20]])

row_sum = observed.sum(axis=1)
col_sum = observed.sum(axis=0)

grand_total = observed.sum()

expected = np.outer(row_sum,col_sum) / grand_total
dof = (observed.shape[0] - 1) * (observed.shape[1] - 1)

chi2 = sum(((observed - expected) ** 2) / expected)
p_value = stats.chi2.sf(chi2 , dof)

# 2. Test for Independence.
# Q1. A survey was done to find out if there is any effect of social media ads on buying behaviour.
# Observations were as follows:
# Facebook: Bought:20, Not Bought: 80
# Instagram: Bought: 40, Not Bought: 60
# Twitter: Bought: 30, Not Bought: 70
# Find out if there is any effect of social media platform used on the buying behavior using Chi Square Test.

observed = np.array([[20,80],
                    [30,70],
                    [30,70]])
row_sum = observed.sum(axis=0)
col_sum = observed.sum(axis=1)
grand_total = observed.sum()

expected = np.outer(row_sum,col_sum) / grand_total
dof  = (observed.shape[0] - 1) * (observed.shape[1] - 1)
chi2 = sum(((observed - expected) ** 2) / expected)
p_value = stats.chi2.sf(chi2,dof)