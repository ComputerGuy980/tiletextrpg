import sys
import json
from time import sleep

keywords = {"movement":["move","go","walk","run","hike"],
            "subtile":["enter","open"],
            "enter":["into","inside"],
            "exit":["leave","exit"]}

# Game Attributes
map = {}
playerpos = [None,None]
playersubtile = ""

def openfile(file):
    try:
        game = open(file)
        return game
    except FileNotFoundError:
        print("file not found: " + file)
        sys.exit()

def idk(term):
    print("What does \"" + term + "\" mean?")

def parsemap(inputmap):

    global map

    try:
        map = json.loads(inputmap.read())
    except:
        print("failed to load JSON data from " + str(inputmap))
        sys.exit()

def findplayerhome(map):

    global playerpos

    try:
        x = int(map["home"].split(",")[0])
        y = int(map["home"].split(",")[1])
    except:
        print("home formatted incorrectly: " + str(map))
        sys.exit()

    playerpos = [x,y]

def printgametitle():

    global map

    try:
        print("\n")
        print("#~#~#~#~#~#~#~#~#~#~#~#~#")
        print("\n")
        print(map["game"])
        print("\n")
        print("#~#~#~#~#~#~#~#~#~#~#~#~#")
        print("\n")
    except:
        print("no game title found.")
        sys.exit()

def updateplayer(subtile=None):

    global playerpos
    global playersubtile
    pp = str(playerpos).strip("[]")

    if subtile != None and subtile in map["tiles"][pp]["subtile"]:
        playersubtile = subtile
        print("\n")
        print("-> " + subtile)
        print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
        print(map["tiles"][pp]["subtile"][subtile]["desc"])
        if death in map["tiles"][pp]["subtile"][subtile]:
            death(map["tiles"][pp]["subtile"][subtile]["death"]["cause"],map["tiles"][pp]["subtile"][subtile]["death"]["msg"])
    else:
        playersubtile = ""
        print("\n")
        print(map["tiles"][pp]["name"])
        print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
        print(map["tiles"][pp]["desc"])
        if "death" in map["tiles"][pp]:
            death(map["tiles"][pp]["death"]["cause"],map["tiles"][pp]["death"]["msg"])

def checkfortile(x,y,direction):

    global playerpos

    if str([playerpos[0] + x,playerpos[1] + y]).strip("[]") in map["tiles"]:
        playerpos = [playerpos[0] + x,playerpos[1] + y]
        updateplayer()
    else:
        print("There is no location to the " + direction)

def parseinput(userinput):

    inputwords = userinput.lower().split(" ")

    if inputwords[0] in keywords["movement"]:
        if inputwords[1] not in keywords["enter"]:
            move(inputwords[1])
        else:
            print("Did you want to enter a sub-area? Use \"enter\" or \"open\".")
    elif inputwords[0] in keywords["subtile"]:
        entersubtile(inputwords[1])
    elif inputwords[0] in keywords["exit"]:
        entersubtile()
    elif inputwords[0] == "quit":
        quitgame()
    elif inputwords[0] == "":
        print("Please type something other than \"\".")
    else:
        idk(inputwords[0])

def move(direction):

    global playerpos

    if direction == "north" or direction == "up":
        checkfortile(0,1,"north")
    elif direction == "south" or direction == "down":
        checkfortile(0,-1,"south")
    elif direction == "east" or direction == "right":
        checkfortile(1,0,"east")
    elif direction == "west" or direction == "left":
        checkfortile(-1,0,"west")
    else:
        idk(direction)

def entersubtile(name=None):
    
    global playerpos
    pp = str(playerpos).strip("[]")
    if name != None:
        if "subtile" in map["tiles"][pp]:
            if name in map["tiles"][pp]["subtile"]:
                updateplayer(subtile=name)
    else:
        updateplayer()

def quitgame():
    print("Goodbye.")
    sys.exit()

def death(cause,message):
    sleep(2)
    print("\n")
    print(message)
    print("\n")
    sleep(1)
    print("***YOU HAVE DIED***".center(26))
    print(("Cause of death: " + cause).center(30))
    print("\n")
    sleep(2)
    print("Thank you for playing.")
    sleep(3)
    quitgame()

# If code is run individually, this is used

#inputfile = "/home/brady/code/python/tiletextrpg/map.json"
try:
    inputfile = sys.argv[1]
except:
    print("no command line argument given")
    sys.exit()

parsemap(openfile(inputfile))
findplayerhome(map)

printgametitle()

updateplayer()

while True:
    try:
        parseinput(input("> "))
    except KeyboardInterrupt:
        quitgame()