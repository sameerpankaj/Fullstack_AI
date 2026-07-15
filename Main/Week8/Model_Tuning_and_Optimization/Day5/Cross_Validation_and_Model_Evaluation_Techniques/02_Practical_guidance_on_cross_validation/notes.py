'''

Here's a practical guide to choosing and using cross-validation in real machine learning projects.

1. Small Dataset (< 1,000 samples)

Use 5-fold or 10-fold cross-validation.

from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5)

Reason: With limited data, cross-validation makes better use of all samples.

2. Medium Dataset (1,000–100,000 samples)

Use 5-fold cross-validation.

Good balance between accuracy and computation time.
This is the most common choice in industry.
scores = cross_val_score(model, X, y, cv=5)
3. Very Large Dataset (>100,000 samples)

A simple train-test split is often enough.

train_test_split(X, y, test_size=0.2, random_state=42)

Reason: Training five or ten models may take much longer, while a large dataset already provides a reliable estimate.

4. Imbalanced Classification

Use Stratified K-Fold.

Example:

Normal = 95%
Fraud = 5%

Each fold keeps roughly the same class proportions.

from sklearn.model_selection import StratifiedKFold

cv = StratifiedKFold(n_splits=5)

Examples:

Fraud detection
Disease diagnosis
Spam detection
5. Time-Series Data

Never shuffle the data.

Use:

from sklearn.model_selection import TimeSeriesSplit

cv = TimeSeriesSplit(n_splits=5)

Examples:

Stock prices
Weather forecasting
Sales forecasting
6. Hyperparameter Tuning

Use cross-validation together with tuning methods like:

GridSearchCV
RandomizedSearchCV
Optuna (often with cross-validation inside the objective function)

Example:

from sklearn.model_selection import GridSearchCV

grid = GridSearchCV(
    model,
    param_grid,
    cv=5
)
7. Very Small Dataset

Use:

LeaveOneOut()

Only when the dataset is very small (for example, fewer than 100 samples), because it is computationally expensive.

Recommended values
Situation	Recommendation
General classification	StratifiedKFold (5 folds)
General regression	KFold (5 folds)
Small dataset	10-fold CV
Large dataset	Train-test split or 5-fold CV
Hyperparameter tuning	5-fold CV
Time series	TimeSeriesSplit
Imbalanced data	StratifiedKFold
Grouped data	GroupKFold
Common mistakes

❌ Using the test set during hyperparameter tuning

Wrong:

Training → Test → Tune → Test again

The test set should be used only once, after all model selection and tuning are complete.

❌ Scaling before cross-validation

Wrong:

scaler.fit(X)
X = scaler.transform(X)

cross_val_score(model, X, y, cv=5)

This causes data leakage because information from all samples is used before splitting into folds.

Correct:

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", model)
])

scores = cross_val_score(pipeline, X, y, cv=5)

The scaler is fit separately within each training fold.

❌ Using ordinary K-Fold for imbalanced classification

If one fold contains almost no minority-class samples, evaluation becomes unreliable.

Use StratifiedKFold instead.

Industry workflow
Collect Data
      │
      ▼
Train/Test Split
      │
      ▼
Training Set
      │
      ▼
5-Fold Cross-Validation
      │
      ▼
Hyperparameter Tuning
      │
      ▼
Train Final Model
      │
      ▼
Evaluate Once on Test Set
Rule of thumb
Classification: StratifiedKFold(cv=5)
Regression: KFold(cv=5)
Time series: TimeSeriesSplit
Hyperparameter tuning: Combine cross-validation with GridSearchCV, RandomizedSearchCV, or Optuna.
Always keep the test set untouched until the very end. This gives the most trustworthy estimate of how your final model will perform on new data.
'''