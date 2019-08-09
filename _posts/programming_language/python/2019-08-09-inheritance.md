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