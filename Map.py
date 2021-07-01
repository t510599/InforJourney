from Events import Shop, Blacksmith
from Data import Bosses as Boss
from Entity import Monster
from Gen import ChestGen, MonsterGen
from Data import Positions

def GenMap():
    Map = [None for i in range(41)]
    l = list(range(41))
    for i in Positions["Boss"]:
        l.remove(i)
        Map[i] = Monster(*Boss[i//10-1][0:7])

    for i in Positions["Shop"]:
        l.remove(i)
        Map[i] = Shop(i//10)
        
    for i in Positions["Blacksmith"]:
        l.remove(i)
        Map[i] = Blacksmith(i//10)

    for i in Positions["ChestGen"]:
        l.remove(i)
        Map[i] = ChestGen()
    for i in l: # MonsterGen
        Map[i] = MonsterGen()
    return Map