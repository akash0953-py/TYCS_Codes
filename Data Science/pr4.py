import numpy as np
from scipy import stats

# ============================================================
# Q1. Mean starting age of smokers (is it at least 19?)
# ============================================================
print("Q1:")
x = 18.1
u = 19
psd = 2.1
n = 40
a = 0.05

z = round((x - u) / (psd / np.sqrt(n)), 2)
print("Z value =", z)

p = stats.norm.cdf(z)
print("P value =", p)

if p > a:
    print("Accept Null Hypothesis")
else:
    print("Reject Null Hypothesis")

print()

# ============================================================
# Q2. Mean cost of a daily newspaper (is it 100p?)
# ============================================================
print("Q2:")
x = 95
u = 100
psd = 20
n = 12
a = 0.01

z = round((x - u) / (psd / np.sqrt(n)), 2)
print("Z value =", z)

p = 2 * stats.norm.cdf(z)   # Two-tailed test
print("P value =", p)

if p > a:
    print("Accept Null Hypothesis")
else:
    print("Reject Null Hypothesis")

print()

# ============================================================
# Q3. Blood glucose levels on raw cornstarch diet
# ============================================================
print("Q3:")
x = 140
u = 100
psd = 15
n = 30
a = 0.05

z = round((x - u) / (psd / np.sqrt(n)), 2)
print("Z value =", z)

p = 2 * (1 - stats.norm.cdf(z))
print("P value =", p)

if p > a:
    print("Accept Null Hypothesis")
else:
    print("Reject Null Hypothesis")

print()

# ============================================================
# Q4. Teenagers' phone usage hours per week
# ============================================================
print("Q4:")
x = 4.75
u = 4.5
ssd = 2
n = 15
a = 0.05

t = round((x - u) / (ssd / np.sqrt(n)), 2)
print("t value =", t)

p = 1 - stats.t.cdf(t, df=n-1)
print("P value =", p)

if p > a:
    print("Accept Null Hypothesis")
else:
    print("Reject Null Hypothesis")

print()

# ============================================================
# Q5. LTCC students' hours of sleep per night
# ============================================================
print("Q5:")
x = 7.24
u = 7
ssd = 1.93
n = 22
a = 0.05

t = round((x - u) / (ssd / np.sqrt(n)), 2)
print("t value =", t)

p = stats.t.cdf(t, df=n-1)
print("P value =", p)

if p > a:
    print("Accept Null Hypothesis")
else:
    print("Reject Null Hypothesis")

print()

# ============================================================
# Q6. Tire lifespan claim (at least 50,000 miles)
# ============================================================
print("Q6:")
x = 46500
u = 50000
psd = 8000
n = 28
a = 0.05

z = round((x - u) / (psd / np.sqrt(n)), 2)
print("Z value =", z)

p = stats.norm.cdf(z)
print("P value =", p)

if p > a:
    print("Accept Null Hypothesis")
else:
    print("Reject Null Hypothesis")