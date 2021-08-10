# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 21:55:12 2021

@author: y
"""

path = r"C:\Users\y\Desktop\DataGlacier-VC\Task7"    

# Reading Data
import pandas as pd
df = pd.read_csv(path+"/Healthcare_dataset.csv", delimiter=",")
df.head()

# Droping Unknown Values 
df.drop(df.index[df['Ntm_Speciality'] == 'Unknown'], inplace = True)
df.drop(df.index[df['Ethnicity'] == 'Unknown'], inplace = True)
df.drop(df.index[df['Risk_Segment_During_Rx'] == 'Unknown'], inplace = True)
df.drop(df.index[df['Tscore_Bucket_During_Rx'] == 'Unknown'], inplace = True)
df.drop(df.index[df['Change_T_Score'] == 'Unknown'], inplace = True)
df.drop(df.index[df['Change_Risk_Segment'] == 'Unknown'], inplace = True)
df.drop(df.index[df['Adherent_Flag'] == 'Unknown'], inplace = True)

# Checking Null Valeus
print(df.isnull().sum().sum())

# Unnecessary Because Data Is Cleaned 
print("\n----------- Calculate Mean -----------\n")
print(df.mean())
df_mean = df
df_mean['Count_Of_Risks'].fillna(value=df_mean['Count_Of_Risks'].mean(), inplace=True)
df_mean['Dexa_Freq_During_Rx'].fillna(value=df_mean['Dexa_Freq_During_Rx'].mean(), inplace=True)

# Unnecessary Because Data Is Cleaned 
print("\n----------- Calculate Median -----------\n")
print(df.median())
df_median = df
df_median['Count_Of_Risks'].fillna(value=df_median['Count_Of_Risks'].mean(), inplace=True)
df_median['Dexa_Freq_During_Rx'].fillna(value=df_median['Dexa_Freq_During_Rx'].mean(), inplace=True)

# Unnecessary Because Data Is Cleaned 
print("\n----------- Calculate Mode -----------\n")
print(df.mode())
df_mode = df
df_mode['Count_Of_Risks'].fillna(value=df_mode['Count_Of_Risks'].mean(), inplace=True)
df_mode['Dexa_Freq_During_Rx'].fillna(value=df_mode['Dexa_Freq_During_Rx'].mean(), inplace=True)

# Exporting The Cleaned Data
df.to_csv("Healthcare_cleaned_dataset.csv", index = False)


# Checking Outliers 
import seaborn as sns
# Box plot
sns.boxplot(df.Dexa_Freq_During_Rx)
# Distribution plot
sns.distplot(df.Dexa_Freq_During_Rx)


# Box plot
sns.boxplot(df.Count_Of_Risks)
# Distribution plot
sns.distplot(df.Count_Of_Risks)
