# 1. Program to print your name
print("J.Hima Bindu Sailakshmi")
# 2. Single line and multi-line comments
# This is a single-line comment
'''
This is a multi-line comment.
You can write multiple lines here.
'''
# 3. Defining variables of different data types and printing them
int_A = 98
bool = True      
char_A = "CODING"       
float_A = 29.6      
double_A  = 45.612356

print("Integer:", int_A)
print("Boolean:", bool)
print("Character:", char_A)
print("Float:", float_A)
print("Double:", double_A)
# 4. Local and Global variables with the same name
global_var = "I am a global variable"

def my_function():
    global_var = "I am a local variable"  # This is a local variable
    print("Inside function:", global_var)

my_function()
print("Outside function:", global_var)  # This prints the global variable
