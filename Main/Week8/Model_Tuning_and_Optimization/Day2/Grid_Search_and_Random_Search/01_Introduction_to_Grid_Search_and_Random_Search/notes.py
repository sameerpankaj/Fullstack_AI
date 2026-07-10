'''
Grid Search and Random Search are techniques for hyperparameter tuning—finding the best settings for a machine learning model.

What are Hyperparameters?

Hyperparameters are values you set before training.

Example for a Decision Tree:

max_depth=5
min_samples_split=4
criterion='gini'

The model does not learn these values; you choose them.

Grid Search

Grid Search tries every possible combination of hyperparameters.

Suppose you have:

param_grid = {
    'max_depth': [3, 5, 7],
    'min_samples_split': [2, 4]
}

Grid Search tests:

max_depth	min_samples_split
3	2
3	4
5	2
5	4
7	2
7	4

Total combinations:

3 × 2 = 6

If each model takes 10 seconds:

6 × 10 = 60 seconds
Grid Search Example
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

iris = load_iris()

model = DecisionTreeClassifier()

param_grid = {
    'max_depth': [3, 5, 7],
    'criterion': ['gini', 'entropy']
}

grid = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=5,
    scoring='accuracy'
)

grid.fit(iris.data, iris.target)

print(grid.best_params_)
print(grid.best_score_)

Example output:

{'criterion': 'gini', 'max_depth': 5}
0.973
Random Search

Random Search doesn't test every combination. It randomly selects a fixed number of combinations.

Example:

param_dist = {
    'max_depth': [3,5,7,9,11,13],
    'min_samples_split': [2,4,6,8],
    'criterion': ['gini','entropy']
}

Possible combinations:

6 × 4 × 2 = 48

Instead of trying all 48, Random Search might try only 10 (n_iter=10).

Random Search Example
from sklearn.model_selection import RandomizedSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

iris = load_iris()

model = DecisionTreeClassifier()

param_dist = {
    'max_depth': [3,5,7,9,11],
    'min_samples_split': [2,4,6,8],
    'criterion': ['gini','entropy']
}

random = RandomizedSearchCV(
    estimator=model,
    param_distributions=param_dist,
    n_iter=10,
    cv=5,
    scoring='accuracy',
    random_state=42
)

random.fit(iris.data, iris.target)

print(random.best_params_)
print(random.best_score_)
Comparison
Feature	Grid Search	Random Search
Tries every combination	✅	❌
Randomly samples combinations	❌	✅
Speed	Slower	Faster
Guarantees best within the grid	✅	❌
Good for many hyperparameters	❌	✅
Computational cost	High	Lower
Visual Example

Suppose:

max_depth = [3,5,7]
learning_rate = [0.01,0.1,1]

There are 9 possible combinations.

Grid Search:

✓ (3,0.01)
✓ (3,0.1)
✓ (3,1)
✓ (5,0.01)
✓ (5,0.1)
✓ (5,1)
✓ (7,0.01)
✓ (7,0.1)
✓ (7,1)

Random Search (n_iter=4):

✓ (5,0.1)
✓ (7,1)
✓ (3,0.01)
✓ (7,0.1)

Only 4 random combinations are evaluated.

When to Use Which?
Use Grid Search when:
You have a small number of hyperparameters.
The search space is small.
You want the best combination within the specified grid.
Use Random Search when:
You have many hyperparameters.
Training each model is expensive.
You need a good solution quickly.
Interview Questions

Q1. Why is Random Search often preferred?
Because many hyperparameters have little effect on performance. Random Search explores more unique regions of the search space in the same amount of time, often finding near-optimal settings much faster.

Q2. Does Grid Search always find the global optimum?
No. It only finds the best combination within the values you provide. If the true optimum lies outside your grid, it won't find it.

Q3. What is cv=5?
It means 5-fold cross-validation. The data is split into five parts; the model trains on four and validates on one, repeating this process five times. The average score is used to evaluate each hyperparameter combination.

Q4. What does scoring='accuracy' mean?
It tells the search procedure to rank hyperparameter combinations using classification accuracy. For regression, you might use metrics such as 'neg_mean_squared_error' or 'r2'.

In practice, a common workflow is to start with Random Search to quickly identify promising regions of the hyperparameter space, then perform a Grid Search around the best values for fine-tuning.

'''