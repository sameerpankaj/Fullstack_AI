'''
Bagging(Bootstrap Aggregating)
    --Trains multiple models independently on different subsets of data created through bootstaping
    --Combines predictions by averaging(regression) or majority(classfication)
    --Example:Random Forest
    --Strengths: Reduces variance without increasing bias
Boosting
    --Trains models sequentially, where each model focuses on correcting the errors made by the previous ones
    --Combines predictions through weighted averaging or voting
    --Examples: AdaBoost, Gradient Boosting, XGBoost, LightGBM
    --Strengths:Reduces both bias and variance by focusing on hard to predict instances
Stacking
    --Combines predictions from multiple base models(of different types) using a meta model to learn how to best combine their outputs
    --Strengths: can utilize diverse model types to maximize perfromance



'''