# 1. Generate Arithmetic Exception without handling
def arithmetic_exception():
    result = 10 / 0  # This will cause ZeroDivisionError
    print(result)

# 2. Handle Arithmetic Exception using try-except block
def handle_arithmetic_exception():
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Arithmetic Exception Caught: Cannot divide by zero!")

# 3. Method that throws exception and calls it in main class without try block
def throw_exception():
    raise ValueError("This is a manually raised exception")

# 4. Program with multiple catch (except) blocks
def multiple_exceptions():
    try:
        num = int("Hello")  # ValueError
    except ZeroDivisionError:
        print("Caught ZeroDivisionError")
    except ValueError:
        print("Caught ValueError")
    except Exception as e:
        print(f"General Exception: {e}")

# 5. Throw exception with custom message
def throw_with_message():
    try:
        raise Exception("Custom Exception Message")
    except Exception as e:
        print(f"Caught Exception: {e}")

# 6. Create your own exception
class MyCustomException(Exception):
    pass

def custom_exception():
    try:
        raise MyCustomException("This is a user-defined exception")
    except MyCustomException as e:
        print(f"Caught Custom Exception: {e}")

# 7. Program with finally block
def finally_block():
    try:
        print("Executing Try Block")
        result = 10 / 0  # Will raise ZeroDivisionError
    except ZeroDivisionError:
        print("Caught ZeroDivisionError")
    finally:
        print("Finally Block Executed")

# 8. Generate Arithmetic Exception
def generate_arithmetic_exception():
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Arithmetic Exception: {e}")

# Calling all functions
print("\n1. Arithmetic Exception without handling (will crash):")
# arithmetic_exception()  # Uncomment to see error

print("\n2. Handling Arithmetic Exception:")
handle_arithmetic_exception()

print("\n3. Throw Exception Without Try Block:")
# throw_exception()  # Uncomment to see the exception

print("\n4. Multiple Exception Handling:")
multiple_exceptions()

print("\n5. Throw Exception with Custom Message:")
throw_with_message()

print("\n6. Custom Exception Handling:")
custom_exception()

print("\n7. Finally Block Execution:")
finally_block()

print("\n8. Generate Arithmetic Exception:")
generate_arithmetic_exception()
