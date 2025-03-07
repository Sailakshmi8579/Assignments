# 1. Define a static variable and access it through a class
class Example:
    static_var = 100  # Static variable

print("Accessing static variable through class:", Example.static_var)


# 2. Define a static variable and access it through an instance
class Example2:
    static_var = 200  # Static variable

obj = Example2()
print("Accessing static variable through instance:", obj.static_var)


# 3. Define a static variable and change it within the instance
class Example3:
    static_var = 300  # Static variable

obj1 = Example3()
obj1.static_var = 400  # Changing static variable only for this instance
print("Static variable after modifying in instance:", obj1.static_var)
print("Static variable in class remains same:", Example3.static_var)


# 4. Define a static variable and change it within the class
class Example4:
    static_var = 500  # Static variable

print("Before modifying in class:", Example4.static_var)
Example4.static_var = 600  # Changing at class level
print("After modifying in class:", Example4.static_var)
