import numpy as np
from scipy import stats
# Z - TEST :
z = 1
# TWO TAILED TEST
p = 2 * (1 - stats.norm.cdf(abs(z)))

# LEFT TAILED TEST 
p = stats.norm.cdf(z)

# RIGTH TAILED TEST
p = 1 - stats.norm.cdf(z)

# T - TEST :
n = 10
t = 1
df = n - 1
# TWO TAILED TEST
p = 2 * (1 - stats.t.cdf(abs(t), df))

# LEFT TAILED TEST
p = stats.t.cdf(t, df)

# RIGHT TAILED TEST
p = 1 - stats.t.cdf(t, df)

# 1. From generation to generation, the mean age when smokers first start to smoke varies.
# However, the standard deviation of that age remains constant of around 2.1 years. A survey of
# 40 smokers of this generation was done to see if the mean starting age is at least 19.
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

psd = 20
u = 100
x = 95
n = 12
a = 0.01

z = round(( x-u) / (psd / np.sqrt(n)),2)

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

u = 4.5
x = 4.75
ssd =2.0
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

# practice question 
# A company claims that the average battery life of its phone is 10 hours. A researcher believes that the actual average battery life is greater than 10 hours.

# A sample of 36 phones has an average battery life of 10.8 hours. The population standard deviation is 2.4 hours.

# Test the claim at the 5% significance level.

import numpy as np
from scipy import stats

n = 36
u = 10
x = 10.8
psd = 2.4
a = 0.05

z = round( (x-u)/ (psd / np.sqrt(n)) ,2)

p = 1 - stats.norm.cdf(z)

if p > a:
    print("Accept Null Hypothesis")
else:
    print("Reject Null Hypothesis")

# The average amount of time a student spends on social media is believed to be 3 hours per day, 
# with a population standard deviation of 0.8 hours. A researcher wants to determine 
# whether students who use a new productivity app have a different average social-media usage time.
# A sample of 36 students using the app has a mean usage time of 2.7 hours per day.
import numpy as np
from scipy import stats

# h0 is u = 3
# h1 is u < 3
psd = 0.8 
n = 36
x = 2.7
u = 3
a = 0.05

z = round((x-u)/(psd / np.sqrt(n))  ,2)
p = stats.norm.cdf(z)

if p > a:
    print("Accept Null Hypothesis")
else:
    print("Reject Null Hypothesis")

# The mean lifetime of a particular type of light bulb is 1200 hours. The standard deviation is known to be 100 hours.
# A manufacturer introduces a new production method and wants to determine whether the new method increases the average lifetime.
# A sample of 49 bulbs produced using the new method has a mean lifetime of 1235 hours.
# Test at the 1% significance level.

import numpy as np
from scipy import stats

u = 1200 
psd = 100
n =49
x = 1235
a = 0.01

z = ((x-u) / (psd / np.sqrt(n))  ,2)
p = 1 - stats.norm.cdf(z)

if p > a:
    print("Accept Null Hypothesis")
else:
    print("Reject Null Hypothesis")

# The average amount of time required to complete a certain computer task is 50 seconds, 
# with a population standard deviation of 8 seconds. A new software tool is introduced, and 
# a researcher wants to determine whether the new tool changes the average completion time.
# A sample of 64 users using the new software has a mean completion time of 48 seconds.
# Test the hypothesis at the 5% significance level

import numpy as np
from scipy import stats 

u = 50
psd = 8
n = 64
x = 48
a = 0.05

z = round((x - u)/ (psd / np.sqrt(n))  ,2)
p = 2 * (1 - stats.norm.cdf(abs(z)))

if p > a:
    print("Accept Null Hypothesis")
else:
    print("Reject Null Hypothesis")