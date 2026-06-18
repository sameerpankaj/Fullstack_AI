#groupby pandas

# grouped = df.groupby('column_name')

# for name, group in grouped:
#     print(name)
#     print(group)


# grouped.mean()
# grouped.sum()

# #using groupby
# df.groupby('category_column')['numeric_column'].mean()
# df.groupby('category_column').agg({'numeric_column': ['mean', 'max', 'min']})

# #using the pivot_tables
# pivot = df.pivot_table(
#     values = 'numberic_column',
#     index = 'category_column',
#     aggfunc = 'mean'
# )

# #custom aggregation
# def range_func(x):
#     return x.max() - x.min()

# df.groupby('category_column')['numeric_column'].agg(range_func)



# #Mean
# df.groupby('category_column')['numeric_column'].mean()

# #Max
# df.groupby('category_column')['numeric_column'].max()

# #Min
# df.groupby('category_column')['numeric_column'].min()


# #Multi Aggegation
# df.groupby('category_column').agg({'numeric_column': ['mean', 'max', 'min']})

