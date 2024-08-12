def my_generator():
    yield [12, 3, 0.0027349150119391733]

# Iterate over the values
for value in my_generator():
    print(value)

# Convert to a list
values = list(my_generator())
print(values)
