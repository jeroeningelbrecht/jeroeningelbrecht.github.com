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

Example.__dict__ # {'__module__': '__main__', 'counter': 0, '__init__': <function Example.__init__ at 0x7fb01b097ea0>, '__dict__': <attribute '__dict__' of 'Example' objects>, '__weakref__': <attribute '__weakref__' of 'Example' objects>, '__doc__': None}

e.__dict__ # {'_Example__val': 1}
    
```