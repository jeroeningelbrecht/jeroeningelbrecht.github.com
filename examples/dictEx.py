class Example:
    counter = 0

    def __init__(self, val=1):
        self.__val = val


e = Example()

print(Example.__dict__)
print(e.__dict__)
