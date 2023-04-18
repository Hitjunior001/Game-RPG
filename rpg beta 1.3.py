from random import randint
import os
import datetime


class Game():
    def __init__(self, place):
        self.place = place
class bc:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
# --------------------CLASS DOS MOB--------------------
class Item():
    def __init__(self, name, typer,race, damage = 0, armor = 0, life = 0, energy = 0, equipped = False):
        self.name = name
        self.typer = typer
        self.energy = energy
        self.race = race
        self.damage = damage
        self.armor = armor
        self.life = life
        self.equipped = equipped
    def __str__(self):
        if self.equipped == True:
            f = f'{self.name} - {bc.BOLD}Equipped{bc.ENDC}\nDamage: +{self.damage} 💪\nArmor: +{self.armor} 🛡️'
            return f
        elif self.typer == 'utility':
            f = f'{self.name}\nLife: +{self.life} 💗\nEnergy: +{self.energy} ⚡'
            return f
        else:
            if self.equipped == False:
                if len(Hero.equip_weapon) == 1:
                    damage = Hero.equip_weapon[0].damage
                    if self.typer == 'weapon':
                        if damage > self.damage:
                            f = f'{self.name}\nDamage: -{bc.RED}{bc.BOLD}{damage - self.damage}{bc.ENDC} 💪\nArmor: +{self.armor} 🛡️'
                            return f
                        else:
                            f = f'{self.name}\nDamage: +{bc.GREEN}{bc.BOLD}{self.damage - damage}{bc.ENDC} 💪\nArmor: +{self.armor} 🛡️'
                            return f
                if len(Hero.equip_chest) == 1:
                    armor = Hero.equip_chest[0].damage
                    if self.typer == 'chest':
                        if armor > self.armor:
                            f = f'{self.name}\nDamage: +{self.damage} 💪\nArmor: -{bc.RED}{bc.BOLD}{armor - self.armor}{bc.ENDC} 🛡️'
                            return f
                        else:
                            f = f'{self.name}\nDamage: +{self.damage}💪\nArmor: +{bc.GREEN}{bc.BOLD}{self.armor - armor}{bc.ENDC} 🛡️'
                            return f
                else:
                    f = f'{self.name}\nDamage: +{self.damage} 💪\nArmor: +{self.armor} 🛡️'
                    return f


class Bag(Item):
    def __init__(self, items = []):
        self.items = items
    def openBag(self):
        if len(self.items) > 0:
            Hero.equip_use()
        else:
            print("\nYOU BAG: 🎒\n")
            print("------------------")
            print("Is empty.")
            print("------------------")
    def pickItem(self, Item):
            print('=================================================')
            print(F'You found {Item.name} what do you want to do?')
            print(Item)
            while True:
                print("[1] Pick")
                print("[2] Ignore")
                print('=================================================')
                choice = input("Option: ")
                if choice == '1':
                    if len(self.items) <= 9:
                        print("\n")
                        print(f'{Item.name} guarded.')
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
    def buyItem(self, Item, gold):
            print('=================================================')
            print(F'Do you want to buy the {Item.name}?')
            print(Item)
            while True:
                print("[1] Buy")
                print("[2] Exit")
                print('=================================================')
                choice = input("Option: ")
                if choice == '1':
                    if len(self.items) <= 9:
                        print("\n")
                        self.golds -= gold
                        print(f'{Item.name} Bought.')
                        self.items.append(Item)
                        break
                    else:
                        print("Bag is full!!")

                elif choice == '2':
                    print("You exit.")
                    break
                else:
                    print("\nWHAT THE FUCK IS OPTION!!??\n")
class Mob(object):
    def __init__(self, name, hp = 100, maxHp = 100, energy = 130, maxEnergy = 130, alive = True, damage = 10, items = [], kills = 0, equip_chest = [], equip_weapon = [], weapon = 0, armor = 0, combat = False, golds = 0,exp=0, level=0,up_level=50,special_attack = False):
        self.hp = hp
        self.special_attack = special_attack
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

    def Move(self):
        hour()
        probability = randint(0,30)
        self.energy_loss(randint(1,4))
        if probability >= 0 and probability <=11:
            Spawn()
        elif probability >= 11 and probability <=17:
            self.pickItem(Axe)
        else:
            print("You moved.")
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
            print(f"Missed attack in {target.name}")
            print('=================================================')
        elif(attack > 10 and attack < 18):
            if target == mob:
                print('=================================================')
                print("Attack")
                print(f"🗡️ Caused {self.damage} damage in {target.name}")
                print('=================================================')
                target.take_damage(self.damage)
            else:
                print('=================================================')
                print("Attack")
                print(f"🗡️ Caused {self.damage} damage in {target.name}")
                print('=================================================')
                target.take_damage(self.damage)
        else:
            if target == mob:
                print('=================================================')
                print("ATTACK CRIT!!!")
                print(f"🗡️ Caused {self.damage*2} damage in {target.name}")
                print('=================================================')
                target.take_damage(self.damage*2)
            else:
                print('=================================================')
                print("ATTACK CRIT!!!")
                print(f"🗡️ Caused {self.damage*2} damage in {target.name}")
                print('=================================================')
                target.take_damage(self.damage*2)
    def win_exps(self,exp):
        self.exp += exp
        self.level_up()
        return self.exp
    def set_combat(self, combat):
       self.combat = combat
       return self.combat
    def energy_loss(self, energy):
        self.energy -= energy
        return self.energy
        self.verify_energy()
    def verify_energy(self):
        if self.energy > self.maxEnergy:  
            self.energy = self.maxEnergy
            return self.energy
        elif self.energy <= 0:
            self.energy = 0
            return self.energy
    def sleep(self):
        global day,mounth,year,hours,minute
        if hours >= 0 and hours <= 6 or hours >=18:
            if self.energy < self.maxEnergy:
                random = randint(5,10)
                print(f"You sleep 6 hours and 17 minutes")
                print(f"recupered {random+30} energy")
                self.energy += 30
                self.energy += random
                self.verify_energy()
                hours += 6
                hour()
            else:
                print("You Energy is full, stranger")
        else:
            print("YOU DON'T SLEEP!! IT'S DAY!")
            
    def get_hp(self):
        return self.hp
    def get_golds(self):
        return self.golds
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
    def use_potion(self, potion_life, potion_energy):
        self.hp += potion_life
        self.energy += potion_energy
        if self.hp > self.maxHp:
            self.hp = self.maxHp
        elif self.energy > self.maxEnergy:
            self.energy = self.maxEnergy
    def delete_use(self, option, item):
        while True:
            print("You choice: ")
            print('------------')
            print(item)
            print('------------')
            print('What do you want to do with it?')
            print("[1] Use Item")
            print("[2] Delete Item")
            print("[3] Exit\n")
            option2 = input("You option: ")
            if option2 == '1':
                return True
            elif option2 == '2':
                if item.equipped == True:
                    print("It is not possible to delete this item because you are equipped with it.")
                else:
                    self.items.pop(option)
                    print(f"You deleted {item.name}")
                    return False
            elif option2 == '3':
                return False
            else:
                print("NOP!!")
    def equip_use(self):
        if len(self.items) == 0:
            print("You no have Items!!!!")
        while True:
            self.check_equip()
            print(Hero)
            print("\n------------------")
            for count, item in enumerate(self.items):
                print(f'[{count}] - {item}         ')   
                print("------------------")
            print("[11] to Exit\n")
            print("\nChoose an item")
            option = int(input("You option: "))
            print('\n\n')
            if option == 11:
                break
            item = self.items[option]
            if item.typer == 'chest':
                if self.delete_use(option, item) == True:
                    if len(self.equip_chest) == 0:
                        self.equip_chest.append(item)
                        print('\n\n\n==============================================')
                        print(f"Have you equipped yourself with a {item.name}")
                        print('==============================================\n')
                        item.equipped = True
                        if self.combat == True:
                            break  
                    else:
                        self.equip_chest[0].equipped = False
                        self.equip_chest.pop()
                        self.equip_chest.append(item)
                        print('\n\n\n==============================================')
                        print(f"Have you equipped yourself with a {item.name}")
                        print('==============================================\n')
                        item.equipped = True
                        if self.combat == True:
                            break  
                else:
                    pass
            elif item.typer == 'weapon':
                if self.delete_use(option, item) == True:
                    if len(self.equip_weapon) == 0:
                        self.equip_weapon.append(item)
                        print('\n\n\n==============================================')
                        print(f"Have you equipped yourself with a {item.name}")
                        print('==============================================\n')
                        item.equipped = True
                        if self.combat == True:
                            break  
                    else:
                        self.equip_weapon[0].equipped = False
                        self.equip_weapon.pop()
                        self.equip_weapon.append(item)
                        print('\n\n\n==============================================')
                        print(f"Have you equipped yourself with a {item.name}")
                        print('==============================================\n')
                        item.equipped = True
                        if self.combat == True:
                            break  
                else:
                    pass
            elif item.typer == 'utility':
                if self.delete_use(option, item) == True:
                    potion_life = item.life
                    potion_energy = item.energy
                    if self.energy < self.maxEnergy and self.hp < self.maxHp:
                        self.use_potion(potion_life,potion_energy)
                        print(f"You cured {potion_life} of life and {potion_energy} of energy ")
                        self.items.pop(option)
                        if self.combat == True:
                            break  
                    elif self.energy >= self.maxEnergy and self.hp < self.maxHp:
                        print("You energy is full!!")
                        self.use_potion(potion_life,0)
                        self.items.pop(option)
                        print(f"You cured {potion_life} of life")
                        if self.combat == True:
                            break  
                    elif self.hp >= self.maxHp and self.energy < self.maxEnergy:
                        print("You life is full!!")
                        self.use_potion(0,potion_energy)
                        self.items.pop(option)
                        print(f"You cured {potion_energy} of energy ")
                        if self.combat == True:
                            break  
                    else:
                        print("You life and energy is full!!")
                else:
                    pass
            else:
                print("This option not exist")    

    def check_equip(self):              
        if len(self.equip_chest) == 0 and len(self.equip_weapon) == 0:
            pass
        elif len(self.equip_chest) == 1 and len(self.equip_weapon) == 0:
            self.armor = self.equip_chest[0].armor
            self.equip_chest[0].equipped = True
            self.set_armor_hp()

        elif len(self.equip_chest) == 1 and len(self.equip_weapon) == 1:
            self.weapon = self.equip_weapon[0].damage
            self.armor = self.equip_chest[0].armor
            self.equip_chest[0].equipped = True
            self.equip_weapon[0].equipped = True
            self.set_weapon_damage()
            self.set_armor_hp()
        elif len(self.equip_chest) == 0 and len(self.equip_weapon) == 1:
            self.weapon = self.equip_weapon[0].damage
            self.equip_weapon[0].equipped = True
            self.set_weapon_damage()

    def get_damage(self):
        return self.damage
    def take_damage(self, damage):
        self.hp -= damage
        return self.hp
    def Kills(self):
        self.kills += 1
    def __str__(self):
        f = f'--------\nLife of {self.name}: {self.hp}💗 Damage of {self.name}: {self.damage}🛡️'
        return f
class Warrior(Mob, Bag, Item):
    def __init__(self,name, hp = 100 ,maxHp = 100, energy = 130, maxEnergy = 130, alive = True, damage = 15, items = [],equip_chest = [], equip_weapon = [], weapon = 0, armor = 0, combat = False, golds = 0,exp=0, level=0,up_level=50):
        super().__init__(name, hp = 150,maxHp = 150, energy = 130, maxEnergy = 130,  alive = True, damage = 15, items = [], kills=0, equip_chest = [], equip_weapon = [], weapon = 0, armor = 0, golds = 0,exp=0, level=0,up_level=50, special_attack= False)
    def Special_Attack(self):
        if self.energy >= 100:
            self.special_attack = True
            self.energy_loss(100)
            print('=================================================')
            print("Special Attack!! You gained magic to fight and increased your damage!!!")
            print("Damage +100 💪")
            print('=================================================')
            self.damage += 100
            if mob.name == "OVERPOWER":
                self.damage += 1000
        else:
            print('=================================================')
            print("You don't have energy")
            print('=================================================')
            pass
    def Disable_Special_Attack(self):
        if self.special_attack == True:
            self.special_attack = False
            if mob.name == "OVERPOWER":
                self.damage -= 1100
            else:
                self.damage -= 100
    def __str__(self):
        f = f'Life of Warrior: {self.hp}/{self.maxHp}💗  Energy of Warrior: {self.energy}/{self.maxEnergy}⚡ Damage of Warrior: {self.damage}🛡️'
        return f
class Lancer(Mob, Bag, Item):
    def __init__(self,name, hp = 100 ,maxHp = 100, energy = 130, maxEnergy = 130, alive = True, damage = 15, items = [],equip_chest = [], equip_weapon = [], weapon = 0, armor = 0, combat = False, golds = 0,exp=0, level=0,up_level=50):
        super().__init__(name, hp = 110 ,maxHp = 110, energy = 120, maxEnergy = 120, alive = True, damage = 20, items = [],equip_chest = [], equip_weapon = [], weapon = 0, armor = 0, combat = False, golds = 0,exp=0, level=0,up_level=50,special_attack= False)
    def Special_Attack(self, target):
        if self.energy >= 90:
            self.special_attack = True
            self.energy_loss(90)
            self.damage += 50
            print('=================================================')
            print("Special Attack!! You impaling your enemy and gain additional fury damage!!!")
            print("Damage +50 💪")
            print(f"🗡️ Impaling on the enemy caused {self.damage+80} damage in {target.name}")
            print('=================================================')
            target.take_damage(self.damage+80)
        else:
            print('=================================================')
            print("You no have energy")
            print('=================================================')
            pass
    def Disable_Special_Attack(self):
        if self.special_attack == True:
            self.special_attack = False
            self.damage -= 50
    def __str__(self):
        f = f'Life of Lancer: {self.hp}/{self.maxHp}💗 Energy of Lancer: {self.energy}/{self.maxEnergy}⚡ Damage of Lancer: {self.damage}🛡️'
        return f
class Monk(Mob, Bag, Item):
    def __init__(self,name, hp = 100 ,maxHp = 100, energy = 130, maxEnergy = 130, alive = True, damage = 15, items = [],equip_chest = [], equip_weapon = [], weapon = 0, armor = 0, combat = False, golds = 0,exp=0, level=0,up_level=50):
        super().__init__(name, hp = 100 ,maxHp = 100, energy = 200, maxEnergy = 200, alive = True, damage = 20, items = [],equip_chest = [], equip_weapon = [], weapon = 0, armor = 0, combat = False, golds = 0,exp=0, level=0,up_level=50,special_attack = False)
    def Special_Attack(self):
        if self.energy >= 100:
            self.special_attack = True
            self.energy_loss(100)
            print('=================================================')
            print("Special Attack!! You have reached the minimum level of concentration!!!")
            print("Damage +30 💪")
            print("Life +50 💗")
            print('=================================================')
            self.hp += 50
            self.damage += 30
            self.maxHp +=50
        else:
            print('=================================================')
            print("You no have energy")
            print('=================================================')
            pass
    def Disable_Special_Attack(self):
        if self.special_attack == True:
            self.special_attack = False
            self.damage -= 30
            if self.hp < 50:
                self.hp -= 40
                self.maxHp -=40
            else:
                self.hp -= 50
                self.maxHp -=50
    def __str__(self):
        f = f'Life of Monk: {self.hp}/{self.maxHp}💗 Energy of Monk: {self.energy}/{self.maxEnergy}⚡ Damage of Monk: {self.damage}🛡️'
        return f
class Dragontooth():
    def __init__(self,name,hp = 30, maxHp = 30, alive = True, damage = 10):
        self.name = name
        self.hp = hp
        self.maxHp = maxHp
        self.alive = alive
        self.damage = damage
    def Attack(self,target):
        attack = randint(0,20)
        if (attack <=10 and attack > 0):
            print(f"Missed attack in {target.name}")
            print('=================================================')
        elif(attack > 10 and attack < 18):
            damage = self.damage
            print("Attack")
            print(f"🗡️ Caused {damage} damage in {target.name}")
            target.take_damage(damage)
            print('=================================================')
        else:
            damage = self.damage * 2
            print("ATTACK CRIT!!!")
            print(f"🗡️ Caused {damage} damage in {target.name}")
            target.take_damage(damage)
            print('=================================================')
    def take_damage(self,damage):
        self.hp -= damage
        return self.hp

    def __str__(self):
        f = f'Life of {self.name}: {self.hp}/{self.maxHp}💗 Damage of Subordinate Monk: {self.damage}🛡️'
        return f
class Archer(Mob, Bag, Item):
    def __init__(self,name, hp = 80 ,maxHp = 80, energy = 50,maxEnergy = 50,  alive = True, damage = 25, items = [],equip_chest = [], equip_weapon = [], weapon = 0, armor = 0, arrows = 30,combat = False, golds = 0,exp=0, level=0,up_level=50):
        self.arrows = arrows
        super().__init__(name, hp = 90,maxHp = 90, energy = 60,maxEnergy = 60,  alive = True, damage = 25, items = [],equip_chest = [], equip_weapon = [], weapon = 0, armor = 0,combat = False, golds = 0,exp=0, level=0,up_level=50)
    def use_arrow(self, arrow):
        if self.arrows > 0:
            self.arrows -= arrow
            return self.arrows
    def get_arrow(self, arrow):
        self.arrows += arrow
        return self.arrows
    def Special_Attack(self,target):
        if self.energy >= 35:
            self.energy_loss(35)
            print('=================================================')
            print("Special Attack!! Double Attack")
            print(f"🗡️ Caused {self.damage *1.2} damage in {target.name}")
            print(f"🗡️ And again you caused {self.damage *1.2} damage in {target.name}")
            print('=================================================')
            target.take_damage(self.damage *1.2)
            target.take_damage(self.damage *1.2)
        else:
            print('=================================================')
            print("You no have energy")
            print('=================================================')

    def __str__(self):
        f = f'Life of Archer: {self.hp}/{self.maxHp}💗 Energy of Archer: {self.energy}/{self.maxEnergy}⚡ Arrows of Archer: {self.arrows} 🏹  Damage of Archer: {self.damage}🛡️'
        return f
class Enemy():
    def __init__(self,name, hp = 100,maxHp = 100,  damage = 10, golds = 0,exp=0, level= 0,alive = True, items = []):
        self.name = name
        self.hp = hp 
        self.level = level
        self.maxHp = maxHp
        self.damage = damage
        self.alive = alive
        self.items = items
        self.golds = golds
        self.exp = exp


    def Still_Gold(self, target):
        random = randint(0,10)
        random_gold = randint(3,20)
        if random > 0 and random < 8:
            if target.golds > 0:
                target.golds -= random_gold
                print("Globin stole your money.")
                print("Globin: 'ihihihihihihi'")
                print("Globin: 'Lost smaller'")
                print(f"You lossed {random_gold}")
                if target.golds < 0:
                    target.golds = 0
            else:
                print("Globin tried to steal his gold but failed! you went into combat!!")
                Combat()
        else:
            Combat()

    def mob_level(self):
        if Hero.level == Hero.level:
            self.level = Hero.level 
            self.damage += self.level*5
            self.hp += self.level*5
    def status(self):
        if self.hp <= 0:
            self.alive = False
            return self.alive
        elif self.hp > 0:
            self.alive = True
            return self.alive
    def revive(self):
        self.hp = self.maxHp
        return self.hp
        self.status()

    def drop_exp(self):
        print(f'{self.name} dropped {self.exp} exps 💥')
        Hero.win_exps(self.exp)
    def drop_golds(self):
        print(f'{self.name} dropped {self.golds} golds 🟡')
        Hero.win_golds(self.golds)

    def take_damage(self,damage):
        self.hp -= damage
        return self.hp
    def Attack1_E(self,target):
        attack = randint(0,20)
        if (attack <=10 and attack > 0):
            print('=================================================')
            print(f"Missed attack in {target.name}")
            print('=================================================')
        elif (attack > 10 and attack < 18):
            print('=================================================')
            print("Attack")
            print(f"🗡️ Caused {self.damage} damage in {target.name}")
            print('=================================================')
            target.take_damage(self.damage)
        else:
            print('=================================================')
            print("ATTACK CRIT!!!")
            print(f"🗡️ Caused {self.damage*2} damage in {target.name}")
            print('=================================================')
            target.take_damage(self.damage*2)
    def __str__(self):
        f = f'Life of {self.name}: {self.hp}💗 Damage: {self.damage}🛡️'
        return f
def Combat():
    Hero.set_combat(True)
    while True: 
        if Hero.hp > 0 and mob.hp > 0:
            hour()
            print('=================================================')
            print("Enemy:", mob)
            print('=================================================')
            print("You:", Hero)
            print('=================================================')
            print("What your next action front MOB!!")
            print("[1] Attack  🗡️")
            print("[2] Special Attack ⚔️")
            print("[3] Open Bag 🎒")
            print("[4] Run 🚪")
            print('=================================================')
            option_attack = input("Your option: ")
            print('\n')
            if option_attack == '1':
                if (type(Hero).__name__) == 'Archer':
                    if Hero.arrows > 0:
                        Hero.use_arrow(1)
                        Hero.Attack1_E(mob)
                        print('\n')
                        if mob.hp > 0:
                            mob.Attack1_E(Hero)
                        else:
                            print('=================================================')
                            print("Mob is killed.")
                            print('=================================================\n\n')
                    else:
                        print("RUN RUN YOU NO HAVE ARROWS")
                        print('\n')
                else:
                    Hero.Attack1_E(mob)
                    print('\n')
                    if mob.hp > 0:
                        mob.Attack1_E(Hero)
                    else:
                        print("Mob is killed.")
            elif option_attack == '2':
                if (type(Hero).__name__) == 'Archer':
                    if Hero.arrows > 0:
                        Hero.use_arrow(2)
                        Hero.Special_Attack(mob)
                        print('\n')
                        if mob.hp > 0:
                            mob.Attack1_E(Hero)
                        else:
                            print("Mob is killed.")
                    else:
                        print("RUN RUN YOU NO HAVE ARROWS")
                elif (type(Hero).__name__) == 'Monk':
                    if Hero.special_attack == False:
                        Hero.Special_Attack()
                    else:
                        print("Special Attack in USE!!!!")
                elif (type(Hero).__name__) == 'Lancer':
                    if Hero.special_attack == False:
                        Hero.Special_Attack(mob)
                    else:
                        print("Special Attack in USE!!!!")
                elif (type(Hero).__name__) == 'Warrior':
                    if Hero.special_attack == False:
                        Hero.Special_Attack()
                    else:
                        print("Special Attack in USE!!!!")
            elif option_attack == '3':
                Hero.equip_use()
            elif option_attack == '4':
                print('\n')
                probability = randint(0,10)
                if probability >= 0 and probability <=5:
                    if Hero.energy >=5:
                        Hero.energy -= 5
                        Hero.verify_energy()
                        print("You run sucess and used 5 energy")
                        Hero.set_combat(False)
                        if (type(Hero).__name__) == 'Monk':
                            Hero.Disable_Special_Attack()
                        break
                    else:
                        print("You no have energy.")
                elif probability >= 6 and probability <=10:
                    if Hero.energy >= 10:
                        Hero.energy -= 10
                        Hero.verify_energy()
                        mob.Attack1_E(Hero)
                        print("You failed run and used 10 energy")
                        print('=================================================')
                    else:
                        print("You no have energy to run")
                print('\n')
        elif mob.hp <= 0:
            print(f"{mob.name} is dead")
            Hero.Kills()
            print('=================================================')
            mob.drop_golds()
            mob.drop_exp() 
            Hero.set_combat(False)
            mob.revive()
            if (type(Hero).__name__) == 'Monk' or (type(Hero).__name__) == 'Warrior' or (type(Hero).__name__) == 'Lancer':
                Hero.Disable_Special_Attack()
            break
        elif Hero.hp<= 0:
            print("\n")
            print("You is dead..💀")
            break 

def Spawn():
    if mob.name == 'Globin':
        print('=================================================')
        print("The curse, appeared a sneaky globin!\n")
        mob.Still_Gold(Hero)
    else:
        print("\n\n")
        print('=================================================')
        print(f"👾 SPAWN {mob.name} IN YOUR FRONT!!!!\n")
        Combat()

def randomMob():
    random_gold = randint(0,20)
    random_exp = randint(5,30)
    probability = randint(0,16)
    if probability >= 0 and probability <=1:
        mob = Enemy('Old Zombie,', 50,50, 7, random_gold, random_exp)
        mob.mob_level()
        return mob
    elif probability >= 2 and probability <=3:
        mob = Enemy('Zombie', 100,100,10, random_gold, random_exp)
        mob.mob_level()
        return mob
    elif probability >= 4 and probability <=5:
        mob = Enemy('Kid Zombie', 50,50, 25, random_gold, random_exp)
        mob.mob_level()
        return mob
    elif probability >= 6 and probability <=7:
        mob = Enemy('Wolfmen',150,150,20, random_gold, random_exp)
        mob.mob_level()
        return mob  
    elif probability >= 8 and probability <=10:
        mob = Enemy('Evil elfo',70,70,30, random_gold, random_exp)
        mob.mob_level()
        return mob
    elif probability >= 11 and probability <=11:
        mob = Enemy('OVERPOWER', 300,300,50, random_gold, random_exp)
        mob.mob_level()
        return mob
    elif probability >= 12 and probability <=12:
        mob = Enemy('Skeletion Warrior', 150,150,30, random_gold, random_exp)
        mob.mob_level()
        return mob
    elif probability >= 13 and probability <=16:
        mob = Enemy('Globin', 50,50,5, random_gold, random_exp)
        mob.mob_level()
        return mob
def randomWeapon():
    probability = randint(1,17)
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
    elif probability >= 10 and probability <= 13:
        Axe = Item('Potion Life', 'utility','all', 0, 0, 100)
        return Axe
    elif probability >= 14 and probability <= 15:
        Axe = Item('Potion Energy', 'utility','all', 0, 0, 0, 100)
        return Axe
    elif probability >= 16 and probability <= 16:
        Axe = Item('Potion Full', 'utility','all', 0, 0, 0, 100)
        return Axe
    elif probability >= 17 and probability <= 17:
        Axe = Item('Spear', 'weapon','meele', 30, 0, 0, 0)
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
        #class Monk
        print("[4] Monk 🥋")
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
        elif option == '4':
            Hero = Monk(name)
            return Hero
            break
            print(f"You picked: {Hero}")
        else:
            print("What this option? ")
def hour():
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

def Blacksmith(self):
    while True:
        print('\n\n=================================================')
        print("WELCOME TO BLACKSMITH!!!")
        print('=================================================')
        print(f"You gold's: {self.golds} 🟡")
        print("What do you want?")
        print("[1] - Arrows(5un) - [15] Golds 🟡")
        print("[2] - Potion Life(1un) - [10] Golds 🟡")
        print("[3] - Chest Iron(1un)- [25] Golds 🟡")
        print("[4] - Balesta(1un)- [40] Golds 🟡")
        print("[5] - Potion Energy(1un)- [10] Golds 🟡")
        print("[6] - Potion Full(1un)- [20] Golds 🟡")
        print("[7] - Exit")
        option = input('Your option: ')
        if option == '1':
            if self.golds >= 15:
                self.get_arrow(5)
                self.golds -= 15
            else:
                print("You no have gold's!!")
        elif option == '2':
            if self.golds >= 10:
                self.buyItem(Potion, 10)
            else:
                print("You no have gold's!!")
        elif option == '3':
            if self.golds >= 20:
                self.buyItem(Chest_Iron, 20)
            else:
                print("You no have gold's!!")
        elif option == '4':
            if self.golds >= 40:
                self.buyItem(Balestra, 40)
            else:
                print("You no have gold's!!")
        elif option == '5':
            if self.golds >= 10:
                self.buyItem(Potion1, 10)
            else:
                print("You no have gold's!!")
        elif option == '6':
            if self.golds >= 20:
                self.buyItem(Potion2, 20)
            else:
                print("You no have gold's!!")
        elif option == '7':
            break
        else:
            print("WHAT THE FUCK THIS OPTION??")

if __name__ == "__main__":
    day = 1
    mounth = 1
    year = 2023
    hours = 0
    minute = 1
    print("\n\n\n")
    print('=================================================')
    print("Game Version 1.3!!")
    print("Created by Reginaldo and Andre")
    print("Features:")
    print("- News Mobs and Itens")
    print("- - Globin")
    print("- - - Globin havs a new function")
    print("- - - - He can steal your gold or go into combat")
    print("- Information if it is equipped with an item or not")
    print("- Modification in the use of the backpack, making it easier to use")
    print("- Balancing mobs and items")
    print("- Mobs gaining an increase in strength and health according to their level")
    print("- You cannot delete the item if you have it equipped.")
    print("- Improved the function of buying with Blacksmith.")
    print("- Increased instructions to make game more intuitive.")
    print("- Attributes of items when equipping shows whether you'll get a reduction or addition..")
    print("- Adding information when finding items or purchasing items...")
    print('=================================================')
    print('Welcome to world!')
    print('=================================================')
    Hero = Choice_Hero()
    Potion = Item('Potion Life', 'utility','all', 0, 0, 50)
    Potion1 = Item('Potion Energy', 'utility','all', 0, 0, 0,50)
    Potion2 = Item('Potion Full', 'utility','all', 0, 0,50, 50)
    Chest_Iron = Item('Chest Iron', 'chest','all', 0, 20, 0)
    Balestra  = Item('Balesta', 'weapon','ranged', 25, 0, 0)
    Katana = Item('Katana', 'weapon','meele', 35, 0, 0)
    Hero.items.append(Potion)
    Hero.items.append(Potion1)
    print("You started the game with a Potion of Life 🧉 and Energy")

    while True:
        try: 
            if Hero.hp > 0:  
                Axe = randomWeapon()
                mob = randomMob()
                print('=================================================')
                print(Hero)
                print("You kills: ", Hero.kills, "💀")
                print("You gold's: ", Hero.golds, "🟡")
                print("You level: ", Hero.level, "⭐")
                print(f'Date now: {day}/{mounth}/{year} {hours} hours and {minute} minutes')

                if hours >= 6 and hours < 18:
                    print(f"It's day: ☀️")
                else:
                    print(f"It's night: 🌚")
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
                    Hero.Move()
                elif option == '2':
                    Hero.openBag()
                elif option == '3':
                    Hero.sleep()
                elif option == '4':
                    Blacksmith(Hero)
                elif option == '5':
                    break
                else:
                    print ("WHAT THE FUCK THIS ACTION??????")
            elif Hero.hp<= 0:
                os.system('cls')
                print("GAME OVER!!")
                break 
        except:
            print("FAIL FAIL FAIL FAIL!!!")