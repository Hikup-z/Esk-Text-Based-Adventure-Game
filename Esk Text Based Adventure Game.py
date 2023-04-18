from os import system
import sys 
from sys import exit
import time as t
import random as r
actions = ["move", "read", "pickup", "open", "enter", "shout", "hit", "shoot yourself", "scan room", "view inventory"]
directions = ["north", "east", "south", "west"]
nearbyObjects = []
global currentRoom
currentRoom = "forest1"
inventory = []
global isBedroomDoorLocked
isBedroomDoorLocked = True
global woodenBarsBroken
woodenBarsBroken = False
global windowOpened
windowOpened = False
global gateUnlocked
gateUnlocked = False
global cabinUnlocked
cabinUnlocked = False
global statueDoorUnlocked
statueDoorUnlocked = False

def stage2Begins():
    global currentRoom
    for i in range(40):
        print("$%#" * i)
    t.sleep(4)
    system('cls')
    print("Or so you thought...")
    inventory = []
    t.sleep(5)
    system('cls')
    print("The gate has led you to a huge forest, and you are lost in the middle of it")
    t.sleep(2)
    print("It looks like the sun is setting, and you have to find a way out before it gets dark,\n or you will be stuck in the forest forever.")
    t.sleep(2)
    print("You look around and can just about see a small cave, a cabin, and a grass path. ")
    t.sleep(4)
    currentRoom = "forest1"
    actionPicker(actions, nearbyObjects, inventory)

def gameInfo(actions, nearbyObjects):
    system('cls')
    print("Welcome To Esk!")
    t.sleep(1)
    print("This is a text based adventure game.")
    t.sleep(1)
    print("You will be given a description of your surroundings.")
    t.sleep(1)
    print("You will then be given a list of actions you can take.")
    t.sleep(1)
    print("You will be able to type in the action you want to take.")
    t.sleep(1) 
    print("You will then be given a description of your new surroundings.")
    t.sleep(1)
    print("The Game will now begin.")  
    t.sleep(3)
    system('cls')
    gameStart(actions, nearbyObjects)

def gameStart(actions, nearbyObjects):
    global currentRoom
    print("You have just woken up in a dark room, laying in bed")
    t.sleep(1)
    print("You can't remember how you got here.")
    t.sleep(1)
    print("You can't remember anything.")
    t.sleep(1)
    print("You can't even remember your own name.")
    t.sleep(1)
    print("You need to get out of here.")
    t.sleep(1)
    print("You feel for a light switch, and flick it on.")
    t.sleep(1)
    print("You are in a small room, with a bed, a desk, a shelf and a door")
    t.sleep(1)
    keepAsking = True
    while keepAsking == True:
        print("Your actions are: \n")
        i = 1
        for a in actions:
            print(str(i) + " - " + str(a))
            i += 1
        try:
            action = int(input("\nWhat would you like to do?: "))
        except ValueError:
            print("Enter Valid Data")
            t.sleep(1)
            continue
        
        if action == 1:
            move(nearbyObjects)
            keepAsking = False
        elif action == 2:
            print("You cant do that here!")
        elif action == 3:
            print("You cant do that here!")
        elif action == 4:
            print("You cant do that here!")
        elif action == 5:
            print("You cant do that here!")
        elif action == 6:
            print("You cant do that here!")
        elif action == 7:
            print("You cant do that here!")
        elif action == 8:
            print("You dont have anything to shoot yourself with!")
        elif action == 9:
            t.sleep(1)
            print("You scan the room")
            t.sleep(1)
            currentRoomInfo()
        elif action == 10:
            if len(inventory) == 0:
                print("You have nothing in your inventory!")
                t.sleep(1)
            else:
                print("You have the following in your inventory: ")
                for i in inventory:
                    print("- " + i)
                t.sleep(1)

        else:
            print("Action Not Recognised, Please try again.")


def move(nearbyObjects):
    global currentRoom
    print("These are your possile Directions")
    i = 1
    for d in directions:
        print(str(i) + " - " + str(d))
        i += 1
    try:
        direction = int(input("\nWhich Direction would you like to move in?: "))
    except ValueError:
        print("Enter Valid Data")
        t.sleep(1)
        move(nearbyObjects)
        
    if direction == 1:
        print("You move North")
        t.sleep(1)
        if currentRoom == "bedroom": 
            print("You are standing next to the door")
            nearbyObjects = ["bedroom door"]
            print(nearbyObjects)
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
        elif currentRoom == "bathroom":
            print("You are standing next to the sink and the door. ")
            nearbyObjects = ["sink", "door"]
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
        elif currentRoom == "kitchen":
            print("You are standing next to the fridge")
            nearbyObjects = ["fridge", "wall"]
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
        elif currentRoom == "garden":
            print("You are standing next to the gate")
            nearbyObjects = ["gate"]
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
        elif currentRoom == "forest1":
            print("You are standing next to the cabin")
            nearbyObjects = ["cabin"]
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
        elif currentRoom == "forest2":
            print("You are standing next to the lake. You see a boat, but are unsure if this can take you to safety.")
            nearbyObjects = ["lake", "boat"]
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
    elif direction == 2:
        print("You move East")
        t.sleep(1)
        if currentRoom == "bedroom":
            print("You are standing next to the shelf. It looks like theres a key on it.")
            nearbyObjects = ["key", "shelf", "wall"]
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
        elif currentRoom == "bathroom":
            print("You are standing next to the shower. ")
            nearbyObjects = ["shower", "wall"]
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
        elif currentRoom == "kitchen":
            print("You are standing next to the table and the door. On the table is a note. Weird")
            nearbyObjects = ["note", "table", "door", "wall"]
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
        elif currentRoom == "garden":
            print("You are standing next to the swing")
            nearbyObjects = ["swing"]
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
        elif currentRoom == "forest1":
            print("You are standing next to the cave, but cant quite see inside.")
            nearbyObjects = ["cave"]
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
        elif currentRoom == "forest2":
            print("You are standing next to the grass path")
            goDown = int(input("Would you like to walk down the grass path? (1 - Yes | 2 - No): "))
            if goDown == 1:
                print("You walk down the grass path")
                t.sleep(1)
                currentRoom = "forest1"
                currentRoomInfo()
            elif goDown == 2:
                print("You decide to stay where you are")
                t.sleep(1)
                currentRoomInfo()
            else:
                print("Invalid Input")
                t.sleep(1)
                currentRoomInfo()
            
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
    elif direction == 3:
        print("You move South")
        t.sleep(1)
        if currentRoom == "bedroom":
            print("You are standing next to the bed")
            nearbyObjects = ["bed"]
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
        elif currentRoom == "bathroom":
            print("You are standing next to the toilet. ")
            nearbyObjects = ["toilet"]
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
        elif currentRoom == "kitchen":
            print("You are standing next to the backdoor")
            nearbyObjects = ["door"]
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
        elif currentRoom == "garden":
            print("You are standing next to the house door")
            nearbyObjects = ["door"]
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
        elif currentRoom == "forest1":
            print("You are standing next to the gate back to the garden")
            goDown = int(input("Would you like to walk back to the garden? (1 - Yes | 2 - No): "))
            if goDown == 1:
                print("You walk back to the garden")
                t.sleep(1)
                currentRoom = "garden"
                currentRoomInfo()
            elif goDown == 2:
                print("You decide to stay where you are")
                t.sleep(1)
                currentRoomInfo()
            else:
                print("Invalid Input")
                t.sleep(1)
                currentRoomInfo()
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
        elif currentRoom == "forest2":
            print("You are standing next to the bomb shelter.")
            nearbyObjects = ["bomb shelter"]
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
    elif direction == 4:
        print("You move West")
        if currentRoom == "bedroom":
            print("You are standing next to the desk")
            nearbyObjects = ["desk"]
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
        elif currentRoom == "bathroom":
            print("You are standing next to the window. There is a piece of paper on the windowsill. Weird. ")
            nearbyObjects = ["window", "paper"]
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
        elif currentRoom == "kitchen":
            print("You are standing next to the oven")
            nearbyObjects = ["oven"]
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
        elif currentRoom == "garden":
            print("You are standing next to the shed. On the shed is a piece of grafitti. Weird.")
            nearbyObjects = ["graffiti", "shed"]
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
        elif currentRoom == "forest1":
            print("You are standing next to the grass path")
            goDown = int(input("Would you like to walk down the grass path? (1 - Yes | 2 - No): "))
            if goDown == 1:
                print("You walk down the grass path")
                t.sleep(1)
                currentRoom = "forest2"
                currentRoomInfo()
            elif goDown == 2:
                print("You decide to stay where you are")
                t.sleep(1)
                currentRoomInfo()
            else:
                print("Invalid Input")
                t.sleep(1)
                currentRoomInfo()
        elif currentRoom == "forest2":
            print("You are standing next to the statue, it looks like theres a secret door behind it")
            nearbyObjects = ["statue", "statue door"]
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
    else:
        print("Direction Not Recognised, Please try again.")
        t.sleep(2)
        move(nearbyObjects)

def read(nearbyObjects):
    global currentRoom
    readObjects = ["book", "note", "paper", "graffiti"]
    if "book" in nearbyObjects or "book" in inventory:
        print("You pick up the book and read it")
        t.sleep(1)
        print("It is a book about the history of this house")
        t.sleep(1)
        print("It says that this house was built in 1920")
        t.sleep(1)
        print("It says that the previous owner shot himself in the head. The gun was found by police and returned to the fridge, weird.")
        t.sleep(5)
        nearbyObjects.remove("book")
    elif "note" in nearbyObjects or "note" in inventory:
        print("You pick up the note and read it")
        t.sleep(1)
        print("It says 'To Felicia,\n I love you\n, I'm sorry you will never be able to see me again, but i promise i will always be with you in spirit,\nI know you will never understand why I killed myself, im sorry.\n\n From your husband'")
        t.sleep(5)
        nearbyObjects.remove("note")
    elif "paper" in nearbyObjects or "paper" in inventory:
        print("You pick up the paper and read it")
        t.sleep(1)
        print("It says I hate Myself. My life is a mess. If only I had the courage to drink this poisonous water. I would be free. I would be happy. I would be at peace. I would be dead.")
        t.sleep(5)
        nearbyObjects.remove("paper")
    elif "graffiti" in nearbyObjects:
        t.sleep(1)
        print("The Grafitti says 'IM GONNA OFF MYSELF'")
        t.sleep(5)
        nearbyObjects.remove("graffiti")
    elif "scroll" in nearbyObjects or "scroll" in inventory:
        print("You pick up the scroll and read it")
        t.sleep(1)
        print("It has only 1 word written on it. 'Ben', with the numbers 2514 written underneath it, the place in the alphabet for the letters B, E and N.")
        t.sleep(5)
        nearbyObjects.remove("scroll")
    else:
        print("You cant read that!")
        t.sleep(1)
    actionPicker(actions, nearbyObjects, inventory)
    

def pickup(nearbyObjects, inventory):
    global currentRoom
    pickupObjects = ["knife", "hammer", "key", "antidote", "water", "crowbar", "gun", "scroll", "cabin key", "statue key"]
    
    for o in nearbyObjects:
        if o in pickupObjects:
            if "key" in inventory and "key" in nearbyObjects:
                print("You already have the key")
                t.sleep(1)

            print("You have picked up the " + o)
            inventory.append(o)
            nearbyObjects.remove(o)
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
        else:
            print("You cant pick up the " + o)
            t.sleep(1)
    actionPicker(actions, nearbyObjects, inventory)
        
    

def open(nearbyObjects):
    global cabinUnlocked
    global statueDoorUnlocked
    global windowOpened
    global gateUnlocked
    global currentRoom
    global isBedroomDoorLocked
    openObjects = ["window", "fridge", "oven", "gate", "shed"]
    if "bedroom door" in nearbyObjects:
        if "key" in inventory:
            print("You have used your key and opened the door")
            t.sleep(1)
            print("Hint: You may want to ENTER the door to progress the game")
            t.sleep(1)
            isBedroomDoorLocked = False
            inventory.remove("key")
            actionPicker(actions, nearbyObjects, inventory)
        else:
            print("You try the handle, but quickly realise that the door is locked")
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
    elif "shed" in nearbyObjects:
        print("You open the shed and see a crowbar")
        t.sleep(1)
        nearbyObjects.remove("shed")
        nearbyObjects.append("crowbar")
        actionPicker(actions, nearbyObjects, inventory)
    elif "fridge" in nearbyObjects:
        print("You open the fridge and see a gun")
        t.sleep(1)
        nearbyObjects.remove("fridge")
        nearbyObjects.append("gun")
        actionPicker(actions, nearbyObjects, inventory)
    elif "desk" in nearbyObjects:
        print("You open the desk and see a key, it looks like it would fit the door.")
        t.sleep(1)
        nearbyObjects.remove("toilet")
        nearbyObjects.append("key")
        actionPicker(actions, nearbyObjects, inventory)
    elif "toilet" in nearbyObjects:
        print("You open the toilet and see a key. It looks like it would fit in a gate.")
        t.sleep(1)
        nearbyObjects.remove("toilet")
        nearbyObjects.append("key")
        actionPicker(actions, nearbyObjects, inventory)
    elif "gate" in nearbyObjects:
        if woodenBarsBroken == True:
            if gateUnlocked == False:
                if "key" in inventory: #AAAAAAA
                    print("You unlock the padlock and open the door. You are free! You win!")
                    t.sleep(2)
                    stage2Begins()
                else:
                    print("You try to open the door, but it is locked. You need a key to open it.")
                    t.sleep(1)
                    actionPicker(actions, nearbyObjects, inventory)
            else:
                print("You open the gate and walk out. You are free! You win!")
                t.sleep(2)
                stage2Begins()
        else:
            print("You need to HIT the wooden bars to break them")
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)

    elif "window" in nearbyObjects:
        print("You open the window and think that maybe someone could hear you if you shouted loud enough")
        t.sleep(1)
        windowOpened = True
        actionPicker(actions, nearbyObjects, inventory)

    elif "door" in nearbyObjects:
        print("You must ENTER the door. You can't open it.")
        t.sleep(1)
        currentRoomInfo()

    elif "oven" in nearbyObjects:
        print("You open the oven and see a book")
        t.sleep(1)
        nearbyObjects.remove("oven")
        nearbyObjects.append("book")
        actionPicker(actions, nearbyObjects, inventory)
    elif "cabin" in nearbyObjects:
        if "cabin key" in inventory or cabinUnlocked == True:
            cabinUnlocked = True
            print("You have unlocked the cabin, and inside you see a ancient scroll and a key, it looks like it would fit a secret door.")
            t.sleep(1)
            nearbyObjects.remove("cabin")
            nearbyObjects.append("scroll")
            nearbyObjects.append("statue key")
            if "cabin key" in inventory:
                inventory.remove("cabin key")
            actionPicker(actions, nearbyObjects, inventory)
        elif "cabin key" not in inventory:
            print("The cabin is locked. You need a key to open it.")
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
        else:
            print("Error")
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
    
    
    
    elif "statue door" in nearbyObjects:
        if "statue key" in inventory or statueDoorUnlocked == True:
            statueDoorUnlocked = True
            print("You unlock the secret door, and enter the room.")
            t.sleep(2)
            print("You are in the secret room. Infront of you, you see 3 doors, each with a different number on it.")
            t.sleep(2)
            print("The first door has got the number 19 on it.")
            t.sleep(2)
            print("The second door has got the number 23 on it.")
            t.sleep(2)
            print("The third door has got the number 17 on it.")
            t.sleep(2)
            print("Each of the doors has got a small window looking through it, and a keypad with a 4 digit entry code on it.")
            t.sleep(2)
            print("In room number 19, you see a room full of hungry lions.")
            t.sleep(2)
            print("In room number 23, you see a room full of cavemen, ready to kill you.")
            t.sleep(2)
            x = 1
            print("And in room number 17, you see a tunnel with a light at the end of it")
            t.sleep(3)
            doorChoice = int(input("Which room would you like to gain access to? (19/23/17) : "))
            if doorChoice == 19:
                keepAsk = True
                x = 1
                while keepAsk != False:
                    if x == 1:
                        print("You need to enter a 4 digit passcode to enter the room")
                        passCode = int(input("Enter Passcode here: "))
                        if passCode == 2514:
                            print("You have chosen the correct passcode, the door swings open.")
                            t.sleep(2)
                            print("The lions jump on top of you, and tear you to bits. You died.")
                            t.sleep(2)
                            gameEnd()
                    elif x == 2:
                        print("Ok!")
                        keepAsk = False
                        print("You have left the secret room")
                        t.sleep(2)
                        currentRoomInfo()
                    x = int(input("Would you like to try again?: (1 - Yes | 2 - No)"))

            if doorChoice == 23:
                keepAsk = True
                x=1
                while keepAsk != False:
                    if x == 1:
                        print("You need to enter a 4 digit passcode to enter the room")
                        passCode = int(input("Enter Passcode here: "))
                        if passCode == 2514:
                            print("You have chosen the correct passcode, the door swings open.")
                            t.sleep(2)
                            print("The Cave Men run out of the door and hit you with their sticks. You die.")
                            t.sleep(2)
                            gameEnd()
                    elif x == 2:
                        print("Ok!")
                        keepAsk = False
                        print("You have left the secret room")
                        t.sleep(2)
                        currentRoomInfo()
                    x = int(input("Would you like to try again?: (1 - Yes | 2 - No)"))

            if doorChoice == 17:
                keepAsk = True
                while keepAsk != False:
                    if x == 1:
                        print("You need to enter a 4 digit passcode to enter the room")
                        passCode = int(input("Enter Passcode here: "))
                        if passCode == 2514:
                            print("You have chosen the correct passcode, the door swings open.")
                            t.sleep(2)
                            print("You enter the tunnel, and crawl, and crawl, and crawl. You finally reach the light, and find yourself crawling out of a drain cover.\n You look around and see people all around you. You recognise this place, its your home town. Brighton.\n You have escaped the house. You are free. You win!")
                            t.sleep(10)
                            gameWin()
                    elif x == 2:
                        print("Ok!")
                        keepAsk = False
                        print("You have left the secret room")
                        t.sleep(2)
                        currentRoomInfo()
                    x = int(input("Would you like to try again?: (1 - Yes | 2 - No)"))

            

        else:
            print("The door is locked. You need a key to open it.")
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
      
def enter(nearbyObjects):
    global statueDoorUnlocked
    global cabinUnlocked
    global currentRoom
    global isBedroomDoorLocked
    global gateUnlocked
    global woodenBarsBroken
    enterObjects = ["door"]
    if "door" in nearbyObjects:
        if currentRoom == "bathroom":
            doorChoice = int(input("Would you like to \n1 - enter the bedroom, \n\tor \n2 - enter the kitchen?"))
            if doorChoice == 1:
                print("You enter the bedroom")
                t.sleep(1)
                currentRoom = "bedroom"
                currentRoomInfo()
            elif doorChoice == 2:
                print("You enter the kitchen")
                t.sleep(1)
                currentRoom = "kitchen"
                currentRoomInfo()
            t.sleep(1)

        elif currentRoom == "kitchen":
            doorChoice = int(input("Would you like to \n1 - enter the bathroom, \n\tor \n2 - enter the garden?"))
            if doorChoice == 1:
                print("You enter the bathroom")
                t.sleep(1)
                currentRoom = "bathroom"
                currentRoomInfo()
            elif doorChoice == 2:
                print("You enter the garden")
                t.sleep(1)
                currentRoom = "garden"
                currentRoomInfo()
                t.sleep(1)

        elif currentRoom == "garden":
            print("You enter the kitchen.")
            t.sleep(1)
            currentRoom = "kitchen"
            currentRoomInfo()
    elif "bedroom door" in nearbyObjects:
        global isBedroomDoorLocked
        if isBedroomDoorLocked == False:
            nearbyObjects.remove("bedroom door")
            if "key" in inventory:
                inventory.remove("key")
            print("You enter the bathroom")
            t.sleep(1)
            currentRoom = "bathroom"
            currentRoomInfo()
        else:
            if "key" in inventory:
                print("You have used your key and opened the door")
                t.sleep(1)
                currentRoom = "bathroom"
                inventory.remove("key")
                currentRoomInfo()
            else:
                print("The door is locked. You need a key to open it")
                t.sleep(1)
                actionPicker(actions, nearbyObjects, inventory)
                
    elif "gate" in nearbyObjects:
        if woodenBarsBroken == True:
            if gateUnlocked == False:
                if "key" in inventory:
                    print("You unlock the padlock and open the door. You are free! You win!")
                    t.sleep(2)
                    stage2Begins()
                else:
                    print("You try to open the door, but it is locked. You need a key to open it.")
                    t.sleep(1)
                    actionPicker(actions, nearbyObjects, inventory)
            else:
                print("You open the gate and walk out. You are free! You win!")
                t.sleep(2)
                stage2Begins()
        else:
            print("The gate has wooden bars blocking it. You need a crowbar to break through them.")
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
    elif "cabin" in nearbyObjects:
        if "cabin key" in inventory or cabinUnlocked == True:
            cabinUnlocked = True
            print("You have unlocked the cabin, and inside you see a ancient scroll and a key, it looks like it would fit a secret door.")
            t.sleep(1)
            nearbyObjects.remove("cabin")
            inventory.append("statue key")
            nearbyObjects.append("scroll")
            if "cabin key" in inventory:
                inventory.remove("cabin key")
            actionPicker(actions, nearbyObjects, inventory)
        elif "cabin key" not in inventory:
            print("The cabin is locked. You need a key to open it.")
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
        else:
            print("Error")
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
    elif "cave" in nearbyObjects:
        print("You enter the cave")
        t.sleep(1)
        print("You see a human skeleton, with a hammer in his hand.")
        nearbyObjects.remove("cave")
        nearbyObjects.append("hammer")
        actionPicker(actions, nearbyObjects, inventory)
    elif "bomb shelter" in nearbyObjects:
        print("You enter the bomb shelter")
        t.sleep(1)
        print("You see a key on the floor, which looks like it might fit in the cabin.")
        nearbyObjects.remove("bomb shelter")
        if "cabin key" in inventory:
            print("You have already picked up the key")
        else:
            nearbyObjects.append("cabin key")

        print("You also notice a small tunnel at the back of the shelter. (HINT: ENTER the tunnel to access it)")
        nearbyObjects.append("tunnel")
        t.sleep(5)
        actionPicker(actions, nearbyObjects, inventory)
    elif "tunnel" in nearbyObjects:
        print("You enter the tunnel, and crawl for what feels like forever.\nFinally, you see a light, and crawl through the exit.\n You have found yourself back in the bedroom.")
        currentRoom = "bedroom"
        currentRoomInfo()
    elif "statue door" in nearbyObjects:
        if "statue key" in inventory or statueDoorUnlocked == True:
            statueDoorUnlocked = True
            print("You unlock the secret door, and enter the room.")
            t.sleep(2)
            print("You are in the secret room. Infront of you, you see 3 doors, each with a different number on it.")
            t.sleep(2)
            print("The first door has got the number 19 on it.")
            t.sleep(2)
            print("The second door has got the number 23 on it.")
            t.sleep(2)
            print("The third door has got the number 17 on it.")
            t.sleep(2)
            print("Each of the doors has got a small window looking through it, and a keypad with a 4 digit entry code on it.")
            t.sleep(2)
            print("In room number 19, you see a room full of hungry lions.")
            t.sleep(2)
            print("In room number 23, you see a room full of cavemen, ready to kill you.")
            t.sleep(2)
            print("And in room number 17, you see a tunnel with a light at the end of it")
            t.sleep(3)#
            x = 1
            doorChoice = int(input("Which room would you like to gain access to? (19/23/17) : "))
            if doorChoice == 19:
                keepAsk = True
                while keepAsk != False:
                    if x == 1:
                        print("You need to enter a 4 digit passcode to enter the room")
                        passCode = int(input("Enter Passcode here: "))
                        if passCode == 2514:
                            print("You have chosen the correct passcode, the door swings open.")
                            t.sleep(2)
                            print("The lions jump on top of you, and tear you to bits. You died.")
                            t.sleep(2)
                            gameEnd()
                    elif x == 2:
                        print("Ok!")
                        keepAsk = False
                        print("You have left the secret room")
                        t.sleep(2)
                        currentRoomInfo()
                    x = int(input("Would you like to try again?: (1 - Yes | 2 - No)"))

            if doorChoice == 23:
                keepAsk = True
                while keepAsk != False:
                    if x == 1:
                        print("You need to enter a 4 digit passcode to enter the room")
                        passCode = int(input("Enter Passcode here: "))
                        if passCode == 2514:
                            print("You have chosen the correct passcode, the door swings open.")
                            t.sleep(2)
                            print("The Cave Men run out of the door and hit you with their sticks. You die.")
                            t.sleep(2)
                            gameEnd()
                    elif x == 2:
                        print("Ok!")
                        keepAsk = False
                        print("You have left the secret room")
                        t.sleep(2)
                        currentRoomInfo()
                    x = int(input("Would you like to try again?: (1 - Yes | 2 - No)"))

            if doorChoice == 17:
                keepAsk = True
                while keepAsk != False:
                    if x == 1:
                        print("You need to enter a 4 digit passcode to enter the room")
                        passCode = int(input("Enter Passcode here: "))
                        if passCode == 2514:
                            print("You have chosen the correct passcode, the door swings open.")
                            t.sleep(2)
                            print("You enter the tunnel, and crawl, and crawl, and crawl. You finally reach the light, and find yourself crawling out of a drain cover.\n You look around and see people all around you. You recognise this place, its your home town. Brighton.\n You have escaped the house. You are free. You win!")
                            t.sleep(10)
                            gameWin()
                    elif x == 2:
                        print("Ok!")
                        keepAsk = False
                        print("You have left the secret room")
                        t.sleep(2)
                        currentRoomInfo()
                    x = int(input("Would you like to try again?: (1 - Yes | 2 - No)"))


        else:
            print("The door is locked. You need a key to open it.")
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
            
        
    
    elif "boat" in nearbyObjects:
        print("You have entered the boat. You sail down the river for what feels like forever until finally you see the sea...\nThe river sends you far out, miles away from any form of civilisation.\nYou eventually starve to death. You failed to escape.")
        t.sleep(10)
        gameEnd()

    else:
        print("There is nothing to enter!")
        t.sleep(1)
        actionPicker(actions, nearbyObjects, inventory)
      



import random
def shout(nearbyObjects):
    global windowOpened
    if currentRoom == "garden":
        print("You shouted but nobody can hear you, if you find a window, you may be able to shout out of it")
        t.sleep(1)
        actionPicker(actions, nearbyObjects, inventory)
    if windowOpened == False:
        print("Maybe if you find an open window, you could shout loud enough for someone to hear you")
        t.sleep(1)
        actionPicker(actions, nearbyObjects, inventory)
    elif windowOpened == True:
        print("You shout as loud as you can for help.")
        t.sleep(1)
        randChoice = int(input("You must pick a number between 1 and 5, if you guess the correct number then someone will hear you and come to help you. What number do you pick?: "))
        randomNum = random.randint(1,5)
        if randChoice == randomNum:
            t.sleep(1)
            print("You hear a noise outside and someone smashes through the window to save you, or so you thought. The man kills you, you lose.")
            t.sleep(2)
            gameEnd()
        else:
            print("No one hears you. You are still trapped.")
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)
    else:
        print("The window is closed, so nobody can hear your shouts.")
        t.sleep(1)
        actionPicker(actions, nearbyObjects, inventory)

def hit(nearbyObjects):
    global woodenBarsBroken
    hitObjects = ["wall", "door", "window", "bed", "desk"]
    if "wall" in nearbyObjects:
        print("You hit the wall and it hurts")
        t.sleep(1)
        actionPicker(actions, nearbyObjects, inventory)
    elif "door" in nearbyObjects or "bedroom door" in nearbyObjects:
        print("You hit the door and it hurts")
        t.sleep(1)
        actionPicker(actions, nearbyObjects, inventory)
    elif "window" in nearbyObjects:
        print("You hit the window and it hurts")
        t.sleep(1)
        actionPicker(actions, nearbyObjects, inventory)
    elif "bed" in nearbyObjects:
        print("You hit the bed and it hurts")
        t.sleep(1)
        actionPicker(actions, nearbyObjects, inventory)
    elif "desk" in nearbyObjects:
        print("You hit the desk and it hurts")
        t.sleep(1)
        actionPicker(actions, nearbyObjects, inventory)
    elif "shower" in nearbyObjects:
        print("You hit the shower and it hurts")
        t.sleep(1)
        actionPicker(actions, nearbyObjects, inventory)
    elif "fridge" in nearbyObjects:
        print("You hit the fridge and it hurts")
        t.sleep(1)
        actionPicker(actions, nearbyObjects, inventory)
    elif "oven" in nearbyObjects:
        print("You hit the oven and it hurts")
        t.sleep(1)
        actionPicker(actions, nearbyObjects, inventory)
    elif "toilet" in nearbyObjects:
        print("You hit the toilet and it hurts")
        t.sleep(1)
        actionPicker(actions, nearbyObjects, inventory)
    elif "gate" in nearbyObjects:
        if "crowbar" in inventory:
            if woodenBarsBroken == False:
                print("You hit the wooden bars with your crowbar and they break")
                t.sleep(1)
                woodenBarsBroken = True
                actionPicker(actions, nearbyObjects, inventory)
            else:
                print("You have already broken the wooden bars")
                t.sleep(1)
                actionPicker(actions, nearbyObjects, inventory)
        else:
            print("You hit the wooden bars with your fist and it hurts, you need a crowbar to get through them")
            t.sleep(1)
            actionPicker(actions, nearbyObjects, inventory)

    else:
        print("You cant hit that")
        t.sleep(1)
        actionPicker(actions, nearbyObjects, inventory)

def currentRoomInfo():
    global currentRoom
    if currentRoom == "bedroom":
        print("You are in the bedroom. There is a bed, a desk, a window and a door.")
        t.sleep(2)
        actionPicker(actions, nearbyObjects, inventory)
    elif currentRoom == "bathroom":
        print("You are in the bathroom. There is a toilet, a sink, a window and a door.")
        t.sleep(2)
        actionPicker(actions, nearbyObjects, inventory)
    elif currentRoom == "kitchen":
        print("You are in the kitchen. There is a fridge, an oven, a table and the back door.")
        t.sleep(2)
        actionPicker(actions, nearbyObjects, inventory)
    elif currentRoom == "garden":
        print("You are outside. There is a gate, a shed, a swing and a door.")
        t.sleep(2)
        actionPicker(actions, nearbyObjects, inventory)
    elif currentRoom == "forest1":
        print("You are in the forest, you look around and see a small cave, a cabin, and a grass path.")
        t.sleep(2)
        actionPicker(actions,nearbyObjects, inventory)
    elif currentRoom == "forest2":
        print("Yoy are in a deeper part of the forest, you see a statue, a bomb shelter and a river.")
        t.sleep(2)
        actionPicker(actions, nearbyObjects, inventory)
    #elif currentRoom == "secret room":
    #    print("You are in a small room with a light bulb hanging from the ceiling.\n You see 3 doors, one red, one yellow and one blue.")
    else:
        print("You are in the " + currentRoom)
        t.sleep(2)
        actionPicker(actions, nearbyObjects, inventory)



def actionPicker(actions, nearbyObjects, inventory):
    t.sleep(2)
    system('cls')
    global currentRoom
    global isBedroomDoorLocked
    keepAsking = True
    while keepAsking == True:
        print("Your actions are: \n")
        i = 1
        for a in actions:
            print(str(i) + " - " + str(a))
            i += 1

        try:
            action = int(input("\nWhat would you like to do?: "))
        except ValueError:
            print("Enter Valid Data")
            t.sleep(1)
            actionPicker(action, nearbyObjects, inventory)

        if action == 1:
            move(nearbyObjects)
            keepAsking = False
        elif action == 2:
            readables = ["book", "note", "paper", "graffiti", "scroll"]
            if readables in nearbyObjects:
                read(nearbyObjects)
                keepAsking = False
            else:
                print("Theres nothing to read!")
        elif action == 3:
            if "knife" in nearbyObjects or "hammer" in nearbyObjects or "key" in nearbyObjects or "antidote" in nearbyObjects or "water" in nearbyObjects or "crowbar" in nearbyObjects or "gun" in nearbyObjects or "cabin key" in nearbyObjects or "statue key" in nearbyObjects:
                if "key" in nearbyObjects and "key" in inventory:
                    print("You already have the key")
                    t.sleep(1)
                    actionPicker(actions, nearbyObjects, inventory)
                pickup(nearbyObjects, inventory)
                keepAsking = False
            else:
                print("Theres nothing to pick up!")
        elif action == 4:
            if "window" in nearbyObjects or "fridge" in nearbyObjects or "oven" in nearbyObjects or "gate" in nearbyObjects or "shed" in nearbyObjects or "bedroom door" in nearbyObjects or "door" in nearbyObjects or "toilet" in nearbyObjects or "cabin"  in nearbyObjects or "statue door" in nearbyObjects:
                open(nearbyObjects)
                keepAsking = False
            else:
                print("Theres nothing to open!")
        elif action == 5:
            if "door" in nearbyObjects or "window" in nearbyObjects or "bedroom door" in nearbyObjects or "cabin" in nearbyObjects or "statue door" in nearbyObjects or "cave" in nearbyObjects or "bomb shelter" in nearbyObjects or "tunnel" in nearbyObjects or "boat" in nearbyObjects or "gate" in nearbyObjects:
                enter(nearbyObjects)
                keepAsking = False
            else:
                print("Theres nothing to enter!")
        elif action == 6:
            shout(nearbyObjects)
        elif action == 7:
            if "wall" in nearbyObjects or "door" in nearbyObjects or "window" in nearbyObjects or "bed" in nearbyObjects or "desk" in nearbyObjects or "gate" in nearbyObjects:
                hit(nearbyObjects)
                keepAsking = False
            else:
                print("Theres nothing to hit!")
        elif action == 8:
            if "gun" in inventory:
                randNum  = random.randint(1, 10)
                if randNum == 1:  
                    print("You shoot yourself in the head. You Died!")
                    t.sleep(2)
                    gameEnd()
                else:
                    print("The gun jammed and it broke. Better luck next time!")
                    inventory.remove("gun")
                    t.sleep(2)
                    actionPicker(actions, nearbyObjects, inventory)
            else:
                print("You dont have a gun! (or the facilities for that big man) ")
        elif action == 9:
            t.sleep(1)
            print("You scan the room")
            t.sleep(1)
            currentRoomInfo()
        elif action == 10:
            if len(inventory) == 0:
                print("You have nothing in your inventory!")
                t.sleep(1)
            else:
                print("You have the following in your inventory: ")
                for i in inventory:
                    print("- " + i)
                t.sleep(1)
        else:
            print("Action Not Recognised, Please try again.")


def gameEnd():
    t.sleep(4)
    system('cls')
    print("Game Over")
    t.sleep(4)
    exit()

def gameWin():
    t.sleep(15)
    system('cls')
    for i in range(40):
        print("$%#" * i)
    print("Or so you thought...")
    t.sleep(10)
    system('cls')
    print("just kidding i cba to code anymore")
    t.sleep(4)
    print("Well done you won, only took u 7 weeks to complete.")
    t.sleep(100)
    exit()

#actionPicker(actions, nearbyObjects, inventory)
gameInfo(actions, nearbyObjects)
#stage2Begins()