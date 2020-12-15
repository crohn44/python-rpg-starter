"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.isalive = True

    def attack(self, opponent):
        opponent.health -= self.power
        print("The %s does %d damage to the %s." % (self, self.power, opponent))
        opponent.alive()
        if opponent.isalive == False:
            print("The %s is dead." % opponent)

    def alive(self):
        if self.health < 1:
            self.isalive = False

    def print_status(self):
        print("The %s has %d health and %d power." % (self, self.health, self.power))

class Hero(Character):
    def __str__(self):
        return "Hero"


class Goblin(Character):
    def __str__(self):
        return "Goblin"

hero = Hero(10, 5)
goblin = Goblin(6, 2)

def main():

    while goblin.isalive == True and hero.isalive == True:
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            hero.attack(goblin)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        goblin.alive()
        if goblin.isalive:
            goblin.attack(hero)
        
        print()

main()
