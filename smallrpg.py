# small rpg battle script by sudo-asap
 # on github: https://github.com/sudo-asap/matrixocular
# created from an android phone

from random import choice

from random import randint

weapondamage = 0
weapondmg = weapondamage
playerattack = randint(1, 20) + randint(1, 20) + randint(1, 30) + weapondmg
playeratk = playerattack
skillweapondamage = 0
skillweapondmg = skillweapondamage
skillpoints = 0
skillpts = skillpoints
skillpointsmax = 4
skillptsmax = skillpointsmax
skilldamage = (randint(1, 20) + randint(1, 20) + randint(1, 30)) * (skillpts + 1) + skillweapondmg
skilldmg = skilldamage
playerhealthpoints = 1000
playerhp = playerhealthpoints
mobattack = randint(20, 100)
mobatk = mobattack
mobhealth = 150
mobhp = mobhealth
playermiss = randint(1,100)
defendpercent = .2
defend = round(mobatk*defendpercent)
dfnd = defend
playermisspercent = 7
playermissprcnt = playermisspercent
mobmisspercent = 5
mobmissprcnt = mobmisspercent

def playermobatk():
    global playeratk, weapondmg, mobatk
    playeratk, weapondmg = randint(1, 20) + randint(1, 20) + randint(1, 30) + weapondmg, 0
    mobatk = randint(20, 100)
    
def mobhpzeronewmob():
    global mob, mobhp, mobatk
    mob = choice(moblist)
    mobhp = 150
    mobatk = randint(20, 100)
    if mob[0] in ['A', 'E', 'I', 'O', 'U']:
        print("Player has encountered an " + str(mob))
    else:
        print("Player has encountered a " + str(mob))


equipment = "/equip"
equip = equipment

gamemode = "/gamemode", "on"

moblist = ["Dark Blaze", "Crondor", "Trickador", "Everclear", "Denozor", "Frankenstein", "Deadly Kin", "Olazapi"]
mob = choice(moblist)

if mob[0] in ['A', 'E', 'I', 'O', 'U']:
    print("Player has encountered an " + str(mob))
else:
    print("Player has encountered a " + str(mob))
print("player has", int(playerhp), "health")
playerhp = 1000
while playerhp > 0: 
    xx = str(input("x for attack, y for defend, z for \'skill\', \'/equip\' for equipment"))
    if xx in ['x', 'y', 'z', equip]:
        if xx == str('x'):
            miss = randint(1,100)
            if int(miss) > playermissprcnt:
                playermobatk()
                mobhp = mobhp - playeratk
                print("Player attacked " + str(mob), "for " + str(playeratk), "damage")
                
                playerhp = playerhp - mobatk
                print(str(mob), "attacked player for " + str(mobatk), "damage")
                print(mob, "has " + str(mobhp), "health")
                print("player has " + str(playerhp), "health")
                if mobhp <= 0:
                    mobhpzeronewmob()
            elif miss <= playermissprcnt:
                print('Player has missed')
                mobatk = randint(20, 100)
                print(str(mob), "attacked player for " + str(mobatk), "damage")
                playerhp = playerhp - mobatk
                print(mob, "has " + str(mobhp), "health")
                print("player has " + str(playerhp), "health")
                if mobhp <= 0:
                    mobhpzeronewmob()
        if xx == str('y'):
            if skillpts < skillptsmax:
                skillpts = skillpts + 1
                print("You have defended and gained a skill point")
                print("You now have " + str(skillpts), "\'skill\' points")
                dfnd = round(mobatk*defendpercent)
                mobatk = randint(20, 100)
                playerhp = playerhp - dfnd
                print(str(mob), "attacks player for " + str(dfnd) + ", a small damage")
                print(mob, "has " + str(mobhp), "health")
                print("player has", playerhp, "health")
            elif skillpts >= skillptsmax:
                print("Max \'skill\' points is " + str(skillptsmax) + ", " + "You are at max already")
                print(mob, "has " + str(mobhp), "health")
                print("player has", int(playerhp), "health")
        if xx == str('z'):
            if skillpts > 0:
                skilldmg, skillpts = (randint(1, 20) + randint(1, 20) + randint(1, 30)) * skillpts + skillweapondmg, 0
# debugging skilldmg
#               print("~", skilldmg)
                print("You attacked " + str(mob), "for " + str(skilldmg), "damage")
                mobhp = mobhp - skilldmg
                skillpts = 0
# debugging skilldmg
#               print("~", skilldmg)
                print(str(mob), "has " + str(mobhp), "health")
                print("You now have " + str(skillpts), "\'skill\' points")
                print("player has", int(playerhp), "health")
                if mobhp <= 0:
                    mobhpzeronewmob()
            elif skillpts == 0:
                print("You have " + str(skillpts), "\'skill\' points")
                print("Nothing happened")
                print("player has", int(playerhp), "health")
            else:
                print("\'skill\' points out of bounds")
                break
        if str(xx) == str(equip):
            playeratk, skilldmg = randint(1, 20) + randint(1, 20) + randint(1, 30) + weapondmg, (randint(1, 20) + randint(1, 20) + randint(1, 30)) * (skillpts + 1) + skillweapondmg
            weapondmg = weapondmg + 50
            skillweapondmg = skillweapondmg + 100
    else:
        print("typed something else other than x, y, z, /equip")
