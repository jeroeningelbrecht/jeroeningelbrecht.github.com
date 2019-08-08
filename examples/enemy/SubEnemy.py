from examples.enemy.SuperEnemy import SuperEnemy


class SubEnemy(SuperEnemy):

    def __init__(self, health, name):
        super().__init__(health, name)

    def defend(self):
        super().defend()
        self.__block()

    def __block(self):
        print('__name__:', __name__, '; block')
        self.get_health()

    def specific_attack(self):
        print('specific_attack:', None)

    def __str__(self):
        return '__str__(self): ' + self._SuperEnemy__name


class WaterEnemy(SubEnemy):
    abbrev = 'WE'

    def specific_attack(self):
        print('specific_attack:', 'water')

    pass


class LandEnemy(SubEnemy):
    abbrev = 'LE'

    def specific_attack(self):
        print('specific_attack:', 'land')

    pass

class HybridEnemy(WaterEnemy, LandEnemy):
    pass