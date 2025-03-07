# Superclass A
class A:
    def method1(self):
        print("Method1 from A (Specific to A)")

    def method2(self):
        print("Method2 from A (Specific to A)")

    def override_method(self):
        print("Overridden Method from A")

# Subclass B (inherits from A)
class B(A):
    def method3(self):
        print("Method3 from B (Specific to B)")

    def method4(self):
        print("Method4 from B (Specific to B)")

    def override_method(self):
        print("Overridden Method from B")

# Subclass C (inherits from B)
class C(B):
    def method5(self):
        print("Method5 from C (Specific to C)")

    def method6(self):
        print("Method6 from C (Specific to C)")

    def override_method(self):
        print("Overridden Method from C")

# Creating objects for each class
a_obj = A()
b_obj = B()
c_obj = C()

# Calling methods using respective objects
print("\n--- Calling Methods from A ---")
a_obj.method1()
a_obj.method2()
a_obj.override_method()

print("\n--- Calling Methods from B ---")
b_obj.method1()
b_obj.method2()
b_obj.method3()
b_obj.method4()
b_obj.override_method()

print("\n--- Calling Methods from C ---")
c_obj.method1()
c_obj.method2()
c_obj.method3()
c_obj.method4()
c_obj.method5()
c_obj.method6()
c_obj.override_method()

# Calling overridden method with superclass reference to B and C objects
print("\n--- Overridden Method with Superclass Reference ---")
a_ref = B()
a_ref.override_method()  # Calls B's overridden method

a_ref = C()
a_ref.override_method()  # Calls C's overridden method

# Runtime Polymorphism with Data Members / Instance Variables
class Parent:
    def _init_(self):
        self.value = "Parent Variable"

class Child1(Parent):
    def _init_(self):
        super()._init_()
        self.value = "Child1 Variable"

class Child2(Parent):
    def _init_(self):
        super()._init_()
        self.value = "Child2 Variable"

# Creating objects
parent = Parent()
child1 = Child1()
child2 = Child2()

# Accessing variables using superclass reference
print("\n--- Runtime Polymorphism with Data Members ---")
parent_ref = Parent()
print(parent_ref.value)

parent_ref = Child1()
print(parent_ref.value)

parent_ref = Child2()
print(parent_ref.value)
