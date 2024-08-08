# Sample list of tuples
tuples = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]

# Create a dictionary to store modified tuples
lookup_table = {}

# Modify the tuples and add them to the lookup table
for i, (num, fruit) in enumerate(tuples):
    modified_tuple = (num * 2, fruit.upper())
    lookup_table[i] = modified_tuple

# Print the lookup table
print(lookup_table)
