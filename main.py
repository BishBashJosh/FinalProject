import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import unittest 
import function

df_gcse = pd.read_csv('cleansedGcse.csv', encoding = 'UTF-8')
df_income = pd.read_csv('cleansedIncome.csv', encoding = 'UTF-8')

#Income
#Creating a line graph
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

#Creating a bar chart
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




#Creating line chart for Kensington and Chelsea
df_kensington = df_income[df_income['Area'] == 'Kensington and Chelsea']
df_other_areas = df_income[df_income['Area'] != 'Kensington and Chelsea']

plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='Income', data=df_kensington, marker='o', label='Kensington and Chelsea')

plt.title('Income Over Years in Kensington and Chelsea')
plt.xlabel('Year')
plt.ylabel('Income')
plt.legend()
plt.show()

#Creating line chart for Barking and Dagenham, London and England
plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='Income', hue='Area', data=df_other_areas, marker='o')

plt.title('Income Over Years for Barking and Dagenham, London and England')
plt.xlabel('Year')
plt.ylabel('Income')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

#Mean Scores
#Creating line graph
plt.figure(figsize=(10, 6))
sns.lineplot(x='Year', y='Mean Score', hue='Area', data=df_gcse, marker='o')
plt.title('Mean Scores Over Years')
plt.show()

#Creating Bar Chart
plt.figure(figsize=(10, 6))
sns.barplot(x='Area', y='Mean Score', hue='Year', data=df_gcse)
plt.title('Mean Scores by Area')
plt.show()

#Creating Box Plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Area', y='Mean Score', data=df_gcse)
plt.title('Distribution of Mean Scores by Area')
plt.show()

#Creating line chart for Kensington and Chelsea
df_kensington_gcse = df_gcse[df_gcse['Area'] == 'Kensington and Chelsea']
df_other_areas_gcse = df_gcse[df_gcse['Area'] != 'Kensington and Chelsea']

plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='Mean Score', data=df_kensington_gcse, marker='s', label='Kensington and Chelsea')

plt.title('Mean Scores Over Years in Kensington and Chelsea')
plt.xlabel('Year')
plt.ylabel('Mean Score')
plt.legend()
plt.show()

#Creating line chart for Barking and Dagenham, London and England
plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='Mean Score', hue='Area', data=df_other_areas_gcse, marker='s')

plt.title('Mean Scores Over Years for for Barking and Dagenham, London and England')
plt.xlabel('Year')
plt.ylabel('Mean Score')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()