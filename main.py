# print("hello world")

class Hero:
    
    def __init__(self, name, health, attackPower, armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def attack(self, enemy):
        print(self.name + " menyerang " + enemy.name)
        enemy.attackedBy(self, self.attackPower)

    def attackedBy(self, enemy, enemy_attackPower):
        print(self.name + " diserang ", enemy.name)
        damage_taken = enemy_attackPower/enemy.armorNumber
        print("Serangan terasa : " + str(damage_taken))
        self.health -= damage_taken
        print("Darah " + self.name + " tersisa " + str(self.health))

naruto = Hero("naruto", 100, 10, 5)
sasuke = Hero("sasuke", 100, 5, 10)

naruto.attack(sasuke)
sasuke.attack(naruto)