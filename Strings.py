# 1. Different ways of creating a string
string1 = "Hello"
string2 = 'World'
string3 = """Multiline
String"""
print(string1, string2)
print(string3)

# 2. Concatenating two strings using + operator
str1 = "Python"
str2 = "Programming"
result = str1 + " " + str2
print("Concatenated String:", result)

# 3. Finding the length of the string
str_length = len(result)
print("Length of String:", str_length)

# 4. Extract a string using Substring
substring = result[0:6]
print("Extracted Substring:", substring)

# 5. Searching in strings using index()
index_pos = result.index("gram")
print("Index position of 'gram':", index_pos)

# 6. Matching a String Against a Regular Expression With matches()
import re
pattern = r"Python"
match = re.search(pattern, result)
print("Matching result:", "Found" if match else "Not Found")

# 7. Comparing strings
str3 = "Python"
str4 = "python"
print("Are both strings equal?", str3 == str4)

# 8. startsWith(), endsWith() and compareTo()
print("Starts with 'Py':", result.startswith("Py"))
print("Ends with 'ing':", result.endswith("ing"))

# 9. Trimming strings with strip()
str_trim = "  Hello Python  "
print("Trimmed String:", str_trim.strip())

# 10. Replacing characters in strings with replace()
modified_str = result.replace("Python", "Java")
print("String after replace:", modified_str)

# 11. Splitting strings with split()
split_str = result.split(" ")
print("Split Result:", split_str)

# 12. Converting integer objects to Strings
num = 123
num_str = str(num)
print("Converted Integer to String:", num_str)

# 13. Converting to uppercase and lowercase
print("Uppercase:", result.upper())
print("Lowercase:", result.lower())
