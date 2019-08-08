class SuperEnemy:

    abbrev = "SE"

    def __init__(self, health=100, name='evil_creeper'):
        self.__health = health
        self.__name = name

    def defend(self):
        print('__name__:', __name__, '; self.__name: ', self.__name, ' defend')

    def attack(self):
        print('__name__:', __name__, '; self.__name: ', self.__name, ' attack')

    def get_name(self):
        print('__name__:', __name__, '; self.__name: ', self.__name)

    def get_health(self):
        print('__name__: ', __name__, '; self.__health: ', self.__health)
