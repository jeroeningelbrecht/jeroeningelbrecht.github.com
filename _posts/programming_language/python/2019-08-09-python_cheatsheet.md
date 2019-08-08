---
layout: post
title: Python Cheat sheet
tags: [python, string, introspection, reflection, inheritance]
---

# Python cheat sheet

## Introspection and Reflection

### \_\_dict\_\_
#### scope
* _class_
* _object_

#### what
* class: what are the methods of your class and what are the values of the class variables
* object: what are the values of your object's properties

#### examples
[examples/dictEx.py](../examples/dictEx.py)
```python
class Example:
    counter = 0

    def __init__(self, val=1):
        self.__val = val


e = Example()

Example.__dict__ # {'__module__': '__main__', 'counter': 0, '__init__': <function Example.__init__ at 0x7fb01b097ea0>, '__dict__': <attribute '__dict__' of 'Example' objects>, '__weakref__': <attribute '__weakref__' of 'Example' objects>, '__doc__': None}

e.__dict__ # {'_Example__val': 1}
    
```

### \_\_name\_\_
#### scope
* _class_

#### what
Identify the module in the import system

#### examples
```python
# package foo.bar
# module name: module.py
def print_name():
    print(__name__)
    
print_name()
# prints: '__main__'
```

```python
from foo.bar.module import print_name

print_name() # function defined in the imported module.py
# prints: 'module' <> '__main__' when executed in the module.py file itself ^^
```

### type(obj)
#### scope
* _object_

#### what
returns the _class_ of the object

#### example
```python
class Example:
    pass
    

e = Example()
type(e)  # prints "<class '__main__.Example'>"
```