import numpy as np 
from scipy import stats

dataset = np.array([3,1,4,1,1])

mean = np.mean(dataset)
print(f"Mean: {mean}")

median = np.median(dataset)
print(f"Median: {median}")

mode = stats.mode(dataset)
print(f"Mode: {mode[0][0]}")
print(f"Mode: {mode[0][0]} appeared {mode[1][0]} times in the dataset.")