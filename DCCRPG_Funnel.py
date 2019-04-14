# -*- coding: utf-8 -*-
import sys
print("The Python version is %s.%s.%s" % sys.version_info[:3])

from DCCRPG_Level_0_tables import ABILITIES, ABILITY_SCORE_MODIFIERS, LUCK_SCORE, EQUIPMENT, OCCUPATION, WEAPONS, AMMUNITION

tables = [ABILITY_SCORE_MODIFIERS, LUCK_SCORE, EQUIPMENT, OCCUPATION, WEAPONS, AMMUNITION]



for t in tables:
	print(repr(t['headers']))
	for key in t.keys():
		print(repr(key))
		a = t[key]
		atyp = type(a)
		#print(type(a))
		if 'str' in str(atyp):
			print(a)
		else:
			for i in a:
				ityp = type(i)
				print(ityp)
				if 'str' in str(ityp):
					print(i)
				else:
					#print(repr(i))
					print(len(i))

"""
Character creation in the DCC RPG follows these steps:
1. Roll ability scores.
2. Determine 0-level occupation.
3. Calculate saving throws and choose an alignment.
4. Determine randomly determined equipment.

All 0-level characters start with the following:
• 1d4 hit points, modified by Stamina
• 5d12 copper pieces
• -100 XP
• One randomly determined piece of equipment (see table 3-4)
• One randomly determined occupation (see table 1-3)
• Based on the occupation:
• Possession of and training in one weapon
• Possession of some trade goods
• A +0 modifier to attack rolls and all saving throws
As the character earns experience points, his XP total advances to 1. When his XP total reaches 1, he may choose a class.

"""
import random






def rollDices(num, faces):
	"""
	number of Dices,
	max facets
	"""
	sum = 0
	for d in range(num):
		#print(d)
		sum += random.randint(1,6)
	return sum


'''
Objects
'''



class Entity(object):
    '''
    base for all  creation in map
    '''
    def __init__(self, x=0, y=0, char=' ', solid=False):
        self.x = x
        self.y = y
        self.char = char
        self.solid = solid
        self.movex = 0
        self.movey = 0
        self.frame = 0
        """
        self.images = []
        for i in range(1,5):
            img = pygame.image.load(os.path.join('images','hero' + str(i) + '.png')).convert()
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images.append(img)
            self.image = self.images[0]
            self.rect  = self.image.get_rect()

		"""

class Item(Entity):
    '''
    base for all  creation in map
    '''
    def __init__(self, quality=0, usability=0):
        Entity.__init__(self, x=0, y=0, char=' ', solid=False)
        self.quality = quality
        self.usability = usability




class Actor(Entity):
    '''
    Spawn a player or monster or NPC that acts
    '''
    def __init__(self, age=0):
        Entity.__init__(self, x=0, y=0, char=' ', solid=False)
        self.age = age
        self.abilities = None
        """
        self.images = []
        for i in range(1,5):
            img = pygame.image.load(os.path.join('images','hero' + str(i) + '.png')).convert()
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images.append(img)
            self.image = self.images[0]
            self.rect  = self.image.get_rect()
        """
    def control(self,x,y):
        '''
        control player movement
        '''
        self.movex += x
        self.movey += y
        
		
    def _get_abilities(self):
        return "{0} by {1}".format(self.abilities, self.abilities)

    def _set_abilities(self, ab):
        self.abilities = ab

    entry = property(_get_abilities, _set_abilities)
	

def giveAbilities(entity):
	ab = {'%s'% a :rollDices(3,6)   for a in ABILITIES}
	print(repr(ab))
	entity._set_abilities(ab)


player01 = Actor()
	
giveAbilities(player01)

print(player01._get_abilities)

a = rollDices(3,6)
print(a)

#six ability scores. For character creation, roll 3d6 for each ability score listed on the character sheet, in the order of Strength, Agility, Stamina, Personality, Intelligence, and Luck.


entities = []
entities.append(player01)

for a in ABILITIES:
	print(a)
	
	
for attr in ['age', 'solid']:
    print(getattr(player01, attr))


"""
Then roll d30 on Table 1-2 to determine what
kind of roll your Luck score modifies.


former occupation provides
some set of skills


These skills
also include training in a rudimentary weapon of some kind. Roll
d% on table 1-3 to determine a character’s background. Unless noted
otherwise, a character is human.

play with a properly sized party (at least 15 PCs), and
you will quickly learn what “wealth by attrition” means and how it
applies to low-level play.


ALIGNMENT
In the beginning there was the Void, where the Old Ones
dreamed. In their dreams were Law and Chaos, inherent
forces of unity and entropy. Through endless opposition,
these forces of unity and entropy elected champions who became
gods, who in turn formed planes of existence that reflected their
principles. On one such plane resides your trivial existence, tiny next
to the vastness of Aéreth, even tinier next to the vastness of the cos-
mos. But you are connected back to the greater universe and the end-
less struggle by a fundamental choice: do you back the forces of Law
or the forces of Chaos?

Alignment is a choice of values. In its simplest form it determines
behavior. In higher forms, it determines allegiance to a cosmic force.
Characters choose an alignment at 0 level, and it determines their
options for the rest of their life.
Alignment functions on many levels, but there are two primary ex-
tremes: lawful and chaotic, with the balance of neutrality between. A
character chooses one of these three alignments at 0 level
"""
