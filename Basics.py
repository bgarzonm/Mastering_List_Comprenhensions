# A list comprenhension is a easy way to understand and write for loops
# for example
[i * 2 for i in [1, 2, 3]]

# We normal use the for lop like this:
# We have a list of citys
strings = ["new york", "Boston", "Paris", "Japon"]
# initialice a list
results = []
# iterate over the list of cities and convert them to lists of strings in
# the format expected
for i in strings:
    i = i.upper()
    results.append(i)

# But with list comprenhension the code is pretty simple
results = [i.upper() for i in strings]

# We can also use list comprehension

results = [i.upper() + " CITY" for i in strings if i.isalpha()]


# Now let't create a function
def times(num, times):
    """
    This function takes a number and a number of times and returns the
    product of the number and the number of times.
    """
    return num * times


# test it
times(2, 5)
# Now we can create a for loop
nums = [1, 2, 3, 4, 5, 6]
results = []
for i in nums:
    i = times(i, 5)
    results.append(i)
print(results)

# Now we can do it the same thing but with lists comprehensions
new_nums = [times(i, 5) for i in nums]
# we can also add conditions
new_nums = [times(i, 5) for i in nums if i > 2]
# it's more readable than a normal loop

# Let's create a new example
dicts = [{"name": "Brayan"}, {"name": "Miguel"}]

# The idea is extract the name of the dictionary
result = []
for i in dicts:
    result.append(i["name"])

# now with a list comprehension
result = [i["name"] for i in dicts]
