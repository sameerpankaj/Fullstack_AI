'''
Polynomial regression is an extension of linear regression that models non linear relationships by introducing higher-order terms of the input features.

What is Polynomial regression?
    --In a typical linear regression
        y = ß0 * ß1x + belongs to symbol
    --In polynomial regression, we extend this to include higher degree terms
        y = ß0 + ß1x + ß2x2 +ß33 + ... + ßnxn + belongs to symbol

Steps in Polynomial Regression
    1) Feature Transformation
        --Create polynomial features from the original input data
        --Example: x--->[x, x2, x3 ]

    2) Model Training
        --Perform linear regression on the transformed features
    3) Evaluation
        --Assess the model's ability to capture the data's non linear structure

Advantages
    --Captures non linear relationships effectively

Limitations
    --Prone to overfitting with high degree polynomials
    --May require regularization to avoid overfitting
Example Use Case: Predicting growth patterns in biological systems where relationships are non linear


'''