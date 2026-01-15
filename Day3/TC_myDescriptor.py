class MyDescriptor:
    def __set__(self, instance, value):
        print("Setting value")
        instance._x = value

    def __get__(self, instance, owner):
        print("Getting value")
        return instance._x

class test:
    x = MyDescriptor()
t = test()
t.x = 2
print(t.x)