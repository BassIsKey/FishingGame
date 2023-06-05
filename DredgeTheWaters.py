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


    def createFishObject():

        while True:
            fishTypeList = []

            for x in Fish.fishes:
                fishTypeList.append(x)
            
            fishCaught = random.choice(fishTypeList)
            input(f"""trying {fishCaught}.""")
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

        clearScreen()

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
        self.energy = 10
        self.energyToFish = 5
        self.location = "BARREL"

    
    def addToInventory(self, newThing):
        
        print(f"{newThing.name} added to your inventory")
        self.inventory.append(newThing)
    

    def printInventory(self):

        clearScreen()
        hm.inventoryHeader()

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

        input("""
    PRESS ENTER""")
    

    def checkEnergy(self):

        if self.energy < self.energyToFish:

            input("""    Not enough energy to fish any more today. Press Enter""")
            
            return False
        
        return True
        

    def fullInventoryWarning(self):

        if len(self.inventory) >= self.maxInventory:
            clearScreen()
            input("""
    Your inventory is full. You will need to release your next catch
    or make room in your inventory after your next catch.
    
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

    if not player.checkEnergy():
                
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


def inventoryMakeRoom():

    Fish.catchDescription()
    hm.inventoryHeader()

    player.printInventory()

    print("    Choose the number of the inventory item to throw back")
    selection = input(    "Option #:  ")


def onTheWater():
    clearScreen()
    hm.onTheWaterHeader()
    hm.PlayerInfoHeaderWhileFishing(player, location)




def catchFish():
    fish = Fish.createFishObject()

    input(f"""{fish.catchDescription()}
    
    Press Enter""")

    if not player.fullInventoryWarning():
        print("You don't have inventory space.")
        pass
    player.inventory.append(fish)
    return


def chooseFishingLocation():

    while True:
        #Sets player location attributes. Takes input from menu options, checks prerequisites, adn either
        #returns false if requirements not met, or sets location attribute if requirements met.

        clearScreen()
        hm.chooseLocationHeader()
        hm.fishingLocationsMenu()

        selection = input("""
    Option:  """)

        try:
            selection = int(selection)
        
        except:
            if selection == "x" or selection == "X":
                return main()
            pass

        if selection == 1:
            location.updateLocation("RAIN BARREL")
            return True
        
        elif selection == 2:
            if player.level < 2:
                clearScreen()
                hm.chooseLocationHeader()

                input("""
    You must be Level 1 to fish in the pond. Press Enter""")
                return False
            
            location.name = "POND"
            return True
        
        elif selection == 3:
            if player.level < 4:
                clearScreen()
                hm.chooseLocationHeader()

                input("""
    You must be level 4 to fish in the small lake. Press Enter""")
                return False
            
            player.location = "SMALL LAKE"
            return True
        
        elif selection == 4:
            if player.level < 6:
                clearScreen()
                hm.chooseLocationHeader()

                input("""
    You must be level 6 to fish in the small lake. Press Enter""")
                return False
            
            player.location = "LARGE LAKE"
            return True
        
        elif selection == 5:
            if player.level < 8:
                clearScreen()
                hm.chooseLocationHeader()

                input("""
    You must be level 4 to fish in the small lake. Press Enter""")
                return False
            
            player.location = "CREEK"
            return True
        
        elif selection == 6:
            if player.level < 10:
                clearScreen()
                hm.chooseLocationHeader()

                input("You must be level 4 to fish in the small lake. Press Enter")
                return False
            
            player.location = "RIVER"
            return True
        
        else:
            clearScreen()
            hm.chooseLocationHeader()

            input(f"""
    Please select a location number from the list. Press enter  """)


def tempGoFishing():

    #check energy
    if not player.checkEnergy():
        return
    
    #warn if full inventory
    player.fullInventoryWarning()
    
    #where to fish
    chooseFishingLocation()


def activelyFishing():

    clearScreen()
    hm.PlayerInfoHeaderWhileFishing()
    hm.activeFishingMenu()

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


def main():

    clearScreen()
    hm.mainHeader()
    hm.mainMenu(player)

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

player = Player()
location = Location()


while True:
    
    main()