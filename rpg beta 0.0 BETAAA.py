from random import randint
import os
#--------------------CLASS DE ATAQUES!!--------------------
def Attack1_E(target):
    attack = randint(0,20)
    if (attack <=10 and attack > 0):
        print(f"Missed attack in {target.get_name()}")
    elif(attack > 10 and attack < 18):
        print(f"🗡️ Caused 20 damage in {target.get_name()}")
        damage = 20
        target.loss_hp(damage)
    else:
        print("ATTACK CRIT!!!")
        print(f"🗡️ Caused 40 damage in {target.get_name()}")
        damage = 40
        target.loss_hp(damage)



#--------------------CLASS DOS MOB--------------------
class Bag():
    def __init__(self, items = []):
        self.items = []
    def openBag(self):
        if len(self.items) > 0:
            for i in self.items:
                print(f'You have: {i}')
        else:
            print("You bag is empty.")

class Mob(object):
    def __init__(self, name, hp = 100, alive = True, items = []):
        self.hp = hp
        self.items = []
        self.alive = True
        self.name = name
    def get_hp(self):
        return self.hp
    def loss_hp(self, damage):
        self.hp -= damage
        return self.hp
    def get_name(self):
        return self.name
    def status(self):
        if self.hp <= 0:
            return self.alive == False
        elif self.hp > 0:
            return self.alive == True
    def __str__(self):
        f = f'--------\nLife of mob: {self.hp}💗'
        return f
class Warrior(Mob, Bag):
    def __init__(self,name, hp = 100 ,energy = 100, alive = True, items = 0):
        super().__init__(name, hp = 100, alive = True, items = 0)
        self.energy = energy
    def get_energy(self):
        return self.energy
    def __str__(self):
        f = f'Life of Warrior: {self.hp}💗 Energy of Warrior: {self.energy}'
        return f
class Lancer(Warrior, Bag):
    def __init__(self,name, hp = 100 ,energy = 100, alive = True):
        super().__init__(name, hp = 100,energy = 100, alive = True)
    def __str__(self):
        f = f'Life of Lancer: {self.hp}💗 Energy of Lancer: {self.energy}'
        return f
class Evil_Zombie(Mob):
    def __init__(self,name, hp = 100, alive = True):
        super().__init__(name, hp= 100, alive = True)
    def __str__(self):
        f = f'Life of Zombie: {self.hp}💗 Alive: {self.alive}'
        return f
def Spawn():
    spawnMobs = randint(0,50)
    if spawnMobs >=0 and spawnMobs <=50:
        print("SPAWN ZOMBIE IN YOUR FRONT!!!!")
        if mob.status() == True:
                while True:  
                    print("What your next action front MOB!!")
                    print("[1] Attack 🗡️")
                    print("[2] Run 🚪")
                    print(mob)
                    print(Warrior)
                    if Warrior.get_hp() > 0 and mob.get_hp() > 0:
                        option_attack = input("Your option: ")
                        match option_attack:
                            case '1':
                                Attack1_E(mob)
                                print('\n')
                                Attack1_E(Warrior)
                                print('\n')
                            case '2':
                                print('\n')
                                Run()
                                print('\n')
                            case default:
                                print('\n')
                                print ("WHAT THE FUCK THIS ACTION??????")
                                print('\n')
                    elif mob.get_hp() <= 0:
                        print("Mob is dead")
                        print(mob)
                        break 
                    elif Warrior.get_hp()<= 0:
                        print("You is dead..")
                        break 
        elif mob.status() == False:
            print("Mob is died...")
    else:
        print("Nothing...")
 
def Move():
    probability = randint(0,50)
    if probability >= 0 and probability <=45:
        Spawn()
    else:
        print("You moved.")
def Run():
    mob.alive = True


    
    
              
if __name__ == "__main__":
    mob = Evil_Zombie('Evil_Zombie', 100, True)
    Warrior = Warrior("Warrior1", 150, 100, True)
    print(Warrior)
    print('Welcome to world!')
    while True:  
        print("What your next action")
        print("[1] Move")
        print("[2] Open Bag 🎒")
        print("[3] Exit 🚪")
        if Warrior.get_hp() > 0:
            option = input("Your option: ")
            match option:
                case '1':
                    Move()
                case '2':
                    Warrior.openBag()
                case '3':
                    break
                case default:
                    print ("WHAT THE FUCK THIS ACTION??????")
        elif Warrior.get_hp()<= 0:
            print("GAME OVER!!")
            break 
    
    

