from examples.enemy.SuperEnemy import SuperEnemy
from examples.enemy.SubEnemy import SubEnemy
from examples.enemy.SubEnemy import HybridEnemy

enemy = SubEnemy(100, 'blockingEnemy')

hybrid = HybridEnemy(100, 'hybrid enemy')

print('--- enemy.get_name() ----')
enemy.get_name()

print('\n--- enemy.get_health() ---')
enemy.get_health()

print('\n--- enemy.defend() ---')
enemy.defend()

print('\n--- enemy.attack() ---')
enemy.attack()


print('\n--- the module name (package + name of the python file): enemy.__module__ ---')
print(enemy.__module__)

print('\n--- the name of the class: enemy.__name__')
print(type(enemy).__name__)

print('\n--- get the class of an object (__module__ + __name__: type(enemy) ---')
print(type(enemy))


''' Inheritance'''
print('\n--- SubEnemy._bases__ ---')
print(SubEnemy.__bases__)

print('\n--- is SubEnemy a subclass of SuperEnemy: issubclass(SubEnemy, SuperEnemy)')
print(issubclass(SubEnemy, SuperEnemy))

print('\n--- hybrid.abbrev ---')
print(hybrid.abbrev)

print('\n--- is enemy instance of any of these classes (SubEnemy, SuperEnemy, BaseException):  isinstance(enemy, (SubEnemy, SuperEnemy, BaseException))---')
print(isinstance(enemy, (SubEnemy, SuperEnemy, BaseException)))

print('\n--- string interning: two different string variables refer to the same string object')
print('both variables s1 and s2 point to the same "hello" string object: print(s1 is s2)')
s1 = "hello"
s2 = "hello"
print(s1 is s2)

print('\n--- overriding the __str__(self) method in the SubEnemy class: print(enemy) ---')
print(enemy)

print("\n--- name mangling: there ain't no such thing as 'private in python': print(enemy._SuperEnemy__name)")
print(enemy._SuperEnemy__name)

print("\n--- all values of all properties of the enemy object: print(enemy.__dict__ ---")
print(enemy.__dict__)

print('\n--- the values of the class variables and all functions of the SubEnemy class: print(SubEnemy.__dict__ ---')
print(SubEnemy.__dict__)
