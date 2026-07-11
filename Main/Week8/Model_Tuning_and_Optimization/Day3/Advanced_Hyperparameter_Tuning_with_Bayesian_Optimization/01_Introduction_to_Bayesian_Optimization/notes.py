'''

Bayesian Optimization is a technique for finding the best values of a function that is expensive to evaluate. In Python, it's commonly used to tune hyperparameters of machine learning models.

Simple example

Suppose you're training a model with these hyperparameters:

Learning rate
Number of trees
Maximum depth

Each training run may take several minutes. Instead of trying every combination (Grid Search) or random combinations (Random Search), Bayesian Optimization learns from previous results and chooses the next hyperparameters that are most promising.

How it works
Evaluate a few random hyperparameter combinations.
Build a probabilistic model (called a surrogate model, often a Gaussian Process) of the objective function.
Use an acquisition function to decide the next hyperparameters to test.
Train the model with those hyperparameters.
Update the surrogate model.
Repeat until the evaluation budget is exhausted.
Random points
      │
      ▼
Train ML model
      │
      ▼
Measure performance
      │
      ▼
Build surrogate model
      │
      ▼
Choose next best point
      │
      ▼
Repeat
Why use Bayesian Optimization?
Finds good hyperparameters with fewer model evaluations
Ideal when training is slow or expensive
More efficient than Grid Search or Random Search
Comparison
Method	Speed	Intelligent Search	Best For
Grid Search	Slow	❌	Small search spaces
Random Search	Medium	❌	Baseline tuning
Bayesian Optimization	Fast	✅	Expensive models
Python example

Install:

pip install scikit-optimize

Example:

from skopt import BayesSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

model = RandomForestClassifier()

search = BayesSearchCV(
    estimator=model,
    search_spaces={
        "n_estimators": (10, 300),
        "max_depth": (2, 20),
        "min_samples_split": (2, 10)
    },
    n_iter=20,
    cv=5,
    random_state=42
)

search.fit(X, y)

print(search.best_params_)
print(search.best_score_)
Popular Python libraries
scikit-optimize (skopt) – Simple and integrates with scikit-learn.
Optuna – Very popular, fast, and feature-rich.
Hyperopt – Good for distributed optimization.
BoTorch – Advanced Bayesian Optimization built on PyTorch.
When should you use it?

Use Bayesian Optimization when:

Model training is slow.
You have many hyperparameters.
You want high accuracy with fewer trials.
You're tuning models such as Random Forests, XGBoost, LightGBM, CatBoost, neural networks, or SVMs.

Avoid it when:

Training is very fast (Random Search may be sufficient).
The search space is tiny.
Interview definition

Bayesian Optimization is a sequential optimization algorithm that efficiently finds the best hyperparameters by building a probabilistic surrogate model of the objective function and using an acquisition function to balance exploration and exploitation, reducing the number of expensive evaluations needed.

'''