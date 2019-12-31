import sys
import json

inputfile = "/home/brady/code/python/tiletextrpg/map.txt"
#inputfile = sys.argv[1]

keywords = {"movement":["move","go","walk","run","hike"]}

# Game Attributes
map = {}
playerpos = [None,None]

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
        print("failed to load JSON data from " + inputfile)
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

def updateplayer():

    global playerpos

    print("\n")
    print(map["tiles"][str(playerpos).strip("[]")]["name"])
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print(map["tiles"][str(playerpos).strip("[]")]["desc"])

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
        move(inputwords[1])
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

def quitgame():
    print("Goodbye.")
    sys.exit()