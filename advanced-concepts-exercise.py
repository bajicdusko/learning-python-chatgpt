# 1. Syntactic Sugar
# List comprehension is an example of Python's syntactic sugar.
# Exercise: Convert the following code using list comprehension:
# nums = []
# for i in range(10):
#     if i % 2 == 0:
#         nums.append(i)
# print(nums)

# Solution:
"""
nums = [i for i in range(10) if i % 2 == 0]
print(nums)
"""

# 2. Functions (map, filter, reduce)
# Exercise: Given a list of numbers, use map, filter and reduce to find the product of the squares of even numbers.

# Solution:
"""
from functools import reduce

numbers = [1, 2, 3, 4, 5]
even_squares = map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))
product = reduce(lambda x, y: x * y, even_squares)

print(product) # Output: 16
"""

# 3. Function similar to map, filter, reduce, that are commonly used.
# Exercise: Use the itertools.groupby function to group a list of words by their first letter.

# Solution:
"""
import itertools

words = ["apple", "bat", "bar", "atom", "book"]
words.sort()
groups = itertools.groupby(words, key=lambda x: x[0])

for letter, word in groups:
    print(f"{letter}: {list(word)}")
"""

# 4. Context Managers
# Exercise: Implement a Timer context manager that measures the time taken to execute a block of code.

# Solution:
"""
import time

class Timer:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, type, value, traceback):
        self.end = time.time()
        print(f"Time taken: {self.end - self.start} seconds")
"""

# 5. Decorators
# Exercise: Implement a retry decorator that retries a function if it throws an exception.

# Solution:
"""
import time

def retry(func):
    def wrapper(*args, **kwargs):
        for _ in range(5):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print("Exception caught: ", e)
                time.sleep(1)
        print("Function failed after 5 retries")
    return wrapper
"""

# 6. Coroutines
# Exercise: Implement a coroutine that computes a running average.

# Solution:
"""
async def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count
"""

# 7. Exceptions
# Exercise: Write a function that handles exceptions when dividing two numbers.

# Solution:
"""
def safe_divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Cannot divide by zero")
"""