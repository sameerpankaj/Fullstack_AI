'''
Key cross validation techniques
    --K-Fold cross validation
        --Splits the dataset into K equal parts
        --Trains the model on K-1 folds and tests on the remaining fold, repeating the process K times
        --The average of the K test scores provides the final evaluation metric
    --Stratified K-Fold
        --Ensures each fold has a proportional representation of classes in classfication problems
    --Leave one out corss validation(LOOCV)
        --Trains the model on n-1 samples and tests ont eh remaining one. Repeated for all samples
        --Computatinally expensive for large datasets

Advantages
    --Reduces the risk of overfitting by testing on multiple subsets of data
    --Provides a more generalized evaluation of model performance.

'''