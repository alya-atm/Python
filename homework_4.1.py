import random as rd


# Описание данных
class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = rd.randint(100, 150)
        self.power = rd.randint(20, 30)

    def show_attributes(self):
        return 'Воин {}. Сила атаки:{}. Здоровье: {}'.format(self.name, self.power, self.health)

    def get_damage(self, power_damage):
        self.health = self.health - power_damage

        if self.health < 0:
            return 'Воин {} получил {} урона и погиб '.format(self.name, power_damage, self.health)

        else:
            return 'Воин {} получил {} урона. Осталось здоровья {}.'.format(self.name, power_damage, self.health)


class Warrior_with_shield(Warrior):
    shield = rd.randint(5, 10)

    def get_damage(self, power_damage):
        self.health = self.health - power_damage + self.shield

        if self.health < 0:
            return 'Воин {} получил {} урона и погиб '.format(self.name, power_damage, self.health)
        else:
            return 'Воин {} получил {} урона. Осталось здоровья {}.'.format(self.name, power_damage, self.health)


class Warrior_expert(Warrior):
    def power_expert(self):
        if rd.randint(1, 5) == 1:
            return self.power * 2
        else:
            return self.power
#Задание 1
warrior1 = Warrior('Warrior1')
print(warrior1.show_attributes())
warrior2 = Warrior_with_shield('Warrior2')
print(warrior2.show_attributes())
warrior3 = Warrior_expert('Warrior3')
print(warrior3.show_attributes())

# Задание 2

# Бой между Warrior1 и Warrior2
warrior1 = Warrior('Warrior1')
warrior2 = Warrior_with_shield('Warrior2')

i = 1
print("Бой между Warrior1 и Warrior2")
while warrior1.health > 0 and warrior2.health > 0:
    if i % 2 == 1:
        warrior2.get_damage(warrior1.power)
        i = i + 1
    else:
        warrior1.get_damage(warrior2.power)
        i = i + 1

if warrior1.health <= 0:
    print(warrior2.name, 'победил')
else:
    print(warrior1.name, 'победил')

# Бой между Warrior1 и Warrior3

warrior1 = Warrior('Warrior1')
warrior3 = Warrior_expert('Warrior3')

i = 1
print("Бой между Warrior1 и Warrior3")
while warrior1.health > 0 and warrior3.health > 0:
    if i % 2 == 1:
        warrior3.get_damage(warrior1.power)
        i = i + 1
    else:
        warrior1.get_damage(warrior3.power_expert())
        i = i + 1

if warrior1.health <= 0:
    print(warrior3.name, 'победил')
else:
    print(warrior1.name, 'победил')

# Бой между Warrior1 и Warrior3
warrior2 = Warrior_with_shield('Warrior2')
warrior3 = Warrior_expert('Warrior3')

i = 1
print("Бой между Warrior2 и Warrior3")
while warrior2.health > 0 and warrior3.health > 0:
    if i % 2 == 1:
        warrior3.get_damage(warrior2.power)
        i = i + 1
    else:
        warrior2.get_damage(warrior3.power_expert())
        i = i + 1

if warrior2.health <= 0:
    print(warrior3.name, 'победил')
else:
    print(warrior2.name, 'победил')

# Задание 3
arm1 = []
arm1 = [Warrior('warrior1/1-' + str(i)) for i in range(4)]
arm1.extend(Warrior_with_shield('warrior2/1-' + str(i)) for i in range(4))
arm1.extend(Warrior_expert('warrior3/1-' + str(i)) for i in range(2))

arm2 = []
arm2 = [Warrior('warrior1/2-' + str(i)) for i in range(4)]
arm2.extend(Warrior_with_shield('warrior2/2-' + str(i)) for i in range(4))
arm2.extend(Warrior_expert('warrior3/2-' + str(i)) for i in range(2))

i = 1
while len(arm1) > 0 and len(arm2) > 0:
    w1 = rd.randint(0, len(arm1) - 1)
    w2 = rd.randint(0, len(arm2) - 1)
    if i % 2 == 1:
        if type(arm1[w1]) == Warrior_expert:
            arm2[w2].get_damage(arm1[w1].power_expert())

        else:
            arm2[w2].get_damage(arm1[w1].power)

        if arm2[w2].health < 0:
            del arm2[w2]
    else:
        if type(arm2[w2]) == Warrior_expert:
            arm1[w1].get_damage(arm2[w2].power_expert())

        else:
            arm1[w1].get_damage(arm2[w2].power)

        if arm1[w1].health < 0:
            del arm1[w1]
    i = i + 1
if len(arm1) == 0:
    print('Армия 2 победила')
else:
    print('Армия 1 победила')