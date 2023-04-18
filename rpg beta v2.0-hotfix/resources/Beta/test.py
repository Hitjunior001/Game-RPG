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