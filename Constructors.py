# 1. Write a class with a default constructor, one-argument constructor, and two-argument constructor.
class Example:
    # Default constructor
    def _init_(self):
        print("Default Constructor Called")

    # One-argument constructor
    def _init_(self, arg1):
        self.arg1 = arg1
        print(f"One-argument Constructor Called: {self.arg1}")

    # Two-argument constructor
    def _init_(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        print(f"Two-argument Constructor Called: {self.arg1}, {self.arg2}")

# Instantiating the class (only the last _init_ method will work due to method overriding)
obj1 = Example("Hello", "World")


# 2. Call the constructors of the superclass from a child class.
class Parent:
    def _init_(self):
        print("Parent Default Constructor Called")

    def _init_(self, value):
        self.value = value
        print(f"Parent Constructor with Argument Called: {self.value}")

class Child(Parent):
    def _init_(self):
        super()._init_("Parent Argument")  # Calls the parent class constructor
        print("Child Constructor Called")

obj2 = Child()


# 3. Apply private, public, protected, and default access modifiers to the constructor.
class AccessModifiers:
    def _init_(self, public, protected, private):
        self.public_var = public      # Public attribute
        self._protected_var = protected  # Protected attribute
        self.__private_var = private  # Private attribute

    def display(self):
        print(f"Public: {self.public_var}, Protected: {self.protected_var}, Private: {self._private_var}")

obj3 = AccessModifiers(10, 20, 30)
print(obj3.public_var)  # Accessible
print(obj3._protected_var)  # Accessible but should be used with caution
# print(obj3.__private_var)  # Not directly accessible, will cause an error
obj3.display()


# 4. Illustrate the concept of attributes of a constructor.
class AttributeExample:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

obj4 = AttributeExample("Alice", 25)
obj4.show()
