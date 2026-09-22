import numpy as np
from scipy import stats
import pandas as pd

df = pd.read_csv("Data Science\pr5\College.csv")

ves = np.array(df['Vesasc'])
nga = np.array(df['Nga'])
bt = np.array(df['BT'])

n =5
k =3
N =15

ves_mean = ves.mean()
nga_mean = nga.mean()
bt_mean = bt.mean()

total_mean = np.array([ves_mean ,nga_mean , bt_mean]).mean()

a = (ves_mean - total_mean)**2
b = (nga_mean - total_mean)**2
c = (bt_mean - total_mean)**2

total_sum_mean = n * (a+b+c)
ssb = total_sum_mean / (k-1)

ssw = (sum((ves - ves_mean) **2 ) + sum((nga - nga_mean) ** 2) + sum((bt - bt_mean) ** 2)) / (N-k)

f = ssb/ ssw
p = stats.f.sf(f,(k-1),(N-k))

print("Variance between the group :- ",ssb)
print("Variance within the group :- ", ssw)
print("F statistics score :- ", f)
print("P-value :- ", p)

if p < 0.05:
    print("Reject Null Hypothesis")
else:
    print("Fail to Reject Null Hypothesis")

# PRACTICE QUESTION 
# Given the marks of students from 3 different teaching methods, 
# perform One-Way ANOVA and determine whether there is 
# a significant difference between the group means.

import numpy as np
from scipy import stats

A = np.array([85, 90, 88, 92, 87])
B = np.array([78, 82, 80, 79, 81])
C = np.array([90, 94, 91, 93, 95])

amean = A.mean()
bmean = B.mean()
cmean = C.mean()

n = 5
k = 3
N = 15

total_mean = (amean + bmean + cmean)/3

a = (amean - total_mean) ** 2
b = (bmean - total_mean) ** 2
c = (cmean - total_mean) ** 2

tsm= n * (a+b+c)
ssb = tsm/(k-1)

ssw = ( sum((A - amean)**2) + sum((B - bmean)**2) + sum((C - cmean)**2)) / (N-k)

f = ssb/ssw
p_value = stats.f.sf(f,(k-1),(N-k))

alpha = 0.05
if p_value > alpha:
    print('faile to reject null hypo')
else:
    print('reject null hypo ')
