#reduce()
# Import the reduce() function from the functools module
from functools import reduce

# Create a list of numbers
numbers = [1, 2, 3, 4]

# Use reduce() to repeatedly apply the lambda function to the list elements
# lambda x, y: x * y takes two numbers and returns their product
# reduce() combines the list into a single value by multiplying all elements
product = reduce(lambda x, y: x * y, numbers)

# Print the final result
print(product)

'''
Step-by-step execution

The reduce() function processes the list like this:

numbers = [1, 2, 3, 4]
First iteration
1 * 2 = 2
Second iteration
2 * 3 = 6
Third iteration
6 * 4 = 24

So:

product = 24

Output:

24
Visual Representation
[1, 2, 3, 4]

1 * 2 = 2
      ↓
2 * 3 = 6
      ↓
6 * 4 = 24
      ↓
Result = 24
Equivalent Code Without reduce()
numbers = [1, 2, 3, 4]

product = 1

for num in numbers:
    product *= num

print(product)
What reduce() Does
map() → transforms every element.
filter() → selects some elements.
reduce() → combines all elements into a single value.

Examples:

Sum of numbers
Product of numbers
Finding maximum/minimum
Combining strings

For example:

from functools import reduce

total = reduce(lambda x, y: x + y, [1, 2, 3, 4])

print(total)  # 10

Here, reduce() combines all numbers into a single sum.

'''