class MethodOverloadingExample:

    # Task 1: Method Overloading using Different Number of Parameters (Same Type)
    def add(self, a, b=None):
        if b is None:
            print(f"Single Parameter: {a}")
        else:
            print(f"Two Parameters: {a} + {b} = {a + b}")

    # Task 2: Method Overloading using Different Types of Parameters
    def display(self, data):
        if isinstance(data, int):
            print(f"Integer Data: {data}")
        elif isinstance(data, str):
            print(f"String Data: {data}")
        elif isinstance(data, float):
            print(f"Float Data: {data}")

    # Task 3: Overloading with Same Name and Same Number of Parameters
    def greet(self, name):
        print(f"Hello, {name}!")

    def greet(self, age):  # Python will override the previous greet method
        print(f"You are {age} years old.")

# Creating Object
obj = MethodOverloadingExample()

# Calling methods
print("\nTask 1:")
obj.add(10)        # Calls the method with one parameter
obj.add(10, 20)    # Calls the method with two parameters

print("\nTask 2:")
obj.display(100)     # Integer
obj.display("Bujji") # String
obj.display(10.5)    # Float

print("\nTask 3:")
# obj.greet("Bujji")  # This will cause an issue as Python only keeps the last definition
obj.greet(21)        # Only the last greet() method is accessible
