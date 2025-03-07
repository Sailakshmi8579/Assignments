# 1. Write a program to read a text file
def read_text_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File Content:\n", content)
    except FileNotFoundError:
        print("File not found!")

# 2. Write a program to write text to a .txt file using InputStream
def write_text_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)
    print("Text written successfully!")

# 3. Write a program to read a file stream
def read_file_stream(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found!")

# 4. Write a program to read a file stream that supports random access
def read_random_access(filename, position):
    try:
        with open(filename, 'r') as file:
            file.seek(position)
            content = file.read(20)  # Reading 20 characters from position
            print("Content from position:", content)
    except FileNotFoundError:
        print("File not found!")

# 5. Write a program to read a file at a particular index using seek()
def read_at_position(filename, position):
    try:
        with open(filename, 'r') as file:
            file.seek(position)
            print("Character at position", position, ":", file.read(1))
    except FileNotFoundError:
        print("File not found!")

# 6. Write a program to check whether a file has read and write access permissions
import os

def check_file_permissions(filename):
    if os.access(filename, os.R_OK):
        print("The file has read access.")
    else:
        print("No read access.")

    if os.access(filename, os.W_OK):
        print("The file has write access.")
    else:
        print("No write access.")

# Example Usage
filename = "example.txt"
write_text_file(filename, "Hello, this is a sample text file.\nPython file handling is useful.")
read_text_file(filename)
read_file_stream(filename)
read_random_access(filename, 10)
read_at_position(filename, 5)
check_file_permissions(filename)
