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