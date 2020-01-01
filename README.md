# tiletextrpg
A python program for generic text-based adventure games, loaded from a text file with python dictionary / JSON data.

**How To Use**

In the console, with python 3 installed:

<pre> python3 /path/to/tiletextrpg.py /path/to/map.json </pre>

To make your own game "map", simply create a text file that provides data like this, the *map.json* file:

<pre> 
{"game":"Stupid Zork Clone",
 "home":"0, 0",
    "tiles":{
        "0, 0":{"name":"Home",
                "desc":"You are standing outside your home.\nTo the north is a dirt road, leading off into the distance.\nTo the west is a dense forest, where little sun reaches."},
        "0, 1":{"name":"Road",
                "desc":"A long road stretches out ahead of you, to the north."},
        "0, 2":{"name":"Road",
                "desc":"The road continues ahead of you, to the north; you can now see a house in the distance."},
        "0, 3":{"name":"House",
                "desc":"You are standing in a grassy field, with trees around it. In the middle of a field sits a large, yet quite run-down, house.",
                "subtile":{
                        "house":{"desc":"The inside of the house is very shabby - the windows are boarded and the walls are covered in mold.\nIt is very dark. You may be eaten by a grue..."}}},
        "-1, 0":{"name":"Forest",
                 "desc":"You are standing in a dense forest, made up of tall oak trees.\nTo the west lies a clearing, dark and sinister; to the east lies your home."},
        "-2, 0":{"name":"Forest Clearing",
                 "desc":"It is very dark, so dark you can barely see your hand in front of your face.\nYou are likely to be eaten by a grue.",
                 "death":{"cause":"grue","msg":"Oh no! A lurking grue slithered into the clearing and devoured you!"}}
    }
}
</pre>

More in-depth documentation to come, but this covers the current feature set quite well.

It uses x-y coordinates to specify locations - e.g. north = +1 y, south = -1y, east = +1x, west = -1x

Don't leave out a tile in between other tiles - otherwise, the game obviously won't allow the player to walk into an "abyss".

TODO: Making variables/methods that allow the user to specify custom messages for various parts.

So far, the only thing available to the player is generic "go north/south/east/west" commands - more functionality will be added in the future (e.g. items and inventory, food and health pickups, etc.)
