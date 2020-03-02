# small rpg battle script by sudo-asap

from random import choice

from random import randint

weapondamage = 0
baseattack = randint(0, 3) + randint(0, 3) + randint(0, 4)
baseatk = baseattack
playerattack = randint(0, 3) + randint(0, 3) + randint(0, 4) + weapondamage
playeratk = playerattack
skillweapon = 0
skillwep = skillweapon
skillpoints = 0
skillpts = skillpoints
skillpointsmax = 4
skillptsmax = skillpointsmax
skilldamage = (randint(1, 3) + randint(1, 3) + randint(1, 4)) * skillpts
skilldmg = skilldamage

# skilldmg maths
# skilldmg = (skillpts * playeratk + skillwep) + (skillpts * 2)

moblist = ["Slimeball", "Dark Blaze", "Mud Life", "Crondor", "Pumpkin Head", "Lizard Boss"]
moblistb = ["Trickador", "Everclear", "Harry"]
mob = choice(moblist)
print("You have met an " + mob)

mobhealth = 45
mobhp = mobhealth

while mobhp > 0:
    xx = str(input("x for attack, y for defend, z for \'skill\' "))
    if xx in ['x', 'y', 'z']:
        if xx == str('x'):
            mobhp = mobhp - playeratk
            print("Player attacked " + mob, "for " + str(playeratk), "damage")
            playeratk = randint(0, 3) + randint(0, 3) + randint(0, 4) + weapondamage
            print(mob, "has " + str(mobhp), "health")
        if xx == str('y'):
            if skillpts < skillptsmax:
                skillpts = skillpts + 1
                print("You have defended and gained a skill point")
                mobhp = mobhp
                print("You now have " + skillpts, "\'skill\' points")
                print(mob, "has " + (str)mobhp, "health")
            elif skillpts == skillptsmax:
                print("You have defended")
                print("Max \'skill\' points is " + str(skillptsmax) + ", " + "You are at max")
                print(mob, "has " + str(mobhp), "health")
            else:
                print("\'skill\' points too high")
                break
        if xx == str('z'):
            if skillpts > 0:
                skilldmg, skillpts = (randint(0, 3) + randint(0, 3) + randint(0, 4)) * skillpts, 0
# debugging skilldmg
#               print("~", skilldmg)
                print("You attacked " + mob, "for " + str(skilldmg), "damage")
                mobhp = mobhp - skilldmg
# debugging skilldmg
#               print("~", skilldmg)
                print(mob, "has " + str(mobhp), "health")
                print("You now have " + str(skillpts), "\'skill\' points")
            elif skillpts == 0:
                print("Oops! You have " + str(skillpts), "\'skill\' points")
                print("Nothing happened")
    else:
        print("typed something else other than x, y, z")
        break
