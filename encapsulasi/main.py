class Hero:
    
    __jumlah = 0

    def __init__(self, name, health, attPower, armor):
        self.__name = name
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return "Hero\t:{}\nLevel\t:{}\nXP\t:{}\nHealth\t:{}/{}\nAttack\t:{}\nArmor\t:{}".format(self.__name, self.__level, self.__exp, self.__health, self.__healthMax, self.__attPower, self.__armor)

minato = Hero("minato", 100, 5, 10)