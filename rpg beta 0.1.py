from random import randint
import os
# --------------------CLASS DOS MOB--------------------
class Item():
    def __init__(self, name, typer = ['weapon', 'armor', 'utility'], damage = 0, armor = 0, life = 0):
        self.name = name
        self.typer = typer
        self.damage = damage
        self.armor = armor
        self.life = life
    def getType(self):
        return self.typer
    def getName(self):
        return self.name
    def getDamage(self):
        return self.damage
    def getArmor(self):
        return self.armor
    def __str__(self):
        f = f'\n{self.name} Typer: {self.typer}\nDamage: {self.damage}\nAmor: {self.armor}\n'
        return f
class Bag(Item):
    def __init__(self, items = []):
        self.items = items
    def openBag(self):
        if len(self.items) > 0:
                while True:
                        print("\nYOU BAG: 🎒\n")
                        for count, j in enumerate(self.items):
                            print(f'[{count}] - {j}         ')   
                            print("------------------")
                        print("\nWhat you option in BAG 🎒")
                        print("[1] Delete Item")
                        print("[2] Use Item")
                        print("[3] Exit")
                        option = input("\nYou option: ")
                        if option == '1':
                            print("\nChoice item to delete\n\n")
                            for count, j in enumerate(self.items):
                                print(f'[{count}] - {j}         ')   
                                print("------------------")
                            print("[99] to Exit")
                            option2 = int(input("Choice item to delete or Exit: "))
                            try:
                                if option2 != 99:
                                    self.items.pop(option2)
                                elif option2 == 99:
                                    continue
                                else:
                                    print("\nWHAT THE FUCK THIS OPTION!!!\n")
                            except:
                                print("\nWHAT THE FUCK THIS OPTION!!!\n")
                        elif option == '2':
                            for j in self.items:
                                if j.typer == 'utility':
                                    print("\nChoice item to use\n\n")
                                    for count, j in enumerate(self.items):
                                        if j.typer == 'utility':
                                            print(f'[{count}] - {j}         ')
                                    print("[99] to Exit")
                                    option2 = int(input("Choice item to use or Exit: "))
                                    if option2 != 99 and self.items[option2].typer == 'utility':
                                        self.use_potion()
                                        self.hp += self.items[option2].life
                                        self.items.pop(option2)
                                    else:
                                        print("YOU NO HAVE THIS ITEM!!!!")
                                else:
                                    print("You no have items to use.")

                        elif option == '3':
                            break
                        else:
                            print("\nWHAT THE FUCK THIS OPTION!!!\n")

        else:
            print("\nYOU BAG: 🎒\n")
            print("------------------")
            print("Is empty.")
            print("------------------")
    def pickItem(self, Item):
            print('=================================================')
            print(F'You found {Item.getName()} what do you want to do?')
            while True:
                print("[1] Pick")
                print("[2] Ignore")
                print('=================================================')
                choice = input("Option: ")
                if choice == '1':
                    if len(self.items) <= 9:
                        print("\n")
                        print(f'{Item.getName()} guarded.')
                        print('\n')
                        self.items.append(Item)
                        break
                    else:
                        print("Bag is full!!")

                elif choice == '2':
                    print("You ignored.")
                    break
                else:
                    print("\nWHAT THE FUCK IS OPTION!!??\n")
class Mob(object):
    def __init__(self, name, hp = 100, alive = True, damage = 10, items = [], kills = 0, equip_chest = [], equip_weapon = [], equip_helmet = [], weapon = 0, armor = 0):
        self.hp_fix = hp
        self.hp = self.hp_fix
        self.damage_fix = damage
        self.damage = self.damage_fix
        self.kills = kills
        self.items = items
        self.alive = True
        self.name = name
        self.equip_chest = []
        self.equip_weapon  = []
        self.equip_helmet =  []
        self.weapon = weapon
        self.armor = armor
    def get_hp(self):
        return self.hp
    def set_armor_hp(self):
        self.hp = self.hp_fix + self.armor
        return self.hp
    def set_weapon_damage(self):
        self.damage = self.damage_fix + self.weapon
        return self.damage
    def use_potion(self):
        if self.hp >= 100:
            print("Your life is full!!!")
        elif self.hp <100:
            pass
            
    def equip(self):
        if len(self.items) > 0:
            while True:
                print(self.check_equip())
                self.check_equip()
                print(self.hp)
                print(self.damage)
                print(self.weapon)
                print(self.armor)
                print(self.set_armor_hp())
                print(self.set_weapon_damage())
                print(self.equip_weapon[0].getDamage())
                print("Which part do you want to equip?")
                print('[1] - Helmet')
                print('[2] - Chest')
                print('[3] - Weapon')
                print('[4] - Exit')
                option = input("You option: ")
                print('\n\n')
                if option == '1':
                    for count, j in enumerate(self.items):
                        if j.typer == 'helmet':
                            print(f'[{count}] - {j}         ')
                    while True:
                        print('\n\n[99] to Exit')
                        option = int(input("Choice helmet: "))
                        if option == option and self.items[option].typer == 'helmet' and len(self.equip_helmet) == 0:
                            self.equip_helmet.append(self.items[option])
                            self.check_equip()
                            break
                        elif len(self.equip_helmet) == 1 and self.items[option].typer == 'helmet':
                            print("Helmet replaced ")
                            self.equip_helmet.pop()
                            self.equip_helmet.append(self.items[option])
                            self.check_equip()
                            break
                        elif  self.items[option].typer != 'helmet':
                            print("That't not a helmet ")
                        elif option == 99:
                            break
                        else:
                            print("WHAT THE FUCK THIS OPTION !!!!!!")
                elif option == '2':
                    for count, j in enumerate(self.items):
                        if j.typer == 'chest':
                            print(f'[{count}] - {j}         ') 
                    while True:
                        print('[99] to Exit')
                        option = int(input("Choice chest: "))
                        if option != 99 and self.items[option].typer == 'chest' and len(self.equip_chest) == 0:
                            self.equip_chest.append(self.items[option])
                            self.check_equip()
                            break
                        elif len(self.equip_chest) == 1 and option != 99 and self.items[option].typer == 'chest':
                            print("Chest replaced ")
                            self.equip_chest.pop()
                            self.equip_chest.append(self.items[option])
                            self.check_equip()
                            break
                        elif option != 99 and self.items[option].typer != 'chest':
                            print("That't not a chest ")
                        elif option == 99:
                            break
                        else:
                            print("This option not exist")
                elif option == '3':
                    for count, j in enumerate(self.items):
                        if j.typer == 'weapon':
                            print(f'[{count}] - {j}         ')   
                    while True:
                        print('[99] to Exit')
                        option = int(input("Choice weapon: "))
                        if option != 99 and self.items[option].typer == 'weapon' and len(self.equip_weapon) == 0:
                            self.equip_weapon.append(self.items[option])
                            self.check_equip()
                            break
                        elif len(self.equip_weapon) == 1 and option != 99 and self.items[option].typer == 'weapon':
                            print("Weapon replaced ")
                            self.equip_weapon.pop()
                            self.equip_weapon.append(self.items[option])
                            self.check_equip()
                            break
                        elif option != 99 and self.items[option].typer != 'weapon':
                            print("That't not a weapon ")
                        elif option == 99:
                            break
                elif option == '4':
                    break
                else:
                    print("!! WHAT FUCK THIS OPTION!!")
        else:
            print("You no have Items!!!!")


    def check_equip(self):              
        if len(self.equip_chest) == 0 and len(self.equip_helmet) == 0 and len(self.equip_weapon) == 0:
            f = f'[  ] - Chest'
            g = f'[  ] - Helmet'
            h = f'[  ] - Weapon'
            return f,g,h
        elif len(self.equip_chest) == 1 and len(self.equip_helmet) == 0 and len(self.equip_weapon) == 0:
            f = f'[🛡️ ] - Chest'
            g = f'[  ] - Helmet'
            h = f'[  ] - Weapon'
            return f,g,h
            self.armor = self.equip_chest[0].getArmor()
            self.set_armor_hp()
        elif len(self.equip_chest) == 1 and len(self.equip_helmet) == 1 and len(self.equip_weapon) == 0:
            f = f'[🛡️ ] - Chest'
            g = f'[🛡️ ] - Helmet'
            h = f'[  ] - Weapon'
            return f,g,h
            self.armor = self.equip_chest[0].getArmor() + self.equip_helmet[0].getArmor()
            self.set_armor_hp()
        elif len(self.equip_chest) == 1 and len(self.equip_helmet) == 1 and len(self.equip_weapon) == 1:
            f = f'[🛡️ ] - Chest'
            g = f'[🛡️ ] - Helmet'
            h = f'[🛡️ ] - Weapon'
            return f,g,h
            self.armor = self.equip_chest[0].getArmor() + self.equip_helmet[0].getArmor()
            self.set_armor_hp()
            self.weapon = self.equip_weapon[0].getDamage()
            self.set_weapon_damage()
        elif len(self.equip_chest) == 1 and len(self.equip_helmet) == 0 and len(self.equip_weapon) == 1:
            f = f'[🛡️ ] - Chest'
            g = f'[  ] - Helmet'
            h = f'[🛡️ ] - Weapon'
            return f,g,h
            self.weapon = self.equip_weapon[0].getDamage()
            self.set_weapon_damage()
            self.armor = self.equip_chest[0].getArmor()
            self.set_armor_hp()
        elif len(self.equip_chest) == 0 and len(self.equip_helmet) == 1 and len(self.equip_weapon) == 0:
            f = f'[  ] - Chest'
            g = f'[🛡️ ] - Helmet'
            h = f'[  ] - Weapon'
            return f,g,h
            self.armor = self.equip_helmet[0].getArmor()
            self.set_armor_hp()
        elif len(self.equip_chest) == 0 and len(self.equip_helmet) == 1 and len(self.equip_weapon) == 1:
            f = f'[  ] - Chest'
            g = f'[🛡️ ] - Helmet'
            h = f'[🛡️ ] - Weapon'
            return f,g,h
            self.weapon = self.equip_weapon[0].getDamage()
            self.set_weapon_damage()
            self.armor = self.equip_helmet[0].getArmor()
            self.set_armor_hp()
        elif len(self.equip_chest) == 0 and len(self.equip_helmet) == 0 and len(self.equip_weapon) == 1:
            f = '[  ] - Chest'
            g = '[  ] - Helmet'
            h = '[🛡️ ] - Weapon'
            return f,g,h
            self.weapon = self.equip_weapon[0].getDamage()
            self.set_weapon_damage()

    def get_damage(self):
        return self.damage
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
    def revive(self):
        self.hp = 100
        return self.hp
        self.alive = True
        return self.alive
    def run(self):
        self.hp = 0
        return self.hp
        self.alive = False
        return self.alive

    def __str__(self):
        f = f'--------\nLife of mob: {self.hp}💗'
        return f
class Warrior(Mob, Bag, Item):
    def __init__(self,name, hp = 100 ,energy = 100, alive = True, damage = 10, items = [],equip_chest = [], equip_weapon = [], equip_helmet = [], weapon = 0, armor = 0):
        super().__init__(name, hp = 100, alive = True, damage = 10, items = [], kills=0, equip_chest = [], equip_weapon = [], equip_helmet = [], weapon = 0, armor = 0)
        self.energy = energy
    def get_energy(self):
        return self.energy
    def __str__(self):
        f = f'Life of Warrior: {self.hp}💗 Energy of Warrior: {self.energy} Damage of Warrior: {self.damage}🛡️'
        return f
class Lancer(Warrior, Bag, Item):
    def __init__(self,name, hp = 100 ,energy = 100, alive = True, damage = 10, items = [],equip_chest = [], equip_weapon = [], equip_helmet = [], weapon = 0, armor = 0):
        super().__init__(name, hp = 100,energy = 100, alive = True, damage = 10, items = [],equip_chest = [], equip_weapon = [], equip_helmet = [], weapon = 0, armor = 0)
    def __str__(self):
        f = f'Life of Lancer: {self.hp}💗 Energy of Lancer: {self.energy} Damage of Lancer: {self.damage}🛡️'
        return f
class Archer(Warrior, Bag, Item):
    def __init__(self,name, hp = 100 ,energy = 100, alive = True, damage = 10, items = [],equip_chest = [], equip_weapon = [], equip_helmet = [], weapon = 0, armor = 0):
        super().__init__(name, hp = 100,energy = 100, alive = True, damage = 10, items = [],equip_chest = [], equip_weapon = [], equip_helmet = [], weapon = 0, armor = 0)
    def __str__(self):
        f = f'Life of Archer: {self.hp}💗 Arrows of Archer: {self.energy} Damage of Archer: {self.damage}🛡️'
        return f
class Evil_Zombie(Mob, Item):
    def __init__(self,name, hp = 100, damage = 10, alive = True, items = []):
        super().__init__(name, hp= 100, damage = 10, alive = True, items = [])
    def __str__(self):
        f = f'Life of {self.name}: {self.hp}💗 Alive: {self.alive}'
        return f
class Evil_Wolfmen(Mob, Item):
    def __init__(self,name, hp = 100, damage = 10, alive = True, items = []):
        super().__init__(name, hp= 150, damage = 15, alive = True, items = [])
    def __str__(self):
        f = f'Life of {self.name}: {self.hp}💗 Alive: {self.alive}'
        return f
class Evil_Archer(Mob, Item):
    def __init__(self,name, hp = 100, damage = 10, alive = True, items = []):
        super().__init__(name, hp= 70, damage = 20, alive = True, items = [])
    def __str__(self):
        f = f'Life of {self.name}: {self.hp}💗 Alive: {self.alive}'
        return f
def Attack1_E(target):
    attack = randint(0,20)

    if (attack <=10 and attack > 0):
        print('=================================================')
        print(f"Missed attack in {target.get_name()}")
        print('=================================================')
    elif(attack > 10 and attack < 18):
        if target == mob:
            damage = Hero.get_damage()
            print('=================================================')
            print("Attack")
            print(f"🗡️ Caused {damage} damage in {target.get_name()}")
            print('=================================================')
            target.loss_hp(damage)
        else:
            damage = mob.get_damage()
            print('=================================================')
            print("Attack")
            print(f"🗡️ Caused {damage} damage in {target.get_name()}")
            print('=================================================')
            target.loss_hp(damage)
    else:
        if target == mob:
            damage = Hero.get_damage() * 2
            print('=================================================')
            print("ATTACK CRIT!!!")
            print(f"🗡️ Caused {damage} damage in {target.get_name()}")
            print('=================================================')
            target.loss_hp(damage)
        else:
            damage = mob.get_damage() * 2
            print("ATTACK CRIT!!!")
            print(f"🗡️ Caused {damage} damage in {target.get_name()}")
            target.loss_hp(damage)
def limit_Bag():
    if len(Hero.items) <= 10:
        pass
    else:
        print("Bag is full!!!")
def Combat():
    while True: 
        print('=================================================')
        print("Enemy:", mob)
        print('=================================================')
        print("You:", f"Life: {Hero.get_hp()}💗 Energy: {Hero.get_energy()} Damage: {Hero.get_damage()}")
        print('=================================================')
        print("What your next action front MOB!!")
        print("[1] Attack 🗡️")
        print("[2] Run 🚪")
        print('=================================================')
        if Hero.get_hp() > 0 and mob.get_hp() > 0:
            option_attack = input("Your option: ")
            print('\n')
            print('\n')
            print('\n')
            if option_attack == '1':
                Attack1_E(mob)
                print('\n')
                Attack1_E(Hero)
                print('\n')
            elif option_attack == '2':
                print('\n')
                Run()
                break
                print('\n')
            else:
                print('\n')
                print ("WHAT THE FUCK THIS ACTION??????")
                print('\n')
        elif mob.get_hp() <= 0:
            print("Mob is dead")
            mob.revive()
            break 
        elif Hero.get_hp()<= 0:
            print("\n")
            print("You is dead..💀")
            break 

def Run():
    probability = randint(0,10)
    if probability >= 0 and probability <=5:
        print("You run sucess")
        mob.run()
    elif probability >= 6 and probability <=10:
        print("You failed")
def Kills(self):
    self.kills += 1
def Spawn():
    spawnMobs = randint(0,50)
    if spawnMobs >=0 and spawnMobs <=50:
        print("\n\n\n\n\n\n")
        print(f"SPAWN {mob.get_name()} IN YOUR FRONT!!!!")
        if mob.status() == True:
            Combat()
        elif mob.status() == False:
            print("Mob is died...")
            mob.status() == True
    else:
        print("Nothing...")
 
def Move():
    probability = randint(0,30)
    if probability >= 0 and probability <=11:
        Spawn()
    elif probability >= 11 and probability <=17:
        Hero.pickItem(Axe)
    else:
        print("You moved.")
def randomMob():
    probability = randint(0,10)
    if probability >= 0 and probability <=1:
        mob = Evil_Zombie('Evil_Zombie_Old,', 50, 7)
        return mob
    elif probability >= 2 and probability <=3:
        mob = Evil_Zombie('Evil_Zombie')
        return mob

    elif probability >= 4 and probability <=5:
        mob = Evil_Zombie('Evil_Zombie_Kid', 30, 20)
        return mob

    elif probability >= 6 and probability <=7:
        mob = Evil_Wolfmen('Evil_WolfMen')
        return mob  

    elif probability >= 8 and probability <=10:
        mob = Evil_Archer('Evil_Archer')
        return mob
def randomWeapon():
    probability = randint(1,13)
    if probability >= 1 and probability <= 2:
        Axe = Item('SmallAxe', 'weapon', 10, 0)
        return Axe
    elif probability >=3  and probability <= 5:
        Axe = Item('SmallStick', 'weapon', 5, 0)
        return Axe
    elif probability >= 6 and probability <= 7:
        Axe = Item('Sword', 'weapon', 15, 0)
        return Axe
    elif probability >= 8 and probability <= 8:
        Axe = Item('BigSword', 'weapon', 20, 0)
        return Axe
    elif probability >= 9 and probability <= 9:
        Axe = Item('Chest', 'chest', 0 , 20)
        return Axe
    elif probability >= 10 and probability <= 11:
        Axe = Item('Helmet', 'helmet', 0 , 10)
        return Axe
    elif probability >= 12 and probability <= 13:
        Axe = Item('Helmet', 'helmet', 0 , 10)
        return Axe
def Choice_Hero():
    while True:
        print("Choice your hero.")
        print("[1] Warrior")
        print("[2] Lancer")
        print("[3] Archer")
        option = input("Your option: ")
        if option == '1':
            Hero = Warrior("Warrior")
            return Hero
            break
            print(f"You picked: {Hero}")
        elif option == '2':
            Hero = Lancer('Lancer')
            return Hero
            break
            print(f"You picked: {Hero}")
        elif option == '3':
            Hero = Archer('Archer')
            return Hero
            break
            print(f"You picked: {Hero}")
        else:
            print("What this option? ")



if __name__ == "__main__":
    print("\n\n\n")
    print('=================================================')
    print('Welcome to world!')
    print('=================================================')
    Hero = Choice_Hero()
    Machadão = Item('Machadão', 'Weapon', 30, 0)
    Hero.equip_weapon.append(Machadão)

    while True:
        if Hero.get_hp() > 0:  
            Axe = randomWeapon()
            # Potion = Item('Potion', 'utility', 0, 0, 100)
            # Hero.items.append(Potion)
            # Hero.items.append(Potion)
            # cabeca = Item('Helmet', 'helmet', 0 , 50)
            # Hero.items.append(cabeca)
            mob = randomMob()
            print('=================================================')
            print(Hero)
            print("You kills: ", Hero.kills)
            print('=================================================')
            print("What your next action")
            print("[1] Move 🦶")
            print("[2] Open Bag 🎒")
            print("[3] Equip 🛡️")
            print("[4] Exit 🚪")
            print('=================================================')
            option = input("Your option: ")
            if option == '1':
                Move()
            elif option == '2':
                Hero.openBag()
            elif option == '3':
                Hero.equip()
            elif option == '4':
                break
            else:
                print ("WHAT THE FUCK THIS ACTION??????")
        elif Hero.get_hp()<= 0:
            os.system('cls')
            print("GAME OVER!!")
            break 

