# Import Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from scipy.stats import randint

# Load Datasets
train = pd.read_csv('house-prices-advanced-regression-techniques/train.csv')
test = pd.read_csv('house-prices-advanced-regression-techniques/test.csv')

# Data Preprocessing

# Fill missing categorical values with 'None'
categorical_cols = ['PoolQC', 'MiscFeature', 'Alley', 'Fence', 'FireplaceQu',
                    'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond',
                    'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1',
                    'BsmtFinType2', 'MasVnrType']

for col in categorical_cols:
    train[col] = train[col].fillna('None')
    test[col] = test[col].fillna('None')

# Fill missing numerical values with 0
numerical_cols = ['GarageYrBlt', 'GarageArea', 'GarageCars', 'BsmtFinSF1',
                  'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'BsmtFullBath',
                  'BsmtHalfBath', 'MasVnrArea']

for col in numerical_cols:
    train[col] = train[col].fillna(0)
    test[col] = test[col].fillna(0)

# Fill remaining missing values: categorical with mode, numerical with median
for col in train.columns:
    if train[col].isnull().sum() > 0:
        if train[col].dtype == 'object':
            train[col] = train[col].fillna(train[col].mode()[0])
        else:
            train[col] = train[col].fillna(train[col].median())

for col in test.columns:
    if test[col].isnull().sum() > 0:
        if test[col].dtype == 'object':
            test[col] = test[col].fillna(test[col].mode()[0])
        else:
            test[col] = test[col].fillna(test[col].median())

# Label Encoding for Categorical Features
label_cols = train.select_dtypes(include=['object']).columns

le = LabelEncoder()
for col in label_cols:
    train[col] = le.fit_transform(train[col])
    test[col] = le.transform(test[col])

# Feature Engineering
train['TotalBath'] = train['FullBath'] + (0.5 * train['HalfBath'])
test['TotalBath'] = test['FullBath'] + (0.5 * test['HalfBath'])

train['TotalPorchSF'] = train['OpenPorchSF'] + train['EnclosedPorch'] + train['3SsnPorch'] + train['ScreenPorch']
test['TotalPorchSF'] = test['OpenPorchSF'] + test['EnclosedPorch'] + test['3SsnPorch'] + test['ScreenPorch']

train['HouseAge'] = train['YrSold'] - train['YearBuilt']
test['HouseAge'] = test['YrSold'] - test['YearBuilt']

# Prepare Features and Target
X = train.drop(['SalePrice', 'Id'], axis=1)
y = train['SalePrice']
test_features = test.drop(['Id'], axis=1)

# Train-Test Split
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the Random Forest Model
rf = RandomForestRegressor(random_state=42)

# Define Hyperparameter Space (corrected)
param_dist = {
    'n_estimators': randint(100, 1000),
    'max_depth': randint(10, 50),
    'min_samples_split': randint(2, 10),
    'min_samples_leaf': randint(1, 5),
    'max_features': ['sqrt', 'log2', None]
}

# Randomized Search
random_search = RandomizedSearchCV(estimator=rf, param_distributions=param_dist,
                                   n_iter=30, cv=3, verbose=2, n_jobs=-1, random_state=42,
                                   scoring='neg_mean_squared_error')

random_search.fit(X_train, y_train)

# Best Parameters
print("Best Parameters Found: ", random_search.best_params_)

# Train Final Model
best_rf = random_search.best_estimator_
y_pred = best_rf.predict(X_valid)

# Evaluation
rmse = np.sqrt(mean_squared_error(y_valid, y_pred))
print(f'Validation RMSE after tuning: {rmse:.2f}')

# Predict on Test Set
test_preds = best_rf.predict(test_features)

# Create Submission File
submission = pd.DataFrame({
    'Id': test['Id'],
    'SalePrice': test_preds
})

submission.to_csv('Final_submission.csv', index=False)
print('Submission file "Final_submission.csv" has been created successfully.')