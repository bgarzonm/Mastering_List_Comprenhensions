# Now let's deep into the if statement
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Basic list comprehension return every number in nums
[i for i in nums]
# But let's say we want only the evens numbers and multiply them by 5
[i * 5 for i in nums if i % 2 == 0]
# But we can also add the if statement in the left side
[i * 5 if i % 2 == 0 else i for i in nums]

# So we basically can combine both
[i * 5 if i % 2 == 0 else i for i in nums if i > 4]

# Note that the right side works like a filter
# and if you try to add a else clause to the right side it's not possible

# [i * 5 if i%2 == 0 else i for i in nums if i > 4 else i]
# So remember if you want to use else clause is always to the left side

# This works like a map lambda function
# Map lambda function receives two arguments, the first argument
# is the iteratos and the second argument is the parameter to iterate
list(map(lambda x: x * 5, nums))
# We can also add if statements
list(map(lambda x: x * 5 if x % 2 == 0 else x, nums))
# so this two things are the same thing
[i * 5 if i % 2 == 0 else i for i in nums]

# And the same thing with the filter to the right
list(map(lambda x: x * 5 if x % 2 == 0 else x, filter(lambda x: x > 4, nums)))

[i * 5 if i % 2 == 0 else i for i in nums if i > 4]

# Basically the if statement to the right is the first filter in for loops
# and the second if is the operation.

results = []
for i in nums:
    # The right filter
    if i > 4:
        #  The left if statement
        if i % 2 == 0:
            i = i * 5
        else:
            i
        results.append(i)
