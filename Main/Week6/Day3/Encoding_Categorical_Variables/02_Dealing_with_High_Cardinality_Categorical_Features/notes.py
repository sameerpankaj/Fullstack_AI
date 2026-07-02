'''
High cardinality categorical features contain a large number of unique categories
Challenges
    --Dimensionality
    --Sparse Representation
Solutinos
    --Frequency Encoding
        --Replace categories with their occurence frequency in the dataset
        --Example: City = ['NY', 'LA', 'SF', 'LA'] Encoded: NY = 2, LA = 2, SF = 1.
    --Target Encoding
        --Replace categories with the mean of the target variable for each category
'''