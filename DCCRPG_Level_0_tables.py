# -*- coding: utf-8 -*-

ABILITIES = ['Strength','Agility','Stamina','Personality','Intelligence','Luck']



#TABLE 1-1: ABILITY SCORE MODIFIERS

ABILITY_SCORE_MODIFIERS = {
'headers':['Ability Score', 'Modifier', 'Wizard Spells Known', 'Max Spell Level**'],
'table':[
['3','-3', 'No spellcasting possible', 'No spellcasting possible'],
['4','-2','-2 spells*','1'],
['5','-2','-2 spells*','1'],
['6','-1','-1 spell*','1'],
['7','-1','-1 spell*','1'],
['8','-1','No adjustment','2'],
['9','None','No adjustment','2'],
['10','None','No adjustment','3'],
['11','None','No adjustment','3'],
['12','None','No adjustment','4'],
['13','+1','No adjustment','4'],
['14','+1','+1 spell','5'],
['15','+1','+1 spell','5'],
['16','+2','+1 spell','6'],
['17','+2','+2 spells','6'],
['18','+3','+2 spells','7']
],
'stars':['* Minimum of 1 spell.','** Based on Intelligence for wizards and Personality for clerics.']
}


#TABLE 1-2: LUCK SCORE

LUCK_SCORE = {
'headers':['Roll', 'Birth Augur and Lucky Roll'],
'table':[
['1','Harsh winter: All attack rolls'],
['2','Taurus: Melee attack rolls'],
['3','Fortunate date: Missile fire attack rolls'],
['4','Raised by wolves: Unarmed attack rolls'],
['5','Conceived on horseback: Mounted attack rolls'],
['6','Born on the battlefield: Damage rolls'],
['7','Path of the bear: Melee damage rolls'],
['8','Hawkeye: Missile fire damage rolls'],
['9','Pack hunter: Attack and damage rolls for 0-level trained weapon'],
['10','Born under the loom: Skill checks (including thief skills)'],
['11','Fox’s cunning: Find/disable traps'],
['12','Four-leafed clover: Find secret doors'],
['13','Seventh son: Spell checks'],
['14','The raging storm: Spell damage'],
['15','Righteous heart: Turn unholy checks'],
['16','Survived the plague: Magical healing*'],
['17','Lucky sign: Saving throws'],
['18','Guardian angel: Savings throws to escape traps'],
['19','Survived a spider bite: Saving throws against poison'],
['20','Struck by lightning: Reflex saving throws'],
['21','Lived through famine: Fortitude saving throws'],
['22','Resisted temptation: Willpower saving throws'],
['23','Charmed house: Armor Class'],
['24','Speed of the cobra: Initiative'],
['25','Bountiful harvest: Hit points (applies at each level)'],
['26','Warrior’s arm: Critical hit tables**'],
['27','Unholy house: Corruption rolls'],
['28','The Broken Star: Fumbles**'],
['29','Birdsong: Number of languages'],
['30','Wild child: Speed (each +1 = +5’ speed)']
],
'stars':['* If a cleric, applies to all healing the cleric performs. If not a cleric, applies to all magical healing received from other sources.',
'** Luck normally affects critical hits and fumbles. On this result, the modifier is doubled for purposes of crits or fumbles.']
}



#TABLE 3-4: EQUIPMENT

EQUIPMENT = {
'resume':'A 0-level character gets one randomly determined item of equipment; roll 1d24 per character.',
'headers':['Roll*','Item','Cost'],
'table':[
['1','Backpack','2gp'],
['2','Candle','1cp'],
['3','Chain, 10’','30gp'],
['4','Chalk,','1piece','1cp'],
['5','Chest, empty','2gp'],
['6','Crowbar','2gp'],
['7','Flask, empty','3cp'],
['8','Flint & steel','15cp'],
['9','Grappling hook','1gp'],
['10','Hammer, small','5sp'],
['11','Holy symbol','25gp'],
['12','Holy water,','1vial**','25gp'],
['13','Iron spikes, each','1sp'],
['14','Lantern','10gp'],
['15','Mirror, hand-sized','10gp'],
['16','Oil,','1flask***','2sp'],
['17','Pole, 10-foot','15cp'],
['18','Rations, per day','5cp'],
['19','Rope, 50’','25cp'],
['20','Sack, large','12cp'],
['21','Sack, small','8cp'],
['22','Thieves’ tools','25gp'],
['23','Torch, each','1cp'],
['24','Waterskin','5sp'],
],
'stars':[
'* Roll 1d24 to randomly determine equipment for 0-level characters. Characters who purchase their equipment at a later level ignore this column.',
'** A half-pint vial of holy water inflicts 1d4 damage to any un-dead creature, as well as some demons and devils.',
'*** When ignited and thrown, oil causes 1d6 damage plus fire (DC 10 save vs. Reflex to put out or suffer additional 1d6 damage each round). One flask of oil burns for 6 hours in a lantern.'
]

}



#TABLE 1-3: OCCUPATION

OCCUPATION = {
'headers':['Roll',u'Occupation Trained Weapon†','Trade Goods'],
'table':[
['01','Alchemist','Staff','Oil, 1 flask'],
['02','Animal trainer','Club','Pony'],
['03-04','Armorer','Hammer (as club)','Iron helmet'],
['05','Astrologer','Dagger','Spyglass'],
['06-08','Blacksmith','Hammer (as club)','Steel tongs'],
['09-10','Caravan guard','Short sword','Linen, 1 yard'],
['11','Cobbler','Awl (as dagger)','Shoehorn'],
['12','Confidence artist','Dagger','Quality cloak'],
['13','Cooper','Crowbar (as club)','Barrel'],
['14-15','Cutpurse','Dagger','Small chest'],
['16-17','Ditch digger','Shovel (as staff)','Fine dirt, 1 lb.'],
['18-21','Dwarven blacksmith','Hammer (as club)','Mithril, 1 oz.'],
['22-23','Dwarven herder','Staff','Sow**'],
['24-27','Dwarven miner','Pick (as club)','Lantern'],
['28-31','Elven artisan','Staff','Clay, 1 lb.'],
['32-35','Elven forester','Staff','Herbs, 1 lb.'],
['36-37','Elven sage','Dagger','Parchment and quill pen'],
['38-47','Farmer*','Pitchfork (as spear)','Hen**'],
['48','Fortune-teller','Dagger','Tarot deck'],
['49','Gambler','Club','Dice'],
['50','Gongfarmer','Trowel (as dagger)','Sack of night soil'],
['51-52','Grave digger','Shovel (as staff)','Trowel'],
['53-54','Guild beggar','Sling','Crutches'],
['55-58','Halfling gypsy','Sling','Hex doll'],
['59-62','Halfling trader','Short sword 20 sp'],
['63-64','Halfling vagrant','Club','Begging bowl'],
['65','Healer','Club','Holy water, 1 vial'],
['66','Herbalist','Club','Herbs, 1 lb.'],
['67-69','Herder','Staff','Herding dog**'],
['70-72','Hunter','Shortbow','Deer pelt'],
['73','Indentured servant','Staff','Locket'],
['74','Jester','Dart','Silk clothes'],
['75','Jeweler','Dagger','Gem worth 20 gp'],
['76','Locksmith','Dagger','Fine tools'],
['77','Mercenary','Longsword','Hide armor'],
['78','Miller/baker','Club','Flour, 1 lb.'],
['79','Minstrel','Dagger','Ukulele'],
['80','Noble','Longsword','Gold ring worth 10 gp'],
['81','Orphan','Club','Rag doll'],
['82','Ostler','Staff','Bridle'],
['83','Outlaw','Short sword','Leather armor'],
['84','Scribe','Dart','Parchment, 10 sheets'],
['85','Shaman','Mace','Herbs, 1 lb.'],
['86','Slave','Club','Strange-looking rock'],
['87','Smuggler','Sling','Waterproof sack'],
['88-89','Soldier','Spear','Shield'],
['90-91','Squire','Longsword','Steel helmet'],
['92-93','Trapper','Sling','Badger pelt'],
['94','Urchin','Stick (as club)','Begging bowl'],
['95','Wainwright','Club','Pushcart***'],
['96','Weaver','Dagger','Fine suit of clothes'],
['97','Wizard’s apprentice','Dagger','Black grimoire'],
['98-100','Woodcutter','Handaxe','Bundle of wood'],
],
'stars':['† If a missile fire weapon (such as sling or dart), roll 1d6 to determine number of sling stones or darts.',
'* Roll 1d8 to determine farmer type: (1) potato, (2) wheat, (3) turnip, (4) corn, (5) rice, (6) parsnip, (7) radish, (8) rutabaga.',
'** Why did the chicken cross the hallway? To check for traps! In all seriousness, if the party includes more than one farmer or herder, randomly determine the second and subsequent farm animals for each duplicated profession with 1d6: (1) sheep, (2) goat, (3) cow, (4) duck, (5) goose, (6) mule.',
'*** Roll 1d6 to determine what’s in the cart: (1) tomatoes, (2) nothing, (3) straw, (4) your dead, (5) dirt, (6) rocks.']
}


#TABLE 3-1: WEAPONS

WEAPONS = {
'resume':'At 0 level you won’t have many weapons, but you might need some of these stats.',
'headers':['Weapon','Damage','Range','Cost in gp'],
'table':[
['Battleaxe*','1d8','–','7'],
['Blackjack','1d3***','–','3'],
['Club','1d4','–','3'],
['Crossbow*','1d6','80/160/240','30'],
['Dagger†','1d4','10/20/30**','3'],
['Dart','1d4','20/40/60**','5','sp'],
['Flail','1d6','–','6'],
['Handaxe','1d6','10/20/30**','4'],
['Javelin','1d6','30/60/90**','1'],
['Longbow*','1d6','70/140/210','40'],
['Longsword','1d8','–','10'],
['Mace','1d6','–','5'],
['Polearm*','1d10','–','7'],
['Shortbow*','1d6','50/100/150','25'],
['Short','sword','1d6','–','7'],
['Sling','1d4','40/80/160**','2'],
['Spear','1d8','–','3'],
['Staff','1d4','–','5','sp'],
['Two-handed','sword*','1d10','–','15'],
['Warhammer','1d6','–','5'],
],
'stars':['* Two-handed weapon. Characters using two-handed weapons suffer a -4 penalty to initiative checks.',
'** Strength damage bonus applies with this weapon at close range only. Strength penalties apply at all ranges.',
'*** Damage dealt is always subdual damage.',
'† Characters generally purchase normal straight-edged daggers, but cultists, cave-dwellers, evil priests, alien worshippers, and other bad guys carry curvy or ceremonial daggers known as athame, kris, or tumi.'
]
}


#TABLE 3-2: AMMUNITION

AMMUNITION = {
'headers':['Ammunition','Quantity','Cost in gp'],
'table':[
['Arrows','20','5'],
['Arrow,','silver-tipped','1','5'],
['Quarrels','30','10'],
['Sling','stones','30','1'],
]
}


"""
DUNGEON CRAWL CLASSICS CHARACTER RECORD SHEET
Name Title
Occupation Class Alignment Speed
AC Hit Points
Max: _____
Level XP
Equipment
Treasure
Weapons
Armor
Combat Basics
Initiative: _______
Action dice: _______
Attack: _______
Crit die: _______
Crit table: _______
Melee Attack Melee Damage
Missile Attack Missile Damage
Save
Will
Save
Fort
Save
Ref
Lucky Roll
Languages
Strength
Modifier: ______
Agility
Modifier: ______
Stamina
Modifier: ______
Personality
Modifier: ______
Intelligence
Modifier: ______
Luck
Modifier: ______
Notes
"""
