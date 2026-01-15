fruits = ["apple", "banana", "cherry"]
for index, value in enumerate(fruits):
    print(index, value)

from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
print(Color.RED.value)
print(Color.GREEN.value)
print(Color.BLUE.value)