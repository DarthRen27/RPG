from tkinter import *
from tkinter import ttk
import random
from copy import deepcopy
import os

class FileManager(object):
   def __init__(self, gameManager, GUIManager):
       self.file = ""
       self._gameManager = gameManager
       self._guiManager = GUIManager
                    
   def save(self, filename):
       if not os.path.exists("SaveFiles"):
           os.mkdir("SaveFiles")
       cwd = os.getcwd()
       file = r"\SaveFiles"
       filen = cwd+file+"\\"+filename+".txt"
       print(filen)
       save = open(filen, "w+")
       self.file = save
       self.saveCharacters()
       self.saveStory()
       self.saveMerchant()
       save.close()
       
   def saveCharacters(self):
       for charac in self._gameManager.currentCharacters:
           self.file.write(charac.name + "\n")
           self.file.write(str(charac.XP) + "\n")
           self.file.write(str(charac.Level) + "\n")
           self.file.write(str(charac.cid) + "\n")
           self.file.write(str(charac.health) + "\n")
           self.file.write(str(charac.armor) + "\n")
           self.file.write(str(charac.attackb) + "\n")
           self.file.write(charac.proficiency + "\n")
           self.file.write(charac.race + "\n")
           self.file.write(str(charac.damagedie) + "\n")
           self.file.write(str(charac.strength) + "\n")
           self.file.write(str(charac.dexterity) + "\n")
           self.file.write(str(charac.constitution) + "\n")
           self.file.write(str(charac.intelligence) + "\n")
           self.file.write(str(charac.wisdom) + "\n")
           self.file.write(str(charac.charisma) + "\n")
           self.file.write(charac.weapon.name + "\n")
           for spell in charac.spells:
               self.file.write(spell + ",")
           self.file.write("\n")
           self.file.write(charac.equipment.name + "\n")
           self.file.write(str(charac.player) + "\n")
           self.file.write(str(charac.numdie) + "\n")
           if charac.player == True:
               self.file.write(str(charac.money) + "\n")
               for i in charac.inventory:
                   self.file.write(i.name + ",")
               self.file.write("\n")        
           self.file.write("\n")
       
   def saveMerchant(self):
           self.file.write(str(self._gameManager.currentMerchant.id) + "\n")
           if self._gameManager.currentMerchant.unique == None:
               self.file.write("None\n")
           else: 
               self.file.write(self._gameManager.currentMerchant.unique.name + "\n")
           self.file.write(str(self._gameManager.currentMerchant.money) + "\n")
           self.file.write(self._gameManager.currentMerchant.location + "\n")
           self.file.write("\n")
       
   def saveStory(self):
       self.file.write(self._gameManager.currentlocation + "\n")
       self.file.write(str(self._gameManager.convoIndex) + "\n")
       self.file.write("\n")
       
   def load(self, filename):
       cwd = os.getcwd()
       file = r"\SaveFiles"
       filen = cwd+file+"\\"+filename
       load = open(filen, "r")
       self.file = load.readlines()
       self.loadCharacters()
       self.loadMerchant()
       self.loadStory()
       load.close()
       self._gameManager.newGame = 1
       self._gameManager.setup()
       
   def loadCharacters(self):
       Xp, level, ID, name, heal, arm, att, prof, ra, damd, stren, dex, con, inte, wis, cha, wea, spell, equip, play, num, mon, invent = int(self.file[1].strip()), int(self.file[2].strip()), int(self.file[3].strip()), self.file[0].strip(), int(self.file[4].strip()), int(self.file[5].strip()), int(self.file[6].strip()), self.file[7].strip(), self.file[8].strip(), int(self.file[9].strip()), int(self.file[10].strip()), int(self.file[11].strip()), int(self.file[12].strip()), int(self.file[13].strip()), int(self.file[14].strip()), int(self.file[15].strip()), self.file[16].strip(), self.file[17].strip(), self.file[18].strip(), bool(self.file[19].strip()), int(self.file[20].strip()), int(self.file[21].strip()), self.file[22].strip()
       if prof == "Magic":
           spell = spell.split(",")
           spell.remove("")
       else:
           spell = []
           spell.append("None")
       invent = invent.split(",")
       invent.remove("")
       player = Character(Xp, level, ID, name, heal, arm, att, prof, ra, damd, stren, dex, con, inte, wis, cha, wea, spell, equip, play, num, mon)
       self._gameManager.currentCharacters.append(player)  
       self._gameManager.currentCharacters[0].name = name
       self._gameManager.currentCharacters[0].proficiency = prof
       self._gameManager.currentCharacters[0].XP = Xp
       self._gameManager.currentCharacters[0].Level = level
       self._gameManager.currentCharacters[0].attackb = att
       self._gameManager.currentCharacters[0].equipment = self._gameManager.itemDict[equip]
       self._gameManager.currentCharacters[0].strength = stren
       self._gameManager.currentCharacters[0].dexterity = dex
       self._gameManager.currentCharacters[0].constitution = con
       self._gameManager.currentCharacters[0].wisdom = wis
       self._gameManager.currentCharacters[0].charisma = cha
       self._gameManager.currentCharacters[0].intelligence = inte
       self._gameManager.currentCharacters[0].weapon = self._gameManager.itemDict[wea]
       self._gameManager.currentCharacters[0].player = play
       self._gameManager.currentCharacters[0].health = heal
       self._gameManager.currentCharacters[0].cid = ID
       self._gameManager.currentCharacters[0].race = ra
       self._gameManager.currentCharacters[0].armor = arm
       self._gameManager.currentCharacters[0].damagedie = damd
       self._gameManager.currentCharacters[0].numdie = num
       self._gameManager.currentCharacters[0].money = mon
       self._gameManager.currentCharacters[0].setCharismaBonus
       self._gameManager.currentCharacters[0].setConstitutionBonus()
       self._gameManager.currentCharacters[0].setDexterityBonus()
       self._gameManager.currentCharacters[0].setIntelligenceBonus()
       self._gameManager.currentCharacters[0].setStrengthBonus()
       self._gameManager.currentCharacters[0].setWisdomBonus()
       for i in invent:
           self._gameManager.currentCharacters[0].inventory.append(deepcopy(self._gameManager.itemDict[i]))
       Xp, level, ID, name, heal, arm, att, prof, ra, damd, stren, dex, con, inte, wis, cha, wea, spell, equip, play, num = int(self.file[25].strip()), int(self.file[26].strip()), int(self.file[27].strip()), self.file[24].strip(), int(self.file[28].strip()), int(self.file[29].strip()), int(self.file[30].strip()), self.file[31].strip(), self.file[32].strip(), int(self.file[33].strip()), int(self.file[34].strip()), int(self.file[35].strip()), int(self.file[36].strip()), int(self.file[37].strip()), int(self.file[38].strip()), int(self.file[39].strip()), self.file[40].strip(), self.file[41].strip(), self.file[42].strip(), bool(self.file[43].strip()), int(self.file[44].strip())
       play = False
       if prof == "Magic":
           spell = spell.split(",")
           spell.remove("")
       else:
           spell = []
           spell.append("None")
       Alex = Character(Xp, level, ID, name, heal, arm, att, prof, ra, damd, stren, dex, con, inte, wis, cha, wea, spell, equip, play, num, 0)
       self._gameManager.currentCharacters.append(Alex)
       self._gameManager.currentCharacters[1].proficiency = prof
       self._gameManager.currentCharacters[1].name = name
       self._gameManager.currentCharacters[1].XP = Xp
       self._gameManager.currentCharacters[1].Level = level
       self._gameManager.currentCharacters[1].attackb = att
       self._gameManager.currentCharacters[1].equipment = self._gameManager.itemDict[equip]
       self._gameManager.currentCharacters[1].strength = stren
       self._gameManager.currentCharacters[1].dexterity = dex
       self._gameManager.currentCharacters[1].constitution = con
       self._gameManager.currentCharacters[1].wisdom = wis
       self._gameManager.currentCharacters[1].charisma = cha
       self._gameManager.currentCharacters[1].intelligence = inte
       self._gameManager.currentCharacters[1].weapon = self._gameManager.itemDict[wea]
       self._gameManager.currentCharacters[1].player = play
       self._gameManager.currentCharacters[1].health = heal
       self._gameManager.currentCharacters[1].cid = ID
       self._gameManager.currentCharacters[1].race = ra
       self._gameManager.currentCharacters[1].armor = arm
       self._gameManager.currentCharacters[1].damagedie = damd
       self._gameManager.currentCharacters[1].numdie = num
       self._gameManager.currentCharacters[1].setCharismaBonus
       self._gameManager.currentCharacters[1].setConstitutionBonus()
       self._gameManager.currentCharacters[1].setDexterityBonus()
       self._gameManager.currentCharacters[1].setIntelligenceBonus()
       self._gameManager.currentCharacters[1].setStrengthBonus()
       self._gameManager.currentCharacters[1].setWisdomBonus()
       Xp, level, ID, name, heal, arm, att, prof, ra, damd, stren, dex, con, inte, wis, cha, wea, spell, equip, play, num = int(self.file[47].strip()), int(self.file[48].strip()), int(self.file[49].strip()), self.file[46].strip(), int(self.file[50].strip()), int(self.file[51].strip()), int(self.file[52].strip()), self.file[53].strip(), self.file[54].strip(), int(self.file[55].strip()), int(self.file[56].strip()), int(self.file[57].strip()), int(self.file[58].strip()), int(self.file[59].strip()), int(self.file[60].strip()), int(self.file[61].strip()), self.file[62].strip(), self.file[63].strip(), self.file[64].strip(), bool(self.file[65].strip()), int(self.file[66].strip())
       play = False
       if prof == "Magic":
           spell = spell.split(",")
           spell.remove("")
       else:
           spell = []
           spell.append("None")
       Caswell = Character(Xp, level, ID, name, heal, arm, att, prof, ra, damd, stren, dex, con, inte, wis, cha, wea, spell, equip, play, num, 0)
       self._gameManager.currentCharacters.append(Caswell)
       self._gameManager.currentCharacters[2].proficiency = prof
       self._gameManager.currentCharacters[2].name = name
       self._gameManager.currentCharacters[2].XP = Xp
       self._gameManager.currentCharacters[2].Level = level
       self._gameManager.currentCharacters[2].attackb = att
       self._gameManager.currentCharacters[2].equipment = self._gameManager.itemDict[equip]
       self._gameManager.currentCharacters[2].strength = stren
       self._gameManager.currentCharacters[2].dexterity = dex
       self._gameManager.currentCharacters[2].constitution = con
       self._gameManager.currentCharacters[2].wisdom = wis
       self._gameManager.currentCharacters[2].charisma = cha
       self._gameManager.currentCharacters[2].intelligence = inte
       self._gameManager.currentCharacters[2].weapon = self._gameManager.itemDict[wea]
       self._gameManager.currentCharacters[2].player = play
       self._gameManager.currentCharacters[2].health = heal
       self._gameManager.currentCharacters[2].cid = ID
       self._gameManager.currentCharacters[2].race = ra
       self._gameManager.currentCharacters[2].armor = arm
       self._gameManager.currentCharacters[2].damagedie = damd
       self._gameManager.currentCharacters[2].numdie = num
       self._gameManager.currentCharacters[2].setCharismaBonus
       self._gameManager.currentCharacters[2].setConstitutionBonus()
       self._gameManager.currentCharacters[2].setDexterityBonus()
       self._gameManager.currentCharacters[2].setIntelligenceBonus()
       self._gameManager.currentCharacters[2].setStrengthBonus()
       self._gameManager.currentCharacters[2].setWisdomBonus()
       Xp, level, ID, name, heal, arm, att, prof, ra, damd, stren, dex, con, inte, wis, cha, wea, spell, equip, play, num = int(self.file[69].strip()), int(self.file[70].strip()), int(self.file[71].strip()), self.file[68].strip(), int(self.file[72].strip()), int(self.file[73].strip()), int(self.file[74].strip()), self.file[75].strip(), self.file[76].strip(), int(self.file[77].strip()), int(self.file[78].strip()), int(self.file[79].strip()), int(self.file[80].strip()), int(self.file[81].strip()), int(self.file[82].strip()), int(self.file[83].strip()), self.file[84].strip(), self.file[85].strip(), self.file[86].strip(), bool(self.file[87].strip()), int(self.file[88].strip())
       play = False
       if prof == "Magic":
           spell = spell.split(",")
           spell.remove("")
       else:
           spell = []
           spell.append("None")
       Ela = Character(Xp, level, ID, name, heal, arm, att, prof, ra, damd, stren, dex, con, inte, wis, cha, wea, spell, equip, play, num, 0)
       self._gameManager.currentCharacters.append(Ela)
       self._gameManager.currentCharacters[3].proficiency = prof
       self._gameManager.currentCharacters[3].name = name
       self._gameManager.currentCharacters[3].XP = Xp
       self._gameManager.currentCharacters[3].Level = level
       self._gameManager.currentCharacters[3].attackb = att
       self._gameManager.currentCharacters[3].equipment = self._gameManager.itemDict[equip]
       self._gameManager.currentCharacters[3].strength = stren
       self._gameManager.currentCharacters[3].dexterity = dex
       self._gameManager.currentCharacters[3].constitution = con
       self._gameManager.currentCharacters[3].wisdom = wis
       self._gameManager.currentCharacters[3].charisma = cha
       self._gameManager.currentCharacters[3].intelligence = inte
       self._gameManager.currentCharacters[3].weapon = self._gameManager.itemDict[wea]
       self._gameManager.currentCharacters[3].player = play
       self._gameManager.currentCharacters[3].health = heal
       self._gameManager.currentCharacters[3].cid = ID
       self._gameManager.currentCharacters[3].race = ra
       self._gameManager.currentCharacters[3].armor = arm
       self._gameManager.currentCharacters[3].damagedie = damd
       self._gameManager.currentCharacters[3].numdie = num
       self._gameManager.currentCharacters[3].setCharismaBonus
       self._gameManager.currentCharacters[3].setConstitutionBonus()
       self._gameManager.currentCharacters[3].setDexterityBonus()
       self._gameManager.currentCharacters[3].setIntelligenceBonus()
       self._gameManager.currentCharacters[3].setStrengthBonus()
       self._gameManager.currentCharacters[3].setWisdomBonus()
       
   def loadStory(self):
       self._gameManager.currentlocation = self.file[90].strip()
       self._gameManager.convoIndex = int(self.file[91].strip())
       
   def loadMerchant(self):
       self._gameManager.currentMerchant = self._gameManager.merchantDict[self.file[96].strip()]
       self._gameManager.currentMerchant.id = self.file[93].strip()
       self._gameManager.currentMerchant.unique = deepcopy(self._gameManager.itemDict[self.file[94].strip()])
       self._gameManager.currentMerchant.money = int(self.file[95].strip())

class GameManager(object):
    def __init__(self):
        self.newGame = 0
        self.mode = "Story"
        self.currentlocation = "Belkinus"
        self.currentMerchant = None
        self.storyPoints = {}
        self.choices = {"Release Vampire": False}
        #self.MainQuest = ""
        #self.SubQuest = ""
        self.LootItems = []
        self.StoryItems = []
        self.QuestRewardItems = {}
        self.currentCharacters = []
        self.itemDict = {}
        self.enemiesDict = {}
        self.weaponDamDict = {'sword':4, 'wand':0, 'bow':2, 'knife':3, 'hammer':5, "Elden Wand":6}
        #Number of sides a dice used for a spell has
        self.spellDamDict = {"Fireball":8, "Eldritch Blast":12, "Magic Missile":6, "Scorching Ray":8, "Blight":4}
        #Number of dice a spell rolls
        self.spellDieDict = {"Fireball":2, "Eldritch Blast":1, "Magic Missile":3, "Scorching Ray":2, "Blight":2}
        self.itemdescDict = {"leather armor": "A simple set of leather armor", "metal armor": "A simple set of metal armor", "Health Potion": "A potion that heals 2d4 wounds", "sword": "A simple sword made of metal", "wand": "A wooden stick used to channel magic", "Blood Born Wrappings": "A set of clothing made for Vampires and those they have \ntaken into their service", "knife": "A simple knife made out of metal", "hammer": "A simple warhammer", "Bones": "A bunch of bones, not sure why anyone would want this", "Goblin armor": "Armor made for goblins", "Necrorobes": "Robes worn by members of the Spine of Death", "High Necromancer Robes": "Robes worn by the highest ranking members of the Spine", "Greater Health Potion": "A potion that restores 3d6 wounds", "Damage Potion": "A potion that can be thrown and deal 2d4 damage", "Greater Damage Potion": "A potion that can be thrown and deal 3d6 damage", "Elden Wand": "Totally not the Elder Wand from Harry Potter. \nThis is completely legally distinct", "Elden Sword": "An ancient sword, the technique of it's construction \nhaving been lost to the ages", "Elden Armor": "An ancient set of armor, the techniques of it's construction \nhaving been lost to the ages", "Great Sword": "A very large sword", "Great Bow": "A bow with a much stronger string allowing more force to be put into the arrow", "Great Knife": "A knife almost the size of a sword", "bow": "A simple bow", "Stick of Stickyness": "A perfectly normal stick, nothing special to see here"}
        self.spelldescDict = {}
        self.conversationDict = {0: "The dark necromancer Xalan has raised an army of undead and is now assaulting our nation", 1: "By the powers vested in me by the king I am assigning the four of you to deal with this crisis", 2: "You will all be handsomely rewarded once this crisis has been resolved, until then you may take these 500 gold pieces to help you on your journey", 3: "This journey will be long and hard, but I have faith that you brave adventurers will be able to see it through", 4: "You have your mission, eliminate Xalan and restore peace to these lands"}
        self.optionsDict = {0: ["How is that my problem?", "We have to stop her!", "A wise move, can't lose soldiers", "Wait when did I start living in Ukraine?!"], 1: ["I'm getting paid right?", "I gladly accept this responsibility", "Oh good, freelance work", "I don't wanna be in Ukraine! Get me out of here!"], 2: ["Money, good", "Simply serving my nation is enough reward for me", "Suppose it's better than nothing", "Why do I have to fight Russia?! I'm not part of Ukraine!"], 3: ["It's your money you're wasting so who am I to judge", "Of course, we will complete this mission post haste", "Suppose I prefer this place to one swarming with undead", "This can't be happening, this can't be happening, this can't be happening"], 4: ["Yeah yeah yeah", "At once, on my honor", "*Sigh* Let's get this over with", "I don't wanna diiiiie"]}
        self.convoIndex = 0
        self.currentEnemies = []
        self.merchantDict = {}
        self.turn = 0
        self.lootNum = 0
        self.item = None
        Sword = Equipment(25, False, True, False, "sword", False, False, True, 0, 12)
        Wand = Equipment(15, False, True, False, "wand", False, False, True, 0, 0)
        Leather = Equipment(30, False, True, False, "leather armor", False, True, False, 10, 0)
        Metal = Equipment(50, False, True, False, "metal armor", False, True, False, 12, 0)
        Knife = Equipment(10, False, True, False, "knife", False, False, True, 0, 6)
        Hammer = Equipment(20, False, True, False, "hammer", False, False, True, 0, 4)
        Blood = Equipment(200, False, True, False, "Blood Born Wrappgins", False, True, False, 15, 0)
        Bones = Equipment(0, False, True, False, "Bones", False, True, False, 5, 0)
        Goblin = Equipment(10, False, True, False, "Goblin armor", False, True, False, 4, 0)
        Necro = Equipment(30, False, True, False, "Necrorobes", False, True, False, 4, 0)
        HighNecro = Equipment(5000, False, True, False, "High Necromancer Robes", False, True, False, 14, 0)
        HealthPot = Item(20, False, False, True, "Health Potion", True)
        GreatHeal = Item(50, False, False, True, "Greater Health Potion", True)
        DamagePot = Item(20, False, False, True, "Damage Potion", False)
        GreatDama = Item(50, False, False, True, "Greater Damage Potion", False)
        EldWa = Equipment(240, False, True, False, "Elden Wand", False, False, True, 0, 0)
        EldSw = Equipment(240, False, True, False, "Elden Sword", False, False, True, 0, 16)
        EldAr = Equipment(240, False, True, False, "Elden Armor", False, True, False, 16, 0)
        GreSw = Equipment(120, False, True, False, "Great Sword", False, False, True, 0, 14)
        Stick = Item(5, True, False, True, "Stick of Stickyness", False)
        GreKn = Equipment(100, False, True, False, "Great Knife", False, False, True, 0, 8)
        Bow = Equipment(50, False, True, False, "bow", False, False, True, 0, 5)
        GreBo = Equipment(120, False, True, False, "Great Bow", False, False, True, 0, 8)
        
        
        self.itemDict["sword"] = Sword
        self.itemDict["wand"] = Wand
        self.itemDict["leather armor"] = Leather
        self.itemDict["metal armor"] = Metal
        self.itemDict["knife"] = Knife
        self.itemDict["hammer"] = Hammer
        self.itemDict["Blood Born Wrappings"] = Blood
        self.itemDict["Bones"] = Bones
        self.itemDict["Goblin armor"] = Goblin
        self.itemDict["Necrorobes"] = Necro
        self.itemDict["High Necromancer Robes"] = HighNecro
        self.itemDict["Health Potion"] = HealthPot
        self.itemDict["Greater Health Potion"] = GreatHeal
        self.itemDict["Damage Potion"] = DamagePot
        self.itemDict["Greater Damage Potion"] = GreatDama
        self.itemDict["Elden Wand"] = EldWa
        self.itemDict["Elden Sword"] = EldSw
        self.itemDict["Elden Armor"] = EldAr
        self.itemDict["Great Sword"] = GreSw
        self.itemDict["Stick of Stickyness"] = Stick
        self.itemDict["bow"] = Bow
        self.itemDict["Great Knife"] = GreKn
        self.itemDict["Great Bow"] = GreBo
        self.itemDict["None"] = None
        
        BelkMerch = Merchant(0, 500, EldWa, "Belkinus")
        BelkMerch.inventory.append(deepcopy(self.itemDict["sword"]))
        BelkMerch.inventory.append(deepcopy(self.itemDict["knife"]))
        BelkMerch.inventory.append(deepcopy(self.itemDict["wand"]))
        BelkMerch.inventory.append(deepcopy(self.itemDict["hammer"]))
        BelkMerch.inventory.append(deepcopy(self.itemDict["Goblin armor"]))
        BelkMerch.inventory.append(deepcopy(self.itemDict["Health Potion"]))
        BelkMerch.inventory.append(deepcopy(self.itemDict["Health Potion"]))
        BelkMerch.inventory.append(deepcopy(self.itemDict["Greater Health Potion"]))
        BelkMerch.inventory.append(deepcopy(self.itemDict["Damage Potion"]))
        BelkMerch.inventory.append(deepcopy(self.itemDict["Damage Potion"]))
        BelkMerch.inventory.append(deepcopy(self.itemDict["Greater Damage Potion"]))
        BelkMerch.origInv.append(deepcopy(self.itemDict["sword"]))
        BelkMerch.origInv.append(deepcopy(self.itemDict["knife"]))
        BelkMerch.origInv.append(deepcopy(self.itemDict["wand"]))
        BelkMerch.origInv.append(deepcopy(self.itemDict["hammer"]))
        BelkMerch.origInv.append(deepcopy(self.itemDict["Goblin armor"]))
        BelkMerch.origInv.append(deepcopy(self.itemDict["Health Potion"]))
        BelkMerch.origInv.append(deepcopy(self.itemDict["Health Potion"]))
        BelkMerch.origInv.append(deepcopy(self.itemDict["Greater Health Potion"]))
        BelkMerch.origInv.append(deepcopy(self.itemDict["Damage Potion"]))
        BelkMerch.origInv.append(deepcopy(self.itemDict["Damage Potion"]))
        BelkMerch.origInv.append(deepcopy(self.itemDict["Greater Damage Potion"]))
        self.merchantDict["Belkinus"] = BelkMerch
        self.currentMerchant = BelkMerch
        CloveMerch = Merchant(1, 250, EldSw, "Cloveway")
        CloveMerch.inventory.append(deepcopy(self.itemDict["sword"]))
        CloveMerch.inventory.append(deepcopy(self.itemDict["knife"]))
        CloveMerch.inventory.append(deepcopy(self.itemDict["wand"]))
        CloveMerch.inventory.append(deepcopy(self.itemDict["hammer"]))
        CloveMerch.inventory.append(deepcopy(self.itemDict["bow"]))
        CloveMerch.inventory.append(deepcopy(self.itemDict["Health Potion"]))
        CloveMerch.inventory.append(deepcopy(self.itemDict["Health Potion"]))
        CloveMerch.inventory.append(deepcopy(self.itemDict["Greater Health Potion"]))
        CloveMerch.inventory.append(deepcopy(self.itemDict["Damage Potion"]))
        CloveMerch.inventory.append(deepcopy(self.itemDict["Damage Potion"]))
        CloveMerch.inventory.append(deepcopy(self.itemDict["Greater Damage Potion"]))
        CloveMerch.origInv.append(deepcopy(self.itemDict["sword"]))
        CloveMerch.origInv.append(deepcopy(self.itemDict["knife"]))
        CloveMerch.origInv.append(deepcopy(self.itemDict["wand"]))
        CloveMerch.origInv.append(deepcopy(self.itemDict["hammer"]))
        CloveMerch.origInv.append(deepcopy(self.itemDict["bow"]))
        CloveMerch.origInv.append(deepcopy(self.itemDict["Health Potion"]))
        CloveMerch.origInv.append(deepcopy(self.itemDict["Health Potion"]))
        CloveMerch.origInv.append(deepcopy(self.itemDict["Greater Health Potion"]))
        CloveMerch.origInv.append(deepcopy(self.itemDict["Damage Potion"]))
        CloveMerch.origInv.append(deepcopy(self.itemDict["Damage Potion"]))
        CloveMerch.origInv.append(deepcopy(self.itemDict["Greater Damage Potion"]))
        self.merchantDict["Cloveway"] = CloveMerch
        ChestMerch = Merchant(2, 250, EldAr, "Chester City")
        ChestMerch.inventory.append(deepcopy(self.itemDict["sword"]))
        ChestMerch.inventory.append(deepcopy(self.itemDict["knife"]))
        ChestMerch.inventory.append(deepcopy(self.itemDict["wand"]))
        ChestMerch.inventory.append(deepcopy(self.itemDict["hammer"]))
        ChestMerch.inventory.append(deepcopy(self.itemDict["Necrorobes"]))
        ChestMerch.inventory.append(deepcopy(self.itemDict["Health Potion"]))
        ChestMerch.inventory.append(deepcopy(self.itemDict["Health Potion"]))
        ChestMerch.inventory.append(deepcopy(self.itemDict["Greater Health Potion"]))
        ChestMerch.inventory.append(deepcopy(self.itemDict["Damage Potion"]))
        ChestMerch.inventory.append(deepcopy(self.itemDict["Damage Potion"]))
        ChestMerch.inventory.append(deepcopy(self.itemDict["Greater Damage Potion"]))
        ChestMerch.origInv.append(deepcopy(self.itemDict["sword"]))
        ChestMerch.origInv.append(deepcopy(self.itemDict["knife"]))
        ChestMerch.origInv.append(deepcopy(self.itemDict["wand"]))
        ChestMerch.origInv.append(deepcopy(self.itemDict["hammer"]))
        ChestMerch.origInv.append(deepcopy(self.itemDict["Necrorobes"]))
        ChestMerch.origInv.append(deepcopy(self.itemDict["Health Potion"]))
        ChestMerch.origInv.append(deepcopy(self.itemDict["Health Potion"]))
        ChestMerch.origInv.append(deepcopy(self.itemDict["Greater Health Potion"]))
        ChestMerch.origInv.append(deepcopy(self.itemDict["Damage Potion"]))
        ChestMerch.origInv.append(deepcopy(self.itemDict["Damage Potion"]))
        ChestMerch.origInv.append(deepcopy(self.itemDict["Greater Damage Potion"]))
        self.merchantDict["Chester City"] = ChestMerch
        Town1Merch = Merchant(3, 125, GreSw, "Town 1")
        Town1Merch.inventory.append(deepcopy(self.itemDict["sword"]))
        Town1Merch.inventory.append(deepcopy(self.itemDict["knife"]))
        Town1Merch.inventory.append(deepcopy(self.itemDict["wand"]))
        Town1Merch.inventory.append(deepcopy(self.itemDict["hammer"]))
        Town1Merch.inventory.append(deepcopy(self.itemDict["bow"]))
        Town1Merch.inventory.append(deepcopy(self.itemDict["Health Potion"]))
        Town1Merch.inventory.append(deepcopy(self.itemDict["Health Potion"]))
        Town1Merch.inventory.append(deepcopy(self.itemDict["Greater Health Potion"]))
        Town1Merch.inventory.append(deepcopy(self.itemDict["Damage Potion"]))
        Town1Merch.inventory.append(deepcopy(self.itemDict["Damage Potion"]))
        Town1Merch.inventory.append(deepcopy(self.itemDict["Greater Damage Potion"]))
        Town1Merch.origInv.append(deepcopy(self.itemDict["sword"]))
        Town1Merch.origInv.append(deepcopy(self.itemDict["knife"]))
        Town1Merch.origInv.append(deepcopy(self.itemDict["wand"]))
        Town1Merch.origInv.append(deepcopy(self.itemDict["hammer"]))
        Town1Merch.origInv.append(deepcopy(self.itemDict["bow"]))
        Town1Merch.origInv.append(deepcopy(self.itemDict["Health Potion"]))
        Town1Merch.origInv.append(deepcopy(self.itemDict["Health Potion"]))
        Town1Merch.origInv.append(deepcopy(self.itemDict["Greater Health Potion"]))
        Town1Merch.origInv.append(deepcopy(self.itemDict["Damage Potion"]))
        Town1Merch.origInv.append(deepcopy(self.itemDict["Damage Potion"]))
        Town1Merch.origInv.append(deepcopy(self.itemDict["Greater Damage Potion"]))
        self.merchantDict["Town 1"] = Town1Merch
        Town2Merch = Merchant(4, 125, GreSw, "Town 2")
        Town2Merch.inventory.append(deepcopy(self.itemDict["sword"]))
        Town2Merch.inventory.append(deepcopy(self.itemDict["knife"]))
        Town2Merch.inventory.append(deepcopy(self.itemDict["wand"]))
        Town2Merch.inventory.append(deepcopy(self.itemDict["hammer"]))
        Town2Merch.inventory.append(deepcopy(self.itemDict["Goblin armor"]))
        Town2Merch.inventory.append(deepcopy(self.itemDict["Health Potion"]))
        Town2Merch.inventory.append(deepcopy(self.itemDict["Health Potion"]))
        Town2Merch.inventory.append(deepcopy(self.itemDict["Damage Potion"]))
        Town2Merch.inventory.append(deepcopy(self.itemDict["Damage Potion"]))
        Town2Merch.inventory.append(deepcopy(self.itemDict["Greater Damage Potion"]))
        Town2Merch.origInv.append(deepcopy(self.itemDict["sword"]))
        Town2Merch.origInv.append(deepcopy(self.itemDict["knife"]))
        Town2Merch.origInv.append(deepcopy(self.itemDict["wand"]))
        Town2Merch.origInv.append(deepcopy(self.itemDict["hammer"]))
        Town2Merch.origInv.append(deepcopy(self.itemDict["Goblin armor"]))
        Town2Merch.origInv.append(deepcopy(self.itemDict["Health Potion"]))
        Town2Merch.origInv.append(deepcopy(self.itemDict["Health Potion"]))
        Town2Merch.origInv.append(deepcopy(self.itemDict["Damage Potion"]))
        Town2Merch.origInv.append(deepcopy(self.itemDict["Damage Potion"]))
        Town2Merch.origInv.append(deepcopy(self.itemDict["Greater Damage Potion"]))
        self.merchantDict["Town 2"] = Town2Merch
        Town3Merch = Merchant(4, 125, GreKn, "Town 3")
        Town3Merch.inventory.append(deepcopy(self.itemDict["sword"]))
        Town3Merch.inventory.append(deepcopy(self.itemDict["knife"]))
        Town3Merch.inventory.append(deepcopy(self.itemDict["wand"]))
        Town3Merch.inventory.append(deepcopy(self.itemDict["hammer"]))
        Town3Merch.inventory.append(deepcopy(self.itemDict["Health Potion"]))
        Town3Merch.inventory.append(deepcopy(self.itemDict["Health Potion"]))
        Town3Merch.inventory.append(deepcopy(self.itemDict["Greater Health Potion"]))
        Town3Merch.inventory.append(deepcopy(self.itemDict["Damage Potion"]))
        Town3Merch.inventory.append(deepcopy(self.itemDict["Damage Potion"]))
        Town3Merch.inventory.append(deepcopy(self.itemDict["Greater Damage Potion"]))
        Town3Merch.origInv.append(deepcopy(self.itemDict["sword"]))
        Town3Merch.origInv.append(deepcopy(self.itemDict["knife"]))
        Town3Merch.origInv.append(deepcopy(self.itemDict["wand"]))
        Town3Merch.origInv.append(deepcopy(self.itemDict["hammer"]))
        Town3Merch.origInv.append(deepcopy(self.itemDict["Health Potion"]))
        Town3Merch.origInv.append(deepcopy(self.itemDict["Health Potion"]))
        Town3Merch.origInv.append(deepcopy(self.itemDict["Greater Health Potion"]))
        Town3Merch.origInv.append(deepcopy(self.itemDict["Damage Potion"]))
        Town3Merch.origInv.append(deepcopy(self.itemDict["Damage Potion"]))
        Town3Merch.origInv.append(deepcopy(self.itemDict["Greater Damage Potion"]))
        self.merchantDict["Town 3"] = Town3Merch
        Town4Merch = Merchant(4, 125, GreKn, "Town 4")
        Town4Merch.inventory.append(deepcopy(self.itemDict["knife"]))
        Town4Merch.inventory.append(deepcopy(self.itemDict["wand"]))
        Town4Merch.inventory.append(deepcopy(self.itemDict["hammer"]))
        Town4Merch.inventory.append(deepcopy(self.itemDict["Goblin armor"]))
        Town4Merch.inventory.append(deepcopy(self.itemDict["Health Potion"]))
        Town4Merch.inventory.append(deepcopy(self.itemDict["Health Potion"]))
        Town4Merch.inventory.append(deepcopy(self.itemDict["Greater Health Potion"]))
        Town4Merch.inventory.append(deepcopy(self.itemDict["Damage Potion"]))
        Town4Merch.inventory.append(deepcopy(self.itemDict["Damage Potion"]))
        Town4Merch.inventory.append(deepcopy(self.itemDict["Greater Damage Potion"]))
        Town4Merch.origInv.append(deepcopy(self.itemDict["knife"]))
        Town4Merch.origInv.append(deepcopy(self.itemDict["wand"]))
        Town4Merch.origInv.append(deepcopy(self.itemDict["hammer"]))
        Town4Merch.origInv.append(deepcopy(self.itemDict["Goblin armor"]))
        Town4Merch.origInv.append(deepcopy(self.itemDict["Health Potion"]))
        Town4Merch.origInv.append(deepcopy(self.itemDict["Health Potion"]))
        Town4Merch.origInv.append(deepcopy(self.itemDict["Greater Health Potion"]))
        Town4Merch.origInv.append(deepcopy(self.itemDict["Damage Potion"]))
        Town4Merch.origInv.append(deepcopy(self.itemDict["Damage Potion"]))
        Town4Merch.origInv.append(deepcopy(self.itemDict["Greater Damage Potion"]))
        self.merchantDict["Town 4"] = Town4Merch
        Town5Merch = Merchant(4, 125, GreBo, "Town 5")
        Town5Merch.inventory.append(deepcopy(self.itemDict["sword"]))
        Town5Merch.inventory.append(deepcopy(self.itemDict["bow"]))
        Town5Merch.inventory.append(deepcopy(self.itemDict["wand"]))
        Town5Merch.inventory.append(deepcopy(self.itemDict["hammer"]))
        Town5Merch.inventory.append(deepcopy(self.itemDict["Goblin armor"]))
        Town5Merch.inventory.append(deepcopy(self.itemDict["Health Potion"]))
        Town5Merch.inventory.append(deepcopy(self.itemDict["Health Potion"]))
        Town5Merch.inventory.append(deepcopy(self.itemDict["Greater Health Potion"]))
        Town5Merch.inventory.append(deepcopy(self.itemDict["Damage Potion"]))
        Town5Merch.inventory.append(deepcopy(self.itemDict["Damage Potion"]))
        Town5Merch.inventory.append(deepcopy(self.itemDict["Greater Damage Potion"]))
        Town5Merch.origInv.append(deepcopy(self.itemDict["sword"]))
        Town5Merch.origInv.append(deepcopy(self.itemDict["bow"]))
        Town5Merch.origInv.append(deepcopy(self.itemDict["wand"]))
        Town5Merch.origInv.append(deepcopy(self.itemDict["hammer"]))
        Town5Merch.origInv.append(deepcopy(self.itemDict["Goblin armor"]))
        Town5Merch.origInv.append(deepcopy(self.itemDict["Health Potion"]))
        Town5Merch.origInv.append(deepcopy(self.itemDict["Health Potion"]))
        Town5Merch.origInv.append(deepcopy(self.itemDict["Greater Health Potion"]))
        Town5Merch.origInv.append(deepcopy(self.itemDict["Damage Potion"]))
        Town5Merch.origInv.append(deepcopy(self.itemDict["Damage Potion"]))
        Town5Merch.origInv.append(deepcopy(self.itemDict["Greater Damage Potion"]))
        self.merchantDict["Town 5"] = Town5Merch
        Town6Merch = Merchant(4, 125, GreBo, "Town 6")
        Town6Merch.inventory.append(deepcopy(self.itemDict["sword"]))
        Town6Merch.inventory.append(deepcopy(self.itemDict["knife"]))
        Town6Merch.inventory.append(deepcopy(self.itemDict["wand"]))
        Town6Merch.inventory.append(deepcopy(self.itemDict["bow"]))
        Town6Merch.inventory.append(deepcopy(self.itemDict["Goblin armor"]))
        Town6Merch.inventory.append(deepcopy(self.itemDict["Health Potion"]))
        Town6Merch.inventory.append(deepcopy(self.itemDict["Health Potion"]))
        Town6Merch.inventory.append(deepcopy(self.itemDict["Greater Health Potion"]))
        Town6Merch.inventory.append(deepcopy(self.itemDict["Damage Potion"]))
        Town6Merch.inventory.append(deepcopy(self.itemDict["Damage Potion"]))
        Town6Merch.inventory.append(deepcopy(self.itemDict["Greater Damage Potion"]))
        Town6Merch.origInv.append(deepcopy(self.itemDict["sword"]))
        Town6Merch.origInv.append(deepcopy(self.itemDict["knife"]))
        Town6Merch.origInv.append(deepcopy(self.itemDict["wand"]))
        Town6Merch.origInv.append(deepcopy(self.itemDict["bow"]))
        Town6Merch.origInv.append(deepcopy(self.itemDict["Goblin armor"]))
        Town6Merch.origInv.append(deepcopy(self.itemDict["Health Potion"]))
        Town6Merch.origInv.append(deepcopy(self.itemDict["Health Potion"]))
        Town6Merch.origInv.append(deepcopy(self.itemDict["Greater Health Potion"]))
        Town6Merch.origInv.append(deepcopy(self.itemDict["Damage Potion"]))
        Town6Merch.origInv.append(deepcopy(self.itemDict["Damage Potion"]))
        Town6Merch.origInv.append(deepcopy(self.itemDict["Greater Damage Potion"]))
        self.merchantDict["Town 6"] = Town6Merch
        JunctMerch = Merchant(4, 75, Stick, "Junction 1")
        JunctMerch.inventory.append(deepcopy(self.itemDict["Health Potion"]))
        JunctMerch.inventory.append(deepcopy(self.itemDict["Health Potion"]))
        JunctMerch.inventory.append(deepcopy(self.itemDict["Greater Health Potion"]))
        JunctMerch.inventory.append(deepcopy(self.itemDict["Damage Potion"]))
        JunctMerch.inventory.append(deepcopy(self.itemDict["Damage Potion"]))
        JunctMerch.inventory.append(deepcopy(self.itemDict["Greater Damage Potion"]))
        JunctMerch.inventory.append(deepcopy(self.itemDict["Health Potion"]))
        JunctMerch.inventory.append(deepcopy(self.itemDict["Damage Potion"]))
        JunctMerch.inventory.append(deepcopy(self.itemDict["Greater Health Potion"]))
        JunctMerch.inventory.append(deepcopy(self.itemDict["Greater Damage Potion"]))
        JunctMerch.origInv.append(deepcopy(self.itemDict["Health Potion"]))
        JunctMerch.origInv.append(deepcopy(self.itemDict["Health Potion"]))
        JunctMerch.origInv.append(deepcopy(self.itemDict["Greater Health Potion"]))
        JunctMerch.origInv.append(deepcopy(self.itemDict["Damage Potion"]))
        JunctMerch.origInv.append(deepcopy(self.itemDict["Damage Potion"]))
        JunctMerch.origInv.append(deepcopy(self.itemDict["Greater Damage Potion"]))
        JunctMerch.origInv.append(deepcopy(self.itemDict["Health Potion"]))
        JunctMerch.origInv.append(deepcopy(self.itemDict["Damage Potion"]))
        JunctMerch.origInv.append(deepcopy(self.itemDict["Greater Health Potion"]))
        JunctMerch.origInv.append(deepcopy(self.itemDict["Greater Damage Potion"]))
        self.merchantDict["Junction 1"] = JunctMerch
        
    def setup(self):
        setlist = []
        if self.newGame == 0:
            player = Character(0, 1, 1, "", 0, 0, 2, "", "Human", 0, 8, 8, 8, 8, 8, 8, "", [], "", True, 0, 0)
            Alex = Character(0, 1, 2, "Alex", 0, 0, 2, "", "Human", 0, 8, 8, 8, 8, 8, 8, "", [], "", False, 0, 0)
            Caswell = Character(0, 1, 3, "Caswell", 10, 10, 2, "Magic", "Human", 0, 10, 14, 14, 14, 14, 12, deepcopy(self.itemDict["wand"]), ["Fireball", "Magic Missile", "Eldritch Blast"], deepcopy(self.itemDict["leather armor"]), False, 0, 0)
            Ela = Character(0, 1, 4, "Ela", 12, 10, 2, "Martial", "Human", 8, 15, 14, 15, 10, 10, 12, deepcopy(self.itemDict["sword"]), ["None"], deepcopy(self.itemDict["leather armor"]), False, 1, 0)
            self.currentCharacters.append(player)
            self.currentCharacters.append(Alex)
            self.currentCharacters.append(Caswell)
            self.currentCharacters.append(Ela)
            setlist.append(Caswell)
            setlist.append(Ela)
            self.merchantDict["Belkinus"].inventory.append(self.itemDict["Elden Wand"])
            self.merchantDict["Cloveway"].inventory.append(self.itemDict["Elden Sword"])
            self.merchantDict["Chester City"].inventory.append(self.itemDict["Elden Armor"])
            self.merchantDict["Junction 1"].inventory.append(self.itemDict["Stick of Stickyness"])
            self.merchantDict["Town 6"].inventory.append(self.itemDict["Great Bow"])
            self.merchantDict["Town 5"].inventory.append(self.itemDict["Great Bow"])
            self.merchantDict["Town 4"].inventory.append(self.itemDict["Great Knife"])
            self.merchantDict["Town 3"].inventory.append(self.itemDict["Great Knife"])
            self.merchantDict["Town 2"].inventory.append(self.itemDict["Great Sword"])
            self.merchantDict["Town 1"].inventory.append(self.itemDict["Great Sword"])
        else:
            if self.currentlocation == "Belkinus":
                self.merchantDict["Cloveway"].inventory.append(self.itemDict["Elden Sword"])
                self.merchantDict["Chester City"].inventory.append(self.itemDict["Elden Armor"])
                self.merchantDict["Junction 1"].inventory.append(self.itemDict["Stick of Stickyness"])
                self.merchantDict["Town 6"].inventory.append(self.itemDict["Great Bow"])
                self.merchantDict["Town 5"].inventory.append(self.itemDict["Great Bow"])
                self.merchantDict["Town 4"].inventory.append(self.itemDict["Great Knife"])
                self.merchantDict["Town 3"].inventory.append(self.itemDict["Great Knife"])
                self.merchantDict["Town 2"].inventory.append(self.itemDict["Great Sword"])
                self.merchantDict["Town 1"].inventory.append(self.itemDict["Great Sword"])
            elif self.currentlocation == "Cloveway":
                self.merchantDict["Belkinus"].inventory.append(self.itemDict["Elden Wand"])
                self.merchantDict["Chester City"].inventory.append(self.itemDict["Elden Armor"])
                self.merchantDict["Junction 1"].inventory.append(self.itemDict["Stick of Stickyness"])
                self.merchantDict["Town 6"].inventory.append(self.itemDict["Great Bow"])
                self.merchantDict["Town 5"].inventory.append(self.itemDict["Great Bow"])
                self.merchantDict["Town 4"].inventory.append(self.itemDict["Great Knife"])
                self.merchantDict["Town 3"].inventory.append(self.itemDict["Great Knife"])
                self.merchantDict["Town 2"].inventory.append(self.itemDict["Great Sword"])
                self.merchantDict["Town 1"].inventory.append(self.itemDict["Great Sword"])
            elif self.currentlocation == "Chester City":
                self.merchantDict["Belkinus"].inventory.append(self.itemDict["Elden Wand"])
                self.merchantDict["Cloveway"].inventory.append(self.itemDict["Elden Sword"])
                self.merchantDict["Junction 1"].inventory.append(self.itemDict["Stick of Stickyness"])
                self.merchantDict["Town 6"].inventory.append(self.itemDict["Great Bow"])
                self.merchantDict["Town 5"].inventory.append(self.itemDict["Great Bow"])
                self.merchantDict["Town 4"].inventory.append(self.itemDict["Great Knife"])
                self.merchantDict["Town 3"].inventory.append(self.itemDict["Great Knife"])
                self.merchantDict["Town 2"].inventory.append(self.itemDict["Great Sword"])
                self.merchantDict["Town 1"].inventory.append(self.itemDict["Great Sword"])
            elif self.currentlocation == "Junction 1":
                self.merchantDict["Belkinus"].inventory.append(self.itemDict["Elden Wand"])
                self.merchantDict["Cloveway"].inventory.append(self.itemDict["Elden Sword"])
                self.merchantDict["Chester City"].inventory.append(self.itemDict["Elden Armor"])
                self.merchantDict["Town 6"].inventory.append(self.itemDict["Great Bow"])
                self.merchantDict["Town 5"].inventory.append(self.itemDict["Great Bow"])
                self.merchantDict["Town 4"].inventory.append(self.itemDict["Great Knife"])
                self.merchantDict["Town 3"].inventory.append(self.itemDict["Great Knife"])
                self.merchantDict["Town 2"].inventory.append(self.itemDict["Great Sword"])
                self.merchantDict["Town 1"].inventory.append(self.itemDict["Great Sword"])
            elif self.currentlocation == "Town 6":
                self.merchantDict["Belkinus"].inventory.append(self.itemDict["Elden Wand"])
                self.merchantDict["Cloveway"].inventory.append(self.itemDict["Elden Sword"])
                self.merchantDict["Chester City"].inventory.append(self.itemDict["Elden Armor"])
                self.merchantDict["Junction 1"].inventory.append(self.itemDict["Stick of Stickyness"])
                self.merchantDict["Town 5"].inventory.append(self.itemDict["Great Bow"])
                self.merchantDict["Town 4"].inventory.append(self.itemDict["Great Knife"])
                self.merchantDict["Town 3"].inventory.append(self.itemDict["Great Knife"])
                self.merchantDict["Town 2"].inventory.append(self.itemDict["Great Sword"])
                self.merchantDict["Town 1"].inventory.append(self.itemDict["Great Sword"])
            elif self.currentlocation == "Town 5":
                self.merchantDict["Belkinus"].inventory.append(self.itemDict["Elden Wand"])
                self.merchantDict["Cloveway"].inventory.append(self.itemDict["Elden Sword"])
                self.merchantDict["Chester City"].inventory.append(self.itemDict["Elden Armor"])
                self.merchantDict["Junction 1"].inventory.append(self.itemDict["Stick of Stickyness"])
                self.merchantDict["Town 6"].inventory.append(self.itemDict["Great Bow"])
                self.merchantDict["Town 4"].inventory.append(self.itemDict["Great Knife"])
                self.merchantDict["Town 3"].inventory.append(self.itemDict["Great Knife"])
                self.merchantDict["Town 2"].inventory.append(self.itemDict["Great Sword"])
                self.merchantDict["Town 1"].inventory.append(self.itemDict["Great Sword"])
            elif self.currentlocation == "Town 4":
                self.merchantDict["Belkinus"].inventory.append(self.itemDict["Elden Wand"])
                self.merchantDict["Cloveway"].inventory.append(self.itemDict["Elden Sword"])
                self.merchantDict["Chester City"].inventory.append(self.itemDict["Elden Armor"])
                self.merchantDict["Junction 1"].inventory.append(self.itemDict["Stick of Stickyness"])
                self.merchantDict["Town 5"].inventory.append(self.itemDict["Great Bow"])
                self.merchantDict["Town 6"].inventory.append(self.itemDict["Great Bow"])
                self.merchantDict["Town 3"].inventory.append(self.itemDict["Great Knife"])
                self.merchantDict["Town 2"].inventory.append(self.itemDict["Great Sword"])
                self.merchantDict["Town 1"].inventory.append(self.itemDict["Great Sword"])
            elif self.currentlocation == "Town 3":
                self.merchantDict["Belkinus"].inventory.append(self.itemDict["Elden Wand"])
                self.merchantDict["Cloveway"].inventory.append(self.itemDict["Elden Sword"])
                self.merchantDict["Chester City"].inventory.append(self.itemDict["Elden Armor"])
                self.merchantDict["Junction 1"].inventory.append(self.itemDict["Stick of Stickyness"])
                self.merchantDict["Town 5"].inventory.append(self.itemDict["Great Bow"])
                self.merchantDict["Town 6"].inventory.append(self.itemDict["Great Bow"])
                self.merchantDict["Town 4"].inventory.append(self.itemDict["Great Knife"])
                self.merchantDict["Town 2"].inventory.append(self.itemDict["Great Sword"])
                self.merchantDict["Town 1"].inventory.append(self.itemDict["Great Sword"])
            elif self.currentlocation == "Town 2":
                self.merchantDict["Belkinus"].inventory.append(self.itemDict["Elden Wand"])
                self.merchantDict["Cloveway"].inventory.append(self.itemDict["Elden Sword"])
                self.merchantDict["Chester City"].inventory.append(self.itemDict["Elden Armor"])
                self.merchantDict["Junction 1"].inventory.append(self.itemDict["Stick of Stickyness"])
                self.merchantDict["Town 5"].inventory.append(self.itemDict["Great Bow"])
                self.merchantDict["Town 6"].inventory.append(self.itemDict["Great Bow"])
                self.merchantDict["Town 3"].inventory.append(self.itemDict["Great Knife"])
                self.merchantDict["Town 4"].inventory.append(self.itemDict["Great Knife"])
                self.merchantDict["Town 1"].inventory.append(self.itemDict["Great Sword"])
            elif self.currentlocation == "Town 1":
                self.merchantDict["Belkinus"].inventory.append(self.itemDict["Elden Wand"])
                self.merchantDict["Cloveway"].inventory.append(self.itemDict["Elden Sword"])
                self.merchantDict["Chester City"].inventory.append(self.itemDict["Elden Armor"])
                self.merchantDict["Junction 1"].inventory.append(self.itemDict["Stick of Stickyness"])
                self.merchantDict["Town 5"].inventory.append(self.itemDict["Great Bow"])
                self.merchantDict["Town 6"].inventory.append(self.itemDict["Great Bow"])
                self.merchantDict["Town 3"].inventory.append(self.itemDict["Great Knife"])
                self.merchantDict["Town 4"].inventory.append(self.itemDict["Great Knife"])
                self.merchantDict["Town 2"].inventory.append(self.itemDict["Great Sword"])
            
        if self.choices["Release Vampire"] == False:
            Alicinia = Character(0, 1, 3, "Alicinia", 28, 14, 4, "Magic", "Vampire", 0, 14, 18, 18, 16, 14, 20, deepcopy(self.itemDict["wand"]), ["Fireball", "Magic Missile", "Eldritch Blast"], deepcopy(self.itemDict["Blood Born Wrappings"]), False, 0, 0)
            setlist.append(Alicinia)
        
        Wolf = Creature(0, "Wolf", 9, 4, 2, "Martial", "Wolf", 6, 14, 12, 16, 12, 12, 8, False, 1)
        SkeletonWarrior = Humanoid(deepcopy(self.itemDict["sword"]), [], deepcopy(self.itemDict["Bones"]), 0, "Skeleton Warrior", 8, 5, 2, "Martial", "Undead", 8, 12, 12, 10, 8, 8, 8, False, 1)
        BoneGolem = Creature(0, "Bone Golem", 20, 6, 2, "Martial", "Undead", 12, 16, 10, 14, 8, 8, 8, False, 2)
        SkeletonArcher = Humanoid(deepcopy(self.itemDict["bow"]), [], deepcopy(self.itemDict["Bones"]), 0, "Skeleton Archer", 4, 5, 2, "Martial", "Undead", 6, 8, 14, 8, 10, 10, 10, False, 1)
        Zombie = Creature(0, "Zombie", 8, 3, 2, "Martial", "Undead", 4, 10, 8, 8, 6, 6, 6, False, 1)
        Goblin = Humanoid(deepcopy(self.itemDict["knife"]), [], deepcopy(self.itemDict["Goblin armor"]), 0, "Goblin", 8, 4, 2, "Martial", "Goblin", 6, 12, 10, 10, 8, 8, 8, False, 1)
        BoneDragon = Creature(0, "Bone Dragon", 40, 8, 0, "Martial", "Undead", 12, 14, 14, 14, 10, 10, 10, False, 2)
        Bandit = Humanoid(deepcopy(self.itemDict["knife"]), [], deepcopy(self.itemDict["leather armor"]), 0, "Bandit", 13, 5, 2, "Martial", "Human", 6, 14, 12, 10, 10, 10, 8, False, 1)
        Slaver = Humanoid(deepcopy(self.itemDict["hammer"]), [], deepcopy(self.itemDict["leather armor"]), 0, "Slaver", 14, 5, 2, "Martial", "Human", 8, 14, 12, 10, 10, 12, 8, False, 1)
        Skelephant = Creature(0, "Skelephant", 16, 6, 1, "Martial", "Undead", 8, 14, 10, 14, 10, 10, 8, False, 1)
        Necromancer = Humanoid(deepcopy(self.itemDict["wand"]), ["Blight", "Eldritch Blast"], deepcopy(self.itemDict["Necrorobes"]), 0, "Necromancer", 6, 4, 2, "Magic", "Human", 0, 8, 10, 10, 14, 14, 12, False, 0)
        Xalan = Humanoid(deepcopy(self.itemDict["wand"]), ["Blight", "Eldritch Blast", "Fireball", "Magic Missile", "Scorching Ray"], deepcopy(self.itemDict["High Necromancer Robes"]), 0, "Xalan", 80, 14, 4, "Magic", "Human", 0, 10, 10, 10, 18, 20, 16, False, 0)
        setlist.append(Wolf)
        setlist.append(SkeletonWarrior)
        setlist.append(BoneGolem)
        setlist.append(SkeletonArcher)
        setlist.append(Zombie)
        setlist.append(Goblin)
        setlist.append(BoneDragon)
        setlist.append(Bandit)
        setlist.append(Slaver)
        setlist.append(Skelephant)
        setlist.append(Necromancer)
        setlist.append(Xalan)
        
        for ent in setlist:
            ent.setCharismaBonus()
            ent.setConstitutionBonus()
            ent.setWisdomBonus()
            ent.setDexterityBonus()
            ent.setIntelligenceBonus()
            ent.setStrengthBonus()
            ent.setHealth(ent.health+ent.conbonus)
            ent.setArmor(ent.armor+ent.dexbonus)
                
        self.enemiesDict[1] = Wolf
        self.enemiesDict[2] = SkeletonWarrior
        self.enemiesDict[3] = SkeletonArcher
        self.enemiesDict[4] = Skelephant
        self.enemiesDict[5] = Zombie
        self.enemiesDict[6] = BoneDragon
        self.enemiesDict[7] = BoneGolem
        self.enemiesDict[8] = Goblin
        self.enemiesDict[9] = Slaver
        self.enemiesDict[10] = Bandit
        self.enemiesDict[11] = Necromancer
        
    def rollDice(self, sided):
        result = 0
        result = random.randint(1, sided)
        return result
    
    def initiative(self, charac):
        turn = 0
        turn = self.rollDice(20) + charac.dexbonus
        return turn
    
    def fullinitiative(self):
        self.turnOrder = []
        for charac in self.currentCharacters:
            init = self.initiative(charac)
            self.turnOrder.append((init, charac))
            
        for en in self.currentEnemies:
            init = self.initiative(en)
            self.turnOrder.append((init, en))
        
        for tup in self.turnOrder:
            count = 0
            while count < len(self.turnOrder):
                if count == len(self.turnOrder)-1:
                    if self.turnOrder[count][0] > self.turnOrder[0][0]:
                        hold = self.turnOrder[0]
                        self.turnOrder[0] = self.turnOrder[count]
                        self.turnOrder[count] = hold
                else:
                    if self.turnOrder[count+1][0] > self.turnOrder[count][0]:
                        hold = self.turnOrder[count]
                        self.turnOrder[count] = self.turnOrder[count+1]
                        self.turnOrder[count+1] = hold
                count += 1
        
    def RandomEncounter(self):
        currentTurn = None
            
        cause = 1
        currentTurn = self.turnOrder[self.turn][1]
        if currentTurn.alive == True:
            if currentTurn.player == False:
                #Automate enemy target selection
                if currentTurn in self.currentEnemies:
                    target = self.rollDice(len(self.currentCharacters))-1
                    if type(currentTurn) == Humanoid:
                        #Automate enemy spell selection
                        if currentTurn.proficiency == "Magic":
                            spellnum = self.rollDice(len(currentTurn.spells))-1
                            spell = currentTurn.spells[spellnum]
                            currentTurn.setdamagedie(self.spellDamDict[spell])
                            currentTurn.setnumdie(self.spellDieDict[spell])
                            self._guiManager.maingui.conversationText.configure(state="normal")
                            self._guiManager.maingui.conversationText.insert(END, str(currentTurn.name + " is attacking " + self.currentCharacters[target].name+"\n"))
                            self._guiManager.maingui.conversationText.configure(state="disabled")
                            if type(currentTurn.weapon) is str:
                                currentTurn.weapon = self.itemDict[currentTurn.weapon]
                            currentTurn.attack(self.currentCharacters[target], self, self.weaponDamDict[currentTurn.weapon.name])
                        else:
                            self._guiManager.maingui.conversationText.configure(state="normal")
                            self._guiManager.maingui.conversationText.insert(END, str(currentTurn.name + " is attacking " + self.currentCharacters[target].name+"\n"))
                            self._guiManager.maingui.conversationText.configure(state="disabled")
                            if type(currentTurn.weapon) is str:
                                currentTurn.weapon = self.itemDict[currentTurn.weapon]
                            currentTurn.attack(self.currentCharacters[target], self, self.weaponDamDict[currentTurn.weapon.name]-3)
                    else:
                        self._guiManager.maingui.conversationText.configure(state="normal")
                        self._guiManager.maingui.conversationText.insert(END, str(currentTurn.name + " is attacking " + self.currentCharacters[target].name+"\n"))
                        self._guiManager.maingui.conversationText.configure(state="disabled")
                        currentTurn.attack(self.currentCharacters[target], self, currentTurn.strbonus)
                else:
                    target = self.rollDice(len(self.currentEnemies))-1
                    if currentTurn.proficiency == "Magic":
                        spellnum = self.rollDice(len(currentTurn.spells))-1
                        spell = currentTurn.spells[spellnum]
                        currentTurn.setdamagedie(self.spellDamDict[spell])
                        currentTurn.setnumdie(self.spellDieDict[spell])
                        self._guiManager.maingui.conversationText.configure(state="normal")
                        self._guiManager.maingui.conversationText.insert(END, str(currentTurn.name + " is attacking " + self.currentEnemies[target].name)+"\n")
                        self._guiManager.maingui.conversationText.configure(state="disabled")
                        if type(currentTurn.weapon) is str:
                                currentTurn.weapon = self.itemDict[currentTurn.weapon]
                        currentTurn.attack(self.currentEnemies[target], self, self.weaponDamDict[currentTurn.weapon.name])
                    else:
                        self._guiManager.maingui.conversationText.configure(state="normal")
                        self._guiManager.maingui.conversationText.insert(END, str(currentTurn.name + " is attacking " + self.currentEnemies[target].name+"\n"))
                        self._guiManager.maingui.conversationText.configure(state="disabled")
                        if type(currentTurn.weapon) is str:
                                currentTurn.weapon = self.itemDict[currentTurn.weapon]
                        print(currentTurn.name)
                        print(currentTurn.weapon)
                        currentTurn.attack(self.currentEnemies[target], self, self.weaponDamDict[currentTurn.weapon.name])
            else:
                self._guiManager.maingui.openTarget()
        
        if self.turn != len(self.turnOrder)-1:
            if self.turnOrder[self.turn+1][1].player == True:
                self._guiManager.maingui.conversationText.configure(state="normal")
                self._guiManager.maingui.conversationText.insert(END, "Your health is " + str(self.currentCharacters[0].health) +"\n")
                self._guiManager.maingui.conversationText.configure(state="disabled")
            
        for tup in self.turnOrder:
                if tup[1].alive == False:
                    if tup[1].player == True:
                        self.currentEnemies = []
                        cause = 0
                    else:
                        if tup[1] in self.currentEnemies:
                            self.currentEnemies.remove(tup[1])
                            self._guiManager.maingui.conversationText.configure(state="normal")
                            self._guiManager.maingui.conversationText.insert(END, str(tup[1].name + " has been knocked out\n"))
                            self._guiManager.maingui.conversationText.configure(state="disabled")
                        elif tup[1] in self.currentCharacters:
                            self._guiManager.maingui.conversationText.configure(state="normal")
                            self._guiManager.maingui.conversationText.insert(END, str(tup[1].name + " has been knocked out\n"))
                            self._guiManager.maingui.conversationText.configure(state="disabled")
                            
        for charac in self.currentCharacters:
                if charac.alive == True:
                    for tup in self.turnOrder:
                        if charac == tup[1]:
                            check = 1
                    if check == 0:
                        self.turnOrder.append(0, charac)
                        
        if self.turn == len(self.turnOrder)-1:
                self.turn = 0
                print(self.turn)
                print(self.turnOrder)
        else:
                self.turn += 1
        
        if cause == 0 and len(self.currentEnemies) == 0:
            self._guiManager.maingui.conversationText.configure(state="normal")
            self._guiManager.maingui.conversationText.insert(END, "You have died, and your bones shall be bleached white by the sun\n")
            self._guiManager.maingui.conversationText.configure(state="disabled")
        elif cause == 1 and len(self.currentEnemies) == 0:
            self._guiManager.maingui.conversationText.configure(state="normal")
            self._guiManager.maingui.conversationText.insert(END, "You have triumphed over this challenge\nThat is the end of the beta of this game, please close the game now\n\n\n\nI'm serious close the game now")
            self._guiManager.maingui.conversationText.configure(state="disabled")
            self.mode = "Story"
            self._guiManager.maingui.menuButton.configure(state="normal")
            count = 0
            while count < self.lootNum:
                loot = self.createLoot()
                self.currentCharacters[0].inventory.append(loot)
                count += 1
            for charac in self.currentCharacters:
                charac.XP += 10 * self.lootNum
        
    def deceptionCheck(self, difficulty, character):
        check = self.rollDice(20) + character.getCharismaBonus()
        if check >= difficulty:
            return True
        else:
            return False
        
    def persuasionCheck(self, difficulty, character):
        check = self.rollDice(20) + character.getCharismaBonus()
        if check >= difficulty:
            return True
        else:
            return False
        
    def intimidationCheck(self, difficulty, character):
        check = self.rollDice(20) + character.getStrengthBonus()
        if check >= difficulty:
            return True
        else:
            return False
        
    def stealthCheck(self, difficulty, character):
        check = self.rollDice(20) + character.getDexterityBonus()
        if check >= difficulty:
            return True
        else:
            return False
        
    def travel(self, destination):
        self.currentlocation = destination
        
    def createLoot(self):
        listloot = ["Health Potion", "Damage Potion", "leather armor", "metal armor", "Blood Born Wrappings", "sword", "knife", "bow"]
        item = self.rollDice(len(listloot)-1)
        loot = deepcopy(self.itemDict[listloot[item]])
        return loot
    
    def setManagers(self, fileManager, guiManager):
        self._fileManager = fileManager
        self._guiManager = guiManager
    
class Creature(object):
    def __init__(self, cid, name, health, armor, attackb, proficiency, race, damagedie, strength, dexterity, constitution, intelligence, wisdom, charisma, player, numdie):
        self.cid = cid
        self.name = name
        self.health = health
        self.armor = armor
        self.attackb = attackb
        self.race = race
        self.proficiency = proficiency
        self.damagedie = damagedie
        self.numdie = numdie
        self.strength = strength
        self.strbonus = 0
        self.dexterity = dexterity
        self.dexbonus = 0
        self.constitution = constitution
        self.conbonus = 0
        self.intelligence = intelligence
        self.intbonus = 0
        self.wisdom = wisdom
        self.wisbonus = 0
        self.charisma = charisma
        self.charbonus = 0
        self.alive = True
        self.status = []
        self.player = player
          
    def attack(self, target, game, weapond):
        damage = 0
        count = 0
        roll = game.rollDice(20)
        if roll + self.attackb > target.armor:
            while count < self.numdie:
                damage += game.rollDice(self.damagedie)
                if type(self) == Humanoid:
                    damage += weapond
                if self.proficiency == "Magic":
                    damage += self.wisbonus
                else:
                    damage += self.strbonus
                count += 1
        target.takeDamage(damage)
        game._guiManager.maingui.conversationText.configure(state="normal")
        game._guiManager.maingui.conversationText.insert(END, str(self.name + " has dealt " + str(damage) + " damage to " + target.name + "\n"))
        game._guiManager.maingui.conversationText.configure(state="disabled")
        
    def setArmor(self, armorval):
        self.armor = armorval
        
    def setHealth(self, healthval):
        self.health = healthval
        
    def takeDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.alive = False
            
    def setCharisma(self, newChar):
        self.charisma = newChar
        
    def setWisdom(self, newWis):
        self.wisdom = newWis
        
    def setIntelligence(self, newInt):
        self.intelligence = newInt
        
    def setConstitution(self, newCon):
        self.constitution = newCon
        
    def setDexterity(self, newDex):
        self.dexterity = newDex
        
    def setStrength(self, newStr):
        self.strength = newStr
        
    def setCharismaBonus(self):
        charBonus = self.charisma
        charBonus -= 10
        charBonus = charBonus//2
        self.charbonus = charBonus
        
    def setWisdomBonus(self):
        wisBonus = self.wisdom
        wisBonus -= 10
        wisBonus = wisBonus//2
        self.wisbonus = wisBonus
        
    def setIntelligenceBonus(self):
        intBonus = self.intelligence
        intBonus -= 10
        intBonus = intBonus//2
        self.intbonus = intBonus
        
    def setConstitutionBonus(self):
        conBonus = self.constitution
        conBonus -= 10
        conBonus = conBonus//2
        self.conbonus = conBonus
        
    def setDexterityBonus(self):
        dexBonus = self.dexterity
        dexBonus -= 10
        dexBonus = dexBonus//2
        self.dexbonus = dexBonus
        
    def setStrengthBonus(self):
        strBonus = self.strength
        strBonus -= 10
        strBonus = strBonus//2
        self.strbonus = strBonus
        
    def setID(self, iD):
        self.cid = iD
        
    def setdamagedie(self, dam):
        self.damagedie = dam
        
    def setnumdie(self, die):
        self.numdie = die
        
    def setname(self, nameval):
        self.name = nameval
        
class Humanoid(Creature):
    def __init__(self, weapon, spells, equipment, cid, name, health, armor, attackb, proficiency, race, damagedie, strength, dexterity, constitution, intelligence, wisdom, charisma, player, numdie):
        super().__init__(cid, name, health, armor, attackb, proficiency, race, damagedie, strength, dexterity, constitution, intelligence, wisdom, charisma, player, numdie)
        self.weapon = weapon
        self.spells = spells
        self.equipment = equipment
        
class Character(Humanoid):
    def __init__(self, XP, Level, cid, name, health, armor, attackb, proficiency, race, damagedie, strength, dexterity, constitution, intelligence, wisdom, charisma, weapon, spells, equipment, player, numdie, mon):
        super().__init__(weapon, spells, equipment, cid, name, health, armor, attackb, proficiency, race, damagedie, strength, dexterity, constitution, intelligence, wisdom, charisma, player, numdie)
        self.XP = XP
        self.Level = Level
        self.inventory = []
        self.money = mon
    
    def gainXP(self, xP):
        self.XP += xP
        if self.XP > 100:
            self.Level += 1
    
class Merchant(object):
    def __init__(self, Id, mon, uni, loc):
        self.id = Id
        self.inventory = []
        self.money = mon
        self.origMon = deepcopy(mon)
        self.origInv = []
        self.unique = uni
        self.location = loc
        
    def refresh(self):
        self.money = deepcopy(self.origMon)
        self.inventory = deepcopy(self.origInv)
        if self.unique != None:
            self.inventory.append(self.unique)
    
class Item(object):
    def __init__(self, val, sto, isEq, haUs, nam, fri):
        self.value = val
        self.story = sto
        self.isEquippable = isEq
        self.hasUse = haUs
        self.name = nam
        self.friendly = fri
        
    def use(self, target, manager, time):
        if manager.mode == "Combat" and time == 0:
            manager.item = self
            manager._guiManager.openWindow("itemtarget")
            manager.turn += 1
        else:
            if self.friendly == True:
                self.restoreHealth(target, manager)
            else:
                self.dealDamage(target, manager)
                
    def restoreHealth(self, target, manager):
        if target.alive == False:
            if target.health < 0:
                target.health = 0
            target.alive == True
        if self.name == "Health Potion":
            target.health += manager.rollDice(4) + manager.rollDice(4)
        elif self.name == "Greater Health Potion":
            target.health += manager.rollDice(6) * 3
    
    def dealDamage(self, target, manager):
        if self.name == "Stick of Stickyness" and target.name == "Xalan":
            target.alive = False
            manager.currentEnemies.remove(target)
        if self.name == "Damage Potion":
            damage = manager.rollDice(4) + manager.rollDice(4)
        elif self.name == "Greater Damage Potion":
            damage = manager.rollDice(6) * 3
        hit = manager.rollDice(20) + 2
        if hit > target.armor:
            target.takeDamage(damage)
            manager._guiManager.maingui.conversationText.configure(state="normal")
            manager._guiManager.maingui.conversationText.insert(END, str(target.name + " has taken " + str(damage) + " damage\n"))
            manager._guiManager.maingui.conversationText.configure(state="disabled")
    
class Equipment(Item):
    def __init__(self, val, sto, isEq, haUs, nam, fri, isAr, isWe, arVa, daDi):
        super().__init__(val, sto, isEq, haUs, nam, fri)
        self.isArmor = isAr
        self.isWeapon = isWe
        self.armorVal = arVa
        self.damagedie = daDi
        
class GUIManager(object):
    def __init__(self):
        self.root = Tk()
        
    def setManagers(self, ifileManager, igameManager):
        self.fileManager = ifileManager
        self.gameManager = igameManager
        
    def startupGUI(self):
        self.root.withdraw()
        
        self.maingui = mainGUI(self.root, self)
        self.maingui.hide()
        
        self.openWindow("start")
        
        self.root.mainloop()
    
    def openWindow(self, keyword):

        if keyword == "start":
            startGUI(self.root, self)
        elif keyword == "stat":
            statGUI(self.root, self)
        elif keyword == "special":
            specialGUI(self.root, self)
        elif keyword == "name":
            nameGUI(self.root, self)
        elif keyword == "load":
            loadGUI(self.root, self)
        elif keyword == "menu":
            menuGUI(self.root, self)
        elif keyword == "inventory":
            inventoryGUI(self.root, self)
        elif keyword == "equip":
            equipGUI(self.root, self, 0)
        elif keyword == "save":
            saveGUI(self.root, self)
        elif keyword == "map":
            mapGUI(self.root, self)
        elif keyword == "target":
            targetGUI(self.root, self)
        elif keyword == "itemtarget":
            itemtargetGUI(self.root, self)
        elif keyword == "shop":
            shopGUI(self.root, self)
        elif keyword == "main":
            self.maingui.show()
        else:
            print("Incorrect keyword sent to guiManager.openWindow(keyword) . Incorrect keyword: \"" + keyword + "\" not found in guiDict")
    
    def end(self):
        self.root.destroy()
        
class AbstractGUI(object):
    def __init__(self, parent):
        self.window = Toplevel()
        self.window.protocol("WM_DELETE_WINDOW",self.onClose)

    def show(self):
        self.window.deiconify()

    def hide(self):
        self.window.withdraw()

    def focus(self):
        self.window.focus_force()

    def onClose(self):
        self.guiManager.end()
        
class startGUI(AbstractGUI):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.guiManager = manager
        self.window.geometry("400x200+100+100")

        buttonFrame = Frame(master=self.window, height=150)
        buttonFrame.grid()
        
        titleLabel = Label(buttonFrame, text = "Necrohunt")
        titleLabel.grid(row=1, column=1)
        newButton = Button(buttonFrame, text = "New game", command = self.openSpecial)
        newButton.grid(row=2, column=1)
        loadButton = Button(buttonFrame, text = "Load", command = self.openLoad)
        loadButton.grid(row=3, column=1)
        
    def openSpecial(self):
        self.window.destroy()
        self.guiManager.gameManager.setup()
        self.guiManager.openWindow("special")
    
    def openLoad(self):
        self.guiManager.openWindow("load")
        self.window.destroy()

class saveGUI(AbstractGUI):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.guiManager = manager
        self.window.geometry("200x50+100+100")
        
        saveFrame = Frame(master=self.window, height=20)
        saveFrame.grid()
        
        self.nameFrame = Entry(saveFrame, bd = 5)
        self.nameFrame.grid(row=1, column=1)
        saveButton = Button(saveFrame, text="Save", command = self.save)
        saveButton.grid(row=1, column=2)
        
    def save(self):
        self.guiManager.fileManager.save(self.nameFrame.get())
        self.window.destroy()
        self.guiManager.openWindow("main")
    
class nameGUI(AbstractGUI):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.guiManager = manager
        self.window.geometry("300x50+100+100")
        
        nameFrame = Frame(master=self.window, height=20)
        nameFrame.grid()
        
        nameLabel = Label(nameFrame, text="Enter name here")
        nameLabel.grid(row=1, column=1)
        self.namingFrame = Entry(nameFrame, bd = 5)
        self.namingFrame.grid(row=1, column=2)
        saveButton = Button(nameFrame, text="Enter", command = self.name)
        saveButton.grid(row=1, column=3)
        
    def name(self):
        self.guiManager.gameManager.currentCharacters[0].setname(self.namingFrame.get())
        if self.guiManager.gameManager.currentCharacters[0].proficiency == "Magic":
            self.guiManager.gameManager.currentCharacters[0].weapon = deepcopy(self.guiManager.gameManager.itemDict["wand"])
            self.guiManager.gameManager.currentCharacters[1] = Character(0, 1, 2, "Alex", 12, 10, 2, "Martial", "Human", 8, 14, 14, 14, 12, 12, 12, self.guiManager.gameManager.itemDict["sword"], ["None"], self.guiManager.gameManager.itemDict["leather armor"], False, 1, 0)
            self.guiManager.gameManager.currentCharacters[0].inventory.append(self.guiManager.gameManager.currentCharacters[0].weapon)
        else:
            self.guiManager.gameManager.currentCharacters[0].weapon = deepcopy(self.guiManager.gameManager.itemDict["sword"])
            self.guiManager.gameManager.currentCharacters[1] = Character(0, 1, 2, "Alex", 10, 10, 2, "Magic", "Human", 0, 12, 14, 12, 14, 14, 12, self.guiManager.gameManager.itemDict["wand"], ["Magic Missile", "Fireball", "Eldritch Blast"], self.guiManager.gameManager.itemDict["leather armor"], False, 0, 0)
            self.guiManager.gameManager.currentCharacters[0].inventory.append(self.guiManager.gameManager.currentCharacters[0].weapon)
        self.guiManager.gameManager.currentCharacters[0].inventory.append(deepcopy(self.guiManager.gameManager.itemDict["leather armor"]))
        self.guiManager.gameManager.currentCharacters[0].inventory.append(deepcopy(self.guiManager.gameManager.itemDict["Health Potion"]))
        self.guiManager.gameManager.currentCharacters[0].inventory.append(deepcopy(self.guiManager.gameManager.itemDict["Health Potion"]))
        self.guiManager.gameManager.currentCharacters[0].inventory.append(deepcopy(self.guiManager.gameManager.itemDict["Health Potion"]))
        self.guiManager.gameManager.currentCharacters[0].money = 500
        self.guiManager.gameManager.currentCharacters[0].setCharismaBonus()
        self.guiManager.gameManager.currentCharacters[0].setConstitutionBonus()
        self.guiManager.gameManager.currentCharacters[0].setWisdomBonus()
        self.guiManager.gameManager.currentCharacters[0].setDexterityBonus()
        self.guiManager.gameManager.currentCharacters[0].setIntelligenceBonus()
        self.guiManager.gameManager.currentCharacters[0].setStrengthBonus()
        self.guiManager.gameManager.currentCharacters[0].equipment = self.guiManager.gameManager.itemDict["leather armor"]
        self.guiManager.gameManager.currentCharacters[0].setHealth(self.guiManager.gameManager.currentCharacters[0].health+self.guiManager.gameManager.currentCharacters[0].conbonus)
        self.guiManager.gameManager.currentCharacters[0].setArmor(self.guiManager.gameManager.currentCharacters[0].armor+self.guiManager.gameManager.currentCharacters[0].dexbonus)
        self.guiManager.gameManager.currentCharacters[1].setCharismaBonus()
        self.guiManager.gameManager.currentCharacters[1].setConstitutionBonus()
        self.guiManager.gameManager.currentCharacters[1].setWisdomBonus()
        self.guiManager.gameManager.currentCharacters[1].setDexterityBonus()
        self.guiManager.gameManager.currentCharacters[1].setIntelligenceBonus()
        self.guiManager.gameManager.currentCharacters[1].setStrengthBonus()
        self.guiManager.gameManager.currentCharacters[1].setHealth(self.guiManager.gameManager.currentCharacters[1].health+self.guiManager.gameManager.currentCharacters[1].conbonus)
        self.guiManager.gameManager.currentCharacters[1].setArmor(self.guiManager.gameManager.currentCharacters[1].armor+self.guiManager.gameManager.currentCharacters[1].dexbonus)
        self.window.destroy()
        self.guiManager.openWindow("main")
            
class specialGUI(AbstractGUI):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.guiManager = manager
        self.window.geometry("400x400+100+100")
        self.var = IntVar()
        self.special = 0
        
        specialFrame = Frame(master=self.window, height=150)
        specialFrame.grid()
        
        magic = Radiobutton(specialFrame, text="Magic user", variable = self.var, value = 0, command = self.setSpecial)
        magic.grid(row = 1, column = 1)
        nonmagic = Radiobutton(specialFrame, text="Martial", variable = self.var, value = 1, command = self.setSpecial)
        nonmagic.grid(row = 2, column = 1)
        
        nextB = Button(specialFrame, text = "Next", command = self.openStat)
        nextB.grid(row = 9, column = 5)
        
    def openStat(self):
        if self.special == 0:
            self.guiManager.gameManager.currentCharacters[0].proficiency = "Magic"
            self.guiManager.gameManager.currentCharacters[0].health = 10
            self.guiManager.gameManager.currentCharacters[0].spells = ["Magic Missile", "Fireball", "Eldritch Blast", "Scorching Ray", "Blight"]
        else:
            self.guiManager.gameManager.currentCharacters[0].proficiency = "Martial"
            self.guiManager.gameManager.currentCharacters[0].health = 12
            self.guiManager.gameManager.currentCharacters[0].spells = ["None"]
        self.window.destroy()
        self.guiManager.openWindow("stat")
        
    def setSpecial(self):
        self.special = self.var.get()
            
class menuGUI(AbstractGUI):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.guiManager = manager
        self.window.geometry("400x400+100+100")
        
        buttonFrame = Frame(master=self.window, height=150)
        buttonFrame.grid()
        
        saveButton = Button(buttonFrame, text = "Save", command = self.openSave)
        saveButton.grid(row=1, column = 1)
        loadButton = Button(buttonFrame, text = "Load", command = self.openLoad)
        loadButton.grid(row=1, column = 2)
        inventoryButton = Button(buttonFrame, text = "Inventory", command = self.openInventory)
        inventoryButton.grid(row=1, column = 3)
        shopButton = Button(buttonFrame, text = "Shop", command = self.openShop)
        shopButton.grid(row=2, column = 1)
        levelButton = Button(buttonFrame, text = "Level-Up", command = self.openLevel)
        levelButton.grid(row=2, column = 2)
        closeButton = Button(buttonFrame, text = "Close", command = self.openMain)
        closeButton.grid(row=2, column = 3)
        mapButton = Button(buttonFrame, text = "Map", command = self.openMap)
        mapButton.grid(row=3, column = 1)
        equipButton = Button(buttonFrame, text = "Equipment", command = self.openEquip)
        equipButton.grid(row=3, column = 2)
        quitButton = Button(buttonFrame, text = "Quit", command = self.openQuit)
        quitButton.grid(row=3, column = 3)
        
    
    def openSave(self):
        self.guiManager.openWindow("save")
        self.window.destroy()
    
    def openLoad(self):
        self.guiManager.openWindow("load")
        self.window.destroy()
    
    def openInventory(self):
        self.guiManager.openWindow("inventory")
        self.window.destroy()
    
    def openShop(self):
        self.guiManager.openWindow("shop")
        self.window.destroy()
    
    def openLevel(self):
        if self.guiManager.gameManager.currentCharacters[0].XP >= 100:
            self.guiManager.openWindow("stat")
            self.window.destroy()
        else:
            pass
    
    def openMain(self):
        self.guiManager.openWindow("main")
        self.window.destroy()
    
    def openMap(self):
        self.guiManager.openWindow("map")
        self.window.destroy()
    
    def openEquip(self):
        self.guiManager.openWindow("equip")
        self.window.destroy()
    
    def openQuit(self):
        self.guiManager.end()
        
class mapGUI(AbstractGUI):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.guiManager = manager
        self.window.geometry("600x600+100+100")
        self.map = {"Belkinus": ["Junction 1", "Town 1", "Cloveway", "Chester City"], "Chester City": ["Belkinus", "Town 2"], "Town 1": ["Belkinus"], 
                    "Junction 1": ["Town 3", "Town 4", "Belkinus"], "Town 2": ["Town 5", "Town 6", "Chester City"], "Town 5": ["Town 2"], "Town 6": ["Town 2"], "Town 3": ["Junction 1"],
                    "Town 4": ["Junction 1"], "Cloveway": ["Belkinus"]}
        self.location = StringVar()
        self.location.set(self.guiManager.gameManager.currentlocation)
        self.destination = ""
        self.par = parent
        self.dest1 = StringVar()
        self.dest2 = StringVar()
        self.dest3 = StringVar()
        self.dest4 = StringVar()
        check = self.location.get()
        if len(self.map[check]) == 1:
            self.dest1.set(self.map[check][0])
        elif len(self.map[check]) == 2:
            self.dest1.set(self.map[check][0])
            self.dest2.set(self.map[check][1])
        elif len(self.map[check]) == 3:
            self.dest1.set(self.map[check][0])
            self.dest2.set(self.map[check][1])
            self.dest3.set(self.map[check][2])
        else:
            self.dest1.set(self.map[check][0])
            self.dest2.set(self.map[check][1])
            self.dest3.set(self.map[check][2])
            self.dest4.set(self.map[check][3])
        
        mapFrame = Frame(self.window, height=400, width=800)
        mapFrame.grid()
        buttonFrame = Frame(self.window, height=100)
        buttonFrame.grid()
        mapLabel = Label(mapFrame, text = "                                   Town 6 \n"\
                                          "                                       /\ \n"\
                                          "                                      |  | \n"\
                                          "                                       O  \n"\
                                          "                    Chester City  |  \n"\
                                          "                               /\      |  \n"\
                                          "                            /\| |       |  \n"\
                                          "                           | || |       /\ \n"\
                                          "      Town 3            | || |     |  | \n"\
                                          "         /\                    O ----- O  Town 2 \n"\
                                          "        | |                  /         |  \n"\
                                          "         O                  /          |  \n"\
                                          "         |    Belkinus     /           |  \n"\
                                          "         |       /\       /            |  \n"\
                                          "         |    /\| |/\    /            /\  \n"\
                                          "Town 4   |   | || |||   /            | |  \n"\
                                          " /\       |   | || |||  /              O   \n"\
                                          "| |       |   | || ||| /            Town 5 \n"\
                                          "O ------ O ----- O                        \n"\
                                          "    Junction 1  / \                       \n"\
                                          "                 /   \                      \n"\
                                          "                /     \                     \n"\
                                          "               /       \                    \n"\
                                          "              /         \                   \n"\
                                          "           /           \  Town 1          \n"\
                                          "          /             \  /\             \n"\
                                          "         /               \| |             \n"\
                                          "Cloveway/                 O               \n"\
                                          "    /\  /                                  \n"\
                                          " /\|  | /                                   \n"\
                                          "| ||  |/                                    \n"\
                                          "  O                                       \n")
        mapLabel.grid(row=1, column=1)
        destLabel = Label(buttonFrame, text = "Destinations: ")
        destLabel.grid(row=1, column = 1)
        dest1Label = Button(buttonFrame, text = self.dest1.get(), command = self.setDestination1)
        dest1Label.grid(row=1, column =3)
        dest2Label = Button(buttonFrame, text = self.dest2.get(), command = self.setDestination2)
        dest2Label.grid(row=1, column =5)
        dest3Label = Button(buttonFrame, text = self.dest3.get(), command = self.setDestination3)
        dest3Label.grid(row=1, column =7)
        dest4Label = Button(buttonFrame, text = self.dest4.get(), command = self.setDestination4)
        dest4Label.grid(row=1, column =9)
        travelButton = Button(buttonFrame, text="Travel", command = self.travel)
        travelButton.grid(row=2, column=1)
        loclabel = Label(buttonFrame, text = "Location: ")
        loclabel.grid(row=3, column=3)
        loc = Label(buttonFrame, text = self.location.get())
        loc.grid(row=3, column=5)
        close = Button(buttonFrame, text="Close", command=self.openMenu)
        close.grid(row=4, column=1)
        
    def travel(self):
        self.guiManager.gameManager.currentMerchant.refresh()
        self.guiManager.gameManager.currentlocation = self.destination
        self.guiManager.gameManager.currentMerchant = self.guiManager.gameManager.merchantDict[self.destination]
        self.window.destroy()
        self.__init__(self.par, self.guiManager)
        
    def openMenu(self):
        self.guiManager.openWindow("menu")
        self.window.destroy()
        
    def setDestination1(self):
        self.destination = self.dest1.get()
        
    def setDestination2(self):
        self.destination = self.dest2.get()
        
    def setDestination3(self):
        self.destination = self.dest3.get()
        
    def setDestination4(self):
        self.destination = self.dest4.get()
        
    
class equipGUI(AbstractGUI):
    def __init__(self, parent, manager, num):
        super().__init__(parent)
        self.guiManager = manager
        self.window.geometry("500x400+100+100")
        self.mainFrame = Frame(master=self.window, height =200)
        self.mainFrame.grid()
        self.secFrame = Frame(master=self.mainFrame, height =150)
        self.secFrame.grid()
        self.secFrame.grid(row=3, column=4)
        self.charac = num
        self.par = parent
        menuButton = Button(self.secFrame, text = "Menu", command=self.openMenu)
        menuButton.grid(row=1, column=1)
        characLabel = Label(self.secFrame, text = self.guiManager.gameManager.currentCharacters[num].name)
        characLabel.grid(row=1, column=4)
        inventButton = Button(self.secFrame, text = "Inventory", command=self.openInventory)
        inventButton.grid(row=1, column=7)
        leftButton = Button(self.mainFrame, text = "<", command=self.left)
        leftButton.grid(row=3, column=1)
        rightButton = Button(self.mainFrame, text = ">", command=self.right)
        rightButton.grid(row=3, column=7)
        armorLabel = Label(self.secFrame, text = "Equipped Armor: ")
        armorLabel.grid(row=2, column = 4)
        armor = Label(self.secFrame, text = self.guiManager.gameManager.currentCharacters[num].equipment.name)
        armor.grid(row=2, column=5)
        armorDesc = Label(self.secFrame, text = self.guiManager.gameManager.itemdescDict[self.guiManager.gameManager.currentCharacters[num].equipment.name])
        armorDesc.grid(row=3, column=4)
        weaponLabel = Label(self.secFrame, text = "Equipped Weapon: ")
        weaponLabel.grid(row=4, column=4)
        weapon = Label(self.secFrame, text = self.guiManager.gameManager.currentCharacters[num].weapon.name)
        weapon.grid(row=4, column=5)
        weaponDesc = Label(self.secFrame, text = self.guiManager.gameManager.itemdescDict[self.guiManager.gameManager.currentCharacters[num].weapon.name])
        weaponDesc.grid(row=5, column=4)
        
    def openMenu(self):
        self.guiManager.openWindow("menu")
        self.window.destroy()
    
    def openInventory(self):
        self.guiManager.openWindow("inventory")
        self.window.destroy()
    
    def right(self):
        self.window.destroy()
        if self.charac == 3:
            self.charac -= 4
        self.__init__(self.par, self.guiManager, self.charac+1)
    
    def left(self):
        self.window.destroy()
        if self.charac == 0:
            self.charac += 4
        self.__init__(self.par, self.guiManager, self.charac-1)
    
class statGUI(AbstractGUI):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.guiManager = manager
        self.window.geometry("400x400+100+100")
        self.charac = None
        self.getCharac()
        self.points = IntVar()
        
        if self.charac.Level == 1:
            self.points = 27
        else:
            self.points += 5
        
        buttonFrame = Frame(master=self.window, height=150)
        buttonFrame.grid()
        
        strength = StringVar()
        strength.set(str(self.charac.strength))
        dexterity = StringVar()
        dexterity.set(str(self.charac.dexterity))
        constitution = StringVar()
        constitution.set(str(self.charac.constitution))
        intelligence = StringVar()
        intelligence.set(str(self.charac.intelligence))
        wisdom = StringVar()
        wisdom.set(str(self.charac.wisdom))
        charisma = StringVar()
        charisma.set(str(self.charac.charisma))
        
        self.strDisFrame = Label(buttonFrame, text = strength.get())
        self.strDisFrame.grid(row=1, column = 2)
        self.dexDisFrame = Label(buttonFrame, text = dexterity.get())
        self.dexDisFrame.grid(row=2, column = 2)
        self.conDisFrame = Label(buttonFrame, text = constitution.get())
        self.conDisFrame.grid(row=3, column = 2)
        self.intDisFrame = Label(buttonFrame, text = intelligence.get())
        self.intDisFrame.grid(row=4, column = 2)
        self.wisDisFrame = Label(buttonFrame, text = wisdom.get())
        self.wisDisFrame.grid(row=5, column = 2)
        self.chaDisFrame = Label(buttonFrame, text = charisma.get())
        self.chaDisFrame.grid(row=6, column = 2)
        strMinButton = Button(buttonFrame, text = "-", command = self.decreaseStr)
        strMinButton.grid(row=1, column = 1)
        dexMinButton = Button(buttonFrame, text = "-", command = self.decreaseDex)
        dexMinButton.grid(row=2, column = 1)
        conMinButton = Button(buttonFrame, text = "-", command = self.decreaseCon)
        conMinButton.grid(row=3, column = 1)
        intMinButton = Button(buttonFrame, text = "-", command = self.decreaseInt)
        intMinButton.grid(row=4, column = 1)
        wisMinButton = Button(buttonFrame, text = "-", command = self.decreaseWis)
        wisMinButton.grid(row=5, column = 1)
        chaMinButton = Button(buttonFrame, text = "-", command = self.decreaseCha)
        chaMinButton.grid(row=6, column = 1)
        strPlsButton = Button(buttonFrame, text = "+", command = self.increaseStr)
        strPlsButton.grid(row=1, column = 3)
        dexPlsButton = Button(buttonFrame, text = "+", command = self.increaseDex)
        dexPlsButton.grid(row=2, column = 3)
        conPlsButton = Button(buttonFrame, text = "+", command = self.increaseCon)
        conPlsButton.grid(row=3, column = 3)
        intPlsButton = Button(buttonFrame, text = "+", command = self.increaseInt)
        intPlsButton.grid(row=4, column = 3)
        wisPlsButton = Button(buttonFrame, text = "+", command = self.increaseWis)
        wisPlsButton.grid(row=5, column = 3)
        chaPlsButton = Button(buttonFrame, text = "+", command = self.increaseCha)
        chaPlsButton.grid(row=6, column = 3)
        strLabel = Label(buttonFrame, text = "Strength")
        strLabel.grid(row = 1, column = 4)
        dexLabel = Label(buttonFrame, text = "Dexterity")
        dexLabel.grid(row = 2, column = 4)
        conLabel = Label(buttonFrame, text = "Constitution")
        conLabel.grid(row = 3, column = 4)
        intLabel = Label(buttonFrame, text = "Intelligence")
        intLabel.grid(row = 4, column = 4)
        wisLabel = Label(buttonFrame, text = "Wisdom")
        wisLabel.grid(row = 5, column = 4)
        chaLabel = Label(buttonFrame, text = "Charisma")
        chaLabel.grid(row = 6, column = 4)
        pointsLabel = Label(buttonFrame, text = "Points:")
        pointsLabel.grid(row=1, column = 6)
        self.pointTotal = Label(buttonFrame, text=self.points)
        self.pointTotal.grid(row = 1, column = 7)
        if self.charac.Level > 1:
            nextButton = Button(buttonFrame, text = "Confirm", command = self.openMain)
        else:
            nextButton = Button(buttonFrame, text = "Next", command = self.openName)
        nextButton.grid(row=7, column=5)
    
    def getCharac(self):
        self.charac = self.guiManager.gameManager.currentCharacters[0]
    
    def increaseStr(self):
        if self.points == 0:
            pass
        else:
            if self.charac.strength == 15:
                pass
            else:
                if self.charac.strength >= 13:
                    if self.points <= 1:
                        pass
                    else:
                        self.points -= 2
                        self.charac.strength += 1
                else:
                    self.points -= 1
                    self.charac.strength += 1
        self.strDisFrame["text"]= self.charac.strength
        self.pointTotal["text"]= self.points
        
    def increaseDex(self):
        if self.points == 0:
            pass
        else:
            if self.charac.dexterity == 15:
                pass
            else:
                if self.charac.dexterity >= 13:
                    if self.points <= 1:
                        pass
                    else:
                        self.points -= 2
                        self.charac.dexterity += 1
                else:
                    self.points -= 1
                    self.charac.dexterity += 1
        self.dexDisFrame["text"] = self.charac.dexterity
        self.pointTotal["text"]= self.points
        
    def increaseCon(self):
        if self.points == 0:
            pass
        else:
            if self.charac.constitution == 15:
                pass
            else:
                if self.charac.constitution >= 13:
                    if self.points <= 1:
                        pass
                    else:
                        self.points -= 2
                        self.charac.constitution += 1
                else:
                    self.points -= 1
                    self.charac.constitution += 1
        self.conDisFrame["text"] = self.charac.constitution
        self.pointTotal["text"]= self.points
        
    def increaseInt(self):
        if self.points == 0:
            pass
        else:
            if self.charac.intelligence == 15:
                pass
            else:
                if self.charac.intelligence >= 13:
                    if self.points <= 1:
                        pass
                    else:
                        self.points -= 2
                        self.charac.intelligence += 1
                else:
                    self.points -= 1
                    self.charac.intelligence += 1
        self.intDisFrame["text"] = self.charac.intelligence
        self.pointTotal["text"]= self.points
        
    def increaseWis(self):
        if self.points == 0:
            pass
        else:
            if self.charac.wisdom == 15:
                pass
            else:
                if self.charac.wisdom >= 13:
                    if self.points <= 1:
                        pass
                    else:
                        self.charac.wisdom += 1
                        self.points -= 2
                else:
                    self.charac.wisdom += 1
                    self.points -= 1
        self.wisDisFrame["text"] = self.charac.wisdom
        self.pointTotal["text"]= self.points
        
    def increaseCha(self):
        if self.points == 0:
            pass
        else:
            if self.charac.charisma == 15:
                pass
            else:
                if self.charac.charisma > 13:
                    if self.points <= 1:
                        pass
                    else:
                        self.points -= 2
                        self.charac.charisma += 1
                else:
                    self.points -= 1
                    self.charac.charisma += 1
        self.chaDisFrame["text"] = self.charac.charisma
        self.pointTotal["text"]= self.points
        
    def decreaseStr(self):
        if self.charac.strength == 8:
            pass
        else:
            if self.points == 27:
                    pass
            else:
                if self.charac.strength > 13:
                    self.points += 2
                    self.charac.strength -= 1
                else:
                    self.points += 1
                    self.charac.strength -= 1
        self.strDisFrame.config(text = str(self.charac.strength))
        self.pointTotal["text"]= self.points
        
    def decreaseDex(self):
        if self.charac.dexterity == 8:
            pass
        else:
            if self.points == 27:
                    pass
            else:
                if self.charac.dexterity > 13:
                    self.points += 2
                    self.charac.dexterity -= 1
                else:
                    self.points += 1
                    self.charac.dexterity -= 1
        self.dexDisFrame.config(text = str(self.charac.dexterity))
        self.pointTotal["text"]= self.points
        
    def decreaseCon(self):
        if self.charac.constitution == 8:
            pass
        else:
            if self.points == 27:
                    pass
            else:
                if self.charac.constitution > 13:
                    self.points += 2
                    self.charac.constitution -= 1
                else:
                    self.points += 1
                    self.charac.constitution -= 1
        self.conDisFrame.config(text = str(self.charac.constitution))
        self.pointTotal["text"]= self.points
    
    def decreaseInt(self):
        if self.charac.intelligence == 8:
            pass
        else:
            if self.points == 27:
                    pass
            else:
                if self.charac.intelligence > 13:
                    self.points += 2
                    self.charac.intelligence -= 1
                else:
                    self.points += 1
                    self.charac.intelligence -= 1
        self.intDisFrame.config(text = str(self.charac.intelligence))
        self.pointTotal["text"]= self.points
        
    def decreaseWis(self):
        if self.charac.wisdom == 8:
            pass
        else:
            if self.points == 27:
                    pass
            else:
                if self.charac.wisdom > 13:
                    self.points += 2
                    self.charac.wisdom -= 1
                else:
                    self.points += 1
                    self.charac.wisdom -= 1
        self.wisDisFrame.config(text = str(self.charac.wisdom))
        self.pointTotal["text"]= self.points
        
    def decreaseCha(self):
        if self.charac.charisma == 8:
            pass
        else:
            if self.points == 27:
                    pass
            else:
                if self.charac.charisma > 13:
                    self.points += 2
                    self.charac.charisma -= 1
                else:
                    self.points += 1
                    self.charac.charisma -= 1
        self.chaDisFrame.config(text = str(self.charac.charisma))
        self.pointTotal["text"]= self.points
        
    def openName(self):
        if self.points != 0:
            pass
        else:
            self.guiManager.gameManager.newGame = 1
            self.window.destroy()
            self.guiManager.openWindow("name")
            
    def openMain(self):
        if self.points != 0:
            pass
        else:
            self.charac.XP = 0
            self.guiManager.openWindow("main")
            self.window.destroy()
    
class mainGUI(AbstractGUI):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.guiManager = manager
        self.par = parent
        self.window.geometry("500x800+100+100")
        self.gManager = self.guiManager.gameManager
        self.wait = False
        mainFrame = Frame(self.window, width = 100)
        mainFrame.grid()
        self.menuButton = Button(mainFrame, text = "Menu", command=self.openMenu)
        self.menuButton.grid(row=1, column=1)
        scrollbar = Scrollbar(mainFrame)
        scrollbar.grid(row=2, column=2)
        self.conversationText = Text(mainFrame, yscroll = scrollbar.set, height = 40, width = 50, stat="normal", wrap=WORD)
        self.conversationText.grid(row=2, column=1)
        self.conversationText.insert(END, self.gManager.conversationDict[self.gManager.convoIndex])
        self.conversationText.configure(state="disabled")
        scrollbar.config(command = self.conversationText.yview)
        optionFrame = Frame(self.window, width = 100)
        optionFrame.grid()
        self.option1 = Button(optionFrame, text = self.gManager.optionsDict[self.gManager.convoIndex][0], command=self.option1)
        self.option1.grid(row=1, column=1, padx = 10, pady = 10)
        self.option2 = Button(optionFrame, text = self.gManager.optionsDict[self.gManager.convoIndex][1], command=self.option2)
        self.option2.grid(row=1, column=2, padx = 10, pady = 10)
        self.option3 = Button(optionFrame, text = self.gManager.optionsDict[self.gManager.convoIndex][2], command=self.option3)
        self.option3.grid(row=2, column=1, padx = 10, pady = 10)
        self.option4 = Button(optionFrame, text = self.gManager.optionsDict[self.gManager.convoIndex][3], command=self.option4)
        self.option4.grid(row=2, column=2, padx = 10, pady = 10)
        
    def option1(self):
        if self.gManager.mode == "Story":
            self.conversationText.configure(state="normal")
            self.conversationText.insert(END, self.gManager.optionsDict[self.gManager.convoIndex][0]+"\n")
            self.conversationText.configure(state="disabled")
            self.gManager.convoIndex += 1
            if self.gManager.convoIndex == 5:
                self.option2.configure(state="disabled")
                self.option3.configure(state="disabled")
                self.option4.configure(state="disabled")
                self.option1["text"] = "Continue"
                self.menuButton.configure(state="disabled")
                self.combat(5)
            else:
                self.conversationText.configure(state="normal")
                self.conversationText.insert(END, self.gManager.conversationDict[self.gManager.convoIndex]+"\n")
                self.conversationText.configure(state="disabled")
                self.option1["text"] = self.gManager.optionsDict[self.gManager.convoIndex][0]
                self.option2["text"] = self.gManager.optionsDict[self.gManager.convoIndex][1]
                self.option3["text"] = self.gManager.optionsDict[self.gManager.convoIndex][2]
                self.option4["text"] = self.gManager.optionsDict[self.gManager.convoIndex][3]
        else:
            self.wait = False
            self.combat(0)
            if self.gManager.turn+1 == len(self.gManager.turnOrder):
                if self.gManager.turnOrder[0][1].player == True:
                    self.option2.configure(state="normal")
                    self.option2["text"] = "Inventory"
            elif self.gManager.turnOrder[self.gManager.turn+1][1].player == True:
                    self.option2.configure(state="normal")
                    self.option2["text"] = "Inventory"
            else:
                    self.option2.configure(state="disabled")
    
    def option2(self):
        if self.gManager.mode == "Story":
            self.conversationText.configure(state="normal")
            self.conversationText.insert(END, self.gManager.optionsDict[self.gManager.convoIndex][1]+"\n")
            self.conversationText.configure(state="disabled")
            self.gManager.convoIndex += 1
            if self.gManager.convoIndex == 5:
                self.option2.configure(state="disabled")
                self.option3.configure(state="disabled")
                self.option4.configure(state="disabled")
                self.option1["text"] = "Continue"
                self.menuButton.configure(state="disabled")
                self.combat(5)
            else:
                self.conversationText.configure(state="normal")
                self.conversationText.insert(END, self.gManager.conversationDict[self.gManager.convoIndex]+"\n")
                self.conversationText.configure(state="disabled")
                self.option1["text"] = self.gManager.optionsDict[self.gManager.convoIndex][0]
                self.option2["text"] = self.gManager.optionsDict[self.gManager.convoIndex][1]
                self.option3["text"] = self.gManager.optionsDict[self.gManager.convoIndex][2]
                self.option4["text"] = self.gManager.optionsDict[self.gManager.convoIndex][3]
        else:
            self.guiManager.openWindow("inventory")
    
    def option3(self):
        self.conversationText.configure(state="normal")
        self.conversationText.insert(END, self.gManager.optionsDict[self.gManager.convoIndex][2]+"\n")
        self.conversationText.configure(state="disabled")
        self.gManager.convoIndex += 1
        if self.gManager.convoIndex == 5:
            self.option2.configure(state="disabled")
            self.option3.configure(state="disabled")
            self.option4.configure(state="disabled")
            self.menuButton.configure(state="disabled")
            self.option1["text"] = "Continue"
            self.combat(5)
        else:
            self.conversationText.configure(state="normal")
            self.conversationText.insert(END, self.gManager.conversationDict[self.gManager.convoIndex]+"\n")
            self.conversationText.configure(state="disabled")
            self.option1["text"] = self.gManager.optionsDict[self.gManager.convoIndex][0]
            self.option2["text"] = self.gManager.optionsDict[self.gManager.convoIndex][1]
            self.option3["text"] = self.gManager.optionsDict[self.gManager.convoIndex][2]
            self.option4["text"] = self.gManager.optionsDict[self.gManager.convoIndex][3]
    
    def option4(self):
        self.conversationText.configure(state="normal")
        self.conversationText.insert(END, self.gManager.optionsDict[self.gManager.convoIndex][3]+"\n")
        self.conversationText.configure(state="disabled")
        self.gManager.convoIndex += 1
        if self.gManager.convoIndex == 5:
            self.option2.configure(state="disabled")
            self.option3.configure(state="disabled")
            self.option4.configure(state="disabled")
            self.option1["text"] = "Continue"
            self.menuButton.configure(state="disabled")
            self.combat(5)
        else:
            self.conversationText.configure(state="normal")
            self.conversationText.insert(END, self.gManager.conversationDict[self.gManager.convoIndex]+"\n")
            self.conversationText.configure(state="disabled")
            self.option1["text"] = self.gManager.optionsDict[self.gManager.convoIndex][0]
            self.option2["text"] = self.gManager.optionsDict[self.gManager.convoIndex][1]
            self.option3["text"] = self.gManager.optionsDict[self.gManager.convoIndex][2]
            self.option4["text"] = self.gManager.optionsDict[self.gManager.convoIndex][3]
    
    def openMenu(self):
        self.guiManager.openWindow("menu")
        self.hide()
            
    def openTarget(self):
        self.guiManager.openWindow("target")
        self.hide()
    
    def load(self):
        self.window.destroy()
        self.__init__(self.par, self.guiManager)
        
    def combat(self, difficulty):
        self.gManager.mode = "Combat"
        count = 0
        currentId = 5
        if len(self.gManager.currentEnemies) == 0:
            while count < difficulty:
                enemynum = self.gManager.rollDice(5)
                enemy = deepcopy(self.gManager.enemiesDict[enemynum])
                enemy.setID(currentId)
                currentId += 1
                self.gManager.currentEnemies.append(enemy)
                count += 1
        
            self.gManager.fullinitiative()
            self.gManager.lootNum = difficulty
        
        while self.wait == True:
            pass
        self.gManager.RandomEncounter()
        self.wait = True
    
class targetGUI(AbstractGUI):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.guiManager = manager
        self.window.geometry("400x400+100+100")
        self.proficiency = self.guiManager.gameManager.currentCharacters[0].proficiency
        self.time = 0
        self.index = 0
        self.index2 = 1
        self.index3 = 2
        self.index4 = 3
        self.target = 0
        self.gManager = self.guiManager.gameManager
        self.enemies = self.gManager.currentEnemies
        targetFrame = Frame(self.window, width = 400)
        targetFrame.grid()
        scrollUpButton = Button(targetFrame, text = "^", command = self.scrollUp, width=20)
        scrollUpButton.grid(row=1, column=1)
        self.selectFrame = Frame(targetFrame, width = 400)
        self.selectFrame.grid()
        self.selectFrame.grid(row=2, column=1)
        self.spellFrame = Frame(targetFrame, width = 400)
        self.spellFrame.grid()
        self.spellFrame.grid(row=2, column=1)
        self.enemy1 = Button(self.selectFrame, text=self.gManager.currentEnemies[0].name, command=self.attack1, width=20)
        self.enemy1.grid(row=1, column=1)
        if len(self.gManager.currentEnemies) > 1:
            self.enemy2 = Button(self.selectFrame, text=self.gManager.currentEnemies[1].name, command=self.attack2, width=20)
            self.enemy2.grid(row=2, column=1)
        if len(self.gManager.currentEnemies) > 2:
            self.enemy3 = Button(self.selectFrame, text=self.gManager.currentEnemies[2].name, command=self.attack3, width=20)
            self.enemy3.grid(row=3, column=1)
        if len(self.gManager.currentEnemies) > 3:
            self.enemy4 = Button(self.selectFrame, text=self.gManager.currentEnemies[3].name, command=self.attack4, width=20)
            self.enemy4.grid(row=4, column=1)
            
        self.spell1 = Button(self.spellFrame, text=self.gManager.currentCharacters[0].spells[0], command=self.spell1, width=20)
        self.spell1.grid(row=1, column=1)
        if len(self.gManager.currentCharacters[0].spells) > 1:
            self.spell2 = Button(self.spellFrame, text=self.gManager.currentCharacters[0].spells[1], command=self.spell2, width=20)
            self.spell2.grid(row=2, column=1)
        if len(self.gManager.currentCharacters[0].spells) > 2:
            self.spell3 = Button(self.spellFrame, text=self.gManager.currentCharacters[0].spells[2], command=self.spell3, width=20)
            self.spell3.grid(row=3, column=1)
        if len(self.gManager.currentCharacters[0].spells) > 3:
            self.spell4 = Button(self.spellFrame, text=self.gManager.currentCharacters[0].spells[3], command=self.spell4, width=20)
            self.spell4.grid(row=4, column=1)
        
        if self.proficiency == "Martial":
            self.selectFrame.tkraise()
        else:
            self.spellFrame.tkraise()
        scrollDownButton = Button(targetFrame,text= "v", command = self.scrollDown, width=20)
        scrollDownButton.grid(row=3, column=1)
        confirmButton = Button(targetFrame, text= "Comfirm", command=self.confirm)
        confirmButton.grid(row=4, column=1)
        
    def scrollUp(self):
        if self.proficiency == "Magic" and self.time == 0:
            if len(self.gManager.currentCharacters[0].spells) < 5:
                pass
            else:
                self.index += 1
                self.index2 += 1
                self.index3 += 1
                self.index4 += 1
                if self.index >= len(self.gManager.currentCharacters[0].spells):
                    self.index = 0
                    self.spell1["text"] = self.gManager.currentCharacters[0].spells[self.index]
                    self.spell2["text"] = self.gManager.currentCharacters[0].spells[self.index2]
                    self.spell3["text"] = self.gManager.currentCharacters[0].spells[self.index3]
                    self.spell4["text"] = self.gManager.currentCharacters[0].spells[self.index4]
                elif self.index2 >= len(self.gManager.currentCharacters[0].spells):
                    self.spell1["text"] = self.gManager.currentCharacters[0].spells[self.index]
                    self.index2 = 0
                    self.spell2["text"] = self.gManager.currentCharacters[0].spells[self.index2]
                    self.spell3["text"] = self.gManager.currentCharacters[0].spells[self.index3]
                    self.spell4["text"] = self.gManager.currentCharacters[0].spells[self.index4]
                elif self.index3 >= len(self.gManager.currentCharacters[0].spells):
                    self.spell1["text"] = self.gManager.currentCharacters[0].spells[self.index]
                    self.spell2["text"] = self.gManager.currentCharacters[0].spells[self.index2]
                    self.index3 = 0
                    self.spell3["text"] = self.gManager.currentCharacters[0].spells[self.index3]
                    self.spell4["text"] = self.gManager.currentCharacters[0].spells[self.index4]
                elif self.index4 >= len(self.gManager.currentCharacters[0].spells):
                    self.spell1["text"] = self.gManager.currentCharacters[0].spells[self.index]
                    self.spell2["text"] = self.gManager.currentCharacters[0].spells[self.index2]
                    self.spell3["text"] = self.gManager.currentCharacters[0].spells[self.index3]
                    self.index4 = 0
                    self.spell4["text"] = self.gManager.currentCharacters[0].spells[self.index4]
                else:
                    self.spell1["text"] = self.gManager.currentCharacters[0].spells[self.index]
                    self.spell2["text"] = self.gManager.currentCharacters[0].spells[self.index2]
                    self.spell3["text"] = self.gManager.currentCharacters[0].spells[self.index3]
                    self.spell4["text"] = self.gManager.currentCharacters[0].spells[self.index4]
        else:
            if len(self.gManager.currentEnemies) < 5:
                pass
            else:
                self.index += 1
                self.index2 += 1
                self.index3 += 1
                self.index4 += 1
                if self.index >= len(self.gManager.currentEnemies):
                    self.index = 0
                    self.enemy1["text"] = self.gManager.currentEnemies[self.index].name
                    self.enemy2["text"] = self.gManager.currentEnemies[self.index2].name
                    self.enemy3["text"] = self.gManager.currentEnemies[self.index3].name
                    self.enemy4["text"] = self.gManager.currentEnemies[self.index4].name
                elif self.index2 >= len(self.gManager.currentEnemies):
                    self.enemy1["text"] = self.gManager.currentEnemies[self.index].name
                    self.index2 = 0
                    self.enemy2["text"] = self.gManager.currentEnemies[self.index2].name
                    self.enemy3["text"] = self.gManager.currentEnemies[self.index3].name
                    self.enemy4["text"] = self.gManager.currentEnemies[self.index4].name
                elif self.index3 >= len(self.gManager.currentEnemies):
                    self.enemy1["text"] = self.gManager.currentEnemies[self.index].name
                    self.enemy2["text"] = self.gManager.currentEnemies[self.index2].name
                    self.index3 = 0
                    self.enemy3["text"] = self.gManager.currentEnemies[self.index3].name
                    self.enemy4["text"] = self.gManager.currentEnemies[self.index4].name
                elif self.index4 >= len(self.gManager.currentEnemies):
                    self.enemy1["text"] = self.gManager.currentEnemies[self.index].name
                    self.enemy2["text"] = self.gManager.currentEnemies[self.index2].name
                    self.enemy3["text"] = self.gManager.currentEnemies[self.index3].name
                    self.index4 = 0
                    self.enemy4["text"] = self.gManager.currentEnemies[self.index4].name
                else:
                    self.enemy1["text"] = self.gManager.currentEnemies[self.index].name
                    self.enemy2["text"] = self.gManager.currentEnemies[self.index2].name
                    self.enemy3["text"] = self.gManager.currentEnemies[self.index3].name
                    self.enemy4["text"] = self.gManager.currentEnemies[self.index4].name
                
    
    def scrollDown(self):
        if self.proficiency == "Magic" and self.time == 0:
            if len(self.gManager.currentCharacters[0].spells) < 5:
                pass
            else:
                self.index -= 1
                self.index2 -= 1
                self.index3 -= 1
                self.index4 -= 1
                if self.index == (len(self.gManager.currentCharacters[0].spells)+1)* -1:
                    self.index = -1
                    self.spell1["text"] = self.gManager.currentCharacters[0].spells[self.index]
                    self.spell2["text"] = self.gManager.currentCharacters[0].spells[self.index2]
                    self.spell3["text"] = self.gManager.currentCharacters[0].spells[self.index3]
                    self.spell4["text"] = self.gManager.currentCharacters[0].spells[self.index4]
                elif self.index2 == (len(self.gManager.currentCharacters[0].spells)+1) * -1:
                    self.spell1["text"] = self.gManager.currentCharacters[0].spells[self.index]
                    self.index2 = -1
                    self.spell2["text"] = self.gManager.currentCharacters[0].spells[self.index2]
                    self.spell3["text"] = self.gManager.currentCharacters[0].spells[self.index3]
                    self.spell4["text"] = self.gManager.currentCharacters[0].spells[self.index4]
                elif self.index3 == (len(self.gManager.currentCharacters[0].spells)+1) * -1:
                    self.spell1["text"] = self.gManager.currentCharacters[0].spells[self.index]
                    self.spell2["text"] = self.gManager.currentCharacters[0].spells[self.index2]
                    self.index3 = -1
                    self.spell3["text"] = self.gManager.currentCharacters[0].spells[self.index3]
                    self.spell4["text"] = self.gManager.currentCharacters[0].spells[self.index4]
                elif self.index4 == (len(self.gManager.currentCharacters[0].spells)+1) * -1:
                    self.spell1["text"] = self.gManager.currentCharacters[0].spells[self.index]
                    self.spell2["text"] = self.gManager.currentCharacters[0].spells[self.index2]
                    self.spell3["text"] = self.gManager.currentCharacters[0].spells[self.index3]
                    self.index4 = -1
                    self.spell4["text"] = self.gManager.currentCharacters[0].spells[self.index4]
                else:
                    self.spell1["text"] = self.gManager.currentCharacters[0].spells[self.index]
                    self.spell2["text"] = self.gManager.currentCharacters[0].spells[self.index2]
                    self.spell3["text"] = self.gManager.currentCharacters[0].spells[self.index3]
                    self.spell4["text"] = self.gManager.currentCharacters[0].spells[self.index4]
        else:
            if len(self.gManager.currentEnemies) < 5:
                pass
            else:
                self.index -= 1
                self.index2 -= 1
                self.index3 -= 1
                self.index4 -= 1
                if self.index == (len(self.gManager.currentEnemies)+1) * -1:
                    self.index = -1
                    self.enemy1["text"] = self.gManager.currentEnemies[self.index].name
                    self.enemy2["text"] = self.gManager.currentEnemies[self.index2].name
                    self.enemy3["text"] = self.gManager.currentEnemies[self.index3].name
                    self.enemy4["text"] = self.gManager.currentEnemies[self.index4].name
                elif self.index2 == (len(self.gManager.currentEnemies)+1) * -1:
                    self.enemy1["text"] = self.gManager.currentEnemies[self.index].name
                    self.index2 = -1
                    self.enemy2["text"] = self.gManager.currentEnemies[self.index2].name
                    self.enemy3["text"] = self.gManager.currentEnemies[self.index3].name
                    self.enemy4["text"] = self.gManager.currentEnemies[self.index4].name
                elif self.index3 == (len(self.gManager.currentEnemies)+1) * -1:
                    self.enemy1["text"] = self.gManager.currentEnemies[self.index].name
                    self.enemy2["text"] = self.gManager.currentEnemies[self.index2].name
                    self.index3 = -1
                    self.enemy3["text"] = self.gManager.currentEnemies[self.index3].name
                    self.enemy4["text"] = self.gManager.currentEnemies[self.index4].name
                elif self.index4 == (len(self.gManager.currentEnemies)+1) * -1:
                    self.enemy1["text"] = self.gManager.currentEnemies[self.index].name
                    self.enemy2["text"] = self.gManager.currentEnemies[self.index2].name
                    self.enemy3["text"] = self.gManager.currentEnemies[self.index3].name
                    self.index4 = -1
                    self.enemy4["text"] = self.gManager.currentEnemies[self.index4].name
                else:
                    self.enemy1["text"] = self.gManager.currentEnemies[self.index].name
                    self.enemy2["text"] = self.gManager.currentEnemies[self.index2].name
                    self.enemy3["text"] = self.gManager.currentEnemies[self.index3].name
                    self.enemy4["text"] = self.gManager.currentEnemies[self.index4].name
    
    def attack1(self):
        self.target = self.index
    
    def attack2(self):
        self.target = self.index2
        
    def attack3(self):
        self.target = self.index3
        
    def attack4(self):
        self.target = self.index4
        
    def confirm(self):
        if self.proficiency == "Magic" and self.time == 0:
            self.time = 1
            self.index1 = 0
            self.index2 = 1
            self.index3 = 2
            self.index4 = 3
            self.selectFrame.tkraise()
        else:
            self.gManager.currentCharacters[0].attack(self.enemies[self.target], self.gManager, self.gManager.weaponDamDict[self.gManager.currentCharacters[0].weapon.name])
            self.openMain()
    
    def spell1(self):
        self.gManager.currentCharacters[0].setdamagedie(self.gManager.spellDamDict[self.gManager.currentCharacters[0].spells[self.index]])
        self.gManager.currentCharacters[0].setnumdie(self.gManager.spellDieDict[self.gManager.currentCharacters[0].spells[self.index]])
    
    def spell2(self):
        self.gManager.currentCharacters[0].setdamagedie(self.gManager.spellDamDict[self.gManager.currentCharacters[0].spells[self.index2]])
        self.gManager.currentCharacters[0].setnumdie(self.gManager.spellDieDict[self.gManager.currentCharacters[0].spells[self.index2]])
    
    def spell3(self):
        self.gManager.currentCharacters[0].setdamagedie(self.gManager.spellDamDict[self.gManager.currentCharacters[0].spells[self.index3]])
        self.gManager.currentCharacters[0].setnumdie(self.gManager.spellDieDict[self.gManager.currentCharacters[0].spells[self.index3]])
    
    def spell4(self):
        self.gManager.currentCharacters[0].setdamagedie(self.gManager.spellDamDict[self.gManager.currentCharacters[0].spells[self.index4]])
        self.gManager.currentCharacters[0].setnumdie(self.gManager.spellDieDict[self.gManager.currentCharacters[0].spells[self.index4]])
        
    def openMain(self):
        self.guiManager.openWindow("main")
        self.window.destroy()
        
class loadGUI(AbstractGUI):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.guiManager = manager
        self.fManager = self.guiManager.fileManager
        self.window.geometry("400x400+100+100")
        self.index = 0
        self.index2 = 1
        self.index3 = 2
        self.index4 = 3
        self.load = 0
        self.fileList = []
        
        self.fillFileList()
        text1 = ""
        text2 = ""
        text3 = ""
        text4 = ""
        
        if len(self.fileList) == 1:
            text1 = self.fileList[0]
        elif len(self.fileList) == 2:
            text1 = self.fileList[0]
            text2 = self.fileList[1]
        elif len(self.fileList) == 3:
            text1 = self.fileList[0]
            text2 = self.fileList[1]
            text3 = self.fileList[2]
        elif len(self.fileList) >= 3:
            text1 = self.fileList[0]
            text2 = self.fileList[1]
            text3 = self.fileList[2]
            text4 = self.fileList[3]
        
        LoadFrame = Frame(self.window, width = 200)
        LoadFrame.grid()
        ContainFrame = Frame(LoadFrame, width = 200)
        ContainFrame.grid()
        ContainFrame.grid(row=2, column=1)
        self.save1 = Button(ContainFrame, text = text1, command=self.select1)
        self.save1.grid(row=1)
        self.save2 = Button(ContainFrame, text = text2, command=self.select2)
        self.save2.grid(row=2)
        self.save3 = Button(ContainFrame, text = text3, command=self.select3)
        self.save3.grid(row=3)
        self.save4 = Button(ContainFrame, text = text4, command=self.select4)
        self.save4.grid(row=4)
        upButton = Button(LoadFrame, text="^", command=self.scrollUp)
        upButton.grid(row=1, column=1)
        downButton = Button(LoadFrame, text="v", command=self.scrollDown)
        downButton.grid(row=3, column=1)
        loadButton = Button(LoadFrame, text="Load", command=self.loadGame)
        loadButton.grid(row=4, column=5)
        
    def scrollUp(self):
            if len(self.fileList) < 5:
                pass
            else:
                self.index += 1
                self.index2 += 1
                self.index3 += 1
                self.index4 += 1
                if self.index >= len(self.fileList):
                    self.index = 0
                    self.save1["text"] = self.fileList[self.index]
                    self.save2["text"] = self.fileList[self.index2]
                    self.save3["text"] = self.fileList[self.index3]
                    self.save4["text"] = self.fileList[self.index4]
                elif self.index2 >= len(self.fileList):
                    self.save1["text"] = self.fileList[self.index]
                    self.index2 = 0
                    self.save2["text"] = self.fileList[self.index2]
                    self.save3["text"] = self.fileList[self.index3]
                    self.save4["text"] = self.fileList[self.index4]
                elif self.index3 >= len(self.fileList):
                    self.save1["text"] = self.fileList[self.index]
                    self.save2["text"] = self.fileList[self.index2]
                    self.index3 = 0
                    self.save3["text"] = self.fileList[self.index3]
                    self.save4["text"] = self.fileList[self.index4]
                elif self.index4 >= len(self.fileList):
                    self.save1["text"] = self.fileList[self.index]
                    self.save2["text"] = self.fileList[self.index2]
                    self.save3["text"] = self.fileList[self.index3]
                    self.index4 = 0
                    self.save4["text"] = self.fileList[self.index4]
                else:
                    self.save1["text"] = self.fileList[self.index]
                    self.save2["text"] = self.fileList[self.index2]
                    self.save3["text"] = self.fileList[self.index3]
                    self.save4["text"] = self.fileList[self.index4]               
    
    def scrollDown(self):
            if len(self.fileList) < 5:
                pass
            else:
                self.index -= 1
                self.index2 -= 1
                self.index3 -= 1
                self.index4 -= 1
                if self.index == (len(self.fileList)+1) *-1:
                    self.index = -1
                    self.save1["text"] = self.fileList[self.index]
                    self.save2["text"] = self.fileList[self.index2]
                    self.save3["text"] = self.fileList[self.index3]
                    self.save4["text"] = self.fileList[self.index4]
                elif self.index2 == (len(self.fileList)+1) *-1:
                    self.save1["text"] = self.fileList[self.index]
                    self.index2 = -1
                    self.save2["text"] = self.fileList[self.index2]
                    self.save3["text"] = self.fileList[self.index3]
                    self.save4["text"] = self.fileList[self.index4]
                elif self.index3 == (len(self.fileList)+1) *-1:
                    self.save1["text"] = self.fileList[self.index]
                    self.save2["text"] = self.fileList[self.index2]
                    self.index3 = -1
                    self.save3["text"] = self.fileList[self.index3]
                    self.save4["text"] = self.fileList[self.index4]
                elif self.index4 == (len(self.fileList)+1) *-1:
                    self.save1["text"] = self.fileList[self.index]
                    self.save2["text"] = self.fileList[self.index2]
                    self.save3["text"] = self.fileList[self.index3]
                    self.index4 = -1
                    self.save4["text"] = self.fileList[self.index4]
                else:
                    self.save1["text"] = self.fileList[self.index]
                    self.save2["text"] = self.fileList[self.index2]
                    self.save3["text"] = self.fileList[self.index3]
                    self.save4["text"] = self.fileList[self.index4]
    
    def select1(self):
        self.load = self.index
    
    def select2(self):
        self.load = self.index2
    
    def select3(self):
        self.load = self.index3
    
    def select4(self):
        self.load = self.index4
    
    def fillFileList(self):
        cwd = os.getcwd()
        saves = os.listdir(cwd + r"\SaveFiles")
        for entry in saves:
            self.fileList.append(entry)
            
    def loadGame(self):
        self.fManager.load(self.fileList[self.load])
        self.window.destroy()
        self.guiManager.maingui.window.destroy()
        self.guiManager.maingui = mainGUI(self.guiManager.root, self.guiManager)
        
class inventoryGUI(AbstractGUI):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.guiManager = manager
        self.window.geometry("800x800+100+100")
        self.index = 0
        self.index2 = 1
        self.index3 = 2
        self.index4 = 3
        self.characIndex = 0
        self.charac = self.guiManager.gameManager.currentCharacters[self.characIndex]
        self.select = None
        itemFrame = Frame(self.window, width=400)
        itemFrame.grid()
        descFrame = Frame(itemFrame, width=200)
        descFrame.grid(row=2, column=2)
        descFrame.grid()
        selectFrame = Frame(itemFrame, width=200)
        selectFrame.grid(row=2, column=4)
        selectFrame.grid()
        self.itemdesc = Label(descFrame, text=self.guiManager.gameManager.itemdescDict[self.guiManager.gameManager.currentCharacters[0].inventory[self.index].name])
        self.itemdesc.grid(row=1, column=1)
        up = Button(selectFrame, text = "^", command=self.scrollUp)
        up.grid(row=1)
        self.item1 = Button(selectFrame, text=self.guiManager.gameManager.currentCharacters[0].inventory[self.index].name, command = self.displayDesc1)
        self.item1.grid(row=2)
        self.item2 = Button(selectFrame, text=self.guiManager.gameManager.currentCharacters[0].inventory[self.index2].name, command = self.displayDesc2)
        self.item2.grid(row=3)
        self.item3 = Button(selectFrame, text=self.guiManager.gameManager.currentCharacters[0].inventory[self.index3].name, command = self.displayDesc3)
        self.item3.grid(row=4)
        self.item4 = Button(selectFrame, text=self.guiManager.gameManager.currentCharacters[0].inventory[self.index4].name, command = self.displayDesc4)
        self.item4.grid(row=5)
        down = Button(selectFrame, text = "v", command=self.scrollDown)
        down.grid(row=6)
        self.useButton = Button(descFrame, text="Use", command = self.itemproperty)
        self.useButton.grid(row=2)
        self.useButton.configure(state="disabled")
        equipButton = Button(descFrame, text="Equipment", command=self.openEquip)
        equipButton.grid(row=3)
        self.characLabel = Label(itemFrame, text=self.guiManager.gameManager.currentCharacters[0].name)
        self.characLabel.grid(row=1, column=3)
        self.characHealth = Label(itemFrame, text="Health: " + str(self.guiManager.gameManager.currentCharacters[0].health))
        self.characHealth.grid(row=1, column=2)
        left = Button(itemFrame, text="<", command=self.cycleLeft)
        left.grid(row=2, column=1)
        right = Button(itemFrame, text=">", command=self.cycleRight)
        right.grid(row=2, column=5)
        
    def displayDesc1(self):
        self.itemdesc["text"] = self.guiManager.gameManager.itemdescDict[self.guiManager.gameManager.currentCharacters[0].inventory[self.index].name]
        self.select = self.guiManager.gameManager.currentCharacters[0].inventory[self.index]
        if self.guiManager.gameManager.currentCharacters[0].inventory[self.index].hasUse == True:
            self.useButton.configure(state="normal")
        if self.guiManager.gameManager.mode == "Story":
            if self.guiManager.gameManager.currentCharacters[0].inventory[self.index].isEquippable == True:
                self.useButton.configure(state="normal")
                self.useButton["text"] = "Equip"
        
    def displayDesc2(self):
        self.itemdesc["text"] = self.guiManager.gameManager.itemdescDict[self.guiManager.gameManager.currentCharacters[0].inventory[self.index2].name]
        self.select = self.guiManager.gameManager.currentCharacters[0].inventory[self.index2]
        if self.guiManager.gameManager.currentCharacters[0].inventory[self.index2].hasUse == True:
            self.useButton.configure(state="normal")
        if self.guiManager.gameManager.mode == "Story":
            if self.guiManager.gameManager.currentCharacters[0].inventory[self.index2].isEquippable == True:
                self.useButton.configure(state="normal")
                self.useButton["text"] = "Equip"
        
    def displayDesc3(self):
        self.itemdesc["text"] = self.guiManager.gameManager.itemdescDict[self.guiManager.gameManager.currentCharacters[0].inventory[self.index3].name]
        self.select = self.guiManager.gameManager.currentCharacters[0].inventory[self.index3]
        if self.guiManager.gameManager.currentCharacters[0].inventory[self.index3].hasUse == True:
            self.useButton.configure(state="normal")
        if self.guiManager.gameManager.mode == "Story":
            if self.guiManager.gameManager.currentCharacters[0].inventory[self.index3].isEquippable == True:
                self.useButton.configure(state="normal")
                self.useButton["text"] = "Equip"
        
    def displayDesc4(self):
        self.itemdesc["text"] = self.guiManager.gameManager.itemdescDict[self.guiManager.gameManager.currentCharacters[0].inventory[self.index4].name]
        self.select = self.guiManager.gameManager.currentCharacters[0].inventory[self.index4]
        if self.guiManager.gameManager.currentCharacters[0].inventory[self.index4].hasUse == True:
            self.useButton.configure(state="normal")
        if self.guiManager.gameManager.mode == "Story":
            if self.guiManager.gameManager.currentCharacters[0].inventory[self.index4].isEquippable == True:
                self.useButton.configure(state="normal")
                self.useButton["text"] = "Equip"
        
    def scrollUp(self):
            if len(self.guiManager.gameManager.currentCharacters[0].inventory) < 5:
                pass
            else:
                self.index += 1
                self.index2 += 1
                self.index3 += 1
                self.index4 += 1
                if self.index >= len(self.guiManager.gameManager.currentCharacters[0].inventory):
                    self.index = 0
                    self.item1["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index].name
                    self.item2["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index2].name
                    self.item3["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index3].name
                    self.item4["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index4].name
                elif self.index2 >= len(self.guiManager.gameManager.currentCharacters[0].inventory):
                    self.item1["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index].name
                    self.index2 = 0
                    self.item2["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index2].name
                    self.item3["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index3].name
                    self.item4["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index4].name
                elif self.index3 >= len(self.guiManager.gameManager.currentCharacters[0].inventory):
                    self.item1["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index].name
                    self.item2["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index2].name
                    self.index3 = 0
                    self.item3["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index3].name
                    self.item4["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index4].name
                elif self.index4 >= len(self.guiManager.gameManager.currentCharacters[0].inventory):
                    self.item1["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index].name
                    self.item2["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index2].name
                    self.item3["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index3].name
                    self.index4 = 0
                    self.item4["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index4].name
                else:
                    self.item1["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index].name
                    self.item2["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index2].name
                    self.item3["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index3].name
                    self.item4["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index4].name          
    
    def scrollDown(self):
            if len(self.guiManager.gameManager.currentCharacters[0].inventory) < 5:
                pass
            else:
                self.index -= 1
                self.index2 -= 1
                self.index3 -= 1
                self.index4 -= 1
                if self.index == (len(self.guiManager.gameManager.currentCharacters[0].inventory)+1) *-1:
                    self.index = -1
                    self.item1["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index].name
                    self.item2["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index2].name
                    self.item3["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index3].name
                    self.item4["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index4].name
                elif self.index2 == (len(self.guiManager.gameManager.currentCharacters[0].inventory)+1) *-1:
                    self.item1["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index].name
                    self.index2 = -1
                    self.item2["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index2].name
                    self.item3["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index3].name
                    self.item4["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index4].name
                elif self.index3 == (len(self.guiManager.gameManager.currentCharacters[0].inventory)+1) *-1:
                    self.item1["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index].name
                    self.item2["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index2].name
                    self.index3 = -1
                    self.item3["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index3].name
                    self.item4["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index4].name
                elif self.index4 == (len(self.guiManager.gameManager.currentCharacters[0].inventory)+1) *-1:
                    self.item1["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index].name
                    self.item2["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index2].name
                    self.item3["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index3].name
                    self.index4 = -1
                    self.item4["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index4].name
                else:
                    self.item1["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index].name
                    self.item2["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index2].name
                    self.item3["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index3].name
                    self.item4["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.index4].name
                    
    def cycleRight(self):
        self.characIndex += 1
        if self.characIndex >= len(self.guiManager.gameManager.currentCharacters):
            self.characIndex = 0
        self.charac = self.guiManager.gameManager.currentCharacters[self.characIndex]
        self.characLabel["text"] = self.charac.name
        self.characHealth["text"] = "Health: " + str(self.charac.health)
    
    def cycleLeft(self):
        self.characIndex -= 1
        if self.characIndex == (len(self.guiManager.gameManager.currentCharacters)+1) * -1:
            self.characIndex = -1
        self.charac = self.guiManager.gameManager.currentCharacters[self.characIndex]
        self.characLabel["text"] = self.charac.name
        self.characHealth["text"] = "Health: " + str(self.charac.health)
                    
    def itemproperty(self):
        if self.select.hasUse == True:
            self.select.use(self.charac, self.guiManager.gameManager, 0)
            self.charac.inventory.remove(self.select)
        elif self.select.isEquippable == True:
            if self.charac.equipment != self.select.name:
                if self.select.isArmor == True:
                    oldArmor = self.charac.equipment.armorVal
                    self.charac.equipment = self.select
                    self.charac.armor += self.select.armorVal - oldArmor
                elif self.select.isWeapon == True:
                    self.charac.weapon = self.select
                    self.charac.damageDie = self.select.damagedie
    
    def openEquip(self):
        self.guiManager.openWindow("equip")
        self.window.destroy()
        
class shopGUI(AbstractGUI):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.guiManager = manager
        self.window.geometry("800x800+100+100")
        self.cindex = 0
        self.cindex2 = 1
        self.cindex3 = 2
        self.cindex4 = 3
        self.mindex = 0
        self.mindex2 = 1
        self.mindex3 = 2
        self.mindex4 = 3
        self.buylist = []
        self.selllist = []
        self.select = None
        self.cchanges = 0
        self.mchanges = 0
        shopFrame = Frame(self.window, width=600)
        shopFrame.grid()
        merchantFrame = Frame(shopFrame)
        merchantFrame.grid(row=1, column=1)
        merchantFrame.grid()
        characterFrame = Frame(shopFrame)
        characterFrame.grid(row=1, column=3)
        characterFrame.grid()
        mcontext = Label(merchantFrame, text="Merchant")
        mcontext.grid(row=1)
        ccontext = Label(characterFrame, text="Character")
        ccontext.grid(row=1)
        mupButton = Button(merchantFrame, text = "^", command = self.mscrollUp)
        mupButton.grid(row=2)
        mdownButton = Button(merchantFrame, text = "v", command = self.mscrollDown)
        mdownButton.grid(row=7)
        cupButton = Button(characterFrame, text = "^", command = self.cscrollUp)
        cupButton.grid(row=2)
        cdownButton = Button(characterFrame, text = "v", command = self.cscrollDown)
        cdownButton.grid(row=7)
        self.mitem1 = Button(merchantFrame, text=self.guiManager.gameManager.currentMerchant.inventory[0].name, command = self.buy)
        self.mitem1.grid(row=3)
        self.mitem2 = Button(merchantFrame, text=self.guiManager.gameManager.currentMerchant.inventory[1].name, command = self.buy2)
        self.mitem2.grid(row=4)
        self.mitem3 = Button(merchantFrame, text=self.guiManager.gameManager.currentMerchant.inventory[2].name, command = self.buy3)
        self.mitem3.grid(row=5)
        self.mitem4 = Button(merchantFrame, text=self.guiManager.gameManager.currentMerchant.inventory[3].name, command = self.buy4)
        self.mitem4.grid(row=6)
        self.citem1 = Button(characterFrame, text=self.guiManager.gameManager.currentCharacters[0].inventory[0].name, command = self.sell)
        self.citem1.grid(row=3)
        self.citem2 = Button(characterFrame, text=self.guiManager.gameManager.currentCharacters[0].inventory[1].name, command = self.sell2)
        self.citem2.grid(row=4)
        self.citem3 = Button(characterFrame, text=self.guiManager.gameManager.currentCharacters[0].inventory[2].name, command = self.sell3)
        self.citem3.grid(row=5)
        self.citem4 = Button(characterFrame, text=self.guiManager.gameManager.currentCharacters[0].inventory[3].name, command = self.sell4)
        self.citem4.grid(row=6)
        self.descLabel = Label(shopFrame, text="No item selected yet")
        self.descLabel.grid(row=1, column=2)
        self.mmoney = Label(merchantFrame, text=self.guiManager.gameManager.currentMerchant.money)
        self.mmoney.grid(row=8)
        self.cmoney = Label(characterFrame, text=self.guiManager.gameManager.currentCharacters[0].money)
        self.cmoney.grid(row=8)
        self.ival = Label(shopFrame, text="No value")
        self.ival.grid(row=2, column=2)
        self.mchange = Label(merchantFrame, text="No change yet")
        self.mchange.grid(row=9)
        self.cchange = Label(characterFrame, text="No change yet")
        self.cchange.grid(row=9)
        exchangeButton = Button(shopFrame, text="Confirm", command = self.change)
        exchangeButton.grid(row=3, column=2)
        
    def mscrollUp(self):
            if len(self.guiManager.gameManager.currentMerchant.inventory) < 5:
                pass
            else:
                self.mindex += 1
                self.mindex2 += 1
                self.mindex3 += 1
                self.mindex4 += 1
                if self.mindex >= len(self.guiManager.gameManager.currentMerchant.inventory):
                    self.mindex = 0
                    self.mitem1["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex].name
                    self.mitem2["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex2].name
                    self.mitem3["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex3].name
                    self.mitem4["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex4].name
                elif self.mindex2 >= len(self.guiManager.gameManager.currentMerchant.inventory):
                    self.mitem1["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex].name
                    self.mindex2 = 0
                    self.mitem2["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex2].name
                    self.mitem3["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex3].name
                    self.mitem4["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex4].name
                elif self.mindex3 >= len(self.guiManager.gameManager.currentMerchant.inventory):
                    self.mitem1["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex].name
                    self.mitem2["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex2].name
                    self.mindex3 = 0
                    self.mitem3["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex3].name
                    self.mitem4["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex4].name
                elif self.mindex4 >= len(self.guiManager.gameManager.currentMerchant.inventory):
                    self.mitem1["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex].name
                    self.mitem2["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex2].name
                    self.mitem3["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex3].name
                    self.mindex4 = 0
                    self.mitem4["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex4].name
                else:
                    self.mitem1["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex].name
                    self.mitem2["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex2].name
                    self.mitem3["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex3].name
                    self.mitem4["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex4].name
    
    def mscrollDown(self):
            if len(self.guiManager.gameManager.currentMerchant.inventory) < 5:
                pass
            else:
                self.mindex -= 1
                self.mindex2 -= 1
                self.mindex3 -= 1
                self.mindex4 -= 1
                if self.mindex == (len(self.guiManager.gameManager.currentMerchant.inventory)+1) *-1:
                    self.mindex = -1
                    self.mitem1["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex].name
                    self.mitem2["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex2].name
                    self.mitem3["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex3].name
                    self.mitem4["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex4].name
                elif self.mindex2 == (len(self.guiManager.gameManager.currentMerchant.inventory)+1) *-1:
                    self.mitem1["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex].name
                    self.mindex2 = -1
                    self.mitem2["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex2].name
                    self.mitem3["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex3].name
                    self.mitem4["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex4].name
                elif self.mindex3 == (len(self.guiManager.gameManager.currentMerchant.inventory)+1) *-1:
                    self.mitem1["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex].name
                    self.mitem2["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex2].name
                    self.mindex3 = -1
                    self.mitem3["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex3].name
                    self.mitem4["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex4].name
                elif self.mindex4 == (len(self.guiManager.gameManager.currentMerchant.inventory)+1) *-1:
                    self.mitem1["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex].name
                    self.mitem2["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex2].name
                    self.mitem3["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex3].name
                    self.mindex4 = -1
                    self.mitem4["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex4].name
                else:
                    self.mitem1["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex].name
                    self.mitem2["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex2].name
                    self.mitem3["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex3].name
                    self.mitem4["text"] = self.guiManager.gameManager.currentMerchant.inventory[self.mindex4].name
    
    def cscrollUp(self):
            if len(self.guiManager.gameManager.currentCharacters[0].inventory) < 5:
                pass
            else:
                self.cindex += 1
                self.cindex2 += 1
                self.cindex3 += 1
                self.cindex4 += 1
                if self.cindex >= len(self.guiManager.gameManager.currentCharacters[0].inventory):
                    self.cindex = 0
                    self.citem1["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex].name
                    self.citem2["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex2].name
                    self.citem3["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex3].name
                    self.citem4["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex4].name
                elif self.cindex2 >= len(self.guiManager.gameManager.currentCharacters[0].inventory):
                    self.citem1["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex].name
                    self.cindex2 = 0
                    self.citem2["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex2].name
                    self.citem3["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex3].name
                    self.citem4["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex4].name
                elif self.cindex3 >= len(self.guiManager.gameManager.currentCharacters[0].inventory):
                    self.citem1["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex].name
                    self.citem2["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex2].name
                    self.cindex3 = 0
                    self.citem3["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex3].name
                    self.citem4["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex4].name
                elif self.cindex4 >= len(self.guiManager.gameManager.currentCharacters[0].inventory):
                    self.citem1["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex].name
                    self.citem2["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex2].name
                    self.citem3["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex3].name
                    self.cindex4 = 0
                    self.citem4["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex4].name
                else:
                    self.citem1["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex].name
                    self.citem2["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex2].name
                    self.citem3["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex3].name
                    self.citem4["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex4].name               
    
    def cscrollDown(self):
            if len(self.guiManager.gameManager.currentCharacters[0].inventory) < 5:
                pass
            else:
                self.cindex -= 1
                self.cindex2 -= 1
                self.cindex3 -= 1
                self.cindex4 -= 1
                if self.cindex == (len(self.guiManager.gameManager.currentCharacters[0].inventory)+1) *-1:
                    self.cindex = -1
                    self.citem1["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex].name
                    self.citem2["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex2].name
                    self.citem3["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex3].name
                    self.citem4["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex4].name
                elif self.cindex2 == (len(self.guiManager.gameManager.currentCharacters[0].inventory)+1) *-1:
                    self.citem1["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex].name
                    self.cindex2 = -1
                    self.citem2["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex2].name
                    self.citem3["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex3].name
                    self.citem4["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex4].name
                elif self.cindex3 == (len(self.guiManager.gameManager.currentCharacters[0].inventory)+1) *-1:
                    self.citem1["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex].name
                    self.citem2["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex2].name
                    self.cindex3 = -1
                    self.citem3["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex3].name
                    self.citem4["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex4].name
                elif self.cindex4 == (len(self.guiManager.gameManager.currentCharacters[0].inventory)+1) *-1:
                    self.citem1["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex].name
                    self.citem2["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex2].name
                    self.citem3["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex3].name
                    self.cindex4 = -1
                    self.citem4["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex4].name
                else:
                    self.citem1["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex].name
                    self.citem2["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex2].name
                    self.citem3["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex3].name
                    self.citem4["text"] = self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex4].name
    
    def buy(self):
        if self.guiManager.gameManager.currentMerchant.inventory[self.mindex] not in self.buylist:
            self.buylist.append(self.guiManager.gameManager.currentMerchant.inventory[self.mindex])
            self.descLabel["text"] = self.guiManager.gameManager.itemdescDict[self.guiManager.gameManager.currentMerchant.inventory[self.mindex].name]
            self.ival["text"] = str(self.guiManager.gameManager.currentMerchant.inventory[self.mindex].value)
            self.cchanges -= self.guiManager.gameManager.currentMerchant.inventory[self.mindex].value
            self.cchange["text"] = str(self.cchanges)
        else:
            self.buylist.remove(self.guiManager.gameManager.currentMerchant.inventory[self.mindex])
            self.descLabel["text"] = self.guiManager.gameManager.itemdescDict[self.guiManager.gameManager.currentMerchant.inventory[self.mindex].name]
            self.ival["text"] = str(self.guiManager.gameManager.currentMerchant.inventory[self.mindex].value)
            self.cchanges += self.guiManager.gameManager.currentMerchant.inventory[self.mindex].value
            self.cchange["text"] = str(self.cchanges)
    
    def buy2(self):
        if self.guiManager.gameManager.currentMerchant.inventory[self.mindex2] not in self.buylist:
            self.buylist.append(self.guiManager.gameManager.currentMerchant.inventory[self.mindex2])
            self.descLabel["text"] = self.guiManager.gameManager.itemdescDict[self.guiManager.gameManager.currentMerchant.inventory[self.mindex2].name]
            self.ival["text"] = str(self.guiManager.gameManager.currentMerchant.inventory[self.mindex2].value)
            self.cchanges -= self.guiManager.gameManager.currentMerchant.inventory[self.mindex2].value
            self.cchange["text"] = str(self.cchanges)
        else:
            self.buylist.remove(self.guiManager.gameManager.currentMerchant.inventory[self.mindex2])
            self.descLabel["text"] = self.guiManager.gameManager.itemdescDict[self.guiManager.gameManager.currentMerchant.inventory[self.mindex2].name]
            self.ival["text"] = str(self.guiManager.gameManager.currentMerchant.inventory[self.mindex2].value)
            self.cchanges += self.guiManager.gameManager.currentMerchant.inventory[self.mindex2].value
            self.cchange["text"] = str(self.cchanges)
    
    def buy3(self):
        if self.guiManager.gameManager.currentMerchant.inventory[self.mindex3] not in self.buylist:
            self.buylist.append(self.guiManager.gameManager.currentMerchant.inventory[self.mindex3])
            self.descLabel["text"] = self.guiManager.gameManager.itemdescDict[self.guiManager.gameManager.currentMerchant.inventory[self.mindex3].name]
            self.ival["text"] = str(self.guiManager.gameManager.currentMerchant.inventory[self.mindex3].value)
            self.cchanges -= self.guiManager.gameManager.currentMerchant.inventory[self.mindex3].value
            self.cchange["text"] = str(self.cchanges)
        else:
            self.buylist.remove(self.guiManager.gameManager.currentMerchant.inventory[self.mindex3])
            self.descLabel["text"] = self.guiManager.gameManager.itemdescDict[self.guiManager.gameManager.currentMerchant.inventory[self.mindex3].name]
            self.ival["text"] = str(self.guiManager.gameManager.currentMerchant.inventory[self.mindex3].value)
            self.cchanges += self.guiManager.gameManager.currentMerchant.inventory[self.mindex3].value
            self.cchange["text"] = str(self.cchanges)
    
    def buy4(self):
        if self.guiManager.gameManager.currentMerchant.inventory[self.mindex4] not in self.buylist:
            self.buylist.append(self.guiManager.gameManager.currentMerchant.inventory[self.mindex4])
            self.descLabel["text"] = self.guiManager.gameManager.itemdescDict[self.guiManager.gameManager.currentMerchant.inventory[self.mindex4].name]
            self.ival["text"] = str(self.guiManager.gameManager.currentMerchant.inventory[self.mindex4].value)
            self.cchanges -= self.guiManager.gameManager.currentMerchant.inventory[self.mindex4].value
            self.cchange["text"] = str(self.cchanges)
        else:
            self.buylist.remove(self.guiManager.gameManager.currentMerchant.inventory[self.mindex4])
            self.descLabel["text"] = self.guiManager.gameManager.itemdescDict[self.guiManager.gameManager.currentMerchant.inventory[self.mindex4].name]
            self.ival["text"] = str(self.guiManager.gameManager.currentMerchant.inventory[self.mindex4].value)
            self.cchanges += self.guiManager.gameManager.currentMerchant.inventory[self.mindex4].value
            self.cchange["text"] = str(self.cchanges)
    
    def sell(self):
        if self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex] not in self.selllist:
            self.selllist.append(self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex])
            self.descLabel["text"] = self.guiManager.gameManager.itemdescDict[self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex].name]
            self.ival["text"] = str(self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex].value)
            self.mchanges -= self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex].value
            self.mchange["text"] = str(self.mchanges)
        else:
            self.selllist.remove(self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex])
            self.descLabel["text"] = self.guiManager.gameManager.itemdescDict[self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex].name]
            self.ival["text"] = str(self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex].value)
            self.mchanges += self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex].value
            self.mchange["text"] = str(self.mchanges)
    
    def sell2(self):
        if self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex2] not in self.selllist:
            self.selllist.append(self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex2])
            self.descLabel["text"] = self.guiManager.gameManager.itemdescDict[self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex2].name]
            self.ival["text"] = str(self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex2].value)
            self.mchanges -= self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex2].value
            self.mchange["text"] = str(self.mchanges)
        else:
            self.selllist.remove(self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex2])
            self.descLabel["text"] = self.guiManager.gameManager.itemdescDict[self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex2].name]
            self.ival["text"] = str(self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex2].value)
            self.mchanges += self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex2].value
            self.mchange["text"] = str(self.mchanges)
    
    def sell3(self):
        if self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex3] not in self.selllist:
            self.selllist.append(self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex3])
            self.descLabel["text"] = self.guiManager.gameManager.itemdescDict[self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex3].name]
            self.ival["text"] = str(self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex3].value)
            self.mchanges -= self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex3].value
            self.mchange["text"] = str(self.mchanges)
        else:
            self.selllist.remove(self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex3])
            self.descLabel["text"] = self.guiManager.gameManager.itemdescDict[self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex3].name]
            self.ival["text"] = str(self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex3].value)
            self.mchanges += self.guiManager.gameManager.currentMerchant.inventory[self.mindex3].value
            self.mchange["text"] = str(self.mchanges)
    
    def sell4(self):
        if self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex4] not in self.selllist:
            self.selllist.append(self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex4])
            self.descLabel["text"] = self.guiManager.gameManager.itemdescDict[self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex4].name]
            self.ival["text"] = str(self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex4].value)
            self.mchanges -= self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex4].value
            self.mchange["text"] = str(self.mchanges)
        else:
            self.selllist.remove(self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex4])
            self.descLabel["text"] = self.guiManager.gameManager.itemdescDict[self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex4].name]
            self.ival["text"] = str(self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex4].value)
            self.mchanges += self.guiManager.gameManager.currentCharacters[0].inventory[self.cindex4].value
            self.mchange["text"] = str(self.mchanges)
    
    def change(self):
        if self.cchanges < (self.guiManager.gameManager.currentCharacters[0].money) * -1:
            pass
        elif self.mchanges < (self.guiManager.gameManager.currentMerchant.money) * -1:
            pass
        else:
            for i in self.buylist:
                self.guiManager.gameManager.currentMerchant.inventory.remove(i)
                if i == self.guiManager.gameManager.currentMerchant.unique:
                    self.guiManager.gameManager.currentMerchant.unique = None
                self.guiManager.gameManager.currentCharacters[0].inventory.append(i)
            self.guiManager.gameManager.currentCharacters[0].money += self.cchanges
            self.guiManager.gameManager.currentCharacters[0].money += (self.mchanges *-1)
            for t in self.selllist:
                if t.story == True:
                    pass
                else:
                    self.guiManager.gameManager.currentMerchant.inventory.append(t)
                    self.guiManager.gameManager.currentCharacters[0].inventory.remove(t)
            self.guiManager.gameManager.currentMerchant.money += self.mchanges
            self.guiManager.gameManager.currentMerchant.money += (self.cchanges *-1)
        self.guiManager.openWindow("main")
        self.window.destroy()
        
class itemtargetGUI(AbstractGUI):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.guiManager = manager
        self.window.geometry("800x800+100+100")
        self.time = 0
        self.index = 0
        self.index2 = 1
        self.index3 = 2
        self.index4 = 3
        self.target = 0
        self.gManager = self.guiManager.gameManager
        self.enemies = self.gManager.currentEnemies
        self.Item = self.gManager.item
        targetFrame = Frame(self.window, width = 400)
        targetFrame.grid()
        self.selectFrame = Frame(targetFrame, width = 400)
        self.selectFrame.grid()
        self.selectFrame.grid(row=2, column=1)
        if self.Item.friendly == False:
            scrollUpButton = Button(targetFrame, text = "^", command = self.scrollUp, width=20)
            scrollUpButton.grid(row=1, column=1)
            scrollDownButton = Button(targetFrame,text= "v", command = self.scrollDown, width=20)
            scrollDownButton.grid(row=3, column=1)
            self.enemy1 = Button(self.selectFrame, text=self.gManager.currentEnemies[0].name, command=self.attack1, width=20)
            self.enemy1.grid(row=1, column=1)
            if len(self.gManager.currentEnemies) > 1:
                self.enemy2 = Button(self.selectFrame, text=self.gManager.currentEnemies[1].name, command=self.attack2, width=20)
                self.enemy2.grid(row=2, column=1)
            if len(self.gManager.currentEnemies) > 2:
                self.enemy3 = Button(self.selectFrame, text=self.gManager.currentEnemies[2].name, command=self.attack3, width=20)
                self.enemy3.grid(row=3, column=1)
            if len(self.gManager.currentEnemies) > 3:
                self.enemy4 = Button(self.selectFrame, text=self.gManager.currentEnemies[3].name, command=self.attack4, width=20)
                self.enemy4.grid(row=4, column=1)
        else:
            self.friendly1 = Button(self.selectFrame, text=self.gManager.currentCharacters[0].name, command=self.attack1, width=20)
            self.friendly1.grid(row=1, column=1)
            self.friendly2 = Button(self.selectFrame, text=self.gManager.currentCharacters[1].name, command=self.attack2, width=20)
            self.friendly2.grid(row=2, column=1)
            self.friendly3 = Button(self.selectFrame, text=self.gManager.currentCharacters[2].name, command=self.attack3, width=20)
            self.friendly3.grid(row=3, column=1)
            self.friendly4 = Button(self.selectFrame, text=self.gManager.currentCharacters[3].name, command=self.attack4, width=20)
            self.friendly4.grid(row=4, column=1)
        
        confirmButton = Button(targetFrame, text= "Comfirm", command=self.confirm)
        confirmButton.grid(row=4, column=1)
        
    def scrollUp(self):
            if len(self.gManager.currentEnemies) < 5:
                pass
            else:
                self.index += 1
                self.index2 += 1
                self.index3 += 1
                self.index4 += 1
                if self.index >= len(self.gManager.currentEnemies):
                    self.index = 0
                    self.enemy1["text"] = self.gManager.currentEnemies[self.index].name
                    self.enemy2["text"] = self.gManager.currentEnemies[self.index2].name
                    self.enemy3["text"] = self.gManager.currentEnemies[self.index3].name
                    self.enemy4["text"] = self.gManager.currentEnemies[self.index4].name
                elif self.index2 >= len(self.gManager.currentEnemies):
                    self.enemy1["text"] = self.gManager.currentEnemies[self.index].name
                    self.index2 = 0
                    self.enemy2["text"] = self.gManager.currentEnemies[self.index2].name
                    self.enemy3["text"] = self.gManager.currentEnemies[self.index3].name
                    self.enemy4["text"] = self.gManager.currentEnemies[self.index4].name
                elif self.index3 >= len(self.gManager.currentEnemies):
                    self.enemy1["text"] = self.gManager.currentEnemies[self.index].name
                    self.enemy2["text"] = self.gManager.currentEnemies[self.index2].name
                    self.index3 = 0
                    self.enemy3["text"] = self.gManager.currentEnemies[self.index3].name
                    self.enemy4["text"] = self.gManager.currentEnemies[self.index4].name
                elif self.index4 >= len(self.gManager.currentEnemies):
                    self.enemy1["text"] = self.gManager.currentEnemies[self.index].name
                    self.enemy2["text"] = self.gManager.currentEnemies[self.index2].name
                    self.enemy3["text"] = self.gManager.currentEnemies[self.index3].name
                    self.index4 = 0
                    self.enemy4["text"] = self.gManager.currentEnemies[self.index4].name
                else:
                    self.enemy1["text"] = self.gManager.currentEnemies[self.index].name
                    self.enemy2["text"] = self.gManager.currentEnemies[self.index2].name
                    self.enemy3["text"] = self.gManager.currentEnemies[self.index3].name
                    self.enemy4["text"] = self.gManager.currentEnemies[self.index4].name
                
    
    def scrollDown(self):
            if len(self.gManager.currentEnemies) < 5:
                pass
            else:
                self.index -= 1
                self.index2 -= 1
                self.index3 -= 1
                self.index4 -= 1
                if self.index == (len(self.gManager.currentEnemies)+1) * -1:
                    self.index = -1
                    self.enemy1["text"] = self.gManager.currentEnemies[self.index].name
                    self.enemy2["text"] = self.gManager.currentEnemies[self.index2].name
                    self.enemy3["text"] = self.gManager.currentEnemies[self.index3].name
                    self.enemy4["text"] = self.gManager.currentEnemies[self.index4].name
                elif self.index2 == (len(self.gManager.currentEnemies)+1) * -1:
                    self.enemy1["text"] = self.gManager.currentEnemies[self.index].name
                    self.index2 = -1
                    self.enemy2["text"] = self.gManager.currentEnemies[self.index2].name
                    self.enemy3["text"] = self.gManager.currentEnemies[self.index3].name
                    self.enemy4["text"] = self.gManager.currentEnemies[self.index4].name
                elif self.index3 == (len(self.gManager.currentEnemies)+1) * -1:
                    self.enemy1["text"] = self.gManager.currentEnemies[self.index].name
                    self.enemy2["text"] = self.gManager.currentEnemies[self.index2].name
                    self.index3 = -1
                    self.enemy3["text"] = self.gManager.currentEnemies[self.index3].name
                    self.enemy4["text"] = self.gManager.currentEnemies[self.index4].name
                elif self.index4 == (len(self.gManager.currentEnemies)+1) * -1:
                    self.enemy1["text"] = self.gManager.currentEnemies[self.index].name
                    self.enemy2["text"] = self.gManager.currentEnemies[self.index2].name
                    self.enemy3["text"] = self.gManager.currentEnemies[self.index3].name
                    self.index4 = -1
                    self.enemy4["text"] = self.gManager.currentEnemies[self.index4].name
                else:
                    self.enemy1["text"] = self.gManager.currentEnemies[self.index].name
                    self.enemy2["text"] = self.gManager.currentEnemies[self.index2].name
                    self.enemy3["text"] = self.gManager.currentEnemies[self.index3].name
                    self.enemy4["text"] = self.gManager.currentEnemies[self.index4].name
    
    def attack1(self):
        self.target = self.index
    
    def attack2(self):
        self.target = self.index2
        
    def attack3(self):
        self.target = self.index3
        
    def attack4(self):
        self.target = self.index4
        
    def confirm(self):
        if self.Item.friendly == True:
            self.Item.use(self.gManager.currentCharacters[self.target], self.gManager, 1)
            self.openMain()
        else:
            self.Item.use(self.gManager.currentEnemies[self.target], self.gManager, 1)
            self.openMain()
        
    def openMain(self):
        self.guiManager.openWindow("main")
        self.window.destroy()
    
def main():
    guiManager = GUIManager()
    gameManager = GameManager()
    fileManager = FileManager(gameManager, guiManager)
    gameManager.setManagers(fileManager, guiManager)
    guiManager.setManagers(fileManager, gameManager)
    guiManager.startupGUI()
    
main()