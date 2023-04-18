from random import randint
import os
import ast
import json
import pickle

# CODIGO FEITO POR REGINALDO E ANDRÉ
# COM APOIO DE JOÃO E JORGE
# SEM USO DE BIBLIOTECAS NÃO PADRÃO DO PYTHON
# TUDO COMENTADO



#ESSE É UM SISTEMA DE TRADUÇÃO DE EN E PT
def read_language_file(language):
    if language == "pt":
        with open(r"resources/Languages/pt.txt",encoding='utf-8') as f:
            return {line.split("=")[0].strip(): line.split("=")[1].strip() for line in f if "=" in line}
    elif language == "en":
        with open(r"resources/Languages/en.txt",encoding='utf-8') as f:
            return {line.split("=")[0].strip(): line.split("=")[1].strip() for line in f if "=" in line}
    else:
        raise ValueError("Invalid language")
#ESSA É A FUNÇÃO AO ABRIR O FERREIRO, UM LUGAR PARA COMPRAR OS ITENS COM O OURO GANHO.

#ESSA FUNÇÃO AQUI É SÓ PRA PRINTAR AS ATUALIZAÇÕES NO ARQUIVOS DO JOGO .TXT
def features(language):
    features = []
    if language == '1':
        with open("resources/TextFiles/features_pt.txt","r",encoding='utf-8') as file:
            features = file.readlines()
    else:
        with open("resources/TextFiles/features_en.txt","r",encoding='utf-8') as file:
            features = file.readlines()
    for line in features:
        print(line.strip())

# ESSA FUNÇÃO É UM SAVE GAME, PRA SALVAR OS DADOS 

def save_game(Hero):
    with open("saves/player_save.txt", "w") as file:
        file.write(f"{Hero.name}\n")
        file.write(f"{Hero.hp}\n")
        file.write(f"{Hero.maxHp}\n")
        file.write(f"{Hero.energy}\n")
        file.write(f"{Hero.maxEnergy}\n")
        file.write(f"{Hero.damage}\n")
        file.write(f"{Hero.kills}\n")
        file.write(f"{Hero.weapon}\n")
        file.write(f"{Hero.armor}\n")
        file.write(f"{Hero.golds}\n")
        file.write(f"{Hero.exp}\n")
        file.write(f"{Hero.level}\n")
        file.write(f"{Hero.up_level}\n")
        file.write(f"{Hero.x}\n")
        file.write(f"{Hero.y}\n")
        file.write(f"{Hero.style}\n")
    with open("saves/player_itens_save.bin", "wb") as f:
        # escreve a lista de itens no arquivo binário
        pickle.dump(Hero.items, f)
        pickle.dump(Hero.equip_chest, f)
        pickle.dump(Hero.equip_weapon, f)
# ESSA AQUI É PRA PEGAR OS DADOS QUE FORAM SALVOS NO SAVE GAME
def load_game():
    if os.path.exists("saves/player_save.txt"):
        with open("saves/player_save.txt", "r") as file:
            name = file.readline().strip()
            hp = float(file.readline().strip())
            maxHp = int(file.readline().strip())
            energy = int(file.readline().strip())
            maxEnergy = int(file.readline().strip())
            damage = int(file.readline().strip())
            kills = int(file.readline().strip())
            weapon = int(file.readline().strip())
            armor = int(file.readline().strip())
            golds = int(file.readline().strip())
            exp	= float(file.readline().strip())
            level = int(file.readline().strip())
            up_level = float(file.readline().strip())
            x = int(file.readline().strip())
            y = int(file.readline().strip())
            style= file.readline().strip()
        with open("saves/player_itens_save.bin", "rb") as f:
            items = pickle.load(f)
            equip_weapon = pickle.load(f)
            equip_chest = pickle.load(f)
        return name, hp, maxHp, energy, maxEnergy, damage, kills, weapon, armor, golds, exp, level, up_level, x, y, style, items,  equip_chest, equip_weapon
    else:
        return None


# CLASS Map, MOSTRAR ONDE VOCÊ TÁ NO MOMENTO, DIGAMOS "MAPA" E ALGUMAS CONFIGURAÇÕES INICIAS
class Map():
    def __init__(self, place, minute = 0, hours = 1, day = 1, mounth = 2, years = 2023, cord_door_x = 3, cord_door_y = 3):
        self.place = place
        self.minute = minute
        self.hours = hours
        self.day = day
        self.mounth = mounth
        self.years = years
        self.cord_door_x = cord_door_x
        self.cord_door_y = cord_door_y
    def location(self, place):
        if place != self.place:
            self.place = place
            return self.place
        else:
            pass   
    def show_map(self):
        if Hero.check_item('Map') == True:
            print(strings['map_menu'] +'\n')
            print('[1] - ',strings['map_option1'])
            print('[2] - ',strings['exit'])
            option = input(strings['choice'])
            if option == '1':
                Map.Exit_Dungeon()
            elif option == '2':
                pass
            else:
                print(strings['invalid'])
        else:
            print(strings['enought_map'])
            
    #SISTEMA UNIVERSAL DE HORA DO JOGO, SEMPRE COMEÇADO DO 1/1/2023 0H AND 0MINUTE
    def hour(self):
        self.minute += 17
        if self.minute >= 60:
            self.hours +=1
            self.minute = 0
        elif self.hours >=24:
            self.hours = 0
            self.day += 1
        elif self.day >= 30:
            self.day = 0
            self.mounth += 1
        elif Hero.combat == True:
            self.hours += 1
    #FUNÇÃO DAS DUGEON E A DEFINIÇÃO DO MAP.
    def Donjon(self):
        self.location('Donjon')
        print(strings["divider"])
        print(strings["donjon_enter"])
        print(strings["divider"])
    def Exit_Donjon(self):
        print(strings["divider"])
        print(strings['donjon_escape'])
        self.location('Ground')
        print(strings["divider"])
    def Dungeon(self):
        self.location('Dungeon')
        # self.cord_door_x = randint(1,4)
        # self.cord_door_y = randint(1,8)
        print(strings["divider"])
        print(strings["dungeon_enter"])
        print(strings["divider"])
    def Exit_Dungeon(self):
        if Map.place == 'Dungeon':
            print(strings['found_door'])
            print('[1]',strings['yes'])
            print('[2]',strings['no'])
            option = input("You choice: ")
            if option == '1':
                if Hero.check_item('Key') == True:
                    print(strings["divider"])
                    print(strings["dungeon_escape"])
                    print(strings["divider"])
                    self.location('Ground')
                else:
                    print(strings["divider"])
                    print(strings["no_key"])
                    print(strings["divider"])
            elif option == '2':
                print(strings['ignored'])
            else:
                print(strings['invalid'])
#CLASS COLORES, PRA COLOCAR CORES EM CERTOS TEXTOS
#EXP PRINT(f'{bc.BLUE}Welcome{bc.ENDC)
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
    def __init__(self, name, typer,style, damage = 0, armor = 0, life = 0, energy = 0, gold = 0, probability_min = 0, probability_max = 0, equipped = False):
        self.name = name
        self.typer = typer
        self.energy = energy
        self.style = style
        self.damage = damage
        self.armor = armor
        self.life = life
        self.gold = gold
        self.probability_min = probability_min
        self.probability_max = probability_max
        self.equipped = equipped
    #DEFINIÇÃO DA STRING DE ACORDO COM OS ITEM
    def __str__(self):
        if self.equipped == True:
            f = f'{self.name} - {bc.BOLD}Equipped\nDamage: +{self.damage} 💪\nArmor: +{self.armor} 🛡️\nFor: {bc.GREEN}{bc.BOLD}{self.style}{bc.ENDC}{bc.BOLD}\nGold: {self.gold}🟡'
            return f
        elif self.typer == 'potion':
            f = f'{self.name}\nLife: +{self.life} 💗\nEnergy: +{self.energy} ⚡\nGold: {self.gold}🟡'
            return f
        elif self.typer == 'utility':
            f = f'{self.name}\nGold: +{self.gold}🟡'
            return f
        elif self.typer == 'test':
            test_description = strings['test_description']
            f = f'{self.name}\n{test_description}\nGold: {self.gold}🟡'
            return f
        else:
            if self.equipped == False:
                cannot_equip = strings['cannot_equip']
                can_equip = strings['can_equip']
                if len(Hero.equip_weapon) == 1:
                    damage = Hero.equip_weapon[0].damage
                    if self.typer == 'weapon':
                        if self.style == Hero.style or self.style == 'all':
                            if damage > self.damage:
                                f = f'{self.name}\nDamage: -{bc.RED}{bc.BOLD}{damage - self.damage}{bc.ENDC}{bc.BOLD} 💪\nArmor: +{self.armor} 🛡️\nFor: {bc.GREEN}{bc.BOLD}{self.style}{bc.ENDC}{bc.BOLD}\nGold: {self.gold}🟡\n{bc.GREEN}{can_equip}{bc.ENDC}{bc.BOLD}'
                                return f
                            else:
                                f = f'{self.name}\nDamage: +{bc.GREEN}{bc.BOLD}{self.damage - damage}{bc.ENDC}{bc.BOLD} 💪\nArmor: +{self.armor} 🛡️\nFor: {bc.GREEN}{bc.BOLD}{self.style}{bc.ENDC}{bc.BOLD}\nGold: {self.gold}🟡\n{bc.GREEN}{can_equip}{bc.ENDC}{bc.BOLD}'
                                return f
                        else:
                            if damage > self.damage:
                                f = f'{self.name}\nDamage: -{bc.RED}{bc.BOLD}{damage - self.damage}{bc.ENDC}{bc.BOLD} 💪\nArmor: +{self.armor} 🛡️\nFor: {bc.RED}{bc.BOLD}{self.style}{bc.ENDC}{bc.BOLD}\nGold: {self.gold}🟡\n{bc.RED}{cannot_equip}{bc.ENDC}{bc.BOLD}'
                                return f
                            else:
                                f = f'{self.name}\nDamage: +{bc.GREEN}{bc.BOLD}{self.damage - damage}{bc.ENDC}{bc.BOLD} 💪\nArmor: +{self.armor} 🛡️\nFor: {bc.RED}{bc.BOLD}{self.style}{bc.ENDC}{bc.BOLD}\nGold: {self.gold}🟡\n{bc.RED}{cannot_equip}{bc.ENDC}{bc.BOLD}'
                                return f

                if len(Hero.equip_chest) == 1:
                    armor = Hero.equip_chest[0].armor
                    if self.typer == 'chest':
                        if armor > self.armor:
                            f = f'{self.name}\nDamage: +{self.damage} 💪\nArmor: -{bc.RED}{bc.BOLD}{armor - self.armor}{bc.ENDC}{bc.BOLD} 🛡️\nFor: {self.style}\nGold: {self.gold}🟡\nGold: {self.gold}🟡'
                            return f
                        else:
                            f = f'{self.name}\nDamage: +{self.damage}💪\nArmor: +{bc.GREEN}{bc.BOLD}{self.armor - armor}{bc.ENDC}{bc.BOLD} 🛡️\nFor: {self.style}\nGold: {self.gold}🟡\nGold: {self.gold}🟡'
                            return f
                else:
                    if self.style == Hero.style or self.style == 'all':
                        f = f'{self.name}\nDamage: +{self.damage} 💪\nArmor: +{self.armor} 🛡️\nFor: {bc.GREEN}{bc.BOLD}{self.style}{bc.ENDC}{bc.BOLD}\nGold: {self.gold}🟡\n{bc.GREEN}{can_equip}{bc.ENDC}{bc.BOLD}'
                        return f
                    else:
                        f = f'{self.name}\nDamage: +{self.damage} 💪\nArmor: +{self.armor} 🛡️\nFor: {bc.RED}{bc.BOLD}{self.style}{bc.ENDC}{bc.BOLD}\nGold: {self.gold}🟡\n{bc.RED}{cannot_equip}{bc.ENDC}{bc.BOLD}'
                        return f

#CLASS DA MOCHILA
class Bag(Item):
    def __init__(self, items = []):
        self.items = items
    def rodar_itens(self):
        for items in self.items:
            items = items.name
            return items
    #FUNÇÃO DE ABRIR MOCHILA SE HOUVER ITENS
    def openBag(self):
        if len(self.items) == 0:
            print(strings['empty'])
        while True:
            self.check_equip()
            print(Hero)
            print("\n------------------")
            for count, item in enumerate(self.items):
                print(f'[{count}] - {item}         ')   
                print("------------------")
            print("[11] to Exit\n")
            print(strings['item'])
            option = int(input(strings['choice']+ ": "))
            print('\n\n')
            if option == 11:
                break
            item = self.items[option]
            #PRA SABER QUAL ITEM SERÁ USADO, É FEITO UMA VERFICAÇÃO DO TIPO DE ITEM.
            if self.delete_use(option, item) == True:
                self.equip_use(item,option)
    #FUNÇÃO PRA PEGAR O ITEM SEJA NO DROP, QUANDO O MOB DROPAR ALGO
    def pickItem(self, Item):
            print(strings["divider"])
            print(strings["found_item"].format(Item.name))
            print(Item)
            while True:
                if Item.typer in ['weapon','chest']:
                    print("[1] -",strings["pick"])
                    print("[2] -",strings['equip'])
                    print("[3] -",strings['ignore'])
                    print(strings["divider"])
                    choice = input(strings['choice']+ ": ")
                    #SE A ESCOLHA FOR 1, VAI GUARDAR O ITEM SE TIVER ESPAÇO NA MOCHILA
                    if choice == '1':
                        if len(self.items) <= 9:
                            print("\n")
                            print(f'{Item.name} guarded.')
                            print('\n')
                            self.items.append(Item)
                            break
                        else:
                            print(strings['bag_full'])
                    elif choice == '2':
                        #USA O MESMO SISTEMA DE EQUIP_USE PORÉM DE UMA MANEIRA SIMPLIFICADA APENAS PRA EQUIPAR DE UMA VEZ E FAZER AS VERIFICAÇÕES
                        #PRA SABER QUAL ITEM SERÁ USADO, É FEITO UMA VERFICAÇÃO DO TIPO DE ITEM.
                        if len(self.items) <= 9:
                            if self.equipItem(Item) == True:
                                break
                        else:
                            print(strings['bag_full'])
                        print('\n\n')
                    #SE ESCOLHIDO A OPÇÃO 3, IGNORA O ITEM E SEGUE
                    elif choice == '3':
                        print(strings['ignore'])
                        break
                    else:
                        print('\n',strings['invalid'],'\n')
                else:
                    print("[1]",strings["pick"])
                    print("[2]",strings['ignore'])
                    print(strings["divider"])
                    choice = input(strings['choice']+ ": ")
                    if choice == '1':
                        if len(self.items) <= 9:
                            print("\n")
                            print(f'{Item.name} guarded.')
                            print('\n')
                            self.items.append(Item)
                            break
                        else:
                            print(strings['bag_full'])
                    elif choice == '2':
                        print("You ignored.")
                        break
                    else:
                        print('\n',strings['invalid'],'\n')
    #FUNÇÃO PRA VENDER OS ITENS PEGO PELA A METADE DO PREÇO
    def sellItem(self,option, item):
        print(strings['sure'])
        print(f"Item will be sold by {item.gold//2}🟡")
        while True:
            print("[1]",strings['yes'])
            print("[2]",strings['no'])
            option2 = input(strings['choice']+ ": ")
            if option2 == '1':
                if item.equipped == False:
                    self.get_golds(item.gold//2)
                    self.items.pop(option)
                    print(f'\nYou received {item.gold//2}🟡 for the sale of {self.name}\n')
                    return True
                else:
                    print(strings['fail_sell'])
            else:
                break
            return False
    #USA O MESMO SISTEMA DE EQUIP_USE PORÉM DE UMA MANEIRA SIMPLIFICADA APENAS PRA EQUIPAR DE UMA VEZ E FAZER AS VERIFICAÇÕES
    #PRA SABER QUAL ITEM SERÁ USADO, É FEITO UMA VERFICAÇÃO DO TIPO DE ITEM.
    def equipItem(self, Item):
        if Item.typer == 'chest':
            if len(self.equip_chest) == 0:
                self.items.append(Item)
                self.equip_chest.append(Item)
                print('\n\n\n==============================================')
                print(strings['equip_item'].format(Item.name))
                print('==============================================\n')
                self.check_equip()
            else:
                self.equip_chest[0].equipped = False
                self.equip_chest.pop()
                self.items.append(Item)
                self.equip_chest.append(Item)
                print('\n\n\n==============================================')
                print(strings['equip_item'].format(Item.name))
                print('==============================================\n')
                self.check_equip()
        elif Item.typer == 'weapon':
            if self.style == Item.style or Item.style == 'all':
                if len(self.equip_weapon) == 0:
                    self.items.append(Item)
                    self.equip_weapon.append(Item)
                    print('\n\n\n==============================================')
                    print(strings['equip_item'].format(Item.name))
                    print('==============================================\n')
                    self.check_equip()
                else:
                    self.equip_weapon[0].equipped = False
                    self.equip_weapon.pop()
                    self.items.append(Item)
                    self.equip_weapon.append(Item)
                    print('\n\n\n==============================================')
                    print(strings['equip_item'].format(Item.name))
                    print('==============================================\n')
                    self.check_equip()
            else:
                print('==============================================\n')
                print(strings['fail_equip'])
                print('==============================================\n')
                return False
        return True
    #FUNÇÃO DE COMPRAR ITENS
    def buyItem(self, Item):
            print(strings["divider"])
            print(F'Do you want to buy the {Item.name}?')
            print("-------------")
            print(Item)
            print("-------------\n")
            while True:
                print("[1]",strings['buy'])
                print("[2]",strings['exit'])
                print(strings["divider"])
                choice = input(strings['choice']+ ": ")
                if choice == '1':
                    if len(self.items) <= 9:
                        if self.golds >= Item.gold:
                            print("\n")
                            self.golds -= Item.gold
                            print(f'{Item.name} Bought.')
                            self.items.append(Item)
                            break
                        else:
                            print(strings['fail_buy'])
                    else:
                        print(strings['bag_full'])

                elif choice == '2':
                    print(strings['exit'])
                    break
                else:
                    print('\n',strings['invalid'],'\n')
#CLASS DE MOB, A CLASS QUE SERÁ O PAI DE TODOS HEROIS.
class Mob(object):
    def __init__(self, name, hp = 100, maxHp = 100, energy = 130, maxEnergy = 130, damage = 0, kills = 0, weapon = 0, armor = 0, golds = 0,exp=0, level=0,up_level=30, x = 0, y = 0, style = '', items = [], equip_chest = [], equip_weapon = [], alive = True,special_attack = False, combat = False):
        self.hp = hp
        self.x = x 
        self.y = y
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
        Sharptooth = 'sharptooth'
        equipped_found = False
        for i in self.items:
            if i.typer == 'weapon':
                if i.equipped == True:           
                    if i.style == 'all': 
                        equipped_found = True
                        return All   
                    elif (type(Hero).__name__) == 'Archer':
                        if i.style == 'archery':
                            equipped_found = True
                            return Archery                                  
                    elif (type(Hero).__name__) == 'Warrior':
                        if i.style == 'sword':
                            equipped_found = True
                            return Sword                                  
                    elif (type(Hero).__name__) == 'Lancer':
                        if i.style == 'lancer':
                            equipped_found = True
                            return Lancer                                  
                    elif (type(Hero).__name__) == 'Monk':
                        if i.style == 'meele':
                            equipped_found = True
                            return Meele               
                    elif (type(Hero).__name__) == 'Dragontooth':
                        if i.style == 'sharptooth':
                            equipped_found = True
                            return Sharptooth                      
        if not equipped_found:
            print(strings['unequipped'])
            return "unequipped"

    #FUNÇÃO BÁSICA DO JOGO QUE SERÁ SE MOVER.
    def Move(self):
        Map.hour()
        probability = randint(0,28)
        self.energy_loss(randint(1,4))
        # if scorpion_king_kills >= 1:
        #     print("Congratulations, you killed the scorpion king, you are free")
        #     print("You left of Donjon")
        #     Map.location('Ground')
        # elif scorpion_kills >= 10:
        #     print("yeah... you didn't prove your worth, but for your effort you're released")
        #     print("You left of Donjon")
        #     scorpion_kills = 0
        #     Map.location('Ground')
        if probability >= 0 and probability <=13:
            Spawn()
        elif probability >= 14 and probability <=20:
            self.pickItem(itemAleatory)
        elif probability >= 21 and probability <=24:
            if Map.place == 'Ground':
                if self.kills < 10:
                    print(strings['found_dungeon'])
                else:
                    Map.Dungeon()
            else:
                if Map.place == 'Dungeon':
                    Spawn()
                else:
                    print(strings['move_msg'].format(Map.place))
        elif probability >= 25 and probability <=28:
            if Map.place == 'Ground':
                if self.kills < 10:
                    print(strings['found_dungeon'])
                else:
                    Map.Donjon()
            elif Map.place != 'Dungeon' and Map.place != 'Ground':
                if probability >= 25 and probability <=28:
                    Map.Exit_Donjon()
        else:
            print(strings['move_msg'].format(Map.place))
    #FUNÇÃO DE MELHORAR OS ATRIBUTOS SEMPRE QUE UPAR DE LEVEL, ELA É EXECUTADA AO SUBIR DE NIVEL..
    def leveL_attributes(self):
        if self.level < 5:
            self.damage_fix = 0
            self.set_weapon_damage()
        elif self.level >= 5 and self.level < 7:
            self.damage_fix = 5
            self.set_weapon_damage()
        elif self.level >= 7 and self.level < 10:
            self.damage_fix = 15
            self.set_weapon_damage()
        elif self.level > 10 and self.level < 13:
            self.damage_fix = 15
            self.set_weapon_damage()
        else:
            level_factor = (self.level - 10) // 3
            self.damage_fix = 20 * level_factor
            self.set_weapon_damage()
    #FUNÇÃO DE LEVEL_UP QUE SEMPRE É EXECUTADA AO GANHAR EXP..
    def level_up(self):
        if self.exp >= self.up_level:
            self.level += 1
            self.leveL_attributes()
            self.exp -= self.up_level
            self.up_level *= 1.2
            print(strings['level_up'])
            return self.up_level
        else:
            pass
    #FUNÇÃO PARA DEFINIÇÃO DE UMA ARMADURA ÚNICA SEMPRE USADO AO USAR equip_use().
    def set_armor_hp(self):
        self.armor =  self.armor_fix + self.armor
        return self.armor
    #FUNÇÃO PARA DEFINIÇÃO DE UM DANO ÚNICA SEMPRE USADO AO USAR equip_use().
    def set_weapon_damage(self):
        self.damage =  self.damage_fix + self.weapon
        return self.damage
    #FUNÇÃO BÁSICA DE ATAQUE DE TODOS OS INIMIGOS, DE ACORDOM COM NÚMERO ALEÁTORIO, FUNÇÃO EXECUTADA DENTRO DE Combat()
    def Attack1_E(self,target):
        attack = randint(0,20)
        if (attack <=10 and attack > 0):
            print(strings["divider"])
            print(strings['miss_attack'].format(self.name, target.name))
            print(strings["divider"])
        elif(attack > 10 and attack < 18):
            if target == mob:
                print(strings["divider"])
                print(strings['basic_attack'].format(self.name,self.damage,target.name))
                print(strings["divider"])
                target.take_damage(self.damage)
            else:
                print(strings["divider"])
                print(strings['basic_attack'].format(self.name, self.damage,target.name))
                print(strings["divider"])
                target.take_damage(self.damage)
        else:
            if target == mob:
                print(strings["divider"])
                print(strings['critical_attack'].format(self.name, self.damage*2,target.name))
                print(strings["divider"])
                target.take_damage(self.damage*2)
            else:
                print(strings["divider"])
                print(strings['critical_attack'].format(self.name, self.damage*2,target.name))
                print(strings["divider"])
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
        self.verify_energy()
        return self.energy
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
        random_energy = randint(5,10)
        random_life = randint(5,15)
        #COMO DITO NO INICIO DO CODIGO, A CLASS Map SENDO EXECUTADO PRA DEFINIR O LOCAL DE SUA POSIÇÃO, QUE SERÁ MUITO USADO.
        if Map.place != 'Ground':
            if Hero.check_item('Torch') == True:
                if self.energy < 90:
                    print(strings['sleep_success'])
                    print(strings['sleep_sucess_energy'].format(random_energy+20))
                    print(strings['sleep_sucess_life'].format(random_life))
                    self.energy += 20
                    self.energy += random_energy
                    self.verify_energy()
                    Map.hours += 8
                    Map.hour()
                else:
                    print(strings['sleep_fail_dungeon'])
                    print(strings['sleep_fail_dungeon2'])
            elif Hero.check_item('Torch') == False and self.energy <=5:
                print(strings['sleep_success'])
                print(strings['sleep_sucess_energy'].format(random_energy+20))
                print(strings['sleep_sucess_life'].format(random_life))
                self.energy += 20
                self.energy += random_energy
                self.verify_energy()
                Map.hours += 8
                Map.hour()
            else:
                print(strings['sleep_fail_dungeon_torch'])
        elif Map.hours <= 0 and Map.hours >= 6 or Map.hours <=18 and self.energy < 20:
                random = randint(5,10)
                print(strings['sleep_success'])
                print(strings['sleep_sucess_energy'].format(random_energy+20))
                self.energy += 20
                self.energy += random
                self.verify_energy()
                Map.hours += 8
                Map.hour()
        elif Map.hours >= 0 and Map.hours <= 6 or Map.hours >=18:
            if self.energy < self.maxEnergy:
                random = randint(5,10)
                print(strings['sleep_success'])
                print(strings['sleep_sucess_energy'].format(random_energy+20))
                self.energy += 20
                self.energy += random
                self.verify_energy()
                Map.hours += 8
                Map.hour()
            else:
                print(strings['sleep_fail_ground_energy'])
        else:
            print(strings['sleep_fail_ground_day'])
    #FUNÇÃO BÁSICA DE GANHO/PEGAR DE GOLD.       
    def get_golds(self,gold):
        self.golds += gold
        return self.golds
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
            print(strings['choice']+ ": ")
            print('------------')
            print(item)
            print('------------')
            print(strings['want'])
            print("[1]",strings['use'])
            print("[2]",strings['delete'])
            print("[3]",strings['sell'])
            print("[4]",strings['exit'],'\n')
            option2 = input(strings['choice']+ ": ")
            if option2 == '1':
                return True
            elif option2 == '2':
                if item.equipped == True:
                    print(strings['fail_delete'])
                else:
                    self.items.pop(option)
                    print(f"You deleted {item.name}")
                    return False
            elif option2 == '3':
                self.sellItem(option, item)
                return False
            elif option2 == '4':
                return False
            else:
                print("NOP!!")
    #FUNÇÃO DE EQUIPAR OU USAR POÇÕES OU ITENS, SEMPRE EXECUTADA AO ABRIR MOCHILA, SEJA EM COMBATE OU NÃO.
    def equip_use(self, item, option):
            if item.typer == 'chest':
                if len(self.equip_chest) == 0:
                    self.equip_chest.append(item)
                    print('\n\n\n==============================================')
                    print(strings['equip_item'].format(item.name))
                    print('==============================================\n')
                else:
                    self.equip_chest[0].equipped = False
                    self.equip_chest.pop()
                    self.equip_chest.append(item)
                    print('\n\n\n==============================================')
                    print(strings['equip_item'].format(item.name))
                    print('==============================================\n')
            elif item.typer == 'weapon':
                if self.style == item.style or item.style == 'all':
                    if len(self.equip_weapon) == 0:
                        self.equip_weapon.append(item)
                        print('\n\n\n==============================================')
                        print(strings['equip_item'].format(item.name))
                        print('==============================================\n')
                    else:
                        self.equip_weapon[0].equipped = False
                        self.equip_weapon.pop()
                        self.equip_weapon.append(item)
                        print('\n\n\n==============================================')
                        print(strings['equip_item'].format(item.name))
                        print('==============================================\n')
                else:
                    print('==============================================\n')
                    print(strings['fail_equip'])
                    print('==============================================\n')
            elif item.typer == 'potion':
                potion_life = item.life
                potion_energy = item.energy
                if self.energy < self.maxEnergy and self.hp < self.maxHp:
                    self.use_potion(potion_life,potion_energy)
                    print(f"You cured {potion_life} of life and {potion_energy} of energy ")
                    self.items.pop(option)
                    #AO ABRIR A MOCHILA EM COMBATE, A FUNÇÃO É ENCERRADA PARA UM COMBATE MAIS RÁPIDO!
                    if self.combat == True:
                        return  
                elif self.energy >= self.maxEnergy and self.hp < self.maxHp:
                    print(strings['full_energy'])
                    self.use_potion(potion_life,0)
                    self.items.pop(option)
                    print(f"You cured {potion_life} of life")
                    #AO ABRIR A MOCHILA EM COMBATE E USAR O ITEM, A FUNÇÃO É ENCERRADA PARA UM COMBATE MAIS RÁPIDO!
                    if self.combat == True:
                        return  
                elif self.hp >= self.maxHp and self.energy < self.maxEnergy:
                    print(strings['full_life '])
                    self.use_potion(0,potion_energy)
                    self.items.pop(option)
                    print(f"You cured {potion_energy} of energy ")
                    #AO ABRIR A MOCHILA EM COMBATE E USAR O ITEM, A FUNÇÃO É ENCERRADA PARA UM COMBATE MAIS RÁPIDO!
                    if self.combat == True:
                        return  
                else:
                    print(strings['full_life '])
                    print(strings['full_energy '])
            elif item.typer == 'utility':
                bag_golds = item.gold
                self.get_golds(bag_golds)
                print(f"You won {bag_golds} of golds")
                self.items.pop(option)
            elif item.typer == 'test':
                print('==============================================\n')
                print(strings['fail_use'])
                print('==============================================\n')
            else:
                print(strings['invalid'])    
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
    #FUNÇÃO BÁSICA PARA MOSTRAR AS INFORMAÇÕES BÁSICAS, DE QUAL CLASSE, A SUA ARMA
    def stats(self):
        weapons = {'sword': 'Sword',
        'lancer': 'Lancer',
        'meele': 'Meele',
        'sharptooth': 'Sharptooth',
        'archery': 'Archery'
        }
        #ESSA FUNÇÃO É PRA PEGAR O NOME DA ARMA DE ACORDO COM O STYLE DO HEROI E COMPARAR SE TEM NO DICIONARIO, CASO O CONTRARIO, RETORNE O FALSE
        weapon = weapons.get(self.style, False)
        while True:
            print(strings["divider"])
            print(f"You Name: {self.name}")
            print(f"You Class: {type(self).__name__}")
            #ESSA FUNÇÃO VAI RETONAR O NOME DA ARMA NO DICIONARIO E IRÁ COMPARAR SE O STYLE DO HEROI SÃO COMPATIVEL E PRINTAR A SUA.
            print(f"Your Weapon Style Type: {weapon if weapon else 'None'} or All")
            print(strings["divider"])
            input('Press any button to exit...')
            break
    def __str__(self):
        f = f'--------\nLife of {self.name}: {self.hp}💗 Damage of {self.name}: {self.damage}🛡️'
        return f
#====================A PARTIR DAQUI SERÁ FEITO AS CLASS DE HEROIS HERDADO DE MOB=====================
#CLASS DO WARRIOR(GUERREIRO)
class Warrior(Mob, Bag, Item):
    def __init__(self, name, hp = 100, maxHp = 100, energy = 130, maxEnergy = 130, damage = 0, kills = 0, weapon = 0, armor = 0, golds = 0,exp=0, level=0,up_level=30, x = 0, y = 0, style = '', items = [], equip_chest = [], equip_weapon = [], alive = True,special_attack = False, combat = False):
        super().__init__(name, hp = 150, maxHp = 150, energy = 130, maxEnergy = 130, damage = 0, kills = 0, weapon = 0, armor = 0, golds = 0,exp=0, level=0,up_level=30, x = 0, y = 0, style = 'sword', items = [], equip_chest = [], equip_weapon = [], alive = True,special_attack = False, combat = False)
        self.__dict__.update({
            "hp": hp,
            "maxHp": maxHp,
            "energy": energy,
            "maxEnergy": maxEnergy,
            "alive": alive,
            "damage": damage,
            "items": items,
            "equip_chest": equip_chest,
            "equip_weapon": equip_weapon,
            "weapon": weapon,
            "armor": armor,
            "combat": combat,
            "golds": golds,
            "exp": exp,
            "level": level,
            "up_level": up_level,
            "x": x,
            "y": y
        })
    #TODO HEROI TEM UM ATAQUE ESPECIAL
    def Special_Attack(self):
        if self.energy >= round(self.maxEnergy/3):
            self.special_attack = True
            self.energy_loss(round(self.maxEnergy/3))
            print(strings["divider"])
            print(strings['warrior_sp'])
            print("Damage +100 💪")
            print(strings["divider"])
            self.damage += 100
            if mob.name == "OVERPOWER":
                self.damage += 1000
        else:
            print(strings["divider"])
            print(strings['no_energy'])
            print(strings["divider"])
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
    def __init__(self, name, hp = 100, maxHp = 100, energy = 130, maxEnergy = 130, damage = 0, kills = 0, weapon = 0, armor = 0, golds = 0,exp=0, level=0,up_level=30, x = 0, y = 0, style = '', items = [], equip_chest = [], equip_weapon = [], alive = True,special_attack = False, combat = False):
        super().__init__(name, hp = 130, maxHp = 130, energy = 150, maxEnergy = 150, damage = 0, kills = 0, weapon = 0, armor = 0, golds = 0,exp=0, level=0,up_level=30, x = 0, y = 0, style = 'lancer', items = [], equip_chest = [], equip_weapon = [], alive = True,special_attack = False, combat = False)
        self.__dict__.update({
            "hp": hp,
            "maxHp": maxHp,
            "energy": energy,
            "maxEnergy": maxEnergy,
            "alive": alive,
            "damage": damage,
            "items": items,
            "equip_chest": equip_chest,
            "equip_weapon": equip_weapon,
            "weapon": weapon,
            "armor": armor,
            "combat": combat,
            "golds": golds,
            "exp": exp,
            "level": level,
            "up_level": up_level,
            "x": x,
            "y": y
        })
    def Special_Attack(self, target):
        if self.energy >= round(self.maxEnergy/3):
            self.special_attack = True
            self.energy_loss(round(self.maxEnergy/3))
            self.damage += 50
            print(strings["divider"])
            print(strings['lancer_sp'])
            print("Damage +50 💪")
            print(f"🗡️ Impaling on the enemy caused {self.damage+80} damage in {target.name}")
            print(strings["divider"])
            target.take_damage(self.damage+80)
        else:
            print(strings["divider"])
            print(strings['no_energy'])
            print(strings["divider"])
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
    def __init__(self, name, hp = 100, maxHp = 100, energy = 130, maxEnergy = 130, damage = 0, kills = 0, weapon = 0, armor = 0, golds = 0,exp=0, level=0,up_level=30, x = 0, y = 0, style = '', items = [], equip_chest = [], equip_weapon = [], alive = True,special_attack = False, combat = False):
        super().__init__(name, hp = 110, maxHp = 110, energy = 300, maxEnergy = 300, damage = 0, kills = 0, weapon = 0, armor = 0, golds = 0,exp=0, level=0,up_level=30, x = 0, y = 0, style = 'meele', items = [], equip_chest = [], equip_weapon = [], alive = True,special_attack = False, combat = False)
        self.__dict__.update({
            "hp": hp,
            "maxHp": maxHp,
            "energy": energy,
            "maxEnergy": maxEnergy,
            "alive": alive,
            "damage": damage,
            "items": items,
            "equip_chest": equip_chest,
            "equip_weapon": equip_weapon,
            "weapon": weapon,
            "armor": armor,
            "combat": combat,
            "golds": golds,
            "exp": exp,
            "level": level,
            "up_level": up_level,
            "x": x,
            "y": y
        })
    def Special_Attack(self):
        if self.energy >= round(self.maxEnergy/3):
            self.special_attack = True
            self.energy_loss(round(self.maxEnergy/3))
            print(strings["divider"])
            print(strings['monk_sp'])
            print("Damage +30 💪")
            print("Life +50 💗")
            print(strings["divider"])
            self.hp += 50
            self.damage += 30
            self.maxHp +=50
        else:
            print(strings["divider"])
            print(strings['no_energy'])
            print(strings["divider"])
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
class Dragontooth(Mob, Bag, Item):
    def __init__(self, name, hp = 100, maxHp = 100, energy = 130, maxEnergy = 130, damage = 0, kills = 0, weapon = 0, armor = 0, golds = 0,exp=0, level=0,up_level=30, x = 0, y = 0, style = '', items = [], equip_chest = [], equip_weapon = [], alive = True,special_attack = False, combat = False):
        super().__init__(name, hp = 160, maxHp = 160, energy = 200, maxEnergy = 200, damage = 0, kills = 0, weapon = 0, armor = 0, golds = 0,exp=0, level=0,up_level=30, x = 0, y = 0, style = 'sharptooth', items = [], equip_chest = [], equip_weapon = [], alive = True,special_attack = False, combat = False)
        self.__dict__.update({
            "hp": hp,
            "maxHp": maxHp,
            "energy": energy,
            "maxEnergy": maxEnergy,
            "alive": alive,
            "damage": damage,
            "items": items,
            "equip_chest": equip_chest,
            "equip_weapon": equip_weapon,
            "weapon": weapon,
            "armor": armor,
            "combat": combat,
            "golds": golds,
            "exp": exp,
            "level": level,
            "up_level": up_level,
            "x": x,
            "y": y
        })
    #TODO HEROI TEM UM ATAQUE ESPECIAL
    def Special_Attack(self):
        if self.energy >= round(self.maxEnergy/3):
            self.special_attack = True
            self.energy_loss(round(self.maxEnergy/3))
            Dragontooth_Warrior.alive = True
            print(strings["divider"])
            print(strings['dragontooth_sp'])
            print(strings["divider"])
        else:
            print(strings["divider"])
            print(strings['no_energy'])
            print(strings["divider"])
            pass
    #TODO HEROI TEM UMA FUNÇÃO PARA DESABILITAR O ATAQUE ESPECIAL DEPENDENDO DO SEU TIPO.
    def Disable_Special_Attack(self):
        if self.special_attack == True:
            Dragontooth_Warrior.alive = False
            Dragontooth_Warrior.hp = 50
            self.special_attack = False
    def Check_Warrior(self):
        if Dragontooth_Warrior.alive == True:
            return True
        else:
            return False

    def __str__(self):
        f = f'Dragontooth {self.name} - Life: {self.hp}/{self.maxHp}💗  Energy: {self.energy}/{self.maxEnergy}⚡ Damage: {self.damage}💪 Armor: {self.armor}🛡️'
        return f
class Dragontooth_Warrior():
    def __init__(self,name, hp = 50 ,maxHp = 50, alive = False, damage = 15):
       self.name = name
       self.hp = hp
       self.maxHp = maxHp
       self.alive = alive
       self.damage = damage
    def take_damage(self,damage):
        self.hp -= damage
        return self.hp
    def attack_mob(self,mob):
        print(strings["divider"])
        print(f"Attack of {self.name}")
        print(f"🗡️ Caused {self.damage} damage in {mob.name}")
        mob.hp -= self.damage
    def __str__(self):
        f = f'{self.name} - Life: {self.hp}/{self.maxHp}💗  Damage: {self.damage}💪'
        return f
#CLASS DA ARCHER(ARQUEIRA)
class Archer(Mob, Bag, Item):
    def __init__(self, name, hp = 100, maxHp = 100, energy = 130, maxEnergy = 130, damage = 0, kills = 0, weapon = 0, armor = 0, golds = 0,exp=0, level=0,up_level=30, x = 0, y = 0, style = '', items = [], equip_chest = [], equip_weapon = [], alive = True,special_attack = False, combat = False, arrows = 0):
        self.arrows = arrows
        super().__init__(name,hp = 100, maxHp = 100, energy = 100, maxEnergy = 100, damage = 0, kills = 0, weapon = 0, armor = 0, golds = 0,exp=0, level=0,up_level=30, x = 0, y = 0, style = 'archery', items = [], equip_chest = [], equip_weapon = [], alive = True,special_attack = False, combat = False)
        self.__dict__.update({
            "hp": hp,
            "maxHp": maxHp,
            "energy": energy,
            "maxEnergy": maxEnergy,
            "alive": alive,
            "damage": damage,
            "items": items,
            "equip_chest": equip_chest,
            "equip_weapon": equip_weapon,
            "weapon": weapon,
            "armor": armor,
            "combat": combat,
            "golds": golds,
            "exp": exp,
            "level": level,
            "up_level": up_level,
            "x": x,
            "y": y
        })
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
                print(strings["divider"])
                print(strings['archer_sp'])
                print(f"🗡️ Caused {self.damage *1.2} damage in {target.name}")
                print(f"🗡️ And again you caused {self.damage *1.2} damage in {target.name}")
                print(strings["divider"])
                target.take_damage(self.damage *1.2)
                target.take_damage(self.damage *1.2)
            else:
                print(strings["divider"])
                print(strings['fail_archer_sp'])
                print(strings["divider"])
        else:
            print(strings["divider"])
            print(strings['no_energy'])
            print(strings["divider"])

    def __str__(self):
        f = f'Archer {self.name} - Life: {self.hp}/{self.maxHp}💗  Energy: {self.energy}/{self.maxEnergy}⚡ Arrows: {self.arrows} 🏹 Damage: {self.damage}💪 Armor: {self.armor}🛡️'
        return f
#CLASS SEGREDA DO GALACTUS, PARA TESTE DE MOBS E FUNÇÃO COMBAT TODA EM SÍ
class Galactus(Mob, Bag, Item):
    def __init__(self,name, hp = 80 ,maxHp = 80, energy = 50,maxEnergy = 50,  alive = True, damage = 25, items = [],equip_chest = [], equip_weapon = [], weapon = 0, armor = 0,combat = False, golds = 0,exp=0, level=0,up_level=30):
        super().__init__(name, hp = 9999,maxHp = 9999, energy = 9999,maxEnergy = 9999,  alive = True, damage = 30, items = [],equip_chest = [], equip_weapon = [], weapon = 0, armor = 0,combat = False, golds = 0,exp=0, level=0,up_level=30)
    def Special_Attack(self,target):
        if self.energy >= 0:
            self.energy_loss(0)
            print(strings["divider"])
            print("Special Attack!! Cosmic explosion!!!!")
            print(f"🗡️ Caused {self.damage *999} damage in {target.name}")
            print(strings["divider"])
            target.take_damage(self.damage *999)
    def __str__(self):
        f = f'Life of Galactus: {self.hp}/{self.maxHp}💗 Energy of Galactus: {self.energy}/{self.maxEnergy}⚡ Damage of Galactus: {self.damage}🛡️'
        return f
#ESSA É A CLASS INIMIGO ONDE NÃO HERDA NADA PARA UMA DEFINIÇÃO MAIS FACIL DOS INIMIGOS.
#PEGA ALGUMAS FUNÇÕES COMO TOMAR DANO, O ATAQUE BÁSICO ALÉM DE OUTRAS
class Enemy():
    def __init__(self,name, hp = 100,maxHp = 100,  damage = 0, golds = 0,exp=0, level= 0,alive = True, items = []):
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
                print(strings['globin_1'])
                print(strings['globin_2'])
                print(strings['globin_3'])
                print(f"You lossed {random_gold} 🟡")
                if target.golds < 0:
                    target.golds = 0
            else:
                print(strings['globin_4'])
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
        print(strings['drop_exp'].format(self.name,self.exp))
        Hero.win_exps(self.exp)
    #FUNÇÃO DE DROP DE OURO DE FORMA DIRETA, JÁ QUE OS ÚNICOS A RECEBER OURO SERIA O HEROI.
    def drop_golds(self):
        print(strings['drop_golds'].format(self.name,self.golds))
        Hero.get_golds(self.golds)
    #FUNÇÃO BÁSICA DE TOMAR DANO, POR ENQUANTO SEM A DEFINIÇÃO DE ARMADURA NOS INIMIGOS.
    def take_damage(self,damage):
        self.hp -= damage
        return self.hp
    #MESMA FUNÇÃO DE ATAQUE BÁSICO DOS HEROIS.
    def Attack1_E(self,target):
        attack = randint(0,20)
        if (attack <=10 and attack > 0):
            print(strings["divider"])
            print(strings['miss_attack'].format(self.name, target.name))
            print(strings["divider"])
        elif (attack > 10 and attack < 18):
            damage = target.take_damage(self.damage)
            print(strings["divider"])
            print(strings['basic_attack'].format(self.name,damage,target.name))
            print(strings["divider"])
        else:
            damage = target.take_damage(self.damage*2)
            print(strings["divider"])
            print(strings['critical_attack'].format(self.name,damage,target.name))
            print(strings["divider"])
    def __str__(self):
        f = f'Life of {self.name}: {self.hp}💗 Damage: {self.damage}🛡️'
        return f
# =============A PARTIR DAQUI SERÁ MOSTRADO AS FUNÇÕES DOS JOGO============
#FUNÇÃO DE COMBATE ONDE RECEBE A MAIORIA DAS FUNÇÕES E É DEFINIDO DE ACORDO COM O HEROI ESCOLHIDO.
def Combat():
    Hero.set_combat(True)
    while True: 
        if Hero.hp > 0 and mob.hp > 0:
            Map.hour()
            print(strings["divider"])
            print("Enemy:", mob)
            print(strings["divider"])
            print(f"{Hero.name}:", Hero)
            if Dragontooth_Warrior.hp > 0:
                if (type(Hero).__name__) == 'Dragontooth' and Hero.special_attack == True and Hero.Check_Warrior() == True:
                    print(Dragontooth_Warrior) 
            else:
                Hero.Disable_Special_Attack()
            print(strings["divider"])
            print(strings['combat_menu_msg'])
            print("[1]",strings['combat_option1'])
            print("[2]",strings['combat_option2'].format(f'{bc.RED}{round(Hero.maxEnergy/3)}{bc.ENDC}{bc.BOLD}'))
            print("[3]",strings['combat_option3'])
            print("[4]",strings['combat_option4'])
            print(strings["divider"])
            option_attack = input(strings['choice']+ ": ")
            print('\n')
            #PRIMEIRO É UM IF SIMPLÊS DE ATAQUE DE AMBOS OS MOBS DE FORMA DE ROUND
            equipped_weapon = Hero.check_equip_style()
            if option_attack == '1':
                if equipped_weapon == 'unequipped':
                    continue
                #UM EXEMPLO A BAIXO ONDE SE A ESCOLHA FOR UMA ARQUEIRA, SEJA EXECUTADO A FUNÇÃO DE PERDER UMA FLECHA A CADA ATAQUE
                elif (type(Hero).__name__) == 'Archer':
                    #COM O RETORNO DADO, SENDO SWORD, ALL, LANCER E ETC, VAI DECIDIR QUAL ATAQUE
                    if equipped_weapon == 'all':
                        Hero.Attack1_E(mob)
                        print('\n')
                        if mob.hp > 0:
                            mob.Attack1_E(Hero)
                        else:
                            print(strings["divider"])
                            print(strings['mob_dead'])
                            print('=================================================\n\n')
                    elif equipped_weapon == 'archery':
                        if Hero.arrows > 0:
                            #FUNÇÃO DA PERDA DE FLECHAS.
                            Hero.use_arrow(1)
                            Hero.Attack1_E(mob)
                            print('\n')
                            if mob.hp > 0:
                                mob.Attack1_E(Hero)
                            else:
                                print(strings["divider"])
                                print(strings['mob_dead'])
                                print('=================================================\n\n')
                        #SE ELA NÃO TIVER MAIS FLECHAS, SERÁ INCAPAZ DE ATACAR.
                        else:
                            print(strings['enough_arrow'])
                            print('\n')
                elif (type(Hero).__name__) == 'Dragontooth' and Hero.Check_Warrior() == True:
                    attack_dragon = randint(1,2)
                    if attack_dragon == 1:
                        Dragontooth_Warrior.attack_mob(mob)
                        Hero.Attack1_E(mob)
                        print('\n')
                        if mob.hp > 0:
                            mob.Attack1_E(Hero)
                        else:
                            print(strings['mob_dead'])
                    else:
                        Dragontooth_Warrior.attack_mob(mob)
                        Hero.Attack1_E(mob)
                        print('\n')
                        if mob.hp > 0:
                            mob.Attack1_E(Dragontooth_Warrior)
                        else:
                            print(strings['mob_dead'])
                else:
                    Hero.Attack1_E(mob)
                    print('\n')
                    if mob.hp > 0:
                        mob.Attack1_E(Hero)
                    else:
                        print(strings['mob_dead'])
            #ONDE É EXECUTADO O ATAQUE ESPECIAL, HEROI NÃO TOMA DANO ENQUANTO ESTIVER USADO ATAQUE ESPECIAL
            elif option_attack == '2':
                if (type(Hero).__name__) == 'Archer':
                    if equipped_weapon == 'archery':
                            Hero.Special_Attack(mob)
                            print('\n')
                            if mob.hp > 0:
                                mob.Attack1_E(Hero)
                            else:
                                print(strings['mob_dead'])
                    else:
                        print(strings['archer_special_fail_weapon'])
                elif (type(Hero).__name__) == 'Galactus':               
                        Hero.Special_Attack(mob)
                elif Hero.special_attack == False:
                    if (type(Hero).__name__) == 'Monk':              
                        Hero.Special_Attack()
                    elif equipped_weapon in ['sword', 'lancer','sharptooth']:
                        if (type(Hero).__name__) == 'Lancer':               
                            Hero.Special_Attack(mob)
                        elif (type(Hero).__name__) == 'Warrior':              
                            Hero.Special_Attack()
                        elif (type(Hero).__name__) == 'Dragontooth':              
                            Hero.Special_Attack()
                    else:
                        print(strings['hero_sp_fail_weapon'])
                else:
                    print(strings['hero_sp_fail_use'])
            #FUNÇÃO DE ABRIR MOCHILA NO MEIO DO COMBATE, A MESMA QUE É USADA PRA ABRIR MOCHILA NORMALMENTE.
            elif option_attack == '3':
                Hero.openBag()
            #AQUI FOI FEITO UM SISTEMA DE FUGIR DE COMBATE, ONDE HÁ UMA POSSIBILIDADE DE FUGIR OU NÃO DEPENDENDO GASTANDO SUA ENERGIA
            elif option_attack == '4':
                print('\n')
                probability = randint(0,10)
                if probability >= 0 and probability <=5:
                    if Hero.energy >=5:
                        Hero.energy_loss(5)
                        print(strings['success_run'])
                        Hero.set_combat(False)
                        if (type(Hero).__name__) == 'Monk':
                            Hero.Disable_Special_Attack()
                        break
                    else:
                        print(strings['no_energy'])
                elif probability >= 6 and probability <=10:
                    if Hero.energy >= 10:
                        Hero.energy_loss(10)
                        mob.Attack1_E(Hero)
                        print(strings['fail_run'])
                        print(strings["divider"])
                    else:
                        print(strings['no_energy'])
                print('\n')
        #A FUNÇÃO DE COMBATE É UM LOOP, SEMPRE QUE É FEITO UMA AÇÃO ELE RODA, SE O MOB TIVER MENOS OU IGUAL A 0, SERÁ EXECUTADO A FUNÇÃO A BAIXO E DEFINARÁ TUDO
        elif mob.hp <= 0:
            print(f"{mob.name} is dead")
            #SOMA DE KILLS DO HEROI
            Hero.Kills()
            print(strings["divider"])
            #O DROP DE GOLD
            mob.drop_golds()
            #E O DROP DE EXPERIÊNCIA
            mob.drop_exp() 
            #E A DEFINIÇÃO DE FALSE AO SAIR DE COMBATE
            Hero.set_combat(False)
            #E ISSO AQUI PARA REVIVER O MOB E DEFINIR OUTRO ALEÁTORIO.
            mob.revive()
            #ESSA FUNÇÃO É EXECUTADO DE ACORDO COM O ESPECIAL, COMO O MONK, WARRIOR E LANCER, MUDAM OS ATRIBUTOS E FEITO UM DISABLE PRA DEVOLVER OS ATRIBUTOS GANHO EM COMBATE.
            if (type(Hero).__name__) == 'Monk' or (type(Hero).__name__) == 'Warrior' or (type(Hero).__name__) == 'Lancer' or (type(Hero).__name__) == 'Dragontooth':
                Hero.Disable_Special_Attack()
            #UM MEIO IMPROVISADO DE COLOCAR UM CONTADOR DE KILLS EM UM BOSS E SEUS CAMPANGAS PARA TERMINAR O DESAFIO, EM BREVE RESOLVEREI!!
            if Map.place == 'Donjon' and mob.name == 'Scorpion':
                Hero.scorpion_kills += 1
            if Map.place == 'Donjon' and mob.name == 'Scorpion King':
                Hero.scorpion_king_kills += 1
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
        print(strings["divider"])
        print("A Scorpion KING!! Get ready for the boss fight!!\n")
        Combat()
    #FUNÇÃO QUE FOI EXPLICADO SEMPRE QUE O MOB SPAWNADO FOR UM GLOBIN.
    elif mob.name == 'Globin Sneaky':
        print(strings["divider"])
        print(strings['globin_spawn'],"\n")
        mob.Still_Gold(Hero)
    else:
        print("\n\n")
        print(strings["divider"])
        print(strings['mob_spawn'].format(mob.name),"\n")
        Combat()
#AQUI É A FUNÇÃO QUE DEFINARÁ QUEM SERÁ O MOB QUE VOCÊ ENFRETARÁ DE MANEIRA ALEÁTORIO, SEMPRE MUDANDO AO EXECUTAR UMA AÇÃO FORA DE COMBATE.
def randomMob():
    random_gold = randint(0,15)
    random_exp = randint(5,30)
    random_gold_Dungeon = randint(5,30)
    random_exp_Dungeon = randint(15,45)
    probability = randint(1,16)
    # DEPENDENDO DE ONDE O HEROI ESTEJA, É SPAWNADO OUTROS MOBS.
    if Map.place == 'Ground':
        if probability >= 0 and probability <=1:
            mob = Enemy('Old Zombie,', 15,15, 7, random_gold, random_exp)
            mob.mob_level()
            return mob
        elif probability >= 2 and probability <=3:
            mob = Enemy('Zombie', 15,15,5, random_gold, random_exp)
            mob.mob_level()
            return mob
        elif probability >= 4 and probability <=5:
            mob = Enemy('Kid Zombie', 15,15, 5, random_gold, random_exp)
            mob.mob_level()
            return mob
        elif probability >= 6 and probability <=7:
            mob = Enemy('Wolfmen',20,20,8, random_gold, random_exp)
            mob.mob_level()
            return mob  
        elif probability >= 8 and probability <=10:
            mob = Enemy('Evil elfo',20,20,8, random_gold, random_exp)
            mob.mob_level()
            return mob
        elif probability >= 12 and probability <=15:
            mob = Enemy('Globin Sneaky', 10,10,3, random_gold, random_exp)
            mob.mob_level()
            return mob
        else:
            mob = Enemy('Globin Lancer', 10,10,3, random_gold, random_exp)
            mob.mob_level()
            return mob
    elif Map.place == 'Donjon':
            if probability >= 0 and probability <=7:
                mob = Enemy('Scorpion', 10,10,4, random_gold, random_exp)
                mob.mob_level()
                return mob
            elif probability >= 8 and probability <=13:
                mob = Enemy('Búfalo', 15,15,5, random_gold, random_exp)
                mob.mob_level()
                return mob
            else:
                mob = Enemy('Scorpion King', 400,400,55, 60, 120)
                mob.mob_level()
                return mob
    else:
        if probability >= 1 and probability <=2:
            mob = Enemy('Skeletion Warrior', 30,30,30, random_gold_Dungeon, random_exp_Dungeon)
            mob.mob_level()
            return mob
        elif probability >= 9 and probability <=9:
            mob = Enemy('Yeti', 50,50,25, random_gold_Dungeon, random_exp_Dungeon)
            mob.mob_level()
            return mob
        elif probability >= 10 and probability <=13:
            mob = Enemy('Rat', 10,10,5, random_gold_Dungeon, random_exp_Dungeon)
            mob.mob_level()
            return mob
        elif probability >= 14 and probability <=16:
            mob = Enemy('Spider', 20,20,15, random_gold_Dungeon, random_exp_Dungeon)
            mob.mob_level()
            return mob
        elif probability >= 3 and probability <=5:
            mob = Enemy('Cockroach', 10,10,1, random_gold_Dungeon, random_exp_Dungeon)
            mob.mob_level()
            return mob
        else:
            mob = Enemy('Globin Sneaky', 15,15,5, random_gold_Dungeon, random_exp_Dungeon)
            mob.mob_level()
            return mob       
#AQUI É A FUNÇÃO QUE DEFINARÁ QUAL SERÁ O ITEM DROPADO QUE VOCÊ ENCONTRARÁ DE MANEIRA ALEÁTORIO, SEMPRE MUDANDO AO EXECUTAR UMA AÇÃO FORA DE COMBATE.
def randomWeapon(map_place):
    with open('resources/items/items_aleatory.json', 'r') as f:
        items_data = json.load(f)
    items = [item for item_id, item in items_data[map_place].items()]
    probability = randint(0, 20)
    for item in items:
        if int(item['probability_min']) <= probability <= int(item['probability_max']):
            return Item(item['name'], item['typer'], item['style'], item['damage'],
                        item['armor'], item['life'], item['energy'], item['gold'])

#FUNÇÃO PRA DEFINIR SEU NOME E A ESCOLHA DE SEU HEROI, EXECUTADA AO INICIAR
def Choice_Hero():
    if Main_menu() == False:
        name = input(strings['choice_name']+ ": ")
        while True:
            print(strings['choice_hero']+ ": ")
            print("[1]",strings['choice_warrior'])
            print("[2]",strings['choice_lancer'])
            print("[3]",strings['choice_archer'])
            print("[4]",strings['choice_monk'])
            print("[5]",strings['choice_dragontooth'])
            option = input(strings['choice']+ ": ")
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
            elif option == '5':
                Hero = Dragontooth(name)
                print(f"You picked: {Hero}")
                return Hero
            elif option == '999':
                Hero = Galactus(name)
                print(f"You picked secret hero: {Hero}")
                return Hero
            else:
                print(strings['invalid'])
    else:
        Hero = Main_menu()
        return Hero
        
#ESSE AQUI É O MENU PRINCIPAL DO JOGO, DE COMEÇAR E CARRRREGAR.
def Main_menu():
    print('[1] '+ strings['main_menu_option1'])
    print('[2] '+ strings['main_menu_option2'])
    print(strings["divider"])
    option = input(strings['choice']+' ')
    if option == '1':
        return False
    elif option == '2':
        loaded_data = (load_game())
        if 'sword' in loaded_data:
            Hero = Warrior(*loaded_data)
            return Hero
        elif 'lancer' in loaded_data:
            Hero = Lancer(*loaded_data)
            return Hero
        elif 'meele' in loaded_data:
            Hero = Monk(*loaded_data)
            return Hero
        elif 'sharptooth' in loaded_data:
            Hero = Dragontooth(*loaded_data)
            print(Hero.items)
            return Hero
        elif 'archery' in loaded_data:
            Hero = Archer(*loaded_data)
            return Hero
        else:
            print("Não há save para carregar.")
    else:
        print(strings['invalid'])
#ESSA É A FUNÇÃO AO ABRIR O FERREIRO, UM LUGAR PARA COMPRAR OS ITENS COM O OURO GANHO.
def Blacksmith(self):
    with open("resources/items/items_blacksmith.json") as f:
        items = json.load(f)
    while True:
        print('[1]',strings['weapons'])
        print('[2]',strings['armors'])
        print('[3]',strings['potions'])
        print('[4]',strings['exit'])
        option = input(strings['want_buy_category'] + ' ')
        if option == '1':
            category_items = items['weapons']
        elif option == '2':
            category_items = items['armors']
        elif option == '3':
            category_items = items['potions']
        elif option == '4':
            break
        else:
            print(strings['invalid'])
        while True:
            print(strings['divider'])
            print(strings['welcome_blacksmith'])
            print(strings['divider'])
            print(strings['you_golds'].format(self.golds))
            print(strings['want_buy'])
            printed_types = set()
            for i, item in enumerate(category_items):
                if item['style'] not in printed_types:
                    printed_types.add(item['style'])
                    print(f"{bc.YELLOW}Tipo: {item['style']}{bc.ENDC}{bc.BOLD}")
                print(f"[{i + 1}] - {item['name']}(1un) - {item['gold']} Golds 🟡")
            print(bc.YELLOW)
            print('[{}] - Exit'.format(len(category_items) + 1))
            print(f'{bc.ENDC}{bc.BOLD}')
            option = input(strings['choice'])
            try:
                option = int(option)
                if option <= len(category_items):
                    Item_buy = Item(category_items[option - 1]['name'], category_items[option - 1]['typer'], category_items[option - 1]['style'], category_items[option - 1]['damage'], category_items[option - 1]['armor'], category_items[option - 1]['life'], category_items[option - 1]['energy'], category_items[option - 1]['gold'])
                    Hero.buyItem(Item_buy)
                elif option == len(category_items) + 1:
                    break
                else:
                    print(strings['invalid'])
            except ValueError:
                print(strings['invalid'])
#UM FERREIRO DO SUBMUNDO!! ESSE CARA VAI TENTAR PASSAR A PERNA EM VOCê DEVIDO TUA ESCASSEZ
def Salesman(self):
    with open("resources/items/items_salesman.json") as f:
        items = json.load(f)
    category_items = items['all']
    while True:
        print(items)
        print(strings["divider"])
        print(strings['welcome_salesman'])
        print(strings["divider"])
        print(strings['you_golds'].format(self.golds))
        print(strings['want_buy'])
        printed_types = set()
        for i, item in enumerate(category_items):
            if item['style'] not in printed_types:
                print("Tipo:", item['style'])
                printed_types.add(item['style'])
            print(f"[{i + 1}] - {item['name']}(1un) - {item['gold']} Golds 🟡")
        print(bc.YELLOW)
        print('[{}] - Exit'.format(len(category_items) + 1))
        print(f'{bc.ENDC}{bc.BOLD}')
        option = input(strings['choice'])
        try:
            option = int(option)
            if option <= len(category_items):
                Item_buy = Item(category_items[option - 1]['name'], category_items[option - 1]['typer'], category_items[option - 1]['style'], category_items[option - 1]['damage'], category_items[option - 1]['armor'], category_items[option - 1]['life'], category_items[option - 1]['energy'], category_items[option - 1]['gold'])
                Hero.buyItem(Item_buy)
            elif option == len(category_items) + 1:
                break
            else:
                print(strings['invalid'])
        except ValueError:
            print(strings['invalid'])
#FUNÇÃO PRA DEFINIR A LINGUAGEM ATRAVES DO BLOCO DE NOTAS!
def ChoiceLang():
    print("Choose game language!")
    print('[1] - PT-BR')
    print('[2] - EN-US')
    lang = input('Choice: ')
    if lang == '1':
        strings = read_language_file('pt')
        features(lang)
        return strings
    elif lang == '2':
        strings = read_language_file('en')
        features(lang)
        return strings
    else:
        print("???????????? NOP!")
#AQUI É A EXECUÇÃO DO JOGO.
if __name__ == "__main__":
    print(f'{bc.BOLD}')
    #DEFINIÇÃO DA LINGUAGEM DOS JOGOS PUXANDO A TRADUÇÃO ATRAVES DO BLOCO DE NOTA!
    strings = ChoiceLang()
    divider = "=" * 50
    strings["divider"] = divider
    print(strings["divider"])
    #DEFINI~ÇAO INICIAL DO MAPA
    Map = Map('Ground')
    #DEFINIR A DIVISORIAS DAS PALAVRAS USANDO O STRINGS
    print("\n\n\n")
    #A PRIMEIRA COISA QUE APARECERÁ AO INICIAR O JOGO.
    print(strings["divider"])
    print(strings["divider"])
    print(strings['welc'])
    print(strings["divider"])
    Hero = Choice_Hero()
    #INICIAÇÃO DO DRAGON GUERREIRO PARA O ESPECIAL DO DRAGONTOOTH
    Dragontooth_Warrior = Dragontooth_Warrior('Dragontooth Warrior')
    #DEFINIÇÃO DOS ITENS PARA COMPRA NO FERREIRO E A INICIAÇÃO.
    #O HEROI COMEÇA SEMPRE COM DOIS ITENS, UMA POÇÃO DE VIDA E ENERGIA.
    Hero.get_golds(10)
    # print(f'{bc.BOLD}{bc.RED}=================================================')
    # print("!!!!")
    # print(strings['start'])
    # print("!!!")
    # print(f'================================================={bc.ENDC}')

    while True:
        # try:
        #VERIFICAÇÃO PARA O JOGO RODAR, SE O HEROI MORRER EM COMBATE OU DE OUTRAS CAUSAS, É CAUSADO O GAMER OVER
        if Hero.hp > 0 and Hero.scorpion_king_kills == 0:  
            #AS DUAS FUNÇÕES DE DEFINIÇÃO DE MOB E ITENS ALEÁTORIOS.
            print(Map.place)
            itemAleatory = randomWeapon(Map.place)
            mob = randomMob()
            print(f'{bc.BOLD}{bc.CYAN}=================================================')
            print(Hero)
            print(strings['you_kills'].format(Hero.kills))
            print(strings['you_golds'].format(Hero.golds))
            print(strings['you_level'].format(Hero.level))
            if Map.place != 'Ground':
                print(strings['date_inviable'])
            else:
                print(strings['date_now'].format(Map.day,Map.mounth,Map.years,Map.hours,Map.minute))
            print(strings['your_location'].format(Map.place))
            if Map.hours >= 6 and Map.hours < 18 and Map.place == 'Ground':
                print(strings['it_day'])
            elif Map.place == 'Ground':
                print(strings['it_night'])
            elif Map.place != 'Ground':
                print(strings['it_inviable'])
            print(strings["divider"])
            print(strings['next_action'])
            print("[1]",strings['move'])
            print("[2]",strings['open_bag'])
            print("[3]",strings['sleep'])
            if Map.place == 'Ground':
                print("[4]",strings['blacksmith'])
            else:
                print("[4]",strings['salesman'])
            print("[5]",strings['stats'])
            if Map.place == 'Dungeon':
                print("[6]",strings['save'])
                print("[7]",strings['map'])
                print("[8]",strings['exit'])
            else:
                print("[6]",strings['save'])
                print("[7]",strings['exit'])
            print(strings["divider"])
            option = input(strings['choice']+ ": ")
            print(f'{bc.ENDC}{bc.BOLD}')
            if option == '1':
                if Hero.energy <=0:
                    print(strings["divider"])
                    print(strings['zero_energy'])
                    print(strings["divider"])
                else:
                    Hero.Move()
            elif option == '2':
                Hero.openBag()
            elif option == '3':
                Hero.sleep()
            elif option == '4':
                if Map.place == 'Ground':
                    Blacksmith(Hero)
                else:
                    Salesman(Hero)
            elif option == '5':
                Hero.stats()
            elif option == '6':
                save_game(Hero)
            elif option == '7':
                if Map.place == 'Ground':
                    break
                elif Map.place == 'Dungeon':
                    Map.show_map()
                else:
                    break
            elif option == '8':
                break
            else:
                print (strings['invalid'])
        elif Hero.hp<= 0:
            os.system('cls')
            print("GAME OVER!!")
            break 
        elif Hero.hp > 0 and Hero.scorpion_king_kills == 1: 
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
        # except:
        #     print("FAIL FAIL FAIL FAIL!!!")