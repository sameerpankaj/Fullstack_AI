'''
Regularization introduces a penalty term to the loss function duging model training to prevent overfitting by discouraging overly complex models
    --L1 Regularization(Lasso)
        --Adds the absolute values of coefficients to the loss function 
        --Encourages sparsity by setting some coefficients to zero, effectively selecting features
    --L2 Regularization(Ridge)
        --Adds the squared values of coefficients to the loss function
        --Shrinks coefficients toward zero but does not set them to zero
    --Elastic Net
        --Combines L1 and L2 regularization 
        --Useful when there are correlated predictors and when feature selection is disired
        


'''