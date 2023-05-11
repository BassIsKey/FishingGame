from time import sleep
import random
import headers_labels as hl
import fishingGraphic as fg
import os

class Fish:
    
    def __init__(self, name, sizeMin, sizeMax, rarity, valueMin, valueMax):
        self.name = name
        self.sizeMin = sizeMin
        self.sizeMax = sizeMax
        self.rarity = rarity
        self.valueMin = valueMin
        self.valueMax = valueMax
        self.size = 0
        self.value = 0
    
    
    fishes = {"LMB": {"NAME": "Largemouth Bass",
                      "SIZEMIN": .3,
                      "SIZEMAX": 22.3,
                      "RARITY": "common",
                      "VALUEMIN": 2,
                      "VALUEMAX": 65,
                      "LOCATIONS": ["SMALL LAKE", "LARGE LAKE", "RIVER"]},

              "SMB": {"NAME": "Smallmouth Bass",
                      "SIZEMIN": .2,
                      "SIZEMAX": 11.6,
                      "RARITY": "common",
                      "VALUEMIN": 1,
                      "VALUEMAX": 43,
                      "LOCATIONS": ["SMALL LAKE", "CREEK",]},

              "BLG": {"NAME": "Bluegill",
                      "SIZEMIN": .1,
                      "SIZEMAX": 4.7,
                      "RARITY": "common",
                      "VALUEMIN": 1,
                      "VALUEMAX": 18,
                      "LOCATIONS": [""]},

              "CRF": {"NAME": "Crayfish",
                      "SIZEMIN": .1,
                      "SIZEMAX": 1.0,
                      "RARITY": "common",
                      "VALUEMIN": 1,
                      "VALUEMAX": 7}}


    def createFishObject():

        fishTypeList = []

        for x in Fish.fishes:
            fishTypeList.append(x)
        
        fishCaught = random.choice(fishTypeList)
        fish = Fish(Fish.fishes[fishCaught]["NAME"],
                    Fish.fishes[fishCaught]["SIZEMIN"],
                    Fish.fishes[fishCaught]["SIZEMAX"],
                    Fish.fishes[fishCaught]["RARITY"],
                    Fish.fishes[fishCaught]["VALUEMIN"],
                    Fish.fishes[fishCaught]["VALUEMAX"],)
        
        fish.calculateFishSize()
        fish.calculateFishValue()

        return fish    


    # Takes the min and max size for the type of fish being caught and creates a list of random
    # sizes, then shuffles the sizes list and selects one at random.
    # Control the odds of catching small/medium/large by adjusting the loop range for each size.
 
    def calculateFishSize(self):
        
        sizeList = []
        
        smallLimit = (self.sizeMax - self.sizeMin) * 1/3
        mediumLimit = float((self.sizeMax - self.sizeMin) * 2/3)

        for smallSize in range(20):
            smallSize = float(random.uniform(0, smallLimit))
            sizeList.append(round(self.sizeMin + smallSize, 1))
        
        for mediumSize in range(20):
            mediumSize = float(random.uniform(smallLimit, mediumLimit))
            sizeList.append(round(self.sizeMin + mediumSize, 1))
        
        for largeSize in range(2):
            largeSize = float(random.uniform(mediumLimit, self.sizeMax))
            sizeList.append(round((self.sizeMin + largeSize), 1))
        
        self.size = random.choice(sizeList)

        return


    # Calculates the value of the fish caught. The larger the size, the higher the value, up to the max
    # which is unique for each fish type. The percentage of the total value range will be equal to the
    # percentage of the fish size. Catching a 7 lb. fish that has a range 2 to 12 lbs. (10 lb range),
    # is 50% of the size range, and will receive 50% of the value range.

    def calculateFishValue(self):
        y = self.valueMax
        x = self.sizeMax
        m = round((self.valueMax - self.valueMin) / (self.sizeMax - self.sizeMin), 3)
        b = round(y - (m * x), 3)

        self.value = int(m * self.size + b)

        return
    

    def addFishInventory(self):
        self.append(player.inventory)

        return
    

    def catchDescription(self):
        return f"You caught a {self.size} pound {self.name} worth {self.value}!"


class Player:
    def __init__(self):
        self.name = "Nameless Angler"
        self.experience = 0
        self.level = 1
        self.wallet = 0
        self.inventory = []
        self.maxInventory = 4
        self.catchingPower = 1
        self.quarters = "Campsite"
        self.energy = 15
        self.energyToFish = 5
        self.location = "BARREL"

    
    def addToInventory(self, newThing):
        print(f"{newThing.name} added to your inventory")
        self.inventory.append(newThing)
    

    def printInventory(self):

        clearScreen()

        if len(player.inventory) < 1:
            input("""Your inventory is empty.
            
            Press enter  """)
            return
        
        y = 1

        for i in self.inventory:
            if type(i) == Fish:
                print(f"""        {y}. {i.name} ({i.size})  Value: {i.value}""")
            elif type(i) == Item:
                for i in player.inventory:
                    print(f"""        {y}. {i.name} ({i.rarity})  Value: {i.value}""")
            y += 1

        input("""
              PRESS ENTER""")
    

    def checkEnergy(self):
        if self.energy < self.energyToFish:
            return False
        # else:
        #     return True
    

    def payEnergyCost(self):
        self.energy -= self.energyToFish
        return
    

    def buyWatercraft():
        print("Buy yoru watercraft here!")

        return


class Item:
    def __init__(self, name, description, rarity, value):
        self.name = name
        self.description = description
        self.rarity = rarity
        self.value = value


class Location:
    
    def __init__(self):
        self.name = None
        self.sizeModifier = None

    locations = {"RAIN BARREL": {"NAME": "Rain Barrel",
                                 "SIZE MODIFIER": .2},

                 "POND": {"NAME": "Pond",
                          "SIZE MODIFIER": .6},
                                 
                 "SMALL LAKE": {"NAME": "Small Lake",
                                "SIZE MODIFIER": .8},
                                
                 "LARGE LAKE": {"NAME": "Large Lake",
                                "SIZE MODIFIER": 1},
                 
                 "RIVER": {"NAME": "Large Lake",
                           "SIZE MODIFIER": .7},

                 "CREEK": {"NAME": "Creek",
                           "SIZE MODIFIER": .5}}
    
    def updateLocation(self, newLocation):

        location.name = newLocation["NAME"]
        location.sizeModifier = newLocation["SIZE MODIFIER"]


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def fishOrJunk():

    if player.checkEnergy() == False:
        
        print("Not enough energy to fish any more today.")
        input("Press Enter")
        return
    
    if not chooseFishingLocation():
        return
    
    fg.bobberGraphic()

    x = random.random()
    if x <= .1:
        print("You caught an item or junk.")
        return
    
    catchFish()

    return


def catchFish():
    fish = Fish.createFishObject()

    input(f"""{fish.catchDescription()}
    
    Press Enter""")

    if not player.checkEnergy:
        print("You don't have inventory space.")
        pass
    player.inventory.append(fish)
    return


def chooseFishingLocation():

    while True:

        clearScreen()

        print("""Where would you like to fish?

1. The rain barrel
2. Pond
3. Small lake
4. Large lake
5. Creek
6. River)
""")

        selection = input("Option #:  ")

        try:
            selection = int(selection)
        
        except:
            pass

        if selection == 1:
            player.location = "RAIN BARREL"
            return True
        
        elif selection == 2:
            if player.level < 1:
                input("You must be Level 1 to fish in the pond. Press Enter")
                return False
            player.location = "POND"
            return True
        
        elif selection == 3:
            if player.level < 4:
                input("You must be level 4 to fish in the small lake. Press Enter")
                return False
            player.location = "SMALL LAKE"
            return True
        
        elif selection == 4:
            if player.level < 6:
                input("You must be level 4 to fish in the small lake. Press Enter")
                return False
            player.location = "LARGE LAKE"
            return True
        
        elif selection == 5:
            if player.level < 8:
                input("You must be level 4 to fish in the small lake. Press Enter")
                return False
            player.location = "CREEK"
            return True
        
        elif selection == 6:
            if player.level < 10:
                input("You must be level 4 to fish in the small lake. Press Enter")
                return False
            player.location = "RIVER"
            return True
        
        else:
            clearScreen()
            input(f"""You entered "{selection}", which is not a valid location number.
            
Press enter""")


player = Player()
location = Location()


while True:

    clearScreen()

    # hl.gameplayMenu(player.quarters)


    q = input("""
    Option #: """)

    if q == "1":
        fishOrJunk()
        
    elif q == "2":
        pass
    elif q == "3":
        pass
    elif q == "4":
        pass
    elif q == "5":
        player.printInventory()

    # sleep(3)