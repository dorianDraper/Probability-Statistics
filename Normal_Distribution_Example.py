import numpy as np
import scipy.stats as stats

# the test scores o a physics class with 800 students are distributed normally with a mean of 75 and standard deviation of 7
# what percentage of students scored between 68 and 82?
mean = 75
std_dev = 7
x1 = 68
x2 = 82
cdf_x1 = stats.norm.cdf(x1, mean, std_dev) # consider the stats.norm.rvs() function to generate random numbers
cdf_x2 = stats.norm.cdf(x2, mean, std_dev)
percentage = (cdf_x2 - cdf_x1) * 100
print(f'{percentage}% of students scored between 68 and 82')
# how many students have test score between 61 and 89?
x1 = 61
x2 = 89
cdf_x1 = stats.norm.cdf(x1, mean, std_dev)
cdf_x2 = stats.norm.cdf(x2, mean, std_dev)
percentage = (cdf_x2 - cdf_x1) * 100
print(f'{percentage}% of students scored between 61 and 89')
# given percentage is a float, we multiply by 800 students and use the round function to round it to the nearest integer to get the number of students
students_number = (cdf_x2 - cdf_x1) * 800
print(f'{round(students_number)} students scored between 61 and 89')
# what is the probability that a student chosen at random has a test score between 54 and 75?
x1 = 54
x2 = 75
cdf_x1 = stats.norm.cdf(x1, mean, std_dev)
cdf_x2 = stats.norm.cdf(x2, mean, std_dev)
probability = (cdf_x2 - cdf_x1)
print(f'The probability that a student chosen at random has a test score between 54 and 75 is {probability}') # :.2f
# approximately how many students have a test score greater than or equal to 96?
x = 96
cdf_x = stats.norm.cdf(x, mean, std_dev)
students_number = (1 - cdf_x) * 800
print(f'{round(students_number)} students have a test score greater than or equal to 96')
# plot the results using a histogram
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# generate random data
data = np.random.normal(mean, std_dev, 800)
# create a dataframe    
df = pd.DataFrame(data, columns=['Test Score'])
# create a histogram
sns.histplot(df, kde=True)
plt.show()