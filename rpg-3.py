"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

class Hero:
    def __init__(self, health, power):
        self.health = health
        self.power = power
    
    def attack(self, opponent):
        opponent.health -= self.power
        print("You do %d damage to the goblin." % hero.power)
        if opponent.health <= 0:
            print("The goblin is dead.")

class Goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, opponent):
        # Goblin attacks hero
        opponent.health -= self.power
        print("The goblin does %d damage to you." % self.power)
        if opponent.health <= 0:
            print("You are dead.")

hero = Hero(10, 5)
goblin = Goblin(6, 2)

def main():

    while goblin.health > 0 and hero.health > 0:
        print("You have %d health and %d power." % (hero.health, hero.power))
        print("The goblin has %d health and %d power." % (goblin.health, goblin.power))
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

        if goblin.health > 0:
            goblin.attack(hero)

main()
