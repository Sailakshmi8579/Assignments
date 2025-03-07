# Folder Structure

/packages_demo/
    ├──package1/
    │   ├── _init_.py
    │   ├── class1.py
    ├──package2/
    │   ├── _init_.py
    │   ├── class2.py
    ├──main.py



# Step 1: Create package1/class1.py

class Class1:
    def _init_(self):
        print("Constructor of Class1 is called")

    def method1(self):
        print("Method of Class1 is called")



# Step 2: Create package2/class2.py

class Class2:
    def _init_(self):
        print("Constructor of Class2 is called")

    def method2(self):
        print("Method of Class2 is called")



# Step 3: Create package1/_init.py and package2/init_.py

# This file makes the folder a package



#Step 4: Create main.py (Main Program)

# Import classes from packages
from package1.class1 import Class1
from package2.class2 import Class2

# Create objects and call methods
obj1 = Class1()
obj1.method1()

obj2 = Class2()
obj2.method2()


'''
🔹 Expected Output

Constructor of Class1 is called
Method of Class1 is called
Constructor of Class2 is called
Method of Class2 is called


---
 Steps to Run the Code

1. Create a folder packages_demo.


2. Inside packages_demo, create two subfolders: package1 and package2.


3. Inside package1, create class1.py and _init_.py.


4. Inside package2, create class2.py and _init_.py.


5. Create main.py inside packages_demo and run it.
'''
