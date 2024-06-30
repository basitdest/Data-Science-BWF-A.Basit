# Tuples are sequences, typically used to store collections of heterogeneous data.
my_tuple = (1, 2, 3, 'a', 'b', 'c')
print("Tuple:", my_tuple)

# Lists are sequences, typically used to store collections of homogeneous items.
my_list = [4, 5, 6, 'd', 'e', 'f']
print("List:", my_list)

# Sorting a list of numbers in ascending order
sorted_list = sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
print("Sorted List:", sorted_list)

# Slicing a list to get a sublist
sliced_list = my_list[1:4]
print("Sliced List:", sliced_list)

# Dictionaries are mutable mappings of unique keys to values.
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print("Dictionary:", my_dict)

# Set
# Sets are unordered collections of unique elements.
my_set = {1, 2, 3, 4, 4, 5, 5, 6}
print("Set:", my_set)

# Namespaces, Scope, and Local Function
# Demonstrating local scope and global scope
def outer_function():
    outer_var = 'outer'

    def inner_function():
        inner_var = 'inner'
        print("Inner function can access outer_var:", outer_var)

    inner_function()
    # Trying to access inner_var here would result in an error

outer_function()

# Returning Multiple Values
# Functions can return multiple values as a tuple
def min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_max([1, 2, 3, 4, 5])
print("Minimum:", minimum)
print("Maximum:", maximum)

# Generators
# Generators yield items one at a time and are useful for large datasets
def my_generator():
    for i in range(10):
        yield i

for value in my_generator():
    print("Generated value:", value)

