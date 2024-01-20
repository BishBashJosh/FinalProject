import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from scipy import stats
from scipy.stats import pearsonr
import unittest 
import function

# Reading the datasets
df_gcse = pd.read_csv('cleansedGcse.csv', encoding = 'UTF-8')
df_income = pd.read_csv('cleansedIncome.csv', encoding = 'UTF-8')

# Income Visualizations
# Line graph for income trends over the years for different areas
df_income['Year'] = pd.Categorical(df_income['Year'], categories=['2015-16', '2016-17', '2017-18', '2018-19', '2019-20', '2020-21'], ordered=True)

plt.figure(figsize=(10, 6))
for area in df_income['Area'].unique():
    plt.plot(df_income[df_income['Area'] == area]['Year'], df_income[df_income['Area'] == area]['Income'], label=area, marker='o')

plt.title('Income Over Years for Different Areas')
plt.xlabel('Year')
plt.ylabel('Income')
plt.legend()
plt.grid(True)
plt.show()

# Bar chart for income comparison across different areas for each year
df_income['Year'] = pd.Categorical(df_income['Year'], categories=['2015-16', '2016-17', '2017-18', '2018-19', '2019-20', '2020-21'], ordered=True)

plt.figure(figsize=(12, 6))
bar_width = 0.2
years = df_income['Year'].cat.codes.unique()

for i, area in enumerate(df_income['Area'].unique()):
    plt.bar(years + i * bar_width, df_income[df_income['Area'] == area]['Income'], width=bar_width, label=area)

plt.title('Income Comparison Across Areas for Each Year')
plt.xlabel('Year')
plt.ylabel('Income')
plt.legend()
plt.grid(True)
plt.show()




# Line chart for income trends in Kensington and Chelsea
df_kensington = df_income[df_income['Area'] == 'Kensington and Chelsea']
df_other_areas = df_income[df_income['Area'] != 'Kensington and Chelsea']

plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='Income', data=df_kensington, marker='o', label='Kensington and Chelsea')

plt.title('Income Over Years in Kensington and Chelsea')
plt.xlabel('Year')
plt.ylabel('Income')
plt.legend()
plt.show()

# Line chart for income trends in Barking and Dagenham, London, and England
plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='Income', hue='Area', data=df_other_areas, marker='o')

plt.title('Income Over Years for Barking and Dagenham, London and England')
plt.xlabel('Year')
plt.ylabel('Income')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Mean Scores Visualizations
# Line graph for mean scores over the years
plt.figure(figsize=(10, 6))
sns.lineplot(x='Year', y='Mean Score', hue='Area', data=df_gcse, marker='o')
plt.title('Mean Scores Over Years')
plt.show()

# Bar chart for mean scores by area
plt.figure(figsize=(10, 6))
sns.barplot(x='Area', y='Mean Score', hue='Year', data=df_gcse)
plt.title('Mean Scores by Area')
plt.show()

# Box plot for the distribution of mean scores by area
plt.figure(figsize=(10, 6))
sns.boxplot(x='Area', y='Mean Score', data=df_gcse)
plt.title('Distribution of Mean Scores by Area')
plt.show()

# Line chart for mean scores trends in Kensington and Chelsea
df_kensington_gcse = df_gcse[df_gcse['Area'] == 'Kensington and Chelsea']
df_other_areas_gcse = df_gcse[df_gcse['Area'] != 'Kensington and Chelsea']

plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='Mean Score', data=df_kensington_gcse, marker='s', label='Kensington and Chelsea')

plt.title('Mean Scores Over Years in Kensington and Chelsea')
plt.xlabel('Year')
plt.ylabel('Mean Score')
plt.legend()
plt.show()

# Line chart for mean scores trends in Barking and Dagenham, London, and England
plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='Mean Score', hue='Area', data=df_other_areas_gcse, marker='s')

plt.title('Mean Scores Over Years for for Barking and Dagenham, London and England')
plt.xlabel('Year')
plt.ylabel('Mean Score')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Comparison between income and mean score
# Comparison in London
df_income_london = df_income[df_income['Area'] == 'London']
df_gcse_london = df_gcse[df_gcse['Area'] == 'London']

# Creating subplots for income and mean scores in London
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plotting Income for London on the first subplot
color = 'tab:red'
ax1.set_xlabel('Year')
ax1.set_ylabel('Income', color=color)
ax1.plot(df_income_london['Year'], df_income_london['Income'], marker='o', color=color, label='Income (London)')
ax1.tick_params(axis='y', labelcolor=color)
ax1.legend(loc='upper left')

# Creating a second subplot for Mean Score
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Mean Score', color=color)
ax2.plot(df_gcse_london['Year'], df_gcse_london['Mean Score'], marker='s', color=color, label='Mean Score (London)')
ax2.tick_params(axis='y', labelcolor=color)
ax2.legend(loc='upper right')

plt.title('Income and Mean Score in London Over Years')
plt.show()

# Comparison in Barking and Dagenham
# Selecting data for Barking and Dagenham from income and GCSE datasets
df_income_bd = df_income[df_income['Area'] == 'Barking and Dagenham']
df_gcse_bd = df_gcse[df_gcse['Area'] == 'Barking and Dagenham']

# Creating subplots for income and mean scores
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plotting Income for Barking and Dagenham on the first subplot
color = 'tab:red'
ax1.set_xlabel('Year')
ax1.set_ylabel('Income', color=color)
ax1.plot(df_income_bd['Year'], df_income_bd['Income'], marker='o', color=color, label='Income (Barking and Dagenham)')
ax1.tick_params(axis='y', labelcolor=color)
ax1.legend(loc='upper left')

# Creating a second subplot for Mean Score
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Mean Score', color=color)
ax2.plot(df_gcse_bd['Year'], df_gcse_bd['Mean Score'], marker='s', color=color, label='Mean Score (Barking and Dagenham)')
ax2.tick_params(axis='y', labelcolor=color)
ax2.legend(loc='upper right')

plt.title('Income and Mean Score in Barking and Dagenham Over Years')
plt.show()

# Comparison in Kensington and Chelsea
# Selecting data for Kensington and Chelsea from income and GCSE datasets
df_income_kc = df_income[df_income['Area'] == 'Kensington and Chelsea']
df_gcse_kc = df_gcse[df_gcse['Area'] == 'Kensington and Chelsea']

# Creating subplots for income and mean scores
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plotting Income for Kensington and Chelsea on the first subplot
color = 'tab:red'
ax1.set_xlabel('Year')
ax1.set_ylabel('Income', color=color)
ax1.plot(df_income_kc['Year'], df_income_kc['Income'], marker='o', color=color, label='Income (Kensington and Chelsea)')
ax1.tick_params(axis='y', labelcolor=color)
ax1.legend(loc='upper left')

# Creating a second subplot for Mean Score
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Mean Score', color=color)
ax2.plot(df_gcse_kc['Year'], df_gcse_kc['Mean Score'], marker='s', color=color, label='Mean Score (Kensington and Chelsea)')
ax2.tick_params(axis='y', labelcolor=color)
ax2.legend(loc='upper right')

plt.title('Income and Mean Score in Kensington and Chelsea Over Years')
plt.show()

# Comparison in England
# Selecting data for England from income and GCSE datasets
df_income_england = df_income[df_income['Area'] == 'England']
df_gcse_england = df_gcse[df_gcse['Area'] == 'England']

# Creating subplots for income and mean scores
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plotting Income for England on the first subplot
color = 'tab:red'
ax1.set_xlabel('Year')
ax1.set_ylabel('Income', color=color)
ax1.plot(df_income_england['Year'], df_income_england['Income'], marker='o', color=color, label='Income (England)')
ax1.tick_params(axis='y', labelcolor=color)
ax1.legend(loc='upper left')

# Creating a second subplot for Mean Score
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Mean Score', color=color)
ax2.plot(df_gcse_england['Year'], df_gcse_england['Mean Score'], marker='s', color=color, label='Mean Score (England)')
ax2.tick_params(axis='y', labelcolor=color)
ax2.legend(loc='upper right')

plt.title('Income and Mean Score in England Over Years')
plt.show()

# Correlation
# Merging income and GCSE datasets on 'Year' and 'Area'
df_merged = pd.merge(df_income, df_gcse, on=['Year', 'Area'])

# Calculating and printing Pearson correlation coefficient and p-value for Kensington and Chelsea
df_area = df_merged[df_merged['Area'] == 'Kensington and Chelsea']
correlation_coefficient, p_value = pearsonr(df_area['Income'], df_area['Mean Score'])
print(f"Pearson Correlation Coefficient for Kensington and Chelsea: {correlation_coefficient}")
print(f"P-value: {p_value}")

# Calculating and printing Pearson correlation coefficient and p-value for Barking and Dagenham
df_area = df_merged[df_merged['Area'] == 'Barking and Dagenham']
correlation_coefficient, p_value = pearsonr(df_area['Income'], df_area['Mean Score'])
print(f"Pearson Correlation Coefficient for Barking and Dagenham: {correlation_coefficient}")
print(f"P-value: {p_value}")

# Calculating and printing Pearson correlation coefficient and p-value for London
df_area = df_merged[df_merged['Area'] == 'London']
correlation_coefficient, p_value = pearsonr(df_area['Income'], df_area['Mean Score'])
print(f"Pearson Correlation Coefficient for London: {correlation_coefficient}")
print(f"P-value: {p_value}")

# Calculating and printing Pearson correlation coefficient and p-value for England
df_area = df_merged[df_merged['Area'] == 'England']
correlation_coefficient, p_value = pearsonr(df_area['Income'], df_area['Mean Score'])
print(f"Pearson Correlation Coefficient for England: {correlation_coefficient}")
print(f"P-value: {p_value}")