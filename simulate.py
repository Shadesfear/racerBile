import watermelon
import random
from watermelon import *

turns = [0,0,0,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
turns = [0,0,1,0,0,1,0,1,1,1,1,0,0,1,1,]


players = [Player(count, turns) for count in range(3)]


players[0].gear = 1
players[0].pos = 2
players[1].gear = 2
players[1].pos = 1
players[2].gear = 1

players[2].STALIN = True


print(len(turns))

for i in range(10):

    for player in players:


        player.take_turn()

        pos = {player.getPos()[0]: player.getPos()[1] for player in players}

        sidst = min(pos.items(), key=lambda x: x[1])
        først = max(pos.items(), key=lambda x: x[1])

        players[int(sidst[0])].sidst = True
        players[int(først[0])].først = True

        #print("sidste er ", sidst)

print(pos)

for player in players:
    print(player, player.omgange, player.taare)
