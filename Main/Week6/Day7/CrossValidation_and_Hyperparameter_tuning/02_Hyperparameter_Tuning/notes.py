'''
What is Hyperparameter Tuning?  
    --These are parameters that are not learned by the model but are set before training, tuning these heyperparameters is crucial for optimizing performance
Techniques for Hyperparameter Tuning
    --Grid Search
        --Exhaustively searches over a predefiined hyperparameter space
        --Example: Testing all combinations of values for max_depth and learning_rate
    --Random search
        --Randomly samples combinations of hyperparameters from the predefined space
        --More efficient than Grid Search when the parameters space is large
    --IMportance fo Hyperparameter tuning
        --Prevents overfitting and underfitting by selecting the best configuration
        --Enhances model performance by optimizing critical settings

Importance of Tuning Hyperparameters for model performance
    --Without tuning, the model might not reach its optimal performance, leading to:
        Underfitting: Model fails to capture the underlying patterns
        Overfitting: Model memorizes the training data and performs poorly on unseen data

'''