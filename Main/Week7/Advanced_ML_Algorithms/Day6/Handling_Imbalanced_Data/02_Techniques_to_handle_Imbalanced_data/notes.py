'''
Resampling Techniques
    --Oversampling
        --Increase the number fo minority class samples by duplicating or synthesizing new samples
        --Example: SMOTE(Synthetic Minority over sampling Technique) which generates synthetic examples
    --Undersampling
        --Reduce the number fo majority class samples to balance the dataset 
        --Risk: Loss of valuable information from majority class.

Algorithmic Solutions
    --Class Weights
        --Assign higher weights to the minority class during model training 
        --Many algorithms (e.g, Logistic Regression, Random Forest) have built in support for class weights
    --Anomaly Detection Models
        --Treat the minority class as anomalies, focusing the model on detecting them
Evaluation Metrics for Imbalanced Data
    --F1 Score
        --Harmonic mean of precision and recall, focusing on both false positives and false negatives
    --ROC-AUC
        --Measures the ability to distinguish between classes across various threshold values
    --Precision Recall Curve
        --Focuses on performance for the positive class


'''