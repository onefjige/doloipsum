class Format:
    def __init__(self):
        self._mesh = None
    
    @property
    def mesh(self):
        return self._mesh
    
    @mesh.setter
    def mesh(self, value):
        self._mesh = value

# Creating an instance of Format
format = Format()

# Setting the mesh property
format.mesh = "example_value"

# Accessing the mesh property
property_value = format.mesh
print(property_value)  # Output: example_value
