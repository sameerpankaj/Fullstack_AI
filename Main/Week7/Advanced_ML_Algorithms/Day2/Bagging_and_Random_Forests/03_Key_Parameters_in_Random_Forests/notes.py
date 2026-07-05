'''
Number fo Trees(n_estimators)
    --The number of decision trees in the forest
    --Larger values reduce variance but increase computational cost
Maximum Depth(max_depth)
    --Limits the depth of each tree to prevent overfitting
    --Shallower trees generalize better but may underfit
Feature Selection (max_features)
    --Number of features to consider when looking for the best split
    --Options
        --sqrt|log2|None
Minimum Samples per Leaf(min_samples_leaf)
    --Minimum number fo samples required in a leaf node
    --Prevents overly complex trees by ensuring each leaf contains enough samples

'''