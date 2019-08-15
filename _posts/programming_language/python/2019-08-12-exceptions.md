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
* as
* else
* finally

**try:**  
&nbsp;&nbsp;&nbsp;&nbsp;*codeblock*  
{  
\[**except** \[ *exception-class*  \[ as ***noun*** \] ] **:**  
&nbsp;&nbsp;&nbsp;&nbsp;*codeblock*  
|  
**except** \[ **(** ***exception-class-1*** **,** ***exception-class-2*** \[, ... , *exception-class-n*\] **)** \[ as ***noun*** \] \]  
}

## examples
### Dealing with 1 or multiple exceptions
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
output
```
oops, not a correct mathematical operation
finally is always executed
------------------
wrong value José:  -1
finally is always executed
------------------
else is only executed in case no exception was caught
finally is always executed
```

### The 'as' keyword or Exceptions are also classes
Once you get grip of the Exception class, you can do with it whatever you'd do with any other class cfr [python cheat sheet](2019-08-09-python_cheatsheet.md)
```python
def as_error(text):
    try:
        int(text)
    except ValueError as error:
        print('an error occurred')
        print(error)


as_error('hello')
```
output
```
an error occurred
invalid literal for int() with base 10: 'hello'
```