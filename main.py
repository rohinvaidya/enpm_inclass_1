# import the libraries here which you installed
import numpy as np
import pandas  as pd
import matplotlib.pyplot as plt
from data import loading_data

df = loading_data()
print("First 5 rows of the DataFrame:")


df_clean = df[['userId', 'completed']]
task_counts = df_clean.groupby('userId').sum()
print(df_clean.head())

completed_array = task_counts['completed'].to_numpy()
# statistics on the data
mean_completed = np.mean(completed_array)
std_completed = np.std(completed_array)

#plotting number of task completed per user
plt.figure(figsize=(10,6))
task_counts['completed'].plot(kind='bar', color='skyblue')
plt.title('Number of Completed Tasks per User')
plt.xlabel('User ID')
plt.ylabel('Number of Completed Tasks')
plt.xticks(rotation=0)
plt.show()
