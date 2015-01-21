import time
import sys
import os.path
global inventory
inventory = []

def begin():
    print("PORK I - A spin-off of the classic text-based game, ZORK, witten in Python")
    print("Programmed by Meorge")
    time.sleep(3)
    global inventory
    if os.path.isfile("pork-save") and os.path.isfile("location") and os.path.isfile("name"):
        fo = open('name', 'r')
        name = fo.read()
        fo.close()
        print("")
        print("It looks like I have a save file from " + name + " here. Should I use this data or create a new save?")
        print("NOTE: If you create a new save, the old one will be deleted.")
        saveAction = input("")
        if saveAction == "Create a new save" or saveAction == "create a new save" or saveAction == "new save" or saveAction == "new" or saveAction == "New save" or saveAction == "New" or saveAction == "create new save":
            name = input("Please enter your name then, brave adventurer. ")
            fo = open('pork-save', 'w')
            fo.write(name + "\n" + "\n")
            fo.close()
            fo = open('location', 'w')
            fo.write("frontOfHouseEast")
            fo.close()
            print("\n\n\n")
            frontOfHouseEast()
        if saveAction == "Use this save" or saveAction == "Use existing save" or saveAction == "use" or saveAction == "Use" or saveAction == "keep old save":
            fo = open('pork-save', 'r')
            save = fo.read()
            with open('pork-save', 'r') as saveFile:
                for line in saveFile: # let's do some inventory stuff
                    if line.replace('\n', '').replace('\r', '') == "Journal":
                        inventory.append("Journal")
                    if line.replace('\n', '').replace('\r', '') == "Cup":
                        inventory.append("Cup")
                    if line.replace('\n', '').replace('\r', '') == "Pencil":
                        inventory.append("Pencil")
                    if line.replace('\n', '').replace('\r', '') == "Twig":
                        inventory.append("Twig")
                    if line.replace('\n', '').replace('\r', '') == "Candle":
                        inventory.append("Candle")
                    if line.replace('\n', '').replace('\r', '') == "KeyStool":
                        inventory.append("KeyStool")
            fo.close()
            fo = open('location', 'r')
            saveloc = fo.read()
            with open('location', 'r') as locationSave:
                for line in locationSave: # next, our position
                    if line.replace('\n', '').replace('\r', '') == "frontOfHouseEast":
                        frontOfHouseEast()
                    if line.replace('\n', '').replace('\r', '') == "nextToCarEast":
                        nextToCarEast()
                    if line.replace('\n', '').replace('\r', '') == "endOfPorchNorth":
                        endOfPorchNorth()
                    if line.replace('\n', '').replace('\r', '') == "endOfPorchSouth":
                        endOfPorchSouth()
                    if line.replace('\n', '').replace('\r', '') == "bottomOfSteps":
                        bottomOfSteps()
                    if line.replace('\n', '').replace('\r', '') == "doorBlock":
                        doorBlock()
                    if line.replace('\n', '').replace('\r', '') == "insideCar":
                        insideCar()
                    if line.replace('\n', '').replace('\r', '') == "sittingInChair":
                        sittingInChair()
                    if line.replace('\n', '').replace('\r', '') == "sittingOnSwing":
                        sittingOnSwing()
                    if line.replace('\n', '').replace('\r', '') == "inspectingVolvo":
                        inspectingVolvo()
                    if line.replace('\n', '').replace('\r', '') == "insideVolvo":
                        insideVolvo()
                    if line.replace('\n', '').replace('\r', '') == "garden":
                        garden()
                    if line.replace('\n', '').replace('\r', '') == "insideHouseDog":
                        insideHouseDog()
                    if line.replace('\n', '').replace('\r', '') == "dogStickLoop":
                        dogStickLoop()
                    if line.replace('\n', '').replace('\r', '') == "dogPencilLoop":
                        dogPencilLoop()
                    if line.replace('\n', '').replace('\r', '') == "happyDogTwig":
                        happyDogTwig()
                    if line.replace('\n', '').replace('\r', '') == "happyDogPencil":
                        happyDogPencil()
        else:
            print("I'm sorry, but I don't understand that.")
            begin()


    else:
        name = input("Please enter your name, brave adventurer. ")
        fo = open('name', 'w')
        fo.write(name)
        fo.close()
        fo = open('location', 'w')
        fo.write("frontOfHouseEast")
        fo.close()
        print("\n\n\n")
        frontOfHouseEast()


def frontOfHouseEast():
    area = "frontOfHouseEast"
    print("")
    print("Front Of House - Facing East")
    if "Journal" in inventory:
        print("You are standing on the front porch of a white house. A car is parked in the driveway in front of you. Behind you is a locked door.")
    else:
        print("You are standing on the front porch of your house. A car is parked in the driveway. Behind you is a locked door. On the ground in front of you is a small journal.")
    direction = input("")
    if direction == "Go east" or direction == "e" or direction == "go east" or direction == "walk east" or direction == "east":
        nextToCarEast()
    if direction == "Go south" or direction == "s" or direction == "go south" or direction == "walk south" or direction == "south":
        endOfPorchSouth()
    if direction == "Go north" or direction == "n" or direction == "go north" or direction == "walk north" or direction == "north":
        endOfPorchNorth()
    if direction == "Go west" or direction == "w" or direction == "go west" or direction == "walk west" or direction == "west":
        doorBlock()
    if direction == "Take journal" or direction == "take journal" and "Journal" not in inventory:
        print("Taken.")
        inventory.append("Journal")
        time.sleep(1)
        print("")
        frontOfHouseEast()
    if direction == "Read journal" or direction == "read journal" and "Journal" in inventory:
        import journaltext
        time.sleep(2)
        frontOfHouseEast()
    if direction == "items" or direction == "inventory" or direction == "i":
        print(inventory)
        time.sleep(2)
        frontOfHouseEast()
    if direction == "quit" or direction == "exit" or direction == "leave":
        print("")
        print("Are you sure? Y/N")
        leave = input("")
        if leave == "y" or leave == "Y":
            fo = open('pork-save', 'w')
            fo.write('\n'.join(inventory))
            fo.close()
            sys.exit()
        if leave == "n" or leave == "N":
            frontOfHouseEast()
    else:
        print("Sorry, I don't understand \"" + direction + "\".")
        time.sleep(1)
        frontOfHouseEast()

def nextToCarEast():
    area = "nextToCarEast"
    print("")
    print("Next To Car - Facing East")
    print("Next to you is a small green car. The door to the car is unlocked. Ahead of you, there is a small garden, where it looks like something has been covered up.")
    direction = input("")
    if direction == "Get in car" or direction == "c" or direction == "car" or direction == "get in car":
        insideCar()
    if direction == "Go west" or direction == "w" or direction == "go west" or direction == "walk west" or direction == "west":
        frontOfHouseEast()
    if direction == "Go east" or direction == "e" or direction == "go east" or direction == "walk east" or direction == "east":
        garden()
    if direction == "Read journal" or direction == "read journal" and "Journal" in inventory:
        import journaltext
        time.sleep(2)
        nextToCarEast()
    if direction == "items" or direction == "inventory" or direction == "i":
        print(inventory)
        time.sleep(2)
        nextToCarEast()
    if direction == "quit" or direction == "exit" or direction == "leave":
        print("")
        print("Are you sure? Y/N")
        leave = input("")
        if leave == "y" or leave == "Y":
            fo = open('pork-save', 'w')
            fo.write('\n'.join(inventory))
            fo.close()
            fo = open('location', 'w')
            fo.write(area)
            fo.close()
            sys.exit()
        if leave == "n" or leave == "N":
            nextToCarEast()
    else:
        print("Sorry, I don't understand \"" + direction + "\".")
        time.sleep(1)
        nextToCarEast()

def endOfPorchNorth():
    area = "endOfPorchNorth"
    print("")
    print("End Of Porch - Facing North")
    print("You are standing on the north end of the porch. There are three steps in front of you that go down onto the driveway. A chair is sitting next to you on the porch.")
    direction = input("")
    if direction == "Go north" or direction == "n" or direction == "go north" or direction == "walk north" or direction == "north" or direction == "Walk down steps" or direction == "walk down steps":
        bottomOfSteps()
    if direction == "Go south" or direction == "s" or direction == "go south" or direction == "walk south" or direction == "south":
        frontOfHouseEast()
    if direction == "Sit in chair" or direction == "sit down" or direction == "Chair" or direction == "chair" or direction == "c":
        sittingInChair()
    if direction == "Read journal" or direction == "read journal" and "Journal" in inventory:
        import journaltext
        time.sleep(2)
        endOfPorchNorth()
    if direction == "items" or direction == "inventory" or direction == "i":
        print(inventory)
        time.sleep(2)
        endOfPorchNorth()
    if direction == "quit" or direction == "exit" or direction == "leave":
        print("")
        print("Are you sure? Y/N")
        leave = input("")
        if leave == "y" or leave == "Y":
            fo = open('pork-save', 'w')
            fo.write('\n'.join(inventory))
            fo.close()
            fo = open('location', 'w')
            fo.write(area)
            fo.close()
            sys.exit()
        if leave == "n" or leave == "N":
            endOfPorchNorth()
    else:
        print("Sorry, I don't understand \"" + direction + "\".")
        time.sleep(1)
        endOfPorchNorth()


def endOfPorchSouth():
    area = "endOfPorchSouth"
    print("")
    print("End Of Porch - Facing South")
    print("You are facing the railing on the end of the porch. You cannot go any further north because of this. A swing is in front of you.")
    direction = input("")
    if direction == "Go north" or direction == "n" or direction == "go north" or direction == "walk north" or direction == "north":
        frontOfHouseEast()
    if direction == "Sit on swing" or direction == "sit down" or direction == "Swing" or direction == "swing" or direction == "c" or direction == "sit on swing":
        sittingOnSwing()
    if direction == "Read journal" or direction == "read journal" and "Journal" in inventory:
        import journaltext
        time.sleep(2)
        endOfPorchSouth()
    if direction == "items" or direction == "inventory" or direction == "i":
        print(inventory)
        time.sleep(2)
        endOfPorchSouth()
    if direction == "quit" or direction == "exit" or direction == "leave":
        print("")
        print("Are you sure? Y/N")
        leave = input("")
        if leave == "y" or leave == "Y":
            fo = open('pork-save', 'w')
            fo.write('\n'.join(inventory))
            fo.close()
            fo = open('location', 'w')
            fo.write(area)
            fo.close()
            sys.exit()
        if leave == "n" or leave == "N":
            endOfPorchSouth()
    else:
        print("Sorry, I don't understand \"" + direction + "\".")
        time.sleep(1)
        endOfPorchSouth()


def doorBlock():
    area = "doorBlock"
    print("")
    print("Front Door of House - Facing West")
    print("A white door impedes your progress this way.")
    direction = input("")
    if direction == "Go back" or direction == "go back" or direction == "back" or direction == "b" or direction == "Go east" or direction == "e" or direction == "go east" or direction == "walk east" or direction == "east":
        frontOfHouseEast()
    if direction == "Read journal" or direction == "read journal" and "Journal" in inventory:
        import journaltext
        time.sleep(2)
        doorBlock()
    if direction == "items" or direction == "inventory" or direction == "i":
        print(inventory)
        time.sleep(2)
        doorBlock()
    if direction == "quit" or direction == "exit" or direction == "leave":
        print("")
        print("Are you sure? Y/N")
        leave = input("")
        if leave == "y" or leave == "Y":
            fo = open('pork-save', 'w')
            fo.write('\n'.join(inventory))
            fo.close()
            fo = open('location', 'w')
            fo.write(area)
            fo.close()
            sys.exit()
        if leave == "n" or leave == "N":
            doorBlock()
    if direction == "open door" or direction == "Open door" or direction == "unlock door" or direction == "Unlock door":
            print("The door is locked tight.")
    if direction == "open door with key" or direction == "Open door with key" or direction == "use key on door" or direction == "Use key on door" or direction == "Unlock door with key" or direction == "unlock door with key" and "KeyStool" in inventory:
        insideHouseDog()
    
    else:
        print("Sorry, I don't understand \"" + direction + "\".")
        time.sleep(1)
        doorBlock()



def insideCar():
    area = "insideCar"
    print("")
    print("Inside Car - Facing South")
    if "Cup" in inventory:
        print("You are sitting inside the green car.")
    else:
        print("You are sitting inside the green car. There is a cup in the cup holder.")
    direction = input("")
    if direction == "Take cup" or direction == "take cup" and "Cup" not in inventory:
        print("Taken.")
        inventory.append("Cup")
        time.sleep(1)
        print()
        insideCar()
    if direction == "Get out of car" or direction == "get out of car" or direction == "outside" or direction == "get out" or direction == "Get out" or direction == "o":
        nextToCarEast()
    if direction == "Read journal" or direction == "read journal" and "Journal" in inventory:
        import journaltext
        time.sleep(2)
        insideCar()
    if direction == "items" or direction == "inventory" or direction == "i":
        print(inventory)
        time.sleep(2)
        insideCar()
    if direction == "quit" or direction == "exit" or direction == "leave":
        print("")
        print("Are you sure? Y/N")
        leave = input("")
        if leave == "y" or leave == "Y":
            fo = open('pork-save', 'w')
            fo.write('\n'.join(inventory))
            fo.close()
            fo = open('location', 'w')
            fo.write(area)
            fo.close()
            sys.exit()
        if leave == "n" or leave == "N":
            insideCar()
    else:
        print("Sorry, I don't understand \"" + direction + "\".")
        time.sleep(1)
        insideCar()



def bottomOfSteps():
    area = "bottomOfSteps"
    print("")
    print("Bottom Of Steps - Facing North")
    print("You are standing in the driveway. A white Volvo sits farther down the driveway, blocking your path. In front of you, there is a wooden fence. Behind you are wooden steps leading up to the porch.")
    direction = input("")
    if direction == "Inspect car" or direction == "inspect car":
        inspectingVolvo()
    if direction == "Go south" or direction == "s" or direction == "go south" or direction == "walk south" or direction == "south" or direction == "Walk up steps" or direction == "walk up steps":
        endOfPorchNorth()
    if direction == "Climb fence" or direction == "climb fence":
        print("The fence is too high for you to climb.")
        time.sleep(2)
        print("")
        bottomOfSteps()
    if direction == "Read journal" or direction == "read journal" and "Journal" in inventory:
        import journaltext
        time.sleep(2)
        bottomOfSteps()
    if direction == "items" or direction == "inventory" or direction == "i":
        print(inventory)
        time.sleep(2)
        bottomOfSteps()
    if direction == "quit" or direction == "exit" or direction == "leave":
        print("")
        print("Are you sure? Y/N")
        leave = input("")
        if leave == "y" or leave == "Y":
            fo = open('pork-save', 'w')
            fo.write('\n'.join(inventory))
            fo.close()
            fo = open('location', 'w')
            fo.write(area)
            fo.close()
            sys.exit()
        if leave == "n" or leave == "N":
            bottomOfSteps()
    else:
        print("Sorry, I don't understand \"" + direction + "\".")
        time.sleep(1)
        bottomOfSteps()



def sittingInChair():
    area = "sittingInChair"
    print("")
    print("Sitting In Chair - Facing East")
    if "Twig" in inventory:
        print("You are sitting in a wooden chair on the porch.")
    else:
        print("You are sitting in a wooden chair on the porch. Next to you, on a small table, is a twig.")
    direction = input("")
    if direction == "Take twig" or direction == "take twig" and "Twig" not in inventory:
        print("Taken.")
        inventory.append("Twig")
        time.sleep(1)
        print()
        sittingInChair()
    if direction == "Get up" or direction == "get up" or direction == "east" or direction == "Go east" or direction == "go east" or "e":
        endOfPorchNorth()
    if direction == "Read journal" or direction == "read journal" and "Journal" in inventory:
        import journaltext
        time.sleep(2)
        sittingInChair()
    if direction == "items" or direction == "inventory" or direction == "i":
        print(inventory)
        time.sleep(2)
        sittingInChair()
    if direction == "quit" or direction == "exit" or direction == "leave":
        print("")
        print("Are you sure? Y/N")
        leave = input("")
        if leave == "y" or leave == "Y":
            fo = open('pork-save', 'w')
            fo.write('\n'.join(inventory))
            fo.close()
            fo = open('location', 'w')
            fo.write(area)
            fo.close()
            sys.exit()
        if leave == "n" or leave == "N":
            sittingInChair()
    else:
        print("Sorry, I don't understand \"" + direction + "\".")
        time.sleep(1)
        sittingInChair()


def sittingOnSwing():
    area = "sittingOnSwing"
    print("")
    print("Sitting On Swing - Facing South")
    if "Candle" in inventory:
        print("You are sitting on a swing facing south.")
    else:
        print("You are sitting on a swing facing south. There is a candle on the table next to you.")
    direction = input("")
    if direction == "Take candle" or direction == "take candle" and "Candle" not in inventory:
        print("Taken.")
        inventory.append("Candle")
        time.sleep(1)
        print()
        sittingOnSwing()
    if direction == "Get up" or direction == "get up" or direction == "south" or direction == "Go south" or direction == "go south" or direction == "s":
        endOfPorchNorth()
    if direction == "Read journal" or direction == "read journal" and "Journal" in inventory:
        import journaltext
        time.sleep(2)
        sittingOnSwing()
    if direction == "items" or direction == "inventory" or direction == "i":
        print(inventory)
        time.sleep(2)
        sittingOnSwing()
    if direction == "quit" or direction == "exit" or direction == "leave":
        print("")
        print("Are you sure? Y/N")
        leave = input("")
        if leave == "y" or leave == "Y":
            fo = open('pork-save', 'w')
            fo.write('\n'.join(inventory))
            fo.close()
            fo = open('location', 'w')
            fo.write(area)
            fo.close()
            sys.exit()
        if leave == "n" or leave == "N":
            endOfPorchSouth()
    else:
        print("Sorry, I don't understand \"" + direction + "\".")
        time.sleep(1)
        endOfPorchSouth()


def inspectingVolvo():
    area = "inspectingVolvo"
    print("")
    print("Volvo - Facing West")
    print("You are standing in front of a white Volvo. The door is unlocked.")
    direction = input("")
    if direction == "Get in car" or direction == "c" or direction == "car" or direction == "get in car" or direction == "v" or direction == "Get in Volvo" or direction == "Get in volvo" or direction == "get in volvo" or direction == "get in Volvo":
        insideVolvo()
    if direction == "Go east" or direction == "e" or direction == "go east" or direction == "walk east" or direction == "east":
        bottomOfSteps()
    if direction == "Read journal" or direction == "read journal" and "Journal" in inventory:
        import journaltext
        time.sleep(2)
        inspectingVolvo()
    if direction == "items" or direction == "inventory" or direction == "i":
        print(inventory)
        time.sleep(2)
        inspectingVolvo()
    if direction == "quit" or direction == "exit" or direction == "leave":
        print("")
        print("Are you sure? Y/N")
        leave = input("")
        if leave == "y" or leave == "Y":
            fo = open('pork-save', 'w')
            fo.write('\n'.join(inventory))
            fo.close()
            fo = open('location', 'w')
            fo.write(area)
            fo.close()
            sys.exit()
        if leave == "n" or leave == "N":
            inspectingVolvo()
    else:
        print("Sorry, I don't understand \"" + direction + "\".")
        time.sleep(1)
        inspectingVolvo()


def insideVolvo():
    area = "insideVolvo"
    print("")
    print("Inside Volvo - Facing West")
    if "Pencil" in inventory:
        print("You are sitting inside the car.")
    else:
        print("You are sitting inside the car. A green mechanical pencil is sitting below the dashboard.")
    direction = input("")
    if direction == "Take pencil" or direction == "take pencil" and "Pencil" not in inventory:
        print("Taken.")
        inventory.append("Pencil")
        time.sleep(1)
        print()
        insideVolvo()
    if direction == "Get out of car" or direction == "get out of car" or direction == "outside" or direction == "get out" or direction == "Get out" or direction == "o":
        inspectingVolvo()
    if direction == "Read journal" or direction == "read journal" and "Journal" in inventory:
        import journaltext
        time.sleep(2)
        frontOfHouseEast()
    if direction == "items" or direction == "inventory" or direction == "i":
        print(inventory)
        time.sleep(2)
        insideVolvo()
    if direction == "quit" or direction == "exit" or direction == "leave":
        print("")
        print("Are you sure? Y/N")
        leave = input("")
        if leave == "y" or leave == "Y":
            fo = open('pork-save', 'w')
            fo.write('\n'.join(inventory))
            fo.close()
            fo = open('location', 'w')
            fo.write(area)
            fo.close()
            sys.exit()
        if leave == "n" or leave == "N":
            insideVolvo()
    else:
        print("Sorry, I don't understand \"" + direction + "\".")
        time.sleep(1)
        insideVolvo()

def garden():
    area = "garden"
    print("")
    print("Garden - Facing East")
    if "KeyStool" in inventory:
        print("There is a small garden here.")
    else:
        print("There is a small garden here. In the dirt, there is an old, rusty key.")
    direction = input("")
    if direction == "Take key" or direction == "take key":
        print("Taken.")
        inventory.append("KeyStool")
        time.sleep(1)
        garden()
    if direction == "Go west" or direction == "go west" or direction == "west" or direction == "w" or direction == "Go back" or direction == "back":
        nextToCarEast()
    if direction == "Read journal" or direction == "read journal" and "Journal" in inventory:
        import journaltext
        time.sleep(2)
        garden()
    if direction == "items" or direction == "inventory" or direction == "i":
        print(inventory)
        time.sleep(2)
        insideVolvo()
    if direction == "quit" or direction == "exit" or direction == "leave":
        print("")
        print("Are you sure? Y/N")
        leave = input("")
        if leave == "y" or leave == "Y":
            fo = open('pork-save', 'w')
            fo.write('\n'.join(inventory))
            fo.close()
            fo = open('location', 'w')
            fo.write(area)
            fo.close()
            sys.exit()
        if leave == "n" or leave == "N":
            garden()
    else:
        print("Sorry, I don't understand \"" + direction + "\".")
        time.sleep(1)
        garden()


def insideHouseDog():
    area = "insideHouseDog"
    print("Inside House - Facing West")
    print("You are standing inside the living room of the house. There is a large dog, who looks very angry.")
    direction = input("")
    if direction == "Go west" or direction == "go west" or direction == "west" or direction == "West" or direction == "w" or direction == "Go back" or direction == "go back" or direction == "run away" or direction == "Run away":
        deathByDogRunaway()
    if direction == "throw stick in house" or direction == "Throw stick in house" or direction == "Toss stick in house" or direction == "toss stick in house" or direction == "throw twig in house" or direction == "Throw twig in house" or direction == "Toss twig in house" or direction == "toss twig in house" and "Twig" in inventory:
        dogStickLoop()
    if direction == "throw stick outside" or direction == "Throw stick outside" or direction == "Toss stick ouside" or direction == "toss stick outside" or direction == "Throw twig outside" or direction == "throw twig outside" and "Twig" in inventory:
        happyDogTwig()
    if direction == "throw pencil in house" or direction == "Throw pencil in house" or direction == "Toss pencil in house" or direction == "toss pencil in house" and "Pencil" in inventory:
        dogPencilLoop()
    if direction == "throw pencil outside" or direction == "Throw pencil outside" or direction == "Toss pencil ouside" or direction == "toss pencil outside" and "Pencil" in inventory:
        happyDogPencil()
    if direction == "pet dog" or "Pet dog":
        petDog()
    if direction == "hug dog" or "Hug dog":
        hugDog()
    if direction == "kick dog" or "Kick dog":
        kickDog()
    if direction == "punch dog" or "Punch dog":
        punchDog()
    if direction == "Throw stick at dog" or direction == "throw stick at dog":
        throwStickAtDog()
    if direction == "Throw pencil at dog" or direction == "throw pencil at dog":
        throwPencilAtDog()
    if direction == "Throw candle at dog" or direction == "throw candle at dog":
        throwCandleAtDog()
    if direction == "Throw key at dog" or direction == "throw key at dog":
        throwKeyAtDog()
    if direction == "Throw journal at dog" or direction == "throw journal at dog":
        throwJournalAtDog()
    if direction == "Read journal" or direction == "read journal" and "Journal" in inventory:
        import journaltext
        time.sleep(2)
        garden()
    if direction == "items" or direction == "inventory" or direction == "i":
        print(inventory)
        time.sleep(2)
        insideVolvo()
    if direction == "quit" or direction == "exit" or direction == "leave":
        print("")
        print("Are you sure? Y/N")
        leave = input("")
        if leave == "y" or leave == "Y":
            fo = open('pork-save', 'w')
            fo.write('\n'.join(inventory))
            fo.close()
            fo = open('location', 'w')
            fo.write(area)
            fo.close()
            sys.exit()
        if leave == "n" or leave == "N":
            insideHouseDog()
    else:
        print("Sorry, I don't understand \"" + direction + "\".")
        time.sleep(1)
        insideHouseDog()



def deathByDogRunaway():
    print("You try to escape, but it is no use -- the dog catches up to you and takes you down.")
    sys.exit()

def dogStickLoop():
    area = "dogStickLoop"
    print("The dog catches the twig, and brings it back to you.")
    direction = input("")
    if direction == "throw stick in house" or direction == "Throw stick in house" or direction == "Toss stick in house" or direction == "toss stick in house" or direction == "throw twig in house" or direction == "Throw twig in house" or direction == "Toss twig in house" or direction == "toss twig in house" and "Twig" in inventory:
        dogStickLoop()
    if direction == "throw stick outside" or direction == "Throw stick outside" or direction == "Toss stick ouside" or direction == "toss stick outside" or direction == "Throw twig outside" or direction == "throw twig outside" and "Twig" in inventory:
        finish()
    if direction == "throw pencil in house" or direction == "Throw pencil in house" or direction == "Toss pencil in house" or direction == "toss pencil in house" and "Pencil" in inventory:
        dogPencilLoop()
    if direction == "throw pencil outside" or direction == "Throw pencil outside" or direction == "Toss pencil ouside" or direction == "toss pencil outside" and "Pencil" in inventory:
        finishPencil()
    if direction == "pet dog" or direction == "Pet dog":
        petDog()
    if direction == "hug dog" or direction == "Hug dog":
        hugDog()
    if direction == "kick dog" or direction == "Kick dog":
        kickDog()
    if direction == "punch dog" or direction == "Punch dog":
        punchDog()
    if direction == "Throw stick at dog" or direction == "throw stick at dog":
        throwStickAtDog()
    if direction == "Throw pencil at dog" or direction == "throw pencil at dog":
        throwPencilAtDog()
    if direction == "Throw candle at dog" or direction == "throw candle at dog":
        throwCandleAtDog()
    if direction == "Throw key at dog" or direction == "throw key at dog":
        throwKeyAtDog()
    if direction == "Throw journal at dog" or direction == "throw journal at dog":
        throwJournalAtDog()
    if direction == "Read journal" or direction == "read journal" and "Journal" in inventory:
        import journaltext
        time.sleep(2)
        garden()
    if direction == "items" or direction == "inventory" or direction == "i":
        print(inventory)
        time.sleep(2)
        insideVolvo()
    if direction == "quit" or direction == "exit" or direction == "leave":
        print("")
        print("Are you sure? Y/N")
        leave = input("")
        if leave == "y" or leave == "Y":
            fo = open('pork-save', 'w')
            fo.write('\n'.join(inventory))
            fo.close()
            fo = open('location', 'w')
            fo.write(area)
            fo.close()
            sys.exit()
        if leave == "n" or leave == "N":
            dogStickLoop()
    else:
        print("Sorry, I don't understand \"" + direction + "\".")
        time.sleep(1)
        dogStickLoop()


def dogPencilLoop():
    area = "dogPencilLoop"
    print("The dog catches the pencil, and brings it back to you.")
    direction = input("")
    if direction == "throw stick in house" or direction == "Throw stick in house" or direction == "Toss stick in house" or direction == "toss stick in house" or direction == "throw twig in house" or direction == "Throw twig in house" or direction == "Toss twig in house" or direction == "toss twig in house" and "Twig" in inventory:
        dogStickLoop()
    if direction == "throw stick outside" or direction == "Throw stick outside" or direction == "Toss stick ouside" or direction == "toss stick outside" or direction == "Throw twig outside" or direction == "throw twig outside" and "Twig" in inventory:
        happyDogTwig()
    if direction == "throw pencil in house" or direction == "Throw pencil in house" or direction == "Toss pencil in house" or direction == "toss pencil in house" and "Pencil" in inventory:
        dogPencilLoop()
    if direction == "throw pencil outside" or direction == "Throw pencil outside" or direction == "Toss pencil ouside" or direction == "toss pencil outside" and "Pencil" in inventory:
        happyDogPencil()
    if direction == "pet dog" or "Pet dog":
        petDog()
    if direction == "hug dog" or "Hug dog":
        hugDog()
    if direction == "kick dog" or "Kick dog":
        kickDog()
    if direction == "punch dog" or "Punch dog":
        punchDog()
    if direction == "Throw stick at dog" or direction == "throw stick at dog":
        throwStickAtDog()
    if direction == "Throw pencil at dog" or direction == "throw pencil at dog":
        throwPencilAtDog()
    if direction == "Throw candle at dog" or direction == "throw candle at dog":
        throwCandleAtDog()
    if direction == "Throw key at dog" or direction == "throw key at dog":
        throwKeyAtDog()
    if direction == "Throw journal at dog" or direction == "throw journal at dog":
        throwJournalAtDog()
    if direction == "Read journal" or direction == "read journal" and "Journal" in inventory:
        import journaltext
        time.sleep(2)
        garden()
    if direction == "items" or direction == "inventory" or direction == "i":
        print(inventory)
        time.sleep(2)
        insideVolvo()
    if direction == "quit" or direction == "exit" or direction == "leave":
        print("")
        print("Are you sure? Y/N")
        leave = input("")
        if leave == "y" or leave == "Y":
            fo = open('pork-save', 'w')
            fo.write('\n'.join(inventory))
            fo.close()
            fo = open('location', 'w')
            fo.write(area)
            fo.close()
            sys.exit()
        if leave == "n" or leave == "N":
            dogPencilLoop()
    else:
        print("Sorry, I don't understand \"" + direction + "\".")
        time.sleep(1)
        dogPencilLoop()



def petDog():
    print("You try to pet the dog, but it takes you down first.")
    sys.exit()

def hugDog():
    print("You try to hug the dog, but it takes you down first.")
    sys.exit()

def kickDog():
    print("You kick the dog, but it catches your foot and takes you down.")
    sys.exit()

def punchDog():
    print("You punch the dog, but it catches your fist and takes you down.")
    sys.exit()

def throwStickAtDog():
    print("You throw the twig at the dog, but it only aggrivates it. The dog then proceeds to take you down.")
    sys.exit()

def throwPencilAtDog():
    print("You throw the pencil at the dog, but it only aggrivates it. The dog then proceeds to take you down.")
    sys.exit()

def throwKeyAtDog():
    print("You throw the key at the dog, but it only aggrivates it. The dog then proceeds to take you down.")
    sys.exit()

def throwJournalAtDog():
    print("You throw the journal at the dog, but it only aggrivates it. The dog then proceeds to take you down.")
    sys.exit()

def throwCandleAtDog():
    print("You throw the candle at the dog, but it only aggrivates it. The dog then proceeds to take you down.")
    sys.exit()

def happyDogTwig():
    area = "happyDogTwig"
    emptyCup = "No"
    if "Paper" in inventory and emptyCup != "Yes":
        print("In front of you, there is a cup of cocoa.")
    elif "Paper" in inventory and emptyCup == "Yes":
        print("In front of you, there is an empty cup.")
    elif emptyCup == "Yes" and "Paper" not in inventory:
        print("In front of you, there is a piece of paper.")
    else:
        print("The dog runs out the door to catch the twig. You close the door behind it, and you are safe. In front of you, there is a cup of cocoa and a piece of paper.")
    direction = input("")
    if direction == "Open door" or direction == "open door":
        print("The dog is waiting at the door, and it takes you down.")
        sys.exit()
    if direction == "Drink cocoa" or direction == "drink cocoa":
        print("It was delicious!")
        emptyCup = "Yes"
        happyDogTwig()
    if direction == "Take cocoa" or direction == "take cocoa" or direction == "Take cup" or direction == "take cup":
        print("You cannot take the cocoa.")
    if direction == "Pour cocoa on floor" or direction == "pour cocoa on floor" or direction == "Drop cocoa" or direction == "drop cocoa" or direction == "Drop cup" or direction == "drop cup":
        print("The cocoa flies back into the cup as it falls.")
    if direction == "Take paper" or direction == "take paper":
        print("Taken.")
        inventory.append("Paper")
        time.sleep(1)
        happyDogTwig()
    if direction == "Read paper" or direction == "read paper" and "Paper" in inventory:
        print("Congradulations! You have successfully completed PORK! Yay!")
    if direction == "Read journal" or direction == "read journal" and "Journal" in inventory:
        import journaltext
        time.sleep(2)
        happyDogTwig()
    if direction == "items" or direction == "inventory" or direction == "i":
        print(inventory)
        time.sleep(2)
        happyDogTwig()
    if direction == "quit" or direction == "exit" or direction == "leave":
        print("")
        print("Are you sure? Y/N")
        leave = input("")
        if leave == "y" or leave == "Y":
            fo = open('pork-save', 'w')
            fo.write('\n'.join(inventory))
            fo.close()
            fo = open('location', 'w')
            fo.write(area)
            fo.close()
            sys.exit()
        if leave == "n" or leave == "N":
            happyDogTwig()
    else:
        print("Sorry, I don't understand \"" + direction + "\".")
        time.sleep(1)
        happyDogTwig()


def happyDogPencil():
    area = "happyDogPencil"
    emptyCup = "No"
    if "Paper" in inventory and emptyCup != "Yes":
        print("In front of you, there is a cup of cocoa.")
    elif "Paper" in inventory and emptyCup == "Yes":
        print("In front of you, there is an empty cup.")
    elif emptyCup == "Yes" and "Paper" not in inventory:
        print("In front of you, there is a piece of paper.")
    else:
        print("The dog runs out the door to catch the pencil. You close the door behind it, and you are safe. In front of you, there is a cup of cocoa and a piece of paper.")
    direction = input("")
    if direction == "Open door" or direction == "open door":
        print("The dog is waiting at the door, and it takes you down.")
        sys.exit()
    if direction == "Drink cocoa" or direction == "drink cocoa":
        print("It was delicious!")
        emptyCup = "Yes"
        happyDogPencil()
    if direction == "Take cocoa" or direction == "take cocoa" or direction == "Take cup" or direction == "take cup":
        print("You cannot take the cocoa.")
        time.sleep(2)
        happyDogPencil()
    if direction == "Pour cocoa on floor" or direction == "pour cocoa on floor" or direction == "Drop cocoa" or direction == "drop cocoa" or direction == "Drop cup" or direction == "drop cup":
        print("The cocoa flies back into the cup as it falls.")
    if direction == "Take paper" or direction == "take paper":
        print("Taken.")
        inventory.append("Paper")
        time.sleep(1)
        happyDogPencil()
    if direction == "Read paper" or direction == "read paper" or direction == "examine paper" or direftion == "Examine paper" and "Paper" in inventory:
        print("Congradulations! You have successfully completed PORK! Yay!")
        sys.exit()
    if direction == "Read journal" or direction == "read journal" and "Journal" in inventory:
        import journaltext
        time.sleep(2)
        happyDogPencil()
    if direction == "items" or direction == "inventory" or direction == "i":
        print(inventory)
        time.sleep(2)
        happyDogPencil()
    if direction == "quit" or direction == "exit" or direction == "leave":
        print("")
        print("Are you sure? Y/N")
        leave = input("")
        if leave == "y" or leave == "Y":
            fo = open('pork-save', 'w')
            fo.write('\n'.join(inventory))
            fo.close()
            fo = open('location', 'w')
            fo.write(area)
            fo.close()
            sys.exit()
        if leave == "n" or leave == "N":
            happyDogPencil()
    else:
        print("Sorry, I don't understand \"" + direction + "\".")
        time.sleep(1)
        happyDogPencil()








if __name__ == '__main__': begin()