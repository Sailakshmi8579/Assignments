from abc import ABC, abstractmethod

# 1. Create an abstract class with abstract and non-abstract methods
class AbstractExample(ABC):
    
    def non_abstract_method(self):
        print("This is a non-abstract method in AbstractExample class")
    
    @abstractmethod
    def abstract_method(self):
        pass

# 2. Create a subclass for the abstract class and implement the abstract method
class ChildExample(AbstractExample):
    
    def abstract_method(self):
        print("Abstract method implemented in ChildExample class")

# 3. Create an instance of the child class and call the abstract method
child_obj = ChildExample()
child_obj.abstract_method()

# 4. Call the non-abstract method using the child class object
child_obj.non_abstract_method()
