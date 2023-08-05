import httpx

# Exercise 1: Make a simple GET request to 'https://httpbin.org/get' and print the status code.
# TODO: Your code here

# Solution:
# response = httpx.get('https://httpbin.org/get')
# print(response.status_code)

# Exercise 2: Pass query parameters to a GET request. Query parameters should be "name" and "age".
# Use the URL 'https://httpbin.org/get'.
# TODO: Your code here

# Solution:
# params = {'name': 'John', 'age': 30}
# response = httpx.get('https://httpbin.org/get', params=params)
# print(response.json())

# Exercise 3: Make a POST request to 'https://httpbin.org/post' with JSON data. The data should be {"key": "value"}.
# TODO: Your code here

# Solution:
# json_data = {'key': 'value'}
# response = httpx.post('https://httpbin.org/post', json=json_data)
# print(response.json())

# Exercise 4: Make a GET request to 'https://httpbin.org/get' and raise an exception for status code errors.
# TODO: Your code here

# Solution:
# response = httpx.get('https://httpbin.org/get')
# response.raise_for_status()

# Exercise 5: Use a session to make a GET request to 'https://httpbin.org/get'.
# TODO: Your code here

# Solution:
# with httpx.Client() as client:
#     response = client.get('https://httpbin.org/get')
#     print(response.json())

# Exercise 6: Make an asynchronous GET request to 'https://httpbin.org/get'.
# TODO: Your code here

# Solution:
# import asyncio
#
# async def fetch_data():
#     async with httpx.AsyncClient() as client:
#         response = await client.get('https://httpbin.org/get')
#         return response.json()
#
# asyncio.run(fetch_data())

# Exercise 7: Make a GET request to 'https://httpbin.org/status/500' and handle potential errors using try/except.
# TODO: Your code here

# Solution:
# try:
#     response = httpx.get('https://httpbin.org/status/500')
#     response.raise_for_status()
# except httpx.HTTPStatusError as e:
#     print(f"An HTTP error occurred: {str(e)}")

# Exercise 8: Define a Python class representing a user. The class should have two properties: 'name' and 'age'.

class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

# Exercise 9: Create a method to deserialize a JSON string into an instance of the User class.
# You can assume the JSON string will be in the format '{"name": "<name>", "age": <age>}' for this exercise.
# TODO: Your code here

# Solution:
# class User:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def from_json(cls, json_str: str) -> Optional['User']:
#         data = json.loads(json_str)
#         if 'name' in data and 'age' in data:
#             return cls(data['name'], data['age'])
#         return None

# Exercise 10: Create a method to serialize an instance of the User class into a JSON string.
# TODO: Your code here

# Solution:
# class User:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def from_json(cls, json_str: str) -> Optional['User']:
#         data = json.loads(json_str)
#         if 'name' in data and 'age' in data:
#             return cls(data['name'], data['age'])
#         return None
#
#     def to_json(self) -> str:
#         return json.dumps({'name': self.name, 'age': self.age})
