data = [1,2,3,4,5,6,2,4]

square = list(map(lambda x: x**2, data));

uniqueEvenNum = set(filter(lambda x: x%2==0, data))

cube = dict(map(lambda x: (x,x**3), data))

print("Squares list", square)
print("unique even Number", uniqueEvenNum)
print("Cube mapped", cube)