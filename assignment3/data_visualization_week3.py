# Titanic Dataset Visualization
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Loading Titanic dataset directly from seaborn's sample datasets
titanic_data = sns.load_dataset('titanic')

# Setting seaborn style
sns.set(style="darkgrid")

# Plot 1: Count of Survivors
plt.figure(figsize=(6,4))
sns.countplot(data=titanic_data, x='survived', palette='Set2')
plt.title("Survival Count (0 = No, 1 = Yes)")
plt.xlabel("Survived")
plt.ylabel("Count")
plt.show()

# Plot 2:=> Survival by Gender
plt.figure(figsize=(6,4))
sns.countplot(data=titanic_data, x='sex', hue='survived', palette='Set1')
plt.title("Survival by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.legend(title='Survived', labels=['No', 'Yes'])
plt.show()

# Plot 3:=> Survival by Passenger Class
plt.figure(figsize=(6,4))
sns.countplot(data=titanic_data, x='pclass', hue='survived', palette='Set3')
plt.title("Survival by Passenger Class")
plt.xlabel("Passenger Class (1 = Upper, 2 = Middle, 3 = Lower)")
plt.ylabel("Count")
plt.legend(title='Survived', labels=['No', 'Yes'])
plt.show()

# Plot 4:=> Age Distribution by Survival
plt.figure(figsize=(8,5))
sns.histplot(data=titanic_data, x='age', hue='survived', bins=30, kde=True, palette='husl')
plt.title("Age Distribution by Survival")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.legend(title='Survived', labels=['No', 'Yes'])
plt.show()

# Plot 5:=> Heatmap of Missing Values
plt.figure(figsize=(10,6))
sns.heatmap(titanic_data.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.xlabel("Columns")
plt.ylabel("Rows")
plt.show()