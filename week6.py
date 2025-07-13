# Import libraries
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from scipy.stats import uniform

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 1: Train Multiple Models and Evaluate
models = {
    'Logistic Regression': LogisticRegression(),
    'Random Forest': RandomForestClassifier(),
    'SVM': SVC()
}

results = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    results[name] = {
        'Accuracy': accuracy_score(y_test, y_pred),
        'Precision': precision_score(y_test, y_pred, average='macro'),
        'Recall': recall_score(y_test, y_pred, average='macro'),
        'F1-score': f1_score(y_test, y_pred, average='macro')
    }

# Display base model evaluation results
print("\nInitial Model Performance (Before Tuning):\n")
print(pd.DataFrame(results).T)

# Step 2: Hyperparameter Tuning

## 2A. GridSearchCV for Random Forest
param_grid_rf = {
    'n_estimators': [10, 50, 100],
    'max_depth': [None, 5, 10],
    'criterion': ['gini', 'entropy']
}

grid_search_rf = GridSearchCV(RandomForestClassifier(), param_grid_rf, cv=5, scoring='f1_macro')
grid_search_rf.fit(X_train, y_train)

print("\nBest parameters (Random Forest - GridSearchCV):", grid_search_rf.best_params_)
print("Best cross-validated F1-score (Random Forest):", grid_search_rf.best_score_)

## 2B. RandomizedSearchCV for SVM
param_dist_svm = {
    'C': uniform(0.1, 10),
    'gamma': ['scale', 'auto'],
    'kernel': ['linear', 'rbf', 'poly']
}

random_search_svm = RandomizedSearchCV(SVC(), param_distributions=param_dist_svm, n_iter=10, cv=5, scoring='f1_macro', random_state=42)
random_search_svm.fit(X_train, y_train)

print("\nBest parameters (SVM - RandomizedSearchCV):", random_search_svm.best_params_)
print("Best cross-validated F1-score (SVM):", random_search_svm.best_score_)

# Step 3: Final Evaluation on Test Set with Tuned Models
def evaluate_model(model, name):
    y_pred = model.predict(X_test)
    print(f"\n{name} - Final Evaluation on Test Set:\n")
    print(classification_report(y_test, y_pred))

best_rf = grid_search_rf.best_estimator_
best_svm = random_search_svm.best_estimator_

evaluate_model(best_rf, "Random Forest (Tuned)")
evaluate_model(best_svm, "SVM (Tuned)")