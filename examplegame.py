import tiletextrpg as tt

inputfile = "map.txt"
#inputfile = sys.argv[1]

tt.parsemap(tt.openfile(inputfile))
tt.findplayerhome(tt.map)

tt.printgametitle()

tt.updateplayer()

while True:
    try:
        tt.parseinput(input("> "))
    except KeyboardInterrupt:
        tt.quitgame()