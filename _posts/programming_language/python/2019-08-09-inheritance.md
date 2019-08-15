---
layout: post
author: jeroen
title: Inheritance
tags: [python, inheritance]
---
# Inheritance
## What defines what object component is being executed
Python looks for objects components in the following order:
* inside the object itself
* in its superclasses, from __top to bottom__
* if there is more than one superclass, Python scans them from left to right

```python
class SuperClass1:

    def speak(self):
        return 'SuperClass1 is speaking'


class SuperClass2:

    def speak(self):
        return 'SuperClass2 is speaking'


class SubClass(SuperClass1, SuperClass2):

    def interact(self):
        print(super().speak())


sub = SubClass()
sub.interact() # prints 'SuperClass1 is speaking'
```

## Polymorphism
```python
class One:
    def do_it(self):
        print('do_it from One')

    def do_anything(self):
        self.do_it()


class Two(One):
    def do_it(self):
        print('do_it from Two')


one = One()
two = Two()
one.do_anything()   # 'do_it from One'
two.do_anything()   # 'do_it from Two'

```
> the situation in which the subclass is able to modify its superclass behavior 
(just like in the example) is called polymorphism.  
The word comes from Greek (polys: "many, much" and morphe, "form, shape"), which means that one and the same class can take various forms depending on the redefinitions done by any of its subclasses

## <a name="base_and_sub"></a>Baseclass(es) and Subclass(es)
There are ways to get the baseclass(es) (superclass(es)) of a class and to get the classes that inherit from one particular class (the subclass(es)).

### Discover the baseclass(es)
**code**: *\_\_bases__*  
**scope**: *class*

**example**  
see below

### Discover the subclass(es)
**code**: *\_\_subclasses__()*  
**scope**: *class*  
**example**
```python
class SuperClass1:

    def speak(self):
        return 'SuperClass1 is speaking'


class SuperClass2:

    def speak(self):
        return 'SuperClass2 is speaking'


class SubClass(SuperClass1, SuperClass2):

    def interact(self):
        print(super().speak())


sub = SubClass()
sub.interact() # prints 'SuperClass1 is speaking'
print(sub.__class__.__bases__)

superC = SuperClass1()
print(superC.__class__.__subclasses__())
```