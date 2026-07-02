'''
Methods
    --Min-Max Scaling
        --Transforms features to a specified range, typically[0, 1]
        --Ensures all feature values are within the same range
        --Use Cases: k-NN or neural networks
        --Limitations: Sensitive to outliers, as extreme values can distort the scale
    --Standarization (Z-Score Scaling)
        --centers the data around zero and scales it to have a standard deviation of 1
        --Ensures a standard normal distribution for each feature 
        --Use Cases: SVM, Logistic regressoin, and PCA
        --Advantages: Handles outliers better than Min-Max Scaling
        
'''