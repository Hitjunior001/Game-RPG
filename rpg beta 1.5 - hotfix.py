from random import randint
import os
import datetime

# CODIGO FEITO POR REGINALDO E ANDRÉ
# SEM USO DE BIBLIOTECAS NÃO PADRÃO DO PYTHON
# TODO COMENTADO

#CLASS Map, MOSTRAR ONDE VOCÊ TÁ NO MOMENTO, DIGAMOS "MAPA"
class Map():
    def __init__(self, place):
        self.place = place
    def location(self, place):
        if place != self.place:
            self.place = place
            return self.place
        else:
            pass   
#CLASS COLORES, PRA COLOCAR CORES EM CERTOS TEXTOS
#EXP PRINT(f'{bc.BLUE}Welcome{bc.ENDC})
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
# CLASS DO ITEM
class Item():
    def __init__(self, name, typer,style, damage = 0, armor = 0, life = 0, energy = 0, gold = 0, equipped = False):
        self.name = name
        self.typer = typer
        self.energy = energy
        self.style = style
        self.damage = damage
        self.armor = armor
        self.life = life
        self.gold = gold
        self.equipped = equipped
    #DEFINIÇÃO DA STRING DE ACORDO COM OS ITEM
    def __str__(self):
        if self.equipped == True:
            f = f'{self.name} - {bc.BOLD}Equipped\nDamage: +{self.damage} 💪\nArmor: +{self.armor} 🛡️'
            return f
        elif self.typer == 'potion':
            f = f'{self.name}\nLife: +{self.life} 💗\nEnergy: +{self.energy} ⚡'
            return f
        elif self.typer == 'utility':
            f = f'{self.name}\nGold: +{self.gold}🟡'
            return f
        elif self.typer == 'test':
            f = f'{self.name}\nThis seems to be useful'
            return f
        else:
            if self.equipped == False:
                if len(Hero.equip_weapon) == 1:
                    damage = Hero.equip_weapon[0].damage
                    if self.typer == 'weapon':
                        if damage > self.damage:
                            f = f'{self.name}\nDamage: -{bc.RED}{bc.BOLD}{damage - self.damage}{bc.ENDC}{bc.BOLD} 💪\nArmor: +{self.armor} 🛡️\nTyper: {self.typer}'
                            return f
                        else:
                            f = f'{self.name}\nDamage: +{bc.GREEN}{bc.BOLD}{self.damage - damage}{bc.ENDC}{bc.BOLD} 💪\nArmor: +{self.armor} 🛡️\nTyper: {self.typer}'
                            return f
                if len(Hero.equip_chest) == 1:
                    armor = Hero.equip_chest[0].damage
                    if self.typer == 'chest':
                        if armor > self.armor:
                            f = f'{self.name}\nDamage: +{self.damage} 💪\nArmor: -{bc.RED}{bc.BOLD}{armor - self.armor}{bc.ENDC}{bc.BOLD} 🛡️\nTyper: {self.typer}'
                            return f
                        else:
                            f = f'{self.name}\nDamage: +{self.damage}💪\nArmor: +{bc.GREEN}{bc.BOLD}{self.armor - armor}{bc.ENDC}{bc.BOLD} 🛡️\nTyper: {self.typer}'
                            return f
                else:
                    f = f'{self.name}\nDamage: +{self.damage} 💪\nArmor: +{self.armor} 🛡️'
                    return f
#CLASS DA MOCHILA
class Bag(Item):
    def __init__(self, items = []):
        self.items = items
    #FUNÇÃO DE ABRIR MOCHILA SE HOUVER ITENS
    def openBag(self):
        if len(self.items) > 0:
            #COMO SÓ O HEROI USA MOCHILA, BOTEI DE FORMA DIRETA.
            Hero.equip_use()
        else:
            print("\nYOU BAG: 🎒\n")
            print("------------------")
            print("Is empty.")
            print("------------------")
    #FUNÇÃO PRA PEGAR O ITEM SEJA NO DROP, QUANDO O MOB DROPAR ALGO
    def pickItem(self, Item):
            print('=================================================')
            print(F'You found {Item.name} what do you want to do?')
            print(Item)
            while True:
                if Item.typer in ['weapon','chest']:
                    print("[1] Pick")
                    print("[2] Pick and Equip")
                    print("[3] Ignore")
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
                        #USA O MESMO SISTEMA DE EQUIP_USE PORÉM DE UMA MANEIRA SIMPLIFICADA APENAS PRA EQUIPAR DE UMA VEZ E FAZER AS VERIFICAÇÕES
                        #PRA SABER QUAL ITEM SERÁ USADO, É FEITO UMA VERFICAÇÃO DO TIPO DE ITEM.
                        print('\n\n')
                        if Item.typer == 'chest':
                            if len(self.equip_chest) == 0:
                                self.items.append(Item)
                                self.equip_chest.append(Item)
                                print('\n\n\n==============================================')
                                print(f"Have you equipped yourself with a {Item.name}")
                                print('==============================================\n')
                                self.check_equip()
                                break
                            else:
                                self.equip_chest[0].equipped = False
                                self.equip_chest.pop()
                                self.items.append(Item)
                                self.equip_chest.append(Item)
                                print('\n\n\n==============================================')
                                print(f"Have you equipped yourself with a {Item.name}")
                                print('==============================================\n')
                                self.check_equip()
                                break
                        if Item.typer == 'weapon':
                            if self.style == Item.style or Item.style == 'all':
                                if len(self.equip_chest) == 0:
                                    self.items.append(Item)
                                    self.equip_weapon.append(Item)
                                    print('\n\n\n==============================================')
                                    print(f"Have you equipped yourself with a {Item.name}")
                                    print('==============================================\n')
                                    self.check_equip()
                                    break
                                else:
                                    self.equip_weapon[0].equipped = False
                                    self.equip_weapon.pop()
                                    self.items.append(Item)
                                    self.equip_weapon.append(Item)
                                    print('\n\n\n==============================================')
                                    print(f"Have you equipped yourself with a {Item.name}")
                                    print('==============================================\n')
                                    self.check_equip()
                                    break
                            else:
                                print('==============================================\n')
                                print('This Item is not for you!!')
                                print('==============================================\n')
                    #SE ESCOLHIDO A OPÇÃO 3, IGNORA O ITEM E SEGUE
                    elif choice == '3':
                        print("You ignored.")
                        break
                    else:
                        print("\nWHAT THE FUCK IS OPTION!!??\n")
                else:
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
    #FUNÇÃO DE COMPRAR ITENS 
    def buyItem(self, Item):
            print('=================================================')
            print(F'Do you want to buy the {Item.name}?')
            print("-------------")
            print(Item)
            print(f'Cost: {Item.gold}🟡')
            print("-------------\n")
            
            while True:
                print("[1] Buy")
                print("[2] Exit")
                print('=================================================')
                choice = input("Option: ")
                if choice == '1':
                    if len(self.items) <= 9:
                        if self.golds >= Item.gold:
                            print("\n")
                            self.golds -= Item.gold
                            print(f'{Item.name} Bought.')
                            self.items.append(Item)
                            break
                        else:
                            print("You no have gold's!!")
                    else:
                        print("Bag is full!!")

                elif choice == '2':
                    print("You exit.")
                    break
                else:
                    print("\nWHAT THE FUCK IS OPTION!!??\n")
#CLASS DE MOB, A CLASS QUE SERÁ O PAI DE TODOS HEROIS.
class Mob(object):
    def __init__(self, name, hp = 100, maxHp = 100, energy = 130, maxEnergy = 130, alive = True, damage = 10, items = [], kills = 0, equip_chest = [], equip_weapon = [], weapon = 0, armor = 0, combat = False, golds = 0,exp=0, level=0,up_level=30,special_attack = False, style = ''):
        self.hp = hp
        self.special_attack = special_attack
        self.exp = exp
        self.up_level = up_level
        self.level = level
        self.maxHp = maxHp
        self.damage_fix = damage
        self.damage = self.damage_fix
        self.armor_fix = armor
        self.armor = self.armor_fix
        self.kills = kills
        self.items = items
        self.alive = True
        self.combat = False
        self.golds = golds
        self.name = name
        self.equip_chest = []
        self.equip_weapon  = []
        self.weapon = weapon
        self.energy = energy
        self.maxEnergy = maxEnergy
        self.style = style
        self.scorpion_kills = 0
        self.scorpion_king_kills = 0
    #FUNÇÃO BÁSICA PARA CHECAR SE HEROI POSSUI TAL ITEM.
    #DEVIDO QUE O DROP DE ITENS PELO MAPA É FEITO COM UMA VARIÁVEL ÚNICA, PARA CHECAR O ITEM SERÁ USADO O NOME DADO EM VEZ DO NOME DO OBJETO.
    def check_item(self, item):
        for i in self.items:
            if i.name == item:
                return True
        return False
    #ESSA FUNÇÃO SERVE PRA VERIFICAR O EQUIPAMENTO QUE O HEROI TÁ USANDO, QUE É USADA NO Combat()
    def check_equip_style(self):
        All = 'all'
        Sword = 'sword'
        Lancer = 'lancer'
        Archery = 'archery'
        Meele = 'meele'
        for i in self.items:
            if i.equipped == True and i.typer == 'weapon':  
                if i.style == 'all':
                    return All
                else:
                    if (type(Hero).__name__) == 'Archer':
                        if i.style == 'archery':
                            return Archery
                    elif (type(Hero).__name__) == 'Warrior':
                        if i.style == 'sword':
                            return Sword
                    elif (type(Hero).__name__) == 'Lancer':
                        if i.style == 'lancer':
                            return Lancer
                    elif (type(Hero).__name__) == 'Monk':
                        if i.style == 'meele':
                            return Meele
                
        else:
            print("You no have weapon equipped")
        return False

    #FUNÇÃO BÁSICA DO JOGO QUE SERÁ SE MOVER.
    def Move(self):
        hour()
        global scorpion_king_kills, scorpion_kills
        probability = randint(0,30)
        self.energy_loss(randint(1,4))
        if scorpion_king_kills >= 1:
            print("Congratulations, you killed the scorpion king, you are free")
            print("You left of Donjon")
            Map.location('Ground')
        elif scorpion_kills >= 10:
            print("yeah... you didn't prove your worth, but for your effort you're released")
            print("You left of Donjon")
            scorpion_kills = 0
            Map.location('Ground')
        elif probability >= 0 and probability <=11:
            Spawn()
        elif probability >= 11 and probability <=17:
            self.pickItem(itemAleatory)
        elif probability >= 18 and probability <=24:
            if Map.place != 'Dungeon' and Map.place != 'Donjon':
                Dungeon()
            else:
                if probability >=18 and probability <=24:
                    if Map.place == 'Dungeon':
                        print("You found a door, do you want to open it?.")
                        print('[1] - Yes')
                        print('[2] - No')
                        option = input("You choice: ")
                        if option == '1':
                            Exit_Dungeon()
                        elif option == '2':
                            print("...You ignored")
                        else:
                            print("This option not exits.")
                    else:
                        print(f"You moved in {Map.place}.")
                else:
                    print(f"You moved in {Map.place}.")
        elif probability >= 25 and probability <=28:
            if Map.place != 'Dungeon' and Map.place != 'Donjon':
                Donjon()
            else:
                if probability >= 25 and probability <=28:
                    Exit_Donjon()
        else:
            print("You moved.")
    #FUNÇÃO DE LEVEL_UP QUE SEMPRE É EXECUTADA AO GANHAR EXP..
    def leveL_attributes(self):
        if self.level <= 5:
            self.damage = self.weapon
        elif self.level > 5 and self.level < 10:
            self.damage = self.weapon + 5
    def level_up(self):
        if self.exp >= self.up_level:
            self.level += 1
            self.exp -= self.up_level
            self.up_level *= 1.6
            print("Congratulations, you've gone up the level 🎉")
            return self.up_level
        else:
            pass
    #FUNÇÃO BÁSICA DE ATAQUE DE TODOS OS INIMIGOS, DE ACORDOM COM NÚMERO ALEÁTORIO, FUNÇÃO EXECUTADA DENTRO DE Combat()
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
    #FUNÇÃO DE GANHO DE EXP BÁSICA E A EXECUÇÃO DO LEVEl_UP PRA DEFINIR SEU HEROI E PRÓXIMO LEVEL.
    def win_exps(self,exp):
        self.exp += exp
        self.level_up()
        return self.exp
    #FUNÇÃO PRA SABER SE ESTIVER EM Combat() PARA ENCERRAMENTO E FUNCIONAMENTO DE OUTRA FUÇÕES.
    def set_combat(self, combat):
       self.combat = combat
       return self.combat
    #FUNÇÃO BÁSICA DE CONSUMO DE ENERGIA, E LOGO DEPOIS A VERIFICAÇÃO PRA NÃO FICAR NEGATIVO OU ESTOURAR O LIMITE MÁXIMO DE ENERGIA
    def energy_loss(self, energy):
        self.energy -= energy
        return self.energy
        self.verify_energy()
    #VERFICAÇÃO DE ENERGIA ONDE JÁ FOI MENCIONADO
    def verify_energy(self):
        if self.energy > self.maxEnergy:  
            self.energy = self.maxEnergy
            return self.energy
        elif self.energy <= 0:
            self.energy = 0
            return self.energy
    #FUNÇÃO DE DORMIR, PRA RECUPERAÇÃO DE ENERGIA E DE VIDA.
    def sleep(self):
        global day,mounth,year,hours,minute
        #COMO DITO NO INICIO DO CODIGO, A CLASS Map SENDO EXECUTADO PRA DEFINIR O LOCAL DE SUA POSIÇÃO, QUE SERÁ MUITO USADO.
        if Map.place == 'Dungeon':
            if self.energy < 80:
                random_energy = randint(5,10)
                random_life = randint(5,15)
                print(f"You sleep 3 hours and 17 minutes")
                print(f"recupered {random_energy+10} energy")
                print(f"recupered {random_life} life")
                self.energy += 10
                self.energy += random_energy
                self.verify_energy()
                hours += 3
                hour()
            else:
                print("You can only sleep if your energy is at least below 80")
                print("You've rested enough, stay tuned!")
        elif hours <= 0 and hours >= 6 or hours <=18 and self.energy < 20:
                random = randint(5,10)
                print(f"You sleep 6 hours and 17 minutes")
                print(f"recupered {random+30} energy")
                self.energy += 20
                self.energy += random
                self.verify_energy()
                hours += 4
                hour()
        elif hours >= 0 and hours <= 6 or hours >=18:
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
    #FUNÇÃO BÁSICA DE GANHO DE GOLD.       
    def win_golds(self,gold):
        self.golds += gold
        return self.golds
    # FUNÇÃO BÁSICO PARA PERCA DE GOLD
    def set_golds(self,gold):
        self.golds -= gold
        return self.golds
    #FUNÇÃO PARA DEFINIÇÃO DE UMA ARMADURA ÚNICA SEMPRE USADO AO USAR equip_use().
    def set_armor_hp(self):
        self.armor =  self.armor_fix + self.armor
        return self.armor
    #FUNÇÃO PARA DEFINIÇÃO DE UM DANO ÚNICA SEMPRE USADO AO USAR equip_use().
    def set_weapon_damage(self):
        self.damage =  self.damage_fix + self.weapon
        return self.damage
    #FUNÇÃO PARA USO DE POTION, SEJA DE ENERGIA OU VIDA, EM BREVE SERÁ REFATORADA DE OUTRA MANEIRA.
    def use_potion(self, potion_life, potion_energy):
        self.hp += potion_life
        self.energy += potion_energy
        if self.hp > self.maxHp:
            self.hp = self.maxHp
        elif self.energy > self.maxEnergy:
            self.energy = self.maxEnergy
    #FUNÇÃO PARA ESCOLHER OU USAR ITEM DA MOCHILA, SEMPRE EXECUTADA AO ESCOLHER UM ITEM PELO equip_use()
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
    #FUNÇÃO DE EQUIPAR OU USAR POÇÕES OU ITENS, SEMPRE EXECUTADA AO ABRIR MOCHILA, SEJA EM COMBATE OU NÃO.
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
            #PRA SABER QUAL ITEM SERÁ USADO, É FEITO UMA VERFICAÇÃO DO TIPO DE ITEM.
            if item.typer == 'chest':
                if self.delete_use(option, item) == True:
                    if len(self.equip_chest) == 0:
                        self.equip_chest.append(item)
                        print('\n\n\n==============================================')
                        print(f"Have you equipped yourself with a {item.name}")
                        print('==============================================\n')
                        #AO ABRIR A MOCHILA EM COMBATE, A FUNÇÃO É ENCERRADA PARA UM COMBATE MAIS RÁPIDO!
                    else:
                        self.equip_chest[0].equipped = False
                        self.equip_chest.pop()
                        self.equip_chest.append(item)
                        print('\n\n\n==============================================')
                        print(f"Have you equipped yourself with a {item.name}")
                        print('==============================================\n')
                else:
                    pass
            elif item.typer == 'weapon':
                if self.delete_use(option, item) == True:
                    if self.style == item.style or item.style == 'all':
                        if len(self.equip_weapon) == 0:
                            self.equip_weapon.append(item)
                            print('\n\n\n==============================================')
                            print(f"Have you equipped yourself with a {item.name}")
                            print('==============================================\n')
                        else:
                            self.equip_weapon[0].equipped = False
                            self.equip_weapon.pop()
                            self.equip_weapon.append(item)
                            print('\n\n\n==============================================')
                            print(f"Have you equipped yourself with a {item.name}")
                            print('==============================================\n')
                    else:
                        print('==============================================\n')
                        print('This item is not for you!!')
                        print('==============================================\n')
                else:
                    pass
            elif item.typer == 'potion':
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
            elif item.typer == 'utility':
                if self.delete_use(option, item) == True:
                    bag_golds = item.gold
                    self.win_golds(bag_golds)
                    print(f"You won {bag_golds} of golds")
                    self.items.pop(option)
                else:
                    pass
            elif item.typer == 'test':
                if self.delete_use(option, item) == True:
                    print('==============================================\n')
                    print("You cannot use this item")
                    print('==============================================\n')
                else:
                    pass
            else:
                print("This option not exist")    
    #FUNÇÃO PARA CHECAR O DANO E ARMADURA DO EQUIPAMENTO E DEFINIR SE TÁ OU NÃO EQUIPADO.
    def check_equip(self):              
        if len(self.equip_chest) == 0 and len(self.equip_weapon) == 0:
            pass
        elif len(self.equip_chest) == 1 and len(self.equip_weapon) == 0:
            self.armor = self.equip_chest[0].armor
            #LERÁ O ITEM E DEFINARÁ O EQUIPPED COMO TRUE PARA INFORMAÇÃO E EM BREVE MAIS USO..
            self.equip_chest[0].equipped = True
            #É EXECUTADA A FUNÇÃO PARA A SOMA DA ARMADURA FIXA
            self.set_armor_hp()

        elif len(self.equip_chest) == 1 and len(self.equip_weapon) == 1:
            self.weapon = self.equip_weapon[0].damage
            self.armor = self.equip_chest[0].armor
            self.equip_chest[0].equipped = True
            self.equip_weapon[0].equipped = True
            #É EXECUTADA A FUNÇÃO PARA A SOMA DO DANO FIXO
            self.set_weapon_damage()
            self.set_armor_hp()
        elif len(self.equip_chest) == 0 and len(self.equip_weapon) == 1:
            self.weapon = self.equip_weapon[0].damage
            self.equip_weapon[0].equipped = True
            self.set_weapon_damage()
    #FUNÇÃO BÁSICA DE COMBATE AO TOMAR UM DANO DE ACORDO COM A ARMADURA
    def take_damage(self, damage):
        if self.armor > 0:
            red_damage = self.armor/100
            damage -= red_damage
            self.hp -= damage
            return damage
        else:
            self.hp -= damage
            return damage
    #FUNÇÃO BÁSICA PARA AUMENTO DE KILLS, EXECUTADA SEMPRE AO MATAR UM MOB
    def Kills(self):
        self.kills += 1
    def __str__(self):
        f = f'--------\nLife of {self.name}: {self.hp}💗 Damage of {self.name}: {self.damage}🛡️'
        return f
#====================A PARTIR DAQUI SERÁ FEITO AS CLASS DE HEROIS HERDADO DE MOB=====================
#CLASS DO WARRIOR(GUERREIRO)
class Warrior(Mob, Bag, Item):
    def __init__(self,name, hp = 100 ,maxHp = 100, energy = 130, maxEnergy = 130, alive = True, damage = 15, items = [],equip_chest = [], equip_weapon = [], weapon = 0, armor = 0, combat = False, golds = 0,exp=0, level=0,up_level=30):
        super().__init__(name, hp = 150,maxHp = 150, energy = 130, maxEnergy = 130,  alive = True, damage = 0, items = [], kills=0, equip_chest = [], equip_weapon = [], weapon = 0, armor = 0, golds = 0,exp=0, level=0,up_level=30, special_attack= False, style = 'sword')
    #TODO HEROI TEM UM ATAQUE ESPECIAL
    def Special_Attack(self):
        if self.energy >= round(self.maxEnergy/3):
            self.special_attack = True
            self.energy_loss(round(self.maxEnergy/3))
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
    #TODO HEROI TEM UMA FUNÇÃO PARA DESABILITAR O ATAQUE ESPECIAL DEPENDENDO DO SEU TIPO.
    def Disable_Special_Attack(self):
        if self.special_attack == True:
            self.special_attack = False
            if mob.name == "OVERPOWER":
                self.damage -= 1100
            else:
                self.damage -= 100
    def __str__(self):
        f = f'Warrior {self.name} - Life: {self.hp}/{self.maxHp}💗  Energy: {self.energy}/{self.maxEnergy}⚡ Damage: {self.damage}💪 Armor: {self.armor}🛡️'
        return f
#CLASS DO LANCER(LANCEIRO)
class Lancer(Mob, Bag, Item):
    def __init__(self,name, hp = 100 ,maxHp = 100, energy = 130, maxEnergy = 130, alive = True, damage = 15, items = [],equip_chest = [], equip_weapon = [], weapon = 0, armor = 0, combat = False, golds = 0,exp=0, level=0,up_level=30):
        super().__init__(name, hp = 110 ,maxHp = 110, energy = 120, maxEnergy = 120, alive = True, damage = 0, items = [],equip_chest = [], equip_weapon = [], weapon = 0, armor = 0, combat = False, golds = 0,exp=0, level=0,up_level=30,special_attack= False, style = 'lancer')
    def Special_Attack(self, target):
        if self.energy >= round(self.maxEnergy/3):
            self.special_attack = True
            self.energy_loss(round(self.maxEnergy/3))
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
        f = f'Lancer {self.name} - Life: {self.hp}/{self.maxHp}💗  Energy: {self.energy}/{self.maxEnergy}⚡ Damage: {self.damage}💪 Armor: {self.armor}🛡️'
        return f
#CLASS DO MONG(MONGE)
class Monk(Mob, Bag, Item):
    def __init__(self,name, hp = 100 ,maxHp = 100, energy = 130, maxEnergy = 130, alive = True, damage = 15, items = [],equip_chest = [], equip_weapon = [], weapon = 0, armor = 0, combat = False, golds = 0,exp=0, level=0,up_level=30):
        super().__init__(name, hp = 100 ,maxHp = 100, energy = 200, maxEnergy = 200, alive = True, damage = 0, items = [],equip_chest = [], equip_weapon = [], weapon = 0, armor = 0, combat = False, golds = 0,exp=0, level=0,up_level=30,special_attack= False, style = 'meele')
    def Special_Attack(self):
        if self.energy >= round(self.maxEnergy/3):
            self.special_attack = True
            self.energy_loss(round(self.maxEnergy/3))
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
        f = f'Monk {self.name} - Life: {self.hp}/{self.maxHp}💗  Energy: {self.energy}/{self.maxEnergy}⚡ Damage: {self.damage}💪 Armor: {self.armor}🛡️'
        return f
#CLASS DO DRAGONTOOTH(DRAGÃO DENTE DE SABRE)
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
#CLASS DA ARCHER(ARQUEIRA)
class Archer(Mob, Bag, Item):
    def __init__(self,name, hp = 80 ,maxHp = 80, energy = 50,maxEnergy = 50,  alive = True, damage = 25, items = [],equip_chest = [], equip_weapon = [], weapon = 0, armor = 0, arrows = 0,combat = False, golds = 0,exp=0, level=0,up_level=30):
        self.arrows = arrows
        super().__init__(name, hp = 90,maxHp = 90, energy = 60,maxEnergy = 60,  alive = True, damage = 0, items = [],equip_chest = [], equip_weapon = [], weapon = 0, armor = 0,combat = False, golds = 0,exp=0, level=0,up_level=30, style = 'archery')
    def use_arrow(self, arrow):
        if self.arrows > 0:
            self.arrows -= arrow
            return self.arrows
    def get_arrow(self, arrow):
        self.arrows += arrow
        return self.arrows
    def Special_Attack(self,target):
        if self.energy >= round(self.maxEnergy/3):
            if self.arrows >= 2:
                self.arrows -= 2
                self.energy_loss(round(self.maxEnergy/3))
                print('=================================================')
                print("Special Attack!! Double Attack")
                print(f"🗡️ Caused {self.damage *1.2} damage in {target.name}")
                print(f"🗡️ And again you caused {self.damage *1.2} damage in {target.name}")
                print('=================================================')
                target.take_damage(self.damage *1.2)
                target.take_damage(self.damage *1.2)
            else:
                print('=================================================')
                print("You no have arrows to use special")
                print('=================================================')
        else:
            print('=================================================')
            print("You no have energy")
            print('=================================================')

    def __str__(self):
        f = f'Warrior {self.name} - Life: {self.hp}/{self.maxHp}💗  Energy: {self.energy}/{self.maxEnergy}⚡ Arrows: {self.arrows} 🏹 Damage: {self.damage}💪 Armor: {self.armor}🛡️'
        return f
#CLASS SEGREDA DO GALACTUS, PARA TESTE DE MOBS E FUNÇÃO COMBAT TODA EM SÍ
class Galactus(Mob, Bag, Item):
    def __init__(self,name, hp = 80 ,maxHp = 80, energy = 50,maxEnergy = 50,  alive = True, damage = 25, items = [],equip_chest = [], equip_weapon = [], weapon = 0, armor = 0,combat = False, golds = 0,exp=0, level=0,up_level=30):
        super().__init__(name, hp = 9999,maxHp = 9999, energy = 9999,maxEnergy = 9999,  alive = True, damage = 30, items = [],equip_chest = [], equip_weapon = [], weapon = 0, armor = 0,combat = False, golds = 0,exp=0, level=0,up_level=30)
    def Special_Attack(self,target):
        if self.energy >= 0:
            self.energy_loss(0)
            print('=================================================')
            print("Special Attack!! Cosmic explosion!!!!")
            print(f"🗡️ Caused {self.damage *999} damage in {target.name}")
            print('=================================================')
            target.take_damage(self.damage *999)
    def __str__(self):
        f = f'Life of Galactus: {self.hp}/{self.maxHp}💗 Energy of Galactus: {self.energy}/{self.maxEnergy}⚡ Damage of Galactus: {self.damage}🛡️'
        return f
#ESSA É A CLASS INIMIGO ONDE NÃO HERDA NADA PARA UMA DEFINIÇÃO MAIS FACIL DOS INIMIGOS.
#PEGA ALGUMAS FUNÇÕES COMO TOMAR DANO, O ATAQUE BÁSICO ALÉM DE OUTRAS
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
    #UMA FUNÇÃÕ ESPECIFICA SE O MOB SPAWNADO FOR UM GLOBIN PARA ROUBAR SEU OURO.
    def Still_Gold(self, target):
        random = randint(0,10)
        random_gold = randint(3,20)
        if random > 0 and random < 8:
            if target.golds > 0:
                target.golds -= random_gold
                print("Globin stole your money.")
                print("Globin: 'ihihihihihihi'")
                print("Globin: 'Lost smaller'")
                print(f"You lossed {random_gold} 🟡")
                if target.golds < 0:
                    target.golds = 0
            else:
                print("Globin tried to steal his gold but failed! you went into combat!!")
                Combat()
        else:
            Combat()
    #UM SISTEMA BÁSICO PARA EVOLUÇÃO DE MOBS SEMPRE QUE VOCÊ UPAR DE LEVEL.
    def mob_level(self):
        if Hero.level == Hero.level:
            self.level = Hero.level 
            self.damage += self.level*5
            self.hp += self.level*5
    #FUNÇÃO NECESSESÁRIA DE REVIVER OS INIMIGOS SEMPRE QUE SAIR DE COMBATE.
    def revive(self):
        self.hp = self.maxHp
        return self.hp
    #FUNÇÃO DE DROP DE EXP DE FORMA DIRETA, JÁ QUE OS ÚNICOS A RECEBER EXP SERIA O HEROI.
    def drop_exp(self):
        print(f'{self.name} dropped {self.exp} exps 💥')
        Hero.win_exps(self.exp)
    #FUNÇÃO DE DROP DE OURO DE FORMA DIRETA, JÁ QUE OS ÚNICOS A RECEBER OURO SERIA O HEROI.
    def drop_golds(self):
        print(f'{self.name} dropped {self.golds} golds 🟡')
        Hero.win_golds(self.golds)
    #FUNÇÃO BÁSICA DE TOMAR DANO, POR ENQUANTO SEM A DEFINIÇÃO DE ARMADURA NOS INIMIGOS.
    def take_damage(self,damage):
        self.hp -= damage
        return self.hp
    #MESMA FUNÇÃO DE ATAQUE BÁSICO DOS HEROIS.
    def Attack1_E(self,target):
        attack = randint(0,20)
        if (attack <=10 and attack > 0):
            print('=================================================')
            print(f"Missed attack in {target.name}")
            print('=================================================')
        elif (attack > 10 and attack < 18):
            damage = target.take_damage(self.damage)
            print('=================================================')
            print("Attack")
            print(f"🗡️ Caused {damage} damage in {target.name}")
            print('=================================================')
        else:
            damage = target.take_damage(self.damage*2)
            print('=================================================')
            print("ATTACK CRIT!!!")
            print(f"🗡️ Caused {damage} damage in {target.name}")
            print('=================================================')
    def __str__(self):
        f = f'Life of {self.name}: {self.hp}💗 Damage: {self.damage}🛡️'
        return f
# =============A PARTIR DAQUI SERÁ MOSTRADO AS FUNÇÕES DOS JOGO============
#FUNÇÃO DUNGEON E A DEFINIÇÃO DO MAP.
def Donjon():
    Map.location('Donjon')
    print('=================================================')
    print("Fuck fuck fuck, This doesn't look good!!!")
    print('=================================================')
def Exit_Donjon():
    print('=================================================')
    print("Congratulations, you made it through the hole.")
    Map.location('Ground')
    print('=================================================')
def Dungeon():
    Map.location('Dungeon')
    print('=================================================')
    print("Oh, my God! You fell into a dungeon, it's too dark, to beware!!!")
    print('=================================================')
def Exit_Dungeon():
    if Hero.check_item('Key') == True:
        print('=================================================')
        print("Congratulations, you made it out of the Dungeon.")
        Map.location('Ground')
        print('=================================================')
    else:
        print('=================================================')
        print("You don't have the key to exit the dungeon")
        print('=================================================')
#FUNÇÃO DE COMBATE ONDE RECEBE A MAIORIA DAS FUNÇÕES E É DEFINIDO DE ACORDO COM O HEROI ESCOLHIDO.
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
            print(f"[2] Special Attack ⚔️ - [{round(Hero.maxEnergy/3)}]⚡")
            print("[3] Open Bag 🎒")
            print("[4] Run 🚪")
            print('=================================================')
            option_attack = input("Your option: ")
            print('\n')
            #PRIMEIRO É UM IF SIMPLÊS DE ATAQUE DE AMBOS OS MOBS DE FORMA DE ROUND
            if option_attack == '1':
                #UM EXEMPLO A BAIXO ONDE SE A ESCOLHA FOR UMA ARQUEIRA, SEJA EXECUTADO A FUNÇÃO DE PERDER UMA FLECHA A CADA ATAQUE
                if (type(Hero).__name__) == 'Archer':
                    #COM O RETORNO DADO, SENDO SWORD, ALL, LANCER E ETC, VAI DECIDIR QUAL ATAQUE
                    if Hero.check_equip_style() == 'all':
                        Hero.Attack1_E(mob)
                        print('\n')
                        if mob.hp > 0:
                            mob.Attack1_E(Hero)
                        else:
                            print('=================================================')
                            print("Mob is killed.")
                            print('=================================================\n\n')
                    elif Hero.check_equip_style() == 'archery':
                        if Hero.arrows > 0:
                            #FUNÇÃO DA PERDA DE FLECHAS.
                            Hero.use_arrow(1)
                            Hero.Attack1_E(mob)
                            print('\n')
                            if mob.hp > 0:
                                mob.Attack1_E(Hero)
                            else:
                                print('=================================================')
                                print("Mob is killed.")
                                print('=================================================\n\n')
                        #SE ELA NÃO TIVER MAIS FLECHAS, SERÁ INCAPAZ DE ATACAR.
                        else:
                            print("YOU NO HAVE ARROWS")
                            print('\n')
                else:
                    Hero.Attack1_E(mob)
                    print('\n')
                    if mob.hp > 0:
                        mob.Attack1_E(Hero)
                    else:
                        print("Mob is killed.")
            #ONDE É EXECUTADO O ATAQUE ESPECIAL, HEROI NÃO TOMA DANO ENQUANTO ESTIVER USADO ATAQUE ESPECIAL
            elif option_attack == '2':
                equipped_weapon = Hero.check_equip_style()
                if (type(Hero).__name__) == 'Archer':
                    if equipped_weapon == 'archery':
                            Hero.Special_Attack(mob)
                            print('\n')
                            if mob.hp > 0:
                                mob.Attack1_E(Hero)
                            else:
                                print("Mob is killed.")
                    else:
                        print("You no have special without a bow or balestra")
                elif (type(Hero).__name__) == 'Galactus':               
                        Hero.Special_Attack(mob)
                elif Hero.special_attack == False:
                    if (type(Hero).__name__) == 'Monk':              
                        Hero.Special_Attack()
                    if equipped_weapon in ['sword', 'lancer']:
                        if (type(Hero).__name__) == 'Lancer':               
                            Hero.Special_Attack(mob)
                        elif (type(Hero).__name__) == 'Warrior':              
                            Hero.Special_Attack()
                    else:
                        print("You cannot use special without your main weapon.")
                else:
                    print("Special Attack in USE!!!!")
            #FUNÇÃO DE ABRIR MOCHILA NO MEIO DO COMBATE, A MESMA QUE É USADA PRA ABRIR MOCHILA NORMALMENTE.
            elif option_attack == '3':
                Hero.equip_use()
            #AQUI FOI FEITO UM SISTEMA DE FUGIR DE COMBATE, ONDE HÁ UMA POSSIBILIDADE DE FUGIR OU NÃO DEPENDENDO GASTANDO SUA ENERGIA
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
        #A FUNÇÃO DE COMBATE É UM LOOP, SEMPRE QUE É FEITO UMA AÇÃO ELE RODA, SE O MOB TIVER MENOS OU IGUAL A 0, SERÁ EXECUTADO A FUNÇÃO A BAIXO E DEFINARÁ TUDO
        elif mob.hp <= 0:
            print(f"{mob.name} is dead")
            #SOMA DE KILLS DO HEROI
            Hero.Kills()
            print('=================================================')
            #O DROP DE GOLD
            mob.drop_golds()
            #E O DROP DE EXPERIÊNCIA
            mob.drop_exp() 
            #E A DEFINIÇÃO DE FALSE AO SAIR DE COMBATE
            Hero.set_combat(False)
            #E ISSO AQUI PARA REVIVER O MOB E DEFINIR OUTRO ALEÁTORIO.
            mob.revive()
            #ESSA FUNÇÃO É EXECUTADO DE ACORDO COM O ESPECIAL, COMO O MONK, WARRIOR E LANCER, MUDAM OS ATRIBUTOS E FEITO UM DISABLE PRA DEVOLVER OS ATRIBUTOS GANHO EM COMBATE.
            if (type(Hero).__name__) == 'Monk' or (type(Hero).__name__) == 'Warrior' or (type(Hero).__name__) == 'Lancer':
                Hero.Disable_Special_Attack()
            #UM MEIO IMPROVISADO DE COLOCAR UM CONTADOR DE KILLS EM UM BOSS E SEUS CAMPANGAS PARA TERMINAR O DESAFIO, EM BREVE RESOLVEREI!!
            global scorpion_king_kills, scorpion_kills
            if Map.place == 'Donjon' and mob.name == 'Scorpion':
                scorpion_kills += 1
            if Map.place == 'Donjon' and mob.name == 'Scorpion King':
                scorpion_king_kills += 1
            break
        #AQUI É DEFINIÇÃO, SE VOCÊ MORRER EM COMBATE O LOOP É QUEBRADO E O JOGO ACABA.
        elif Hero.hp<= 0:
            print("\n")
            print("You is dead..💀")
            break 
#FUNÇÃO DE SPAWN QUE É SEMPRE EXECUTADO AO SE Mover() QUE ESTA NA CLASS MOB
def Spawn():
    #EU VOU TIRAR ESSA FUNÇÃO!! É SÓ POR ENQUANTO PRA TER UM MINI BOSS
    if Map.place == 'Donjon' and mob.name == 'Scorpion King':
        print('=================================================')
        print("A Scorpion KING!! Get ready for the boss fight!!\n")
        Combat()
    #FUNÇÃO QUE FOI EXPLICADO SEMPRE QUE O MOB SPAWNADO FOR UM GLOBIN.
    elif mob.name == 'Globin Sneaky':
        print('=================================================')
        print("The curse, appeared a sneaky globin!\n")
        mob.Still_Gold(Hero)
    else:
        print("\n\n")
        print('=================================================')
        print(f"👾 SPAWN {mob.name} IN YOUR FRONT!!!!\n")
        Combat()
#AQUI É A FUNÇÃO QUE DEFINARÁ QUEM SERÁ O MOB QUE VOCÊ ENFRETARÁ DE MANEIRA ALEÁTORIO, SEMPRE MUDANDO AO EXECUTAR UMA AÇÃO FORA DE COMBATE.
def randomMob():
    random_gold = randint(0,15)
    random_exp = randint(5,30)
    probability = randint(0,16)
    # DEPENDENDO DE ONDE O HEROI ESTEJA, É SPAWNADO OUTROS MOBS.
    if Map.place == 'Ground':
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
        elif probability >= 12 and probability <=15:
            mob = Enemy('Globin Sneaky', 50,50,5, random_gold, random_exp)
            mob.mob_level()
            return mob
        else:
            mob = Enemy('Globin Lancer', 15,15,15, random_gold, random_exp)
            mob.mob_level()
            return mob
    elif Map.place == 'Donjon':
            if probability >= 0 and probability <=13:
                mob = Enemy('Scorpion', 20,20,3, random_gold, random_exp)
                mob.mob_level()
                return mob
            else:
                mob = Enemy('Scorpion King', 400,400,55, 60, 120)
                mob.mob_level()
                return mob
    else:
        if probability >= 1 and probability <=2:
            mob = Enemy('Skeletion Warrior', 150,150,30, random_gold, random_exp)
            mob.mob_level()
            return mob
        elif probability >= 9 and probability <=9:
            mob = Enemy('Yeti', 200,200,25, random_gold, random_exp)
            mob.mob_level()
            return mob
        elif probability >= 10 and probability <=13:
            mob = Enemy('Rat', 10,10,5, random_gold, random_exp)
            mob.mob_level()
            return mob
        elif probability >= 14 and probability <=16:
            mob = Enemy('Spider', 60,60,15, random_gold, random_exp)
            mob.mob_level()
            return mob
        elif probability >= 3 and probability <=5:
            mob = Enemy('Cockroach', 10,10,1, random_gold, random_exp)
            mob.mob_level()
            return mob
        else:
            mob = Enemy('Globin Sneaky', 20,20,5, random_gold, random_exp)
            mob.mob_level()
            return mob
        
#AQUI É A FUNÇÃO QUE DEFINARÁ QUAL SERÁ O ITEM DROPADO QUE VOCÊ ENCONTRARÁ DE MANEIRA ALEÁTORIO, SEMPRE MUDANDO AO EXECUTAR UMA AÇÃO FORA DE COMBATE.
def randomWeapon():
    probability = randint(1,20)
    #DEPENDENDO DO LUGAR, OS ITENS DROPADOS SERÃO DIFERENTES.
    if Map.place == 'Ground':
        if probability >= 1 and probability <= 2:
            itemAleatory = Item('SmallAxe', 'weapon','meele', 10)
            return itemAleatory
        elif probability >=3  and probability <= 5:
            itemAleatory = Item('Stick', 'weapon','all', 5)
            return itemAleatory
        elif probability >= 6 and probability <= 7:
            itemAleatory = Item('Sword', 'weapon','sword', 15)
            return itemAleatory
        elif probability >= 8 and probability <= 8:
            itemAleatory = Item('BigSword', 'weapon','sword', 20)
            return itemAleatory
        elif probability >= 9 and probability <= 9:
            itemAleatory = Item('Chest', 'chest','all', 0 , 20)
            return itemAleatory
        elif probability >= 10 and probability <= 13:
            itemAleatory = Item('Potion Life', 'potion','all', 0, 0, 100)
            return itemAleatory
        elif probability >= 14 and probability <= 15:
            itemAleatory = Item('Potion Energy', 'potion','all', 0, 0, 0, 100)
            return itemAleatory
        elif probability >= 16 and probability <= 16:
            itemAleatory = Item('Potion Full', 'potion','all', 0, 0, 0, 100)
            return itemAleatory
        elif probability >= 17 and probability <= 17:
            itemAleatory = Item('Spear', 'weapon','lancer', 30, 0, 0, 0)
            return itemAleatory
        elif probability >= 18 and probability <= 20:
            itemAleatory = Item('Dagger', 'weapon','all', 10, 0, 0, 0)
            return itemAleatory
    elif Map.place == 'Donjon':
        if probability >= 1 and probability <= 5:
            itemAleatory = Item('Scorpion tail', 'weapon','all', 9, 0, 0, 0)
            return itemAleatory
        if probability >= 6 and probability <= 10:
            itemAleatory = Item('Torch', 'test','all')
            return itemAleatory
        elif probability >=11 and probability <= 14:
            itemAleatory = Item('Potion Life', 'potion','all', 0, 0, 40)
            return itemAleatory
        elif probability >= 15 and probability <= 20:
            itemAleatory = Item('Potion Energy', 'potion','all', 0, 0, 0, 40)
            return itemAleatory
    else:
        random_golds = randint(5,10)
        if probability >= 5 and probability <= 9:
            itemAleatory = Item('Torch', 'test','all')
            return itemAleatory
        elif probability >= 10 and probability <= 14:
            itemAleatory = Item('Key', 'test','all')
            return itemAleatory
        elif probability >= 15 and probability <= 16:
            itemAleatory = Item('Gold_bag', 'utility','all',0,0,0,0,random_golds)
            return itemAleatory
        elif probability >= 17 and probability <= 20:
            itemAleatory = Item('Bone', 'weapon','all',7,0,0,0)
            return itemAleatory
        elif probability >=1 and probability <= 3:
            itemAleatory = Item('Potion Life', 'potion','all', 0, 0, 60)
            return itemAleatory
        elif probability >= 4 and probability <= 4:
            itemAleatory = Item('Potion Energy', 'potion','all', 0, 0, 0, 60)
            return itemAleatory

#FUNÇÃO PRA DEFINIR SEU NOME E A ESCOLHA DE SEU HEROI, EXECUTADA AO INICIAR O Game()
def Choice_Hero():
    name = input("What you name?: ")
    while True:
        print("Choice your hero.")
        print("[1] Warrior ⚔️")
        print("[2] Lancer 🔱")
        print("[3] Archer 🏹")
        print("[4] Monk 🥋")
        option = input("Your option: ")
        if option == '1':
            Hero = Warrior(name)
            print(f"You picked: {Hero}")
            return Hero
        elif option == '2':
            Hero = Lancer(name)
            print(f"You picked: {Hero}")
            return Hero
        elif option == '3':
            Hero = Archer(name)
            print(f"You picked: {Hero}")
            return Hero
        elif option == '4':
            Hero = Monk(name)
            print(f"You picked: {Hero}")
            return Hero
        elif option == '999':
            Hero = Galactus(name)
            print(f"You picked secret hero: {Hero}")
            return Hero
        else:
            print("What this option? ")
#SISTEMA UNIVERSAL DE HORA DO JOGO, SEMPRE COMEÇADO DO 1/1/2023 0H AND 0MINUTE DEFINADA NA 'MAIN'
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

#ESSA É A FUNÇÃO AO ABRIR O FERREIRO, UM LUGAR PARA COMPRAR OS ITENS COM O OURO GANHO.
def Blacksmith(self):
    while True:
        print('\n\n=================================================')
        print("WELCOME TO BLACKSMITH!!!")
        print('=================================================')
        print(f"You gold's: {self.golds} 🟡")
        print("What do you want?")
        print("[1] - Arrows(5un) - [5] Golds 🟡")
        print("[2] - Potion Life(1un) - [10] Golds 🟡")
        print("[3] - Chest Iron(1un)- [25] Golds 🟡")
        print("[4] - Balesta(1un)- [40] Golds 🟡")
        print("[5] - Potion Energy(1un)- [10] Golds 🟡")
        print("[6] - Potion Full(1un)- [20] Golds 🟡")
        print("[7] - Katana(1un)- [50] Golds 🟡")
        print("[8] - Dagger(1un)- [10] Golds 🟡")
        print("[9] - Bow(1un)- [10] Golds 🟡")
        print("[10] - Claymore(1un)- [10] Golds 🟡")
        print("[11] - Spear(1un)- [10] Golds 🟡")
        print("[12] - Exit")
        option = input('Your option: ')
        if option == '1':
        #COMO AS FLECHAS NÃO É DEFINIDO EXATAMENTE COMO UM OBJETO, É A ÚNICA QUE NÃO É POSSIVEL USAR A FUNÇÃO buyItem()
            if self.golds > 5:
                self.get_arrow(5)
                self.golds -= 5
            else:
                print("You no have gold's")
        elif option == '2':
            self.buyItem(Potion)
        elif option == '3':
            self.buyItem(Chest_Iron)
        elif option == '4':
            self.buyItem(Balestra)
        elif option == '5':
            self.buyItem(Potion1)
        elif option == '6':
            self.buyItem(Potion2)
        elif option == '7':
            self.buyItem(Katana)
        elif option == '8':
            self.buyItem(Dagger)
        elif option == '9':
            self.buyItem(Bow)
        elif option == '10':
            self.buyItem(Claymore)
        elif option == '11':
            self.buyItem(Spear)
        elif option == '12':
            break
        else:
            print("WHAT THE FUCK THIS OPTION??")

#AQUI É A EXECUÇÃO DO JOGO.
if __name__ == "__main__":
    #DEFINI~ÇAO INICIAL DO MAPA
    Map = Map('Ground')
    #DEFINIÇÃO DAS HORAS
    day = 1
    mounth = 1
    year = 2023
    hours = 0
    minute = 1
    scorpion_kills = 0
    scorpion_king_kills = 0
    print("\n\n\n")
    #A PRIMEIRA COISA QUE APARECERÁ AO INICIAR O JOGO.
    print('=================================================')
    print("Game Version 1.5 - Hotfix!!")
    print("Created by Reginaldo and Andre")
    print("Participation of João and Jorge")
    print("Features:")
    print(" - Fixed bugs")
    print("- Added a new function when finding weapon or chest, you can equip directly.")
    print("- A small chance to escape the Donjon through the hole.")
    print("- Information on how much it costs to use the special attack.")
    print("- Energy cost update to use special.")
    print('=================================================')
    print('Welcome to world!!!')
    print('=================================================')
    Hero = Choice_Hero()
    #DEFINIÇÃO DOS ITENS PARA COMPRA NO FERREIRO E A INICIAÇÃO.
    Potion = Item('Potion Life', 'potion','all', 0, 0, 50,0,10)
    Potion1 = Item('Potion Energy', 'potion','all', 0, 0, 0,50,10)
    Potion2 = Item('Potion Full', 'potion','all', 0, 0,50, 50,20)
    Chest_Iron = Item('Iron chest', 'chest','all', 0, 20, 0,0,25)
    Balestra  = Item('Balesta', 'weapon','archery', 30, 0, 0,0,25)
    Bow  = Item('Bow', 'weapon','archery', 20, 0, 0,0,15)
    Katana = Item('Katana', 'weapon','sword', 35, 0, 0,0,50)
    Dagger = Item('Dagger', 'weapon','all', 10, 0, 0,0,10)
    Toothpick = Item('Toothpick', 'weapon','all', 3, 0, 0,0,0)
    Claymore = Item('Claymore', 'weapon','sword', 15, 0, 0,0,10)
    Spear = Item('Spear', 'weapon','lancer', 15, 0, 0,0,10)
    #O HEROI COMEÇA SEMPRE COM DOIS ITENS, UMA POÇÃO DE VIDA E ENERGIA.
    Hero.items.append(Potion)
    Hero.items.append(Potion1)
    Hero.items.append(Toothpick)
    print(f'{bc.BOLD}{bc.RED}=================================================')
    print("ATENTION!!!!")
    print("You started the game with a Potion of Life, energy and toothpick!!!")
    print(f'================================================={bc.ENDC}')

    while True:
        try:
    #VERIFICAÇÃO PARA O JOGO RODAR, SE O HEROI MORRER EM COMBATE OU DE OUTRAS CAUSAS, É CAUSADO O GAMER OVER
            if Hero.hp > 0 and scorpion_king_kills == 0:  
                #AS DUAS FUNÇÕES DE DEFINIÇÃO DE MOB E ITENS ALEÁTORIOS.
                itemAleatory = randomWeapon()
                mob = randomMob()
                print(f'{bc.BOLD}{bc.CYAN}=================================================')
                print(Hero)
                print("You kills: ", Hero.kills, "💀")
                print("You gold's: ", Hero.golds, "🟡")
                print("You level: ", Hero.level, "⭐")
                if Map.place != 'Ground':
                    print("Date now: You can't see anything above")
                else:
                    print(f'Date now: {day}/{mounth}/{year} {hours} hours and {minute} minutes')
                print(f'Your location: {Map.place}')
                if hours >= 6 and hours < 18 and Map.place == 'Ground':
                    print(f"It's day: ☀️")
                elif hours >= 6 and hours < 18 and Map.place == 'Ground':
                    print(f"It's night: 🌚")
                elif Map.place != 'Ground':
                    print("It's Inviable: ⚫")
                print('=================================================')
                print("What your next action")
                print("[1] Move 🦶")
                print("[2] Open Bag 🎒")
                print("[3] Sleep 😴")
                print("[4] Blacksmith 🔨")
                print("[5] Exit 🚪")
                print('=================================================')
                option = input(F"Your option: {bc.ENDC}")
                print(f'{bc.BOLD}')
                if option == '1':
                    if Hero.energy <=0:
                        print('=================================================')
                        print("You're practically dead! GO TO REST")
                        print('=================================================')
                    else:
                        Hero.Move()
                elif option == '2':
                    Hero.openBag()
                elif option == '3':
                    if Map.place == 'Ground':
                        Hero.sleep()
                    else:
                        if Hero.check_item('Torch') == True:
                            Hero.sleep()
                        else:
                            print("You can't sleep, it's too dark, try to find a torch!")
                elif option == '4':
                    if Map.place == 'Ground':
                        Blacksmith(Hero)
                    else:
                        print(f"You're in the middle of the {Map.place}, you can't buy anything")
                elif option == '5':
                    break
                else:
                    print ("WHAT THE FUCK THIS ACTION??????")
            elif Hero.hp<= 0:
                os.system('cls')
                print("GAME OVER!!")
                break 
            elif Hero.hp > 0 and scorpion_king_kills == 1: 
                print(f"PARABENS VOCE ZEROU O GAME!!!! PARAAAABENSSSSS {Hero.name}, BRAVO {(type(Hero).__name__)}!!!!!")
                print("[1] - Continue")
                print("[2] - Exit")
                option = input(".....:")
                if option == '1':
                    scorpion_king_kills = 0
                elif option == '2':
                    break
                else:
                    print("nop!")
        except:
            print("FAIL FAIL FAIL FAIL!!!")