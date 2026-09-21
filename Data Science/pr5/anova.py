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