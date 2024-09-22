import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from data import loading_data

df = loading_data()
print("First 5 rows of the DataFrame:")


df_clean = df[['userId', 'completed']]
task_counts = df_clean.groupby('userId').sum()
print(df_clean.head())

# statistics on the data
mean_completed = task_counts['completed'].mean()
std_completed = task_counts['completed'].std()

#plotting number of task completed per user
plt.figure(figsize=(10,6))
task_counts['completed'].plot(kind='bar', color='skyblue')
plt.title('Number of Completed Tasks per User')
plt.xlabel('User ID')
plt.ylabel('Number of Completed Tasks')
plt.xticks(rotation=0)
plt.show()