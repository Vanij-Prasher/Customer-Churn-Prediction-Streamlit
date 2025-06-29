import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset from Seaborn
df = sns.load_dataset('titanic')

# View the first few rows
print(df.head())

# Get the structure and null counts
df.info()

# Summary statistics
print(df.describe())

# Visualize missing values
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')
plt.title('Missing Values Heatmap')
plt.show()

# Univariate Analysis
plt.figure(figsize=(6,4))
sns.countplot(x='survived', data=df)
plt.title('Survival Count')
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x='sex', data=df)
plt.title('Sex Count')
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x='pclass', data=df)
plt.title('Passenger Class Count')
plt.show()

# Age Distribution
plt.figure(figsize=(6,4))
df['age'].hist(bins=30)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Fare Distribution
plt.figure(figsize=(6,4))
sns.histplot(df['fare'], kde=True)
plt.title('Fare Distribution')
plt.show()

# Impute Age
def impute_age(cols):
    age = cols.iloc[0]
    pclass = cols.iloc[1]
    
    if pd.isnull(age):
        if pclass == 1:
            return 37
        elif pclass == 2:
            return 29
        else:
            return 24
    else:
        return age

df['age'] = df[['age', 'pclass']].apply(impute_age, axis=1)

# Drop Cabin and remaining missing values
df.drop('deck', axis=1, inplace=True)
df.dropna(inplace=True)

# Boxplot to detect outliers
plt.figure(figsize=(6,4))
sns.boxplot(x='pclass', y='fare', data=df)
plt.title('Fare Distribution Across Passenger Classes')
plt.show()

# Survival by Gender
plt.figure(figsize=(6,4))
sns.countplot(x='survived', hue='sex', data=df)
plt.title('Survival by Gender')
plt.show()

# Survival by Passenger Class
plt.figure(figsize=(6,4))
sns.countplot(x='survived', hue='pclass', data=df)
plt.title('Survival by Passenger Class')
plt.show()

# Violin Plot of Age, Class, and Survival
plt.figure(figsize=(8,6))
sns.violinplot(x='pclass', y='age', hue='survived', data=df, split=True)
plt.title('Age Distribution by Class and Survival')
plt.show()

# Correlation Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.select_dtypes(include=['float64', 'int64']).corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()