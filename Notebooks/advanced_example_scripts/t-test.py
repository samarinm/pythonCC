# Python Crash Course, 30.09.25
# Author: Maxim Samarin
#
# One sample t-test

from scipy.stats import ttest_1samp

import numpy as np
import matplotlib.pyplot as plt

print("One sample t-test\n")

# We sample uniformly 300 random age values 
# from 0 to 80
age = np.random.randint(low=0, high=80, size=300)

# We sample from a normal distribution with 
# mean = 35 (loc) and standard deviation = 10 
# (sacle) 300 random age values
# age = np.random.normal(loc=35.0, scale=10.0, size=300)

# Plot a histrogram where the age values are
# aggregated in 20 bins
plt.hist(age, bins=20)
plt.xlabel('Age')
plt.ylabel('Occurence')
plt.axvline(x=35, color='red', linestyle='--')
plt.show()

print("Null hypothesis: Mean population age = 35\n")

age_mean = np.mean(age)

print('Data age mean:', age_mean, '\n')

# Check whether the average age is 35 
# (null hypothesis). 
tstat, pval = ttest_1samp(age, popmean=35)

print("p-value:", pval, '\n')

if pval < 0.05:    
    print("We reject the null hypothesis")
else:
    print("We accept the null hypothesis")