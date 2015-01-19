import time
import sys
global inventory
inventory = []

def begin():
    print("Major Adventure")
    print("Created by Meorge")
    time.sleep(2)
    inventory = []
    frontOfHouseEast()

def frontOfHouseEast():
    print("")
    print("Front Of House - Facing East")
    print("You are standing on the front porch of your house. A car is parked in the driveway. Behind you is a locked door.")
    direction = input("")
    if direction == "Go east" or direction == "e" or direction == "go east" or direction == "walk east" or direction == "east":
        nextToCarEast()
    if direction == "Go south" or direction == "s" or direction == "go south" or direction == "walk south" or direction == "south":
        endOfPorchSouth()
    if direction == "Go north" or direction == "n" or direction == "go north" or direction == "walk north" or direction == "north":
        endOfPorchNorth()
    if direction == "Go west" or direction == "w" or direction == "go west" or direction == "walk west" or direction == "west":
        doorBlock()
    if direction == "items" or direction == "inventory" or direction == "i":
        print(inventory)
        time.sleep(2)
        frontOfHouseEast()
    if direction == "quit" or direction == "exit" or direction == "leave":
        print("")
        print("Are you sure? Y/N")
        leave = input("")
        if leave == "y" or leave == "Y":
            sys.exit()
        if leave == "n" or leave == "N":
            frontOfHouseEast()
    else:
        print("Sorry, I don't understand \"" + direction + "\".")
        time.sleep(1)
        frontOfHouseEast()

def nextToCarEast():
    print("")
    print("Next To Car - Facing East")
    print("Next to you is a green 2000 Subaru Forester. The door to the car is unlocked.")
    direction = input("")
    if direction == "Get in car" or direction == "c" or direction == "car" or direction == "get in car":
        insideCar()
    if direction == "Go west" or direction == "w" or direction == "go west" or direction == "walk west" or direction == "west":
        frontOfHouseEast()
    if direction == "items" or direction == "inventory" or direction == "i":
        print(inventory)
        time.sleep(2)
        nextToCarEast()
    if direction == "quit" or direction == "exit" or direction == "leave":
        print("")
        print("Are you sure? Y/N")
        leave = input("")
        if leave == "y" or leave == "Y":
            sys.exit()
        if leave == "n" or leave == "N":
            nextToCarEast()
    else:
        print("Sorry, I don't understand \"" + direction + "\".")
        time.sleep(1)
        nextToCarEast()

def endOfPorchNorth():
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
    if direction == "items" or direction == "inventory" or direction == "i":
        print(inventory)
        time.sleep(2)
        endOfPorchNorth()
    if direction == "quit" or direction == "exit" or direction == "leave":
        print("")
        print("Are you sure? Y/N")
        leave = input("")
        if leave == "y" or leave == "Y":
            sys.exit()
        if leave == "n" or leave == "N":
            endOfPorchNorth()
    else:
        print("Sorry, I don't understand \"" + direction + "\".")
        time.sleep(1)
        endOfPorchNorth()


def endOfPorchSouth():
    print("")
    print("End Of Porch - Facing South")
    print("You are facing the railing on the end of the porch. You cannot go any further north because of this. A swing is in front of you.")
    direction = input("")
    if direction == "Go north" or direction == "n" or direction == "go north" or direction == "walk north" or direction == "north":
        frontOfHouseEast()
    if direction == "Sit on swing" or direction == "sit down" or direction == "Swing" or direction == "swing" or direction == "c" or direction == "sit on swing":
        sittingOnSwing()
    if direction == "items" or direction == "inventory" or direction == "i":
        print(inventory)
        time.sleep(2)
        endOfPorchSouth()
    if direction == "quit" or direction == "exit" or direction == "leave":
        print("")
        print("Are you sure? Y/N")
        leave = input("")
        if leave == "y" or leave == "Y":
            sys.exit()
        if leave == "n" or leave == "N":
            endOfPorchSouth()
    else:
        print("Sorry, I don't understand \"" + direction + "\".")
        time.sleep(1)
        endOfPorchSouth()


def doorBlock():
    print("")
    print("Front Door of House - Facing West")
    print("A white door impedes your progress this way.")
    direction = input("")
    if direction == "Go back" or direction == "go back" or direction == "back" or direction == "b" or direction == "Go east" or direction == "e" or direction == "go east" or direction == "walk east" or direction == "east":
        frontOfHouseEast()
    if direction == "items" or direction == "inventory" or direction == "i":
        print(inventory)
        time.sleep(2)
        doorBlock()
    if direction == "quit" or direction == "exit" or direction == "leave":
        print("")
        print("Are you sure? Y/N")
        leave = input("")
        if leave == "y" or leave == "Y":
            sys.exit()
        if leave == "n" or leave == "N":
            doorBlock()
    else:
        print("Sorry, I don't understand \"" + direction + "\".")
        time.sleep(1)
        doorBlock()



def insideCar():
    print("")
    print("Inside Car - Facing South")
    if "Cup" in inventory:
        print("You are sitting inside the Forester.")
    else:
        print("You are sitting inside the Forester. There is a cup in the cup holder.")
    direction = input("")
    if direction == "Take cup" or direction == "take cup" and "Cup" not in inventory:
        print("Taken.")
        inventory.append("Cup")
        time.sleep(1)
        print()
        insideCar()
    if direction == "Get out of car" or direction == "get out of car" or direction == "outside" or direction == "get out" or direction == "Get out" or direction == "o":
        nextToCarEast()
    if direction == "items" or direction == "inventory" or direction == "i":
        print(inventory)
        time.sleep(2)
        insideCar()
    if direction == "quit" or direction == "exit" or direction == "leave":
        print("")
        print("Are you sure? Y/N")
        leave = input("")
        if leave == "y" or leave == "Y":
            sys.exit()
        if leave == "n" or leave == "N":
            insideCar()
    else:
        print("Sorry, I don't understand \"" + direction + "\".")
        time.sleep(1)
        insideCar()



def bottomOfSteps():
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
    if direction == "items" or direction == "inventory" or direction == "i":
        print(inventory)
        time.sleep(2)
        bottomOfSteps()
    if direction == "quit" or direction == "exit" or direction == "leave":
        print("")
        print("Are you sure? Y/N")
        leave = input("")
        if leave == "y" or leave == "Y":
            sys.exit()
        if leave == "n" or leave == "N":
            bottomOfSteps()
    else:
        print("Sorry, I don't understand \"" + direction + "\".")
        time.sleep(1)
        bottomOfSteps()



def sittingInChair():
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
    if direction == "items" or direction == "inventory" or direction == "i":
        print(inventory)
        time.sleep(2)
        sittingInChair()
    if direction == "quit" or direction == "exit" or direction == "leave":
        print("")
        print("Are you sure? Y/N")
        leave = input("")
        if leave == "y" or leave == "Y":
            sys.exit()
        if leave == "n" or leave == "N":
            sittingInChair()
    else:
        print("Sorry, I don't understand \"" + direction + "\".")
        time.sleep(1)
        sittingInChair()


def sittingOnSwing():
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
    if direction == "items" or direction == "inventory" or direction == "i":
        print(inventory)
        time.sleep(2)
        sittingOnSwing()
    if direction == "quit" or direction == "exit" or direction == "leave":
        print("")
        print("Are you sure? Y/N")
        leave = input("")
        if leave == "y" or leave == "Y":
            sys.exit()
        if leave == "n" or leave == "N":
            endOfPorchSouth()
    else:
        print("Sorry, I don't understand \"" + direction + "\".")
        time.sleep(1)
        endOfPorchSouth()


def inspectingVolvo():
    print("")
    print("Volvo - Facing West")
    print("You are standing in front of a white Volvo. The door is unlocked.")
    direction = input("")
    if direction == "Get in car" or direction == "c" or direction == "car" or direction == "get in car" or direction == "v" or direction == "Get in Volvo" or direction == "Get in volvo" or direction == "get in volvo" or direction == "get in Volvo":
        insideVolvo()
    if direction == "Go east" or direction == "e" or direction == "go east" or direction == "walk east" or direction == "east":
        bottomOfSteps()
    if direction == "items" or direction == "inventory" or direction == "i":
        print(inventory)
        time.sleep(2)
        inspectingVolvo()
    if direction == "quit" or direction == "exit" or direction == "leave":
        print("")
        print("Are you sure? Y/N")
        leave = input("")
        if leave == "y" or leave == "Y":
            sys.exit()
        if leave == "n" or leave == "N":
            inspectingVolvo()
    else:
        print("Sorry, I don't understand \"" + direction + "\".")
        time.sleep(1)
        inspectingVolvo()


def insideVolvo():
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
    if direction == "items" or direction == "inventory" or direction == "i":
        print(inventory)
        time.sleep(2)
        insideVolvo()
    if direction == "quit" or direction == "exit" or direction == "leave":
        print("")
        print("Are you sure? Y/N")
        leave = input("")
        if leave == "y" or leave == "Y":
            sys.exit()
        if leave == "n" or leave == "N":
            insideVolvo()
    else:
        print("Sorry, I don't understand \"" + direction + "\".")
        time.sleep(1)
        insideVolvo()


if __name__ == '__main__': begin()