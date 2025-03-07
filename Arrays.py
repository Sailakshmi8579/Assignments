#1. Function to add integer values of an array

def sum_of_array(arr):
    total = sum(arr)
    print("Sum of array:", total)

arr = [1, 2, 3, 4, 5]
sum_of_array(arr)


#2. Function to calculate the average value of an array of integers

def average_of_array(arr):
    avg = sum(arr) / len(arr)
    print("Average of array:", avg)

arr = [10, 20, 30, 40, 50]
average_of_array(arr)



#3. Program to find the index of an array element

def find_index(arr, value):
    if value in arr:
        print("Index of", value, ":", arr.index(value))
    else:
        print(value, "not found in array")

arr = [5, 10, 15, 20, 25]
find_index(arr, 15)



#4. Function to test if an array contains a specific value

def contains_value(arr, value):
    print("Present" if value in arr else "Not Present")

arr = [1, 2, 3, 4, 5]
contains_value(arr, 3)



#5. Function to remove a specific element from an array

def remove_element(arr, value):
    arr = [x for x in arr if x != value]
    print("Array after removal:", arr)

arr = [10, 20, 30, 40, 50]
remove_element(arr, 30)



#6. Function to copy an array to another array

def copy_array(arr):
    new_arr = arr.copy()
    print("Copied array:", new_arr)

arr = [5, 10, 15, 20]
copy_array(arr)


#7. Function to insert an element at a specific position in the array

def insert_element(arr, value, index):
    arr.insert(index, value)
    print("Array after insertion:", arr)

arr = [1, 2, 4, 5]
insert_element(arr, 3, 2)


#8. Function to find the minimum and maximum value of an array

def min_max(arr):
    print("Minimum:", min(arr))
    print("Maximum:", max(arr))

arr = [50, 10, 20, 70, 30]
min_max(arr)



#9. Function to reverse an array

def reverse_array(arr):
    print("Reversed array:", arr[::-1])

arr = [1, 2, 3, 4, 5]
reverse_array(arr)


#10. Function to find duplicate values in an array

def find_duplicates(arr):
    duplicates = list(set([x for x in arr if arr.count(x) > 1]))
    print("Duplicate values:", duplicates)

arr = [1, 2, 3, 2, 4, 5, 1]
find_duplicates(arr)


#11. Program to find common values between two arrays

def common_values(arr1, arr2):
    common = list(set(arr1) & set(arr2))
    print("Common values:", common)

arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]
common_values(arr1, arr2)


#12. Method to remove duplicate elements from an array

def remove_duplicates(arr):
    arr = list(set(arr))
    print("Array after removing duplicates:", arr)

arr = [10, 20, 10, 30, 20, 40]
remove_duplicates(arr)


#13. Method to find the second largest number in an array

def second_largest(arr):
    arr = list(set(arr))  # Remove duplicates
    arr.sort(reverse=True)
    print("Second largest number:", arr[1] if len(arr) > 1 else "No second largest")

arr = [10, 20, 30, 40, 50]
second_largest(arr)


#14. Alternative method to find the second largest number in an array

def second_largest_alternative(arr):
    largest = second = float('-inf')
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif second < num < largest:
            second = num
    print("Second largest number:", second if second != float('-inf') else "No second largest")

arr = [5, 1, 9, 7, 2]
second_largest_alternative(arr)


#15. Method to find the number of even and odd numbers in an array

def count_even_odd(arr):
    even_count = len([x for x in arr if x % 2 == 0])
    odd_count = len(arr) - even_count
    print("Even count:", even_count)
    print("Odd count:", odd_count)

arr = [1, 2, 3, 4, 5, 6, 7, 8]
count_even_odd(arr)


#16. Function to get the difference between the largest and smallest value

def difference_min_max(arr):
    print("Difference:", max(arr) - min(arr))

arr = [100, 20, 50, 80, 10]
difference_min_max(arr)


#17. Method to verify if the array contains two specified elements (12 and 23)

def contains_elements(arr, elem1, elem2):
    print("Contains both elements" if elem1 in arr and elem2 in arr else "Does not contain both")

arr = [10, 12, 15, 23, 30]
contains_elements(arr, 12, 23)


#18. Program to remove duplicate elements and return a new array

def remove_duplicates_return(arr):
    new_arr = list(set(arr))
    print("New array without duplicates:", new_arr)

arr = [5, 10, 5, 20, 10, 30]
remove_duplicates_return(arr)
