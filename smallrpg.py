# small rpg battle script by sudo-asap
 # on github: https://github.com/sudo-asap/matrixocular
# created from an android phone
# currently working version

from random import choice

from random import randint

weapondamage = 0
playerattack = randint(5,30) + randint(5,30) + weapondamage
playeratk = playerattack
skillweapondamage = 0
skillpoints = 0
skillpts = skillpoints
skillpointsmax = 4
skillptsmax = skillpointsmax
skilldamage = (randint(1,30) + randint(1,30) + randint(1,30)) * (skillpts + 1) + skillweapondamage
skilldmg = skilldamage
playerhealthpoints = 1000
playerhp = playerhealthpoints
# player hp is soft-capped
mobattack = randint(1,20) + randint(1,20) + randint(2,20)
mobatk = mobattack
mobhealth = 150
mobhp = mobhealth
defendpercent = .2
defendedattack = round(mobatk*defendpercent)
dfndatk = defendedattack
playermisspercent = 15
playermissprcnt = playermisspercent
mobmisspercent = 20
mobmissprcnt = mobmisspercent
miss = randint(1,100)
restartb = bool(1)

def playeratk_():
    global playeratk
    playeratk = randint(5,30) + randint(5,30) + randint(5,30) + weapondamage
    
def mobatkrand():
    global mobatk
    mobatk = randint(1,20) + randint(1,20) + randint(2,20)
    
def mobhpzeronewmob():
    if mob[0] in ['A', 'E', 'I', 'O', 'U']:
        print("Player has encountered an " + str(mob))
    else:
        print("Player has encountered a " + str(mob))
        
def moblistatkhp():
    global mob
    global mobhp
    global moblist
    mob = choice(moblist)
    mobhp = 150
    mobatk = randint(1,20) + randint(1,20) + randint(2,20)
    
def weapondamageincrease():
    global weapondamage, skillweapondamage
    weapondamage = randint(5,10)
    skillweapondamage = randint(1,20)
    
def skilldmgexpression():
    global skilldmg, skillpts
    skilldmg, skillpts = (randint(1,30) + randint(1,30) + randint(1,30)) * (skillpts + 1) + skillweapondamage, 0
    
def playerhp_():
    global playerhp
    playerhp = 1000


equip = "/equip"

gamemode = "/gamemode", "on"

moblist = ["Dark Beast", "Vampire", "Dark Gear", "Deranged Lunatic", "Randomizer", "Crondor", "Everclear",]
mob = choice(moblist)

if mob[0] in ['A', 'E', 'I', 'O', 'U']:
    print("Player has encountered an " + str(mob))
else:
    print("Player has encountered a " + str(mob))

print("Player has", int(playerhp), "health")
playerhp_()
print(mob, "has " + str(mobhp), "health")
while restartb == bool(1):
# debugging restartb
#    print("~" + restartb)
    if mobhp <= 0:
        moblistatkhp()
        mobhpzeronewmob()
    xyz = str(input("x for attack, y for defend, z for \'skill\', \'/equip\' for equipment"))
    if xyz in ['x', 'y', 'z', equip]:
        if xyz == 'x':
            if miss > playermissprcnt:
                playeratk_()
                mobhp = mobhp - playeratk
                print("Player attacks " + str(mob), "for " + str(playeratk), "damage")
                miss = randint(1, 100)
                if miss > mobmissprcnt:
                    mobatkrand()
                    print(str(mob), "attacks Player for " + str(mobatk), "damage")
                    playerhp = playerhp - mobatk
                    miss = randint(1, 100)
                elif miss <= mobmissprcnt:
                    print(str(mob), "has missed")
                    miss = randint(1, 100)
            elif miss <= playermissprcnt:
                print('Player has missed')
                miss = randint(1, 100)
                if miss > mobmissprcnt:
                    mobatkrand()
                    print(str(mob), "attacks Player for " + str(mobatk), "damage")
                    playerhp = playerhp - mobatk
                    miss = randint(1, 100)
                elif miss <= mobmissprcnt:
                    print(str(mob), "has missed")
                    miss = randint(1, 100)
        if xyz == 'y':
            if skillpts < skillptsmax:
                skillpts = skillpts + 1
                print("Player has defended and gained a skill point")
                print("Player now has " + str(skillpts), "\'skill\' points")
                dfndatk = round(mobatk*defendpercent)
                mobatkrand()
                playerhp = playerhp - dfndatk
                print(str(mob), "attacks Player for " + str(dfndatk) + ", a small damage")
            elif skillpts >= skillptsmax:
                print("Max \'skill\' points is " + str(skillptsmax) + ", " + "Player is at max")
                print("Nothing happened")
        if xyz == 'z':
            if skillpts > 0:
                skilldmgexpression()
# debugging skilldmg
#               print("~", skilldmg)
                print("Player attacks " + str(mob), "for " + str(skilldmg), "damage")
                mobhp = mobhp - skilldmg
# debugging skilldmg
#               print("~", skilldmg)
                print("Player now has " + str(skillpts), "\'skill\' points")
            elif skillpts == 0:
                print("Player has " + str(skillpts), "\'skill\' points")
                print("Nothing happened")
            else:
                print("\'skill\' points out of bounds")
                break
        if xyz == equip:
            weapondamageincrease()
            print("Player has equipped")
        print(mob, "has " + str(mobhp), "health")
        print("Player has " + str(playerhp), "health")
    else:
        print("typed something else other than x, y, z, equip")

    if playerhp < 1:
        print('Player died')
        restart = input('Restart? y/n')
        while restart != 'y' and restart != 'n':
            print('Typed something else other than y/n')
            restart = input('Restart? y/n')
        if restart == 'y':
            restartb = bool(1)
            print('Game restarts..')
            playerhp_()
            print("Player has", int(playerhp), "health")
            print(mob, "has " + str(mobhp), "health")
        else:
            print('Game ends')
            restartb = bool([])
