# Python cheat sheet

## Introspection and Reflection

### __dict__
#### scope
* class
* object

#### what
* class: what are the methods of your class and what are the values of the class variables
* object: what are the values of your object's properties

#### examples
[examples/dictEx.py](./examples/dictEx.py)
```python
class Example:
    counter = 0

    def __init__(self, val=1):
        self.__val = val


e = Example()

print(Example.__dict__)
print(e.__dict__)
    
```