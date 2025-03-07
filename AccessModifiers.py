# class PrivateExample:
    def _init_(self):
        self.__private_var = "I am Private"  # Private Variable
    
    def __private_method(self):
        return "This is a Private Method"

    def access_private(self):
        return self.__private_method()  # Accessing Private Method

# Creating object and accessing private members within the class
private_obj = PrivateExample()
print("Private Variable (Access via Class Method):", private_obj.access_private())

# Trying to access private members outside the class (will cause an error)
# print(private_obj.__private_var)  # AttributeError
# print(private_obj.__private_method())  #  AttributeError

# Accessing private members using Name Mangling (not recommended)
print("Private Variable (Access via Name Mangling):", private_obj.PrivateExample_private_var)
# ------------------------------------------
# Protected Members Example
# ------------------------------------------

class ProtectedExample:
    def _init_(self):
        self._protected_var = "I am Protected"

    def _protected_method(self):
        return "This is a Protected Method"

class SubProtected(ProtectedExample):
    def access_protected(self):
        return self._protected_method()  # Accessing Protected Method

# Creating object and accessing protected members
protected_obj = SubProtected()
print("Protected Variable (Access via Child Class):", protected_obj._protected_var)
print("Protected Method (Access via Child Class):", protected_obj.access_protected())

# ------------------------------------------
# Public Members Example
# ------------------------------------------

class PublicExample:
    def _init_(self):
        self.public_var = "I am Public"

    def public_method(self):
        return "This is a Public Method"

# Creating object and accessing public members
public_obj = PublicExample()
print("Public Variable:", public_obj.public_var)
print("Public Method:", public_obj.public_method())
