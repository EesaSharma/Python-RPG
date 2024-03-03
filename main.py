import random
from classes.game import Person, bcolors


# Example usage:
player1 = Person("Player 1", 100, 20, 10, 5)
enemy1 = Person("Enemy 1", 80, 10, 8, 3)

print(bcolors.BOLD + bcolors.OKBLUE + "AN ENEMY ATTACKS!" + bcolors.ENDC)

print("======================")
print("\n")
print("NAME                 HP                                     MP")
print(player1.name + "       " + str(player1.hp) + "/" + str(player1.maxhp) + " |" + bcolors.OKGREEN + "█" * int((player1.hp / player1.maxhp) * 20) + bcolors.ENDC + "|"
      + "       " + str(player1.mp) + "/" + str(player1.maxmp) + " |" + bcolors.OKBLUE + "█" * int((player1.mp / player1.maxmp) * 10) + bcolors.ENDC + "|")
print(enemy1.name + "       " + str(enemy1.hp) + "/" + str(enemy1.maxhp) + " |" + bcolors.FAIL + "█" * int((enemy1.hp / enemy1.maxhp) * 20) + bcolors.ENDC + "|"
      + "       " + str(enemy1.mp) + "/" + str(enemy1.maxmp) + " |" + bcolors.OKBLUE + "█" * int((enemy1.mp / enemy1.maxmp) * 10) + bcolors.ENDC + "|")
print("\n")
##

# Player actions
print(bcolors.OKBLUE + bcolors.BOLD + "    ACTIONS:" + bcolors.ENDC)
print("    1. Attack")
print("    2. Magic")
print("    3. Items")

##

def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 2

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        print("                    __________________________________________________ ")
        print(bcolors.BOLD + self.name + "  " +
              current_hp + " |" + bcolors.FAIL + hp_bar + bcolors.ENDC + "|")