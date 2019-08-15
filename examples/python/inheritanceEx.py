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


class One:
    def do_it(self):
        print('doit from One')

    def do_anything(self):
        self.do_it()


class Two(One):
    def do_it(self):
        print('doit from Two')


one = One()
two = Two()
one.do_anything()
two.do_anything()
