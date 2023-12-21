from time import sleep
import random
import headers_menus as hm
import fishingGraphic as fg
import os

class Fish:
    
    def __init__(self, name, sizeMin, sizeMax, rarity, valueMin, valueMax, locations):
        self.name = name
        self.sizeMin = sizeMin
        self.sizeMax = sizeMax
        self.rarity = rarity
        self.valueMin = valueMin
        self.valueMax = valueMax
        self.locations = locations
        self.size = None
        self.value = None

    fishes = {"LMB": {"NAME": "Largemouth Bass",
                      "SIZEMIN": .3,
                      "SIZEMAX": 22.3,
                      "RARITY": "common",
                      "VALUEMIN": 6,
                      "VALUEMAX": 65,
                      "LOCATIONS": ["SMALL LAKE", "LARGE LAKE", "RIVER"]},

              "SMB": {"NAME": "Smallmouth Bass",
                      "SIZEMIN": .3,
                      "SIZEMAX": 11.6,
                      "RARITY": "common",
                      "VALUEMIN": 6,
                      "VALUEMAX": 43,
                      "LOCATIONS": ["SMALL LAKE", "CREEK",]},

              "BLG": {"NAME": "Bluegill",
                      "SIZEMIN": .1,
                      "SIZEMAX": 4.7,
                      "RARITY": "common",
                      "VALUEMIN": 3,
                      "VALUEMAX": 18,
                      "LOCATIONS": ["RAIN BARREL", "POND"]},

              "CRF": {"NAME": "Crayfish",
                      "SIZEMIN": .1,
                      "SIZEMAX": 1.0,
                      "RARITY": "common",
                      "VALUEMIN": 1,
                      "VALUEMAX": 7,
                      "LOCATIONS": ["CREEK"]},
            
              "RKB": {"NAME": "Rock Bass",
                      "SIZEMIN": .3,
                      "SIZEMAX": 3.6,
                      "RARITY": "common",
                      "VALUEMIN": 5,
                      "VALUEMAX": 34,
                      "LOCATIONS": ["CREEK", "RAIN BARREL", "SMALL LAKE"]}}


    def newFish():
        while True:
            possibleFish = []
            for x in Fish.fishes:
                if player.location in Fish.fishes[x]["LOCATIONS"]:
                    possibleFish.append(x)
            
            fishCaught = random.choice(possibleFish)
            fish = Fish(Fish.fishes[fishCaught]["NAME"],
                        Fish.fishes[fishCaught]["SIZEMIN"],
                        Fish.fishes[fishCaught]["SIZEMAX"],
                        Fish.fishes[fishCaught]["RARITY"],
                        Fish.fishes[fishCaught]["VALUEMIN"],
                        Fish.fishes[fishCaught]["VALUEMAX"],
                        Fish.fishes[fishCaught]["LOCATIONS"])
            
            sizeList = []
            sizeWeights = (.7, .2, .1)

            modifiedSizeMax = ((fish.sizeMax - fish.sizeMin) * location.sizeModifier) + fish.sizeMin
            
            smallLimit = (modifiedSizeMax - fish.sizeMin) * 1/3
            mediumLimit = float((modifiedSizeMax - fish.sizeMin) * 2/3)

            smallSize = float(random.uniform(0, smallLimit))
            sizeList.append(round(fish.sizeMin + smallSize, 1))

            mediumSize = float(random.uniform(smallLimit, mediumLimit))
            sizeList.append(round(fish.sizeMin + mediumSize, 1))

            largeSize = float(random.uniform(mediumLimit, fish.sizeMax))
            sizeList.append(round((fish.sizeMin + largeSize), 1))

            # for smallSize in range(3):
            #     smallSize = float(random.uniform(0, smallLimit))
            #     sizeList.append(round(fish.sizeMin + smallSize, 1))
            
            # for mediumSize in range(3):
            #     mediumSize = float(random.uniform(smallLimit, mediumLimit))
            #     sizeList.append(round(fish.sizeMin + mediumSize, 1))
            
            # for largeSize in range(1):
            #     largeSize = float(random.uniform(mediumLimit, fish.sizeMax))
            #     sizeList.append(round((fish.sizeMin + largeSize), 1))
            
            fish.size = random.choice(sizeList, sizeWeights, 1)

            y = fish.valueMax
            x = fish.sizeMax
            m = round((fish.valueMax - fish.valueMin) / (fish.sizeMax - fish.sizeMin), 3)
            b = round(y - (m * x), 3)

            fish.value = int(m * fish.size + b)

            if fish.value < 1:
                fish.value = 1


    def createFishObject():

        while True:
            fishTypeList = []

            for x in Fish.fishes:
                fishTypeList.append(x)
            
            fishCaught = random.choice(fishTypeList)
            fish = Fish(Fish.fishes[fishCaught]["NAME"],
                        Fish.fishes[fishCaught]["SIZEMIN"],
                        Fish.fishes[fishCaught]["SIZEMAX"],
                        Fish.fishes[fishCaught]["RARITY"],
                        Fish.fishes[fishCaught]["VALUEMIN"],
                        Fish.fishes[fishCaught]["VALUEMAX"],
                        Fish.fishes[fishCaught]["LOCATIONS"])
            
            if location.name.upper() in fish.locations:

                fish.calculateFishSize()
                fish.calculateFishValue()

                return fish


    # Takes the min and max size for the type of fish being caught and creates a list of random
    # sizes, then shuffles the sizes list and selects one at random.
    # Control the odds of catching small/medium/large by adjusting the loop range for each size.
 
    def calculateFishSize(self):
        
        sizeList = []

        modifiedSizeMax = ((self.sizeMax - self.sizeMin) * location.sizeModifier) + self.sizeMin
        
        smallLimit = (modifiedSizeMax - self.sizeMin) * 1/3
        mediumLimit = float((modifiedSizeMax - self.sizeMin) * 2/3)

        for smallSize in range(3):
            smallSize = float(random.uniform(0, smallLimit))
            sizeList.append(round(self.sizeMin + smallSize, 1))
        
        for mediumSize in range(3):
            mediumSize = float(random.uniform(smallLimit, mediumLimit))
            sizeList.append(round(self.sizeMin + mediumSize, 1))
        
        for largeSize in range(1):
            largeSize = float(random.uniform(mediumLimit, self.sizeMax))
            sizeList.append(round((self.sizeMin + largeSize), 1))
        
        self.size = random.choice(sizeList)

        return


    def calculateFishValue(self):
        y = self.valueMax
        x = self.sizeMax
        m = round((self.valueMax - self.valueMin) / (self.sizeMax - self.sizeMin), 3)
        b = round(y - (m * x), 3)

        self.value = int(m * self.size + b)

        if self.value < 1:
            self.value = 1

        return
    

    def addFishInventory(self):

        self.append(player.inventory)

        return
    

    def catchDescription(self):

        # clearScreen()

        return f"{self.size} pound {self.name} worth {self.value}"


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
        self.energy = 30
        self.energyToFish = 4
        self.location = "BARREL"

    
    def addToInventory(self, newThing):
        
        print(f"{newThing.name} added to your inventory")
        self.inventory.append(newThing)


    def removeFromInventory():

        while True:
            clearScreen()
            hm.makeRoomHeader()
            player.printInventory()

            selection = input("""    
    Choose an inventory item number to toss back.

    Option #:  """)
            
            try:
                selection = int(selection) - 1
                player.inventory.pop(selection)
            
            except:
                if selection == "x" or selection == "X":
                    return
                pass
    

    def printInventory(self):

        if len(player.inventory) < 1:
            input("""
    Your inventory is empty.
            
    Press enter  """)
            return
        
        y = 1
        print("")
        for i in self.inventory:
            if type(i) == Fish:
                print(f"""    {y}. {i.name} ({i.size})  Value: {i.value}""")
            elif type(i) == Item:
                for i in player.inventory:
                    print(f"""    {y}. {i.name} ({i.rarity})  Value: {i.value}""")
            y += 1
    

    def checkEnergy(self):

        if self.energy < self.energyToFish:
            return False
        
        return True
    

    def checkInventory(self):

        if len(self.inventory) > self.maxInventory:
            return False
        
        return True
        

    def fullInventoryWarning(self):

        if len(self.inventory) >= self.maxInventory:

            clearScreen()
            hm.attentionHeader()
            input("""
        Your inventory is full. You will need to release your next catch
        or make room in your inventory in order to keep your next catch.
    
    Press enter.  """)

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

        self.name = "Undecided"
        self.sizeModifier = "Unknown"

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

        location.name = Location.locations[newLocation]["NAME"]
        location.sizeModifier = Location.locations[newLocation]["SIZE MODIFIER"]


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def fishOrJunk():

    fg.bobberGraphic()
    clearScreen()

    x = random.random()
    if x <= .1:
        input("""You caught junk.""")
        return
    
    if x >.1:
        catchFish()

    return


def inventoryMakeRoom(player, fish):

    while len(player.inventory) >= player.maxInventory:
        
        clearScreen()
        hm.makeRoomHeader()

        print(f"""
    You caught a {fish.catchDescription()} but your inventory is full.

    Choose an item number to throw back or input "x" to release your
    new catch.""")
    
        player.printInventory()

        selection = input("""
    Option #:  """)

        try:
            selection = int(selection) - 1
            removed = player.inventory.pop(selection)
            
            clearScreen()
            hm.makeRoomHeader()

            input(f"""
    You throw back {removed.name} to make room for {fish.name}.
            
        Press Enter  """)

        except:

            if selection == "x" or selection == "X":
                return
            input("""Select an inventory number from the list.
                
                Press Enter  """)
        
    return


def onTheWater():
    clearScreen()
    hm.onTheWaterHeader()
    hm.playerInfoHeaderWhileFishing(player, location)


def catchFish():
    fish = Fish.createFishObject()

    if not player.checkInventory:
        inventoryMakeRoom()
        return
    
    input(f"""
    You caught a {fish.catchDescription()}!
    
    Press Enter""")

    inventoryMakeRoom(player, fish)
    
    player.inventory.append(fish)
    player.payEnergyCost()

    return


def chooseFishingLocation():

    while True:
        #Sets player location attributes. Takes input from menu options, checks prerequisites, adn either
        #returns false if requirements not met, or sets location attribute if requirements met.

        clearScreen()
        hm.chooseLocationHeader()
        hm.fishingLocationsMenu()

        selection = input("""
        Option #:  """)

        try:
            selection = int(selection)
        
        except:
            if selection == "x" or selection == "X":
                return False
            pass

        if selection == 1:
            location.updateLocation("RAIN BARREL")
            return True


        elif selection == 2:
            if player.level >= 2:
                clearScreen()
                hm.chooseLocationHeader()

                location.updateLocation("POND")
                return True

            clearScreen()
            hm.chooseLocationHeader()
            input("""
    You must be at least level 2 to fish in the pond.
    
    PRESS ENTER""")


        elif selection == 3:
            if player.level >= 4:
                clearScreen()
                hm.chooseLocationHeader()

                location.updateLocation("SMALL LAKE")
                return True
            
            clearScreen()
            input("""
    You must be at least level 4 to fish in the small lake.
    
    PRESS ENTER""")
            
        
        elif selection == 4:
            if player.level >= 6:
                clearScreen()
                hm.chooseLocationHeader()

                location.updateLocation("LARGE LAKE")
                return True
            
            clearScreen()
            input("""
    You must be at least level 6 to fish in the large lake.
    
    PRESS ENTER""")
            
        
        elif selection == 5:
            if player.level >= 8:
                clearScreen()
                hm.chooseLocationHeader()

                location.updateLocation("CREEK")
                return True
            
            clearScreen()
            input("""
    You must be at least level 8 to fish in the creek.
    
    PRESS ENTER""")
        
        
        elif selection == 6:
            if player.level >= 10:
                clearScreen()
                hm.chooseLocationHeader()

                location.updateLocation("RIVER")
                return False

            clearScreen()
            input("""
    You must be at least level 4 to fish in the river.
    
    PRESS ENTER""")
            
        
        else:
            # clearScreen()
            # hm.chooseLocationHeader()

            input(f"""
    Select a location number available to you from the list.
    
    Press enter  """)


def goFishing():

    #check energy
    if not player.checkEnergy():

        input("""        Not enough energy to fish any more today.
        
            Press Enter""")
        
        return
        
    #where to fish
    if not chooseFishingLocation():
        return

    #proceed to fishing options
    activelyFishing()


def activelyFishing():

    while True:

        clearScreen()
        hm.fishingHeader(player, location)
        hm.activeFishingMenu()

        if len(player.inventory) >= player.maxInventory:
            print("""
        Warning. Your inventory is full""")

        selection = input("""
        Option #: """)

        try:
            selection = int(selection)
        
        except:
            if selection == "x" or selection == "X":
                return False
            pass

        if selection == 1:
            # player.fullInventoryWarning() Decided to remove this courtesy altogether
            fishOrJunk()


        elif selection == 2:
            pass
        

        elif selection == "3":
            clearScreen()
            hm.inventoryHeader()
            player.printInventory()

            input("""
        Press Enter  """)
        

        else:
            # clearScreen()
            # hm.chooseLocationHeader()

            input(f"""
    Select a location number available to you from the list.
    
    Press enter  """)

    # if q == "1":
    #     fishOrJunk()
        
    # elif q == "2":
    #     pass
    # elif q == "3":
    #     pass
    # elif q == "4":
    #     pass


def main():

    clearScreen()
    hm.mainHeader()
    hm.mainMenu(player)

    q = input("""
    Option #: """)

    if q == "1":
        # activelyFishing()
        goFishing()
        
    elif q == "2":
        pass
    elif q == "3":
        pass
    elif q == "4":
        pass
    elif q == "5":
        clearScreen()
        hm.inventoryHeader()
        player.printInventory()

        input("""
    Press Enter  """)


def homeLodging(player):

    while True:

        clearScreen()
        hm.lodgingQuartersHeader()
        hm.mainMenu(player)

        q = input("""
    Option #: """)

        if q == "1":
            goFishing()
            
        elif q == "2":
            pass
        elif q == "3":
            pass
        elif q == "4":
            pass
        elif q == "5":
            clearScreen()
            hm.inventoryHeader()
            player.printInventory()

            input("""
        Press Enter  """)
    

player = Player()
location = Location()

#these are testing opjects
fish1 = Fish("testfish1", 50, 100, "testcommon", 300, 600, ["RAIN BARREL"])
fish1.value = 300
fish1.size = 100
fish2 = Fish("testfish2", 50, 100, "testcommon", 300, 600, ["RAIN BARREL"])
fish2.value = 300
fish2.size = 100
fish3 = Fish("testfish3", 50, 100, "testcommon", 300, 600, ["RAIN BARREL"])
fish3.value = 300
fish3.size = 100
fish4 = Fish("testfish4", 50, 100, "testcommon", 300, 600, ["RAIN BARREL"])
fish4.value = 300
fish4.size = 100
player.inventory.append(fish1)
player.inventory.append(fish2)
player.inventory.append(fish3)
# player.inventory.append(fish4)

while True:
    # player.location = "RAIN BARREL"
    # catchSumpn = Fish.newFish()
    # print(catchSumpn)

    homeLodging(player)
    input("""
    End of the code. Press Enter  """)