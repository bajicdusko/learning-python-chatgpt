# Exercise 1: Variable Assignment and Print
# Create three different type variables and print their type.

# Your code here

"""
Solution:
x = 10  # integer
y = 20.5  # float
z = "Hello"  # string
print(type(x), type(y), type(z))
"""

# Exercise 2: Strings and Their Methods
# Create a string, print its length, and convert it to uppercase and then to lowercase.

# Your code here

"""
Solution:
text = "Python is cool!"
print(len(text))  # length of the string
print(text.upper())  # convert to uppercase
print(text.lower())  # convert to lowercase
"""

# Exercise 3: Lists
# Create a list, append a new item to the list, remove an item from the list, sort the list, and reverse it.

# Your code here

"""
Solution:
my_list = [10, 20, 30, 40]
my_list.append(50)  # add item
my_list.remove(10)  # remove item
my_list.sort()  # sort the list
my_list.reverse()  # reverse the list
print(my_list)
"""

# Exercise 4: Dictionaries
# Create a dictionary, add a key-value pair to it, remove a key-value pair, modify a value, and retrieve a value for a specified key.

# Your code here

"""
Solution:
my_dict = {"apple": 1, "banana": 2}
my_dict["cherry"] = 3  # add item
del my_dict["apple"]  # remove item
my_dict["banana"] = 4  # modify value
print(my_dict["banana"])  # retrieve value
"""

# Exercise 5: Control Flow
# Write a Python program to find the largest number in a list.

# Your code here

"""
Solution:
numbers = [1, 2, 3, 4, 5]
max_num = max(numbers)
print(max_num)
"""

# Exercise 6: Loops
# Create a list and use a loop to print each item in the list.

# Your code here

"""
Solution:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
"""

# Exercise 7: Functions
# Create a function that takes two arguments and returns their sum.

# Your code here

"""
Solution:
def sum_two_numbers(a, b):
    return a + b

print(sum_two_numbers(5, 7))
"""

# Exercise 8: Exception Handling
# Write a try/except block to handle potential errors in your function from exercise 7.

# Your code here

"""
Solution:
try:
    print(sum_two_numbers(5, "7"))  # this will raise a TypeError
except TypeError:
    print("Inputs to sum_two_numbers must be numbers.")
"""

# Exercise 9: Working with External Libraries
# Use the `requests` library to make a GET request to a website of your choice and print the status code of the response.

# Your code here

"""
Solution:
import requests
response = requests.get("https://www.python.org/")
print(response.status_code)
"""