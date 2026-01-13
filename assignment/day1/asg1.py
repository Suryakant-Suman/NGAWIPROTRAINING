from functools import reduce

num = range(1,20)

evenNum = list(filter(lambda x: x % 2 == 0, num))

squareNum = list(map(lambda x: x ** 2, num))

sumOfEvenSquarenum = reduce(lambda x, y: x + y, evenNum)

for index, value in enumerate(squareNum):
    print(index, value)
    