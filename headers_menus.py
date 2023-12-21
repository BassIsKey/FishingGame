
# Menu headers

def docksHeader():
    print("""
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                     *           On The Docks            *
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

***********************************************************************************""")


def onTheWaterHeader():
    print("""
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                     *           On The Water            *
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

***********************************************************************************""")


def mainHeader():
    print("""
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                     *            Main Menu              *
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

***********************************************************************************""")


def inventoryHeader():
    print("""
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                     *            Inventory              *
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

***********************************************************************************""")


def fishingHeader(player, location):
    print(f"""
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                     *             Fishing               *
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Location: {location.name}     Inventory: {len(player.inventory)}/{player.maxInventory}     Energy: {player.energy}/100
***********************************************************************************""")


def baitShopHeader():
    print("""
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                     *             Bait Shop             *
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

***********************************************************************************""")


def nameChangeHeader():
    print("""
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                     *            Name Change            *
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

***********************************************************************************""")


def communityBoardHeader():
    print("""
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                     *         Community Board           *
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

***********************************************************************************""")


def makeRoomHeader():
    print("""
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                     *       Throw Something Back        *
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

***********************************************************************************""")


def lodgingQuartersHeader():
    print("""
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                     *             Lodging               *
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

***********************************************************************************""")


def whereToFishHeader():
    print("""
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                     *          Where To Fish            *
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

***********************************************************************************""")


def chooseLocationHeader():
    print("""
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                     *          Choose Location          *
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

***********************************************************************************""")


def attentionHeader():
    print("""
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                     *             Attention             *
                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

***********************************************************************************""")


def mainMenu(player):
    print(f"""
    1. Go fishing!                       2. Bait Bucket
    3. Bait Shop (not working)           4. View Inventory""")


def basicPlayerInfoHeader(player):
    print(f"""
    Name: {player.name}                  Level: {player.level}

***********************************************************************************""")


def playerInfoHeaderWhileFishing(player, location):
    print(f"""          Location: {location.name}            Inventory Space: {len(player.inventory)}/{player.maxInventory}
***********************************************************************************""")


def fishingLocationsMenu():
    print("""
    Where would you like to fish?

    1. The rain barrel                   2. Pond
    3. Small lake                        4. Large lake
    5. Creek                             6. River)
    
    "X" to return.""")


def activeFishingMenu():
    print("""
    1. Cast your line                    2. Apply bait
    3. Check inventory
    
    "X" to return.""")