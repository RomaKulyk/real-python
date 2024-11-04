# Understandin map()
#-------------------------------------------------------------------------------
# Python's map() is a built-in function that allows you to process and 
# transform all the items in an iterable without using an explicit for loop,
# a technique commonly known as mapping. map() is useful when you need to apply
# a transformation function to each item in an iterable and transform them into 
# a new iterable. map() is one of the tools that support a functional
# programming style in Python.

str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]
int_nums = map(int, str_nums)
print(int_nums)
print(list(int_nums))
print(str_nums)

# map() applies int() to every value in str_nums. Sinde map() returns an iterator
# (a map object), you'll need call list() so that you can exhaust the iterator
# and turn it into a list object. Note that the original sequence doesn't get
# modified in the process.

# Using map() with different kinds of function
#-------------------------------------------------------------------------------
# You can use any kind of Python callable with map(). The only condition would be 
# that the callable takes an argument and returns a concrete and useful value.
numbers = [-2, -1, 0, 1, 2]
abs_values = list(map(abs, numbers))
print(abs_values)

# Processing multiple input iterables with map()
#-------------------------------------------------------------------------------
# If you supply multiple iterables to map(), then the transformation function
# must takes as many arguments as iterables you pass in. Each iteration of map()
#  will pass one value from each iterables as an argument to function. The
# iteration stops at the end of the shortest iterable.
first_it = [1, 2, 3]
second_it = [4, 5, 6, 7]
print(list(map(pow, first_it, second_it)))

# Transforming iterablse of Strings with Python's map()
#-------------------------------------------------------------------------------
# Using Math Operations
# A commont example  of using math operations to transform an iterable of
# numeric values is to use the power operator(**).
# 
# Converting Temperatures
# Another use case for map() is to convert between units of measure.
# 
# Converting Strings to Numbers
# When working with numeric data, you'll likely deal wiht situations in which all
# your data are string values. To do any further calculation, you'll need to
# convert the string values into numeric values.map() can help with these
# situations, too.