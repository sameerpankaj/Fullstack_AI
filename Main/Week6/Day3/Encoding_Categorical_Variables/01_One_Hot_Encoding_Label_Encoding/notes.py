'''
What are Categorical Variables?
    --Binary Categorical Features: Gender(Male/Female)
    --Multi Class Categorical Featues: Country(USA, Canada, UK)
One Hot Encoding
    --Creates binary columns for each category in a categorical feature
    --Each row is marked with a 1 for its respective category and 0 elsewhere
    --Example: Feature: Color = ['Red', 'Blue', 'Green']
    --Applications
        --Categorical features with a small number of unique categories
        --Tree based mdoels, logistic regression, and neural networks
Label Encoding
    --Label Encoding assigns a unique integer to each category
    --Example: Red = 0, Blue = 1, Green = 2.
    --Applications:
        --Ordinal features where the order matters
        --Can introduce unintended ordinal relationships for nominal features
    --Limitations
        --Can mislead algorithms into interpreting categories as ordered, especially when the variable is nominal



'''