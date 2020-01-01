# tiletextrpg
A python program for generic text-based adventure games, loaded from a text file with python dictionary / JSON data.

**How To Use**

In the console, with python 3 installed:

<pre> python3 /path/to/tiletextrpg.py /path/to/map.json </pre>

To make your own game "map", simply create a text file that provides data like this:

<pre> {"game":"GameTitle",
       "home":"0, 0",
       "tiles":
              {"0, 0":{"name":"TileName","desc":"description text"},
               "0, 1":{"name":"TileName","desc":"description text"},
               "0, -1":{"name":"TileName","desc":"description text"},
               "-1, 0":{"name":"TileName","desc":"description text"},
               "1, 0":{"name":"TileName","desc":"description text"},
               "0, 2":{"name":"TileName","desc":"description text"}}
       }
</pre>

It uses x-y coordinates to specify locations - e.g. north = +1 y, south = -1y, east = +1x, west = -1x

Don't leave out a tile in between other tiles - otherwise, the game obviously won't allow the player to walk into an "abyss".

TODO: Making variables/methods that allow the user to specify custom messages for various parts.

So far, the only thing available to the player is generic "go north/south/east/west" commands - more functionality will be added in the future (e.g. items and inventory, food and health pickups, etc.)
