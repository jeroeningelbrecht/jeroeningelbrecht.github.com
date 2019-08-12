---
layout: post
author: jeroen
title: Exceptions
tags: [python, exceptions]
---
# Exceptions
## keywords
* try
* except
* else
* finally

## example
```python
def divide(n):
    try:
        1/n
        chr(n)
    except (ArithmeticError, ZeroDivisionError):
        print('oops, not a correct mathematical operation')
    except ValueError:
        print('wrong value José: ', n)
    else:
        print('else is only executed in case no exception was caught')
    finally:
        print('finally is always executed')


divide(0)
print('------------------')
divide(-1)
print('------------------')
divide(2)
```
```python
oops, not a correct mathematical operation
finally is always executed
------------------
wrong value José:  -1
finally is always executed
------------------
else is only executed in case no exception was caught
finally is always executed
```