#Here are the answers in a simple Python format:

#1. Print "Bright IT Career" ten times using for loop
for i in range(10):
    print("Bright IT Career")


#2. Print 1 to 20 numbers using while loop
i = 1
while i <= 20:
    print(i, end=" ")
    i += 1


#3. Equal and not equal operators
a, b = 10, 20
print(a == b)  # False
print(a != b)  # True


#4. Print odd and even numbers
print("Even numbers:", [i for i in range(1, 21) if i % 2 == 0])
print("Odd numbers:", [i for i in range(1, 21) if i % 2 != 0])


#5. Find the largest number among three numbers
a, b, c = 5, 10, 7
print("Largest:", max(a, b, c))


#6. Print even numbers between 10 and 20 using while
i = 10
while i <= 20:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1


#7. Print 1 to 10 using do-while loop (Python simulation)
i = 1
while True:
    print(i, end=" ")
    i += 1
    if i > 10:
        break


#8. Check if a number is Armstrong or not
num = 153
armstrong_sum = sum(int(digit) ** 3 for digit in str(num))
print("Armstrong" if armstrong_sum == num else "Not Armstrong")


#9. Check if a number is prime
num = 7
if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
    print("Prime")
else:
    print("Not Prime")


#10. Check if a number is palindrome
num = 121
print("Palindrome" if str(num) == str(num)[::-1] else "Not Palindrome")

#11. Check if a number is EVEN or ODD using if-else (Python doesn't have switch)
num = 4
print("Even" if num % 2 == 0 else "Odd")

#12. Program to identify gender based on M/F input

gender = 'M'
print("Male" if gender == 'M' else "Female" if gender == 'F' else "Invalid input")

