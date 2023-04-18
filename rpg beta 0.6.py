from random import randint
import os
import datetime
# --------------------CLASS DOS MOB--------------------
class Item():
    def __init__(self, name, typer,race, damage = 0, armor = 0, life = 0):
        self.name = name
        self.typer = typer
        self.race = race
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
        f = f'{self.name}\nDamage: {self.damage} 🔥\nArmor: {self.armor} 🛡️\nLife: {self.life} 💗'
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
                        print("[1] Delete Item")
                        print("[2] Use Item")
                        print("[3] Equip Item")
                        print("[4] Exit")
                        option = input("\nYou option: ")
                        if option == '1':
                            print("\nChoice item to delete\n\n")
                            for count, j in enumerate(self.items):
                                print(f'[{count}] - {j}         ')   
                                print("------------------")
                            print("[11] to Exit")
                            option2 = int(input("Choice item to delete or Exit: "))
                            if option2 != 11:
                                self.items.pop(option2)
                            elif option2 == 11:
                                continue
                            else:
                                print("\nWHAT THE FUCK THIS OPTION!!!\n")
                        elif option == '2':
                            Hero.use_item()
                        elif option == '3':
                            Hero.equip()
                        elif option == '4':
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
    def __init__(self, name, hp = 100, maxHp = 100, energy = 130, maxEnergy = 130, alive = True, damage = 10, items = [], kills = 0, equip_chest = [], equip_weapon = [], weapon = 0, armor = 0, combat = False, golds = 0,exp=0, level=0,up_level=50):
        self.hp = hp
        self.exp = exp
        self.up_level = up_level
        self.level = level
        self.maxHp = maxHp
        self.damage_fix = damage
        self.damage = self.damage_fix
        self.kills = kills
        self.items = items
        self.alive = True
        self.combat = False
        self.golds = golds
        self.name = name
        self.equip_chest = []
        self.equip_weapon  = []
        self.weapon = weapon
        self.armor = armor
        self.energy = energy
        self.maxEnergy = maxEnergy
    def level_up(self):
        if self.exp >= self.up_level:
            self.level += 1
            self.exp -= self.up_level
            self.up_level *= 2.2
            print("Congratulations, you've gone up the level 🎉")
            return self.up_level
        else:
            pass
    def Attack1_E(self,target):
        attack = randint(0,20)
        if (attack <=10 and attack > 0):
            print('=================================================')
            print(f"Missed attack in {target.get_name()}")
            print('=================================================')
        elif(attack > 10 and attack < 18):
            if target == mob:
                damage = self.get_damage()
                print('=================================================')
                print("Attack")
                print(f"🗡️ Caused {damage} damage in {target.get_name()}")
                print('=================================================')
                target.loss_hp(damage)
            else:
                damage = self.get_damage()
                print('=================================================')
                print("Attack")
                print(f"🗡️ Caused {damage} damage in {target.get_name()}")
                print('=================================================')
                target.loss_hp(damage)
        else:
            if target == mob:
                damage = self.get_damage() * 2
                print('=================================================')
                print("ATTACK CRIT!!!")
                print(f"🗡️ Caused {damage} damage in {target.get_name()}")
                print('=================================================')
                target.loss_hp(damage)
            else:
                damage = mob.get_damage() * 2
                print('=================================================')
                print("ATTACK CRIT!!!")
                print(f"🗡️ Caused {damage} damage in {target.get_name()}")
                print('=================================================')
                target.loss_hp(damage)
    def win_exps(self,exp):
        self.exp += exp
        self.level_up()
        return self.exp
    def drop_exp(self):
        exp = randint(10,30)
        self.exp += exp
        print(f'{self.name} dropped {exp} exps')
        Hero.win_exps(exp)
    def get_energy(self):
        return self.energy
    def set_combat(self, combat):
       self.combat = combat
       return self.combat
    def set_energy(self):
        if self.energy > self.maxEnergy:
            self.energy = 100
            return self.energy
        elif self.energy <= 0:
            self.energy = 0
            return self.energy
        else:
            return self.energy
    def sleep(self):
        global day,mounth,year,hours,minute
        if hours >= 0 and hours <= 6 or hours >=18:
            if self.energy < self.maxEnergy:
                random = randint(0,10)
                print(f"You sleep 6 hours and 17 minutes")
                print(f"recupered {random} energy")
                self.energy += 30
                self.energy += random
                self.set_energy()
                hours += 6
                horario()
            else:
                print("You Energy is full, stranger")
        else:
            print("YOU DON'T SLEEP!! IT'S DAY!")
            
    def get_hp(self):
        return self.hp
    def get_golds(self):
        return self.golds
    def drop_golds(self):
        gold = randint(0,20)
        self.golds += gold
        print(f'{self.name} dropped {gold} golds')
        Hero.win_golds(gold)
    def win_golds(self,gold):
        self.golds += gold
        return self.golds
    def set_golds(self,gold):
        self.golds -= gold
        return self.golds
    def set_armor_hp(self):
        if self.maxHp == 120:
            self.maxHp += self.armor
        elif self.maxHp == 150:
            self.maxHp += self.armor
        elif self.maxHp == 80:
            self.maxHp += self.armor

    def set_weapon_damage(self):
        self.damage =  self.damage_fix + self.weapon
        return self.damage
    def use_potion(self, potion):
        if self.hp >= self.maxHp:
            print("Your life is full!!!")
        elif self.hp < self.maxHp:
            self.hp += potion
            if self.hp > self.maxHp:
                self.hp = self.maxHp
    def equip(self):
        if len(self.items) > 0:
            while True:
                print(self.check_equip())
                self.check_equip()
                print(Hero)
                print("\nWhich part do you want to equip?\n")
                print('[1] - Chest')
                print('[2] - Weapon')
                print('[3] - Exit\n')
                option = input("You option: ")
                print('\n\n')
                if option == '1':
                    for count, j in enumerate(self.items):
                        if j.typer == 'chest':
                            print(f'[{count}] - {j}         ') 
                    while True:
                        print('[11] to Exit')
                        option = int(input("Choice chest: "))
                        if option != 11 and self.items[option].typer == 'chest' and len(self.equip_chest) == 0:
                            self.equip_chest.append(self.items[option])
                            self.check_equip()
                            break
                        elif len(self.equip_chest) == 1 and option != 11 and self.items[option].typer == 'chest':
                            print("Chest replaced ")
                            self.equip_chest.pop()
                            self.equip_chest.append(self.items[option])
                            self.check_equip()
                            break
                        elif option != 11 and self.items[option].typer != 'chest':
                            print("That't not a chest ")
                        elif option == 11:
                            break
                        else:
                            print("This option not exist")
                elif option == '2':
                    for count, j in enumerate(self.items):
                        if j.typer == 'weapon':
                            print(f'[{count}] - {j}         ')   
                    while True:
                        print('[11] to Exit')
                        option = int(input("Choice weapon: "))
                        if option != 11 and self.items[option].typer == 'weapon' and len(self.equip_weapon) == 0:
                            self.equip_weapon.append(self.items[option])
                            self.check_equip()
                            break
                        elif len(self.equip_weapon) == 1 and option != 11 and self.items[option].typer == 'weapon':
                            print("Weapon replaced ")
                            self.equip_weapon.pop()
                            self.equip_weapon.append(self.items[option])
                            self.check_equip()
                            break
                        elif option != 11 and self.items[option].typer != 'weapon':
                            print("That't not a weapon ")
                        elif option == 11:
                            break
                elif option == '3':
                    break
                else:
                    print("!! WHAT FUCK THIS OPTION!!")
        else:
            print("You no have Items!!!!")

    def use_item(self):
        for j in self.items:
            if j.typer == 'utility':
                print("\nChoice item to use\n\n")
                for count, j in enumerate(self.items):
                    if j.typer == 'utility':
                        print(f'[{count}] - {j}         ')
                        print("-------------------------3")
                print("\n[11] to Exit\n")
                option2 = int(input("Choice item to use: "))
                if option2 != 11 and self.items[option2].typer == 'utility':
                    potion = self.items[option2].life
                    self.use_potion(potion)
                    print(f"You cured {potion} of life")
                    self.items.pop(option2)
                elif option2 == 11:
                    break
                else:
                    print("YOU NO HAVE THIS ITEM!!!!")
            else:
                print("You no have items to use.")
    def check_equip(self):              
        if len(self.equip_chest) == 0 and len(self.equip_weapon) == 0:
            f = f'[  ] - Chest'
            h = f'[  ] - Weapon'
            return (f,h)
        elif len(self.equip_chest) == 1 and len(self.equip_weapon) == 0:
            f = f'[🛡️ ] - Chest'
            h = f'[  ] - Weapon'
            self.armor = self.equip_chest[0].getArmor()
            self.set_armor_hp()
            return (f,h)
        elif len(self.equip_chest) == 1 and len(self.equip_weapon) == 1:
            f = f'[🛡️ ] - Chest'
            h = f'[🛡️ ] - Weapon'
            self.weapon = self.equip_weapon[0].getDamage()
            self.set_weapon_damage()
            self.armor = self.equip_chest[0].getArmor()
            self.set_armor_hp()
            return (f,h)
        elif len(self.equip_chest) == 0 and len(self.equip_weapon) == 1:
            f = '[  ] - Chest'
            h = '[🛡️ ] - Weapon'
            self.weapon = self.equip_weapon[0].getDamage()
            self.set_weapon_damage()
            return(f,h)

    def get_damage(self):
        return self.damage
    def loss_hp(self, damage):
        self.hp -= damage
        return self.hp
    def get_name(self):
        return self.name
    def status(self):
        if self.hp <= 0:
            self.alive = False
            return self.alive
        elif self.hp > 0:
            self.alive = True
            return self.alive
    def revive(self):
        self.hp = 100
        return self.hp
        self.status()
    def Kills(self):
        self.kills += 1
    def __str__(self):
        f = f'--------\nLife of {self.name}: {self.hp}💗 Damage of {self.name}: {self.damage}🛡️'
        return f
class Warrior(Mob, Bag, Item):
    def __init__(self,name, hp = 100 ,maxHp = 100, energy = 130, maxEnergy = 130, alive = True, damage = 15, items = [],equip_chest = [], equip_weapon = [], weapon = 0, armor = 0, combat = False, golds = 0,exp=0, level=0,up_level=50):
        super().__init__(name, hp = 150,maxHp = 150, energy = 130, maxEnergy = 130,  alive = True, damage = 15, items = [], kills=0, equip_chest = [], equip_weapon = [], weapon = 0, armor = 0, golds = 0,exp=0, level=0,up_level=50)
    def __str__(self):
        f = f'Life of Warrior: {self.hp}/{self.maxHp}💗  Energy of Warrior: {self.energy}/{self.maxEnergy}⚡ Damage of Warrior: {self.damage}🛡️'
        return f
class Lancer(Mob, Bag, Item):
    def __init__(self,name, hp = 100 ,maxHp = 100, energy = 130, maxEnergy = 130, alive = True, damage = 15, items = [],equip_chest = [], equip_weapon = [], weapon = 0, armor = 0, combat = False, golds = 0,exp=0, level=0,up_level=50):
        super().__init__(name, hp = 110 ,maxHp = 110, energy = 120, maxEnergy = 120, alive = True, damage = 20, items = [],equip_chest = [], equip_weapon = [], weapon = 0, armor = 0, combat = False, golds = 0,exp=0, level=0,up_level=50)
    def __str__(self):
        f = f'Life of Lancer: {self.hp}💗/{self.maxHp}💗 Energy of Lancer: {self.energy}/{self.maxEnergy}⚡ Damage of Lancer: {self.damage}🛡️'
        return f
class Archer(Mob, Bag, Item):
    def __init__(self,name, hp = 80 ,maxHp = 80, energy = 50,maxEnergy = 50,  alive = True, damage = 25, items = [],equip_chest = [], equip_weapon = [], weapon = 0, armor = 0, arrows = 30,combat = False, golds = 0,exp=0, level=0,up_level=50):
        self.arrows = arrows
        super().__init__(name, hp = 80,maxHp = 80, energy = 50,maxEnergy = 50,  alive = True, damage = 25, items = [],equip_chest = [], equip_weapon = [], weapon = 0, armor = 0,combat = False, golds = 0,exp=0, level=0,up_level=50)
    def use_arrow(self):
        if self.arrows > 0:
            self.arrows -= 1
            return self.arrows
    def get_arrow(self, arrow):
        self.arrows += arrow
        return self.arrows
    def Special_Attack(self,target):
        if self.energy >= 35:
            self.energy -= 35
            if target == mob:
                damage = self.get_damage() *0.9
                print('=================================================')
                print("Special Attack!! Double Attack")
                print(f"🗡️ Caused {damage} damage in {target.get_name()}")
                print(f"🗡️ And again you caused {damage} damage in {target.get_name()}")
                print('=================================================')
                target.loss_hp(damage*2)
        else:
            print("You no have energy")
                
    def __str__(self):
        f = f'Life of Archer: {self.hp}/{self.maxHp}💗 Energy of Archer: {self.energy}/{self.maxEnergy}⚡ Arrows of Archer: {self.arrows} 🏹  Damage of Archer: {self.damage}🛡️'
        return f
class Evil_Zombie(Mob, Item):
    def __init__(self,name, hp = 100,maxHp = 100,  damage = 10, alive = True, items = [], golds = 0,exp=0, level=0,up_level=50):
        super().__init__(name, hp= 100,maxHp = 100,  damage = 10, alive = True, items = [], golds = 0,exp=0, level=0,up_level=50)
    def __str__(self):
        f = f'Life of {self.name}: {self.hp}💗 Damage: {self.damage}🛡️'
        return f
class Evil_Wolfmen(Mob, Item):
    def __init__(self,name, hp = 100,maxHp = 100,  damage = 10, alive = True, items = [], golds = 0,exp=0, level=0,up_level=50):
        super().__init__(name, hp= 150,maxHp = 150,  damage = 15, alive = True, items = [], golds = 0,exp=0, level=0,up_level=50)
    def __str__(self):
        f = f'Life of {self.name}: {self.hp}💗 Damage: {self.damage}🛡️'
        return f
class Evil_Archer(Mob, Item):
    def __init__(self,name, hp = 100,maxHp = 100,  damage = 10, alive = True, items = [], golds = 0,exp=0, level=0,up_level=50):
        super().__init__(name, hp= 70,maxHp = 70,  damage = 20, alive = True, items = [], golds = 0,exp=0, level=0,up_level=50)
    def __str__(self):
        f = f'Life of {self.name}: {self.hp}💗 Damage: {self.damage}🛡️'
        return f
def Combat():
    Hero.set_combat(True)
    while True: 
        horario()
        print('=================================================')
        print("Enemy:", mob)
        print('=================================================')
        print("You:", Hero)
        print('=================================================')
        print("What your next action front MOB!!")
        print("[1] Basic Attack  🗡️")
        print("[2] Special Attack ⚔️")
        print("[3] Open Bag 🎒")
        print("[4] Run 🚪")
        print('=================================================')
        if Hero.get_hp() > 0 and mob.get_hp() > 0:
            option_attack = input("Your option: ")
            print('\n')
            if option_attack == '1':
                if (type(Hero).__name__) == 'Archer':
                    if Hero.arrows > 0:
                        Hero.use_arrow()
                        Hero.Attack1_E(mob)
                        print('\n')
                        mob.Attack1_E(Hero)
                    else:
                        print("RUN RUN YOU NO HAVE ARROWS")
                        print('\n')
                else:
                    Hero.Attack1_E(mob)
                    print('\n')
                    mob.Attack1_E(Hero)
            elif option_attack == '2':
                if (type(Hero).__name__) != 'Archer':
                    Hero.Attack1_E(mob)
                    print('\n')
                    mob.Attack1_E(Hero)
                elif (type(Hero).__name__) == 'Archer':
                    if Hero.arrows > 0:
                        Hero.use_arrow()
                        Hero.use_arrow()
                        Hero.Special_Attack(mob)
                        print('\n')
                        mob.Attack1_E(Hero)
                    else:
                        print("RUN RUN YOU NO HAVE ARROWS")
            elif option_attack == '3':
                Hero.use_item()
            elif option_attack == '4':
                print('\n')
                probability = randint(0,10)
                if probability >= 0 and probability <=5:
                    if Hero.energy >=5:
                        Hero.energy -= 5
                        Hero.set_energy()
                        print("You run sucess and used 5 energy")
                        Hero.set_combat(False)
                        break
                    else:
                        print("You no have energy.")
                elif probability >= 6 and probability <=10:
                    if Hero.energy >= 10:
                        Hero.energy -= 10
                        Hero.set_energy()
                        mob.Attack1_E(Hero)
                        print("You failed run and used 10 energy")
                        print('=================================================')
                    else:
                        print("You no have energy to run")
                print('\n')
            else:
                print('\n')
                print ("WHAT THE FUCK THIS ACTION??????")
                print('\n')
        elif mob.get_hp() <= 0:
            print(f"{mob.get_name()} is dead")
            Hero.Kills()
            mob.drop_golds()
            mob.drop_exp()
            Hero.set_combat(False)
            mob.revive()
            break 
        elif Hero.get_hp()<= 0:
            print("\n")
            print("You is dead..💀")
            break 

def Spawn():
    print("\n\n")
    print('=================================================')
    print(f"👾 SPAWN {mob.get_name()} IN YOUR FRONT!!!!\n")
    Combat()

def Move():
    probability = randint(0,30)
    if probability >= 0 and probability <=11:
        Spawn()
    elif probability >= 11 and probability <=17:
        Hero.pickItem(Axe)
    else:
        print("You moved.")
def randomMob():
    probability = randint(0,12)
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
    elif probability >= 11 and probability <=12:
        mob = Evil_Zombie('Globin', 50,50,5)
        return mob
def randomWeapon():
    probability = randint(1,13)
    if probability >= 1 and probability <= 2:
        Axe = Item('SmallAxe', 'weapon','meele', 10, 0,0)
        return Axe
    elif probability >=3  and probability <= 5:
        Axe = Item('Stick', 'weapon','meele', 5, 0,0)
        return Axe
    elif probability >= 6 and probability <= 7:
        Axe = Item('Sword', 'weapon','meele', 15, 0,0)
        return Axe
    elif probability >= 8 and probability <= 8:
        Axe = Item('BigSword', 'weapon','meele', 20, 0,0)
        return Axe
    elif probability >= 9 and probability <= 9:
        Axe = Item('Chest', 'chest','all', 0 , 20,0)
        return Axe
    elif probability >= 12 and probability <= 13:
        Axe = Item('Potion', 'utility','all', 0, 0, 100)
        return Axe
def Choice_Hero():
    name = input("What you name?: ")
    while True:
        print("Choice your hero.")
        #class Warrior
        print("[1] Warrior ⚔️")
        #class Lancer
        print("[2] Lancer 🔱")
        #class Archer
        print("[3] Archer 🏹")
        option = input("Your option: ")
        if option == '1':
            Hero = Warrior(name)
            return Hero
            break
            print(f"You picked: {Hero}")
        elif option == '2':
            Hero = Lancer(name)
            return Hero
            break
            print(f"You picked: {Hero}")
        elif option == '3':
            Hero = Archer(name)
            return Hero
            break
            print(f"You picked: {Hero}")
        else:
            print("What this option? ")
        
def horario():
    global day,mounth,year,hours,minute
    minute += 17
    if minute >= 60:
        hours +=1
        minute = 0
    elif hours >=24:
        hours = 0
        day += 1
    elif day >= 30:
        day = 0
        mounth += 1
    elif Hero.combat == True:
        hours += 1

def blacksmith(self):
    while True:
        print('\n\n=================================================')
        print("WELCOME TO BLACKSMITH!!!")
        print('=================================================')
        print(f"You gold's: {self.golds} 🟡")
        print("What do you want?")
        print("[1] - Arrows(5un) - [15] Golds 🟡")
        print("[2] - Potion(1un) - [10] Golds 🟡")
        print("[3] - Chest_Iron(1un)- [25] Golds 🟡")
        print("[4] - Balesta(1un)- [40] Golds 🟡")
        print("[5] - Exit")
        option = input('Your option: ')
        if option == '1':
            if self.golds >= 15:
                self.get_arrow(5)
                self.golds -= 15
            else:
                print("You no have gold's!!")
        elif option == '2':
            if self.golds >= 10:
                self.items.append(Potion)
                self.golds -= 10
            else:
                print("You no have gold's!!")
        elif option == '3':
            if self.golds >= 20:
                self.items.append(Chest_Iron)
                self.golds -= 20
            else:
                print("You no have gold's!!")
        elif option == '4':
            if self.golds >= 40:
                self.items.append(Balestra)
                self.golds -= 40
            else:
                print("You no have gold's!!")
        elif option == '5':
            break

if __name__ == "__main__":
    day = 0
    mounth = 1
    year = 2023
    hours = 0
    minute = 1
    print("\n\n\n")
    print('=================================================')
    print("Game Version 1.0!!")
    print("Created by Reginaldo and Andre")
    print("Features:")
    print("- System of LevelUp")
    print("- - Exp")
    print("- - Level")
    print("- System what you name")
    print("- Increment System of combat")
    print("- - Open Bag in combat")
    print("- - Special Attack in combat")
    print("- News itens in Blacksmith")
    print('=================================================')
    print('Welcome to world!')
    print('=================================================')
    Hero = Choice_Hero()
    Potion = Item('Potion', 'utility','all', 0, 0, 50)
    Chest_Iron = Item('Chest_Iron', 'chest','all', 0, 20, 0)
    Balesta  = Item('Balesta', 'weapon','all', 25, 0, 0)
    Hero.items.append(Potion)

    while True:
        if Hero.get_hp() > 0:  
            Axe = randomWeapon()
            mob = randomMob()
            print('=================================================')
            print(Hero)
            print("You kills: ", Hero.kills, "💀")
            print("You gold's: ", Hero.golds, "🟡")
            print("You level: ", Hero.level, "⭐")
            print(f'Date now: {day}/{mounth}/{year} {hours} hours and {minute} minutes')
            print('=================================================')
            print("What your next action")
            print("[1] Move 🦶")
            print("[2] Open Bag 🎒")
            print("[3] Sleep 😴")
            print("[4] Blacksmith 🔨")
            print("[5] Exit 🚪")
            print('=================================================')
            option = input("Your option: ")
            if option == '1':
                horario()
                Move()
            elif option == '2':
                Hero.openBag()
            elif option == '3':
                Hero.sleep()
            elif option == '4':
                blacksmith(Hero)
            elif option == '5':
                break
            else:
                print ("WHAT THE FUCK THIS ACTION??????")
        elif Hero.get_hp()<= 0:
            os.system('cls')
            print("GAME OVER!!")
            break 
        # except:
        #     print("FAIL FAIL FAIL FAIL!!!")


