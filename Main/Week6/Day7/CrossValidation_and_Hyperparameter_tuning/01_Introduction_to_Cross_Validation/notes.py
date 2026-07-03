'''
What is Cross Validation?
    --It is a technique used to access hwo well a machine learning modél generalizes to an independent dataset 
Types fo Cross validation
    K-Fold 
        --Splits the dtaset into K folds of approximately equal size
        --The model is trained on k-1 folds and validated on the remaining fold
        --This process is repeated k times, and the average performance is computed 
    Stratified K-Fold
        --Ensures that each fold maintains the same class distribution as the original dataset
        --useful for imbalanced datasets
    Leave One Out 
        --Use a single data point for validation and the rest for training
        --Repeats this process for all data points
        --Computationalyy expensive but provides the most robust evaluation

'''