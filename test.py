import pandas as pd
import numpy as np
from scipy import stats

observed =  np.array([[23,30,45],
                        [54,67,89]])

row_sum = observed.sum(axis=1)
col_sum = observed.sum(axis=0)
grand_total = observed.sum()

dof = (observed.shape[0] - 1) * (observed.shape[1] -1)

expected = np.outer(row_sum ,col_sum) / grand_total

chi2 = (((observed - expected)**2 / expected)).sum()
p = stats.chi2.sf(chi2,dof)

print(p)