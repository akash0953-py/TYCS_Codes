# 1. From generation to generation, the mean age when smokers first start to smoke varies.
# However, the standard deviation of that age remains constant of around 2.1 years. A survey of
# 40 smokers of this generation was done to see if the mean  starting age is at least 19.
# The sample mean was 18.1 with a sample standard deviation  of 1.3. Do the data  support the
# claim at the 5% level?
import numpy as np
from scipy import stats

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

# 2. The cost of a daily newspaper varies from city to city. However, the
# variation among prices remains steady with a standard deviation of 20p. A
# study was done to test the claim that the mean cost of a daily newspaper
# is 100p. Twelve costs yield a mean cost of 95p with a standard deviation
#  of 18p. Do the data  support the claim at the 1% level?

import numpy as np
from scipy import stats

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

# 3. Blood glucose levels for obese patients have a mean of 100 with a
# standard deviation of 15. A researcher thinks that a diet high in raw
# corn starch will have a positive or negative effect on blood glucose levels. A sample of 30
# patients who have tried the raw cornstarch diet have a mean
# glucose level of 140. Test the hypothesis that the raw cornstarch had an
# effect.

import numpy as np
from scipy import stats

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

# 4. Previously, an organization reported that teenagers spent 4.5 hours per
# week, on average , on the phone. The organization thinks that, currently,
# the mean  is higher. Fifteen randomly chosen teenagers were asked how
# many hours per week they spend on the phone. The sample mean  was
# 4.75 hours with a sample standard deviation  of 2.0. Conduct a hypothesis
#  test. The null and alternative hypotheses are:

import numpy as np
from scipy import stats

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


# 5.It is believed that Lake Tahoe Community College (LTCC) Intermediate
# Algebra students get less than seven hours of sleep per night, on Average
# . A survey of 22 LTCC Intermediate Algebra students generated a Mean  of
# 7.24 hours with a standard deviation  of 1.93 hours. At a level of
# significance of 5%, do LTCC Intermediate Algebra students get less than
# seven hours of sleep per night, on average ?

import numpy as np
from scipy import stats

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

# 6.A particular brand of tires claims that its deluxe tire averages at least 50,000 miles before it
# needs to be replaced. From past studies of this tire, the Standard deviation  is known to be
# 8,000. A survey of owners of that tire design is conducted. From the 28 tires surveyed, the 
# mean  lifespan was 46,500 miles with a standard deviation  of 9,800 miles. Using α=0.05, is
# the data highly inconsistent with the claim?

import numpy as np
from scipy import stats

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