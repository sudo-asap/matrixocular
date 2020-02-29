# small rpg battle script by asap (a_s_a_p)

from random import choice

from random import randint

def function(skillet):
    skilldamage = randint(0, 3) + randint(0, 3) + randint(0, 4) * skillet

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
skilldamage = (randint(0, 3) + randint(0, 3) + randint(0, 4)) * skillpts
skilldmg = skilldamage

# (skillpoints * playerattack + skillwep) + (skillpoints * 2)

moblist = ["slimeball", "dark blaze", "mud life", "crondor", "pumpkin head", "lizard boss"]
mob = choice(moblist)
print("You have met an", mob)

mobhealth = 40
mobhp = mobhealth

while mobhp > 0:
    xx = str(input("x for attack, y for defend, z for \'skill\' "))
    if xx in ['x', 'y', 'z']:
        if xx == str('x'):
            mobhp = mobhp - playeratk
            print("Player attacked", mob, "for", playeratk, "damage")
            playeratk = randint(0, 3) + randint(0, 3) + randint(0, 4) + weapondamage
            print(mob, "has", mobhp, "health")
        if xx == str('y'):
            if skillpts < skillptsmax:
                skillpts = skillpts + 1
                print("You have defended and gained a skill point")
                print("You now have", skillpts, "\'skill\' points")
                print(mob, "has", mobhp, "health")
            elif skillpts == skillptsmax:
                print("You have defended")
                print("Max \'skill\' points is", str(skillptsmax) + ",", "You are at max")
                print(mob, "has", mobhp, "health")
            else:
                print("\'skill\' points too high")
                break
        if xx == str('z'):
            if skillpts > 0 and skillpts <= skillptsmax:
                print("You attacked", mob, "for", skilldmg, "damage with", skillpts, "\'skill\' points")
                mobhp = mobhp - skilldmg
                skilldmg, skillpts = (randint(0, 3) + randint(0, 3) + randint(0, 4)) * skillpts, 0
                print(mob, "has", mobhp, "health")
                print("You now have", skillpts, "\'skill\' points")
            elif skillpts == 0:
                print("Oops! You have", skillpts, "\'skill\' points")
                print("Nothing happened")
            else:
                print("\'skill\' points out of bounds")
                break
    else:
        print("typed something else other than x, y, z")
        
