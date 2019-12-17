from TcAds.Engine import Engine as Engine

from device1 import Device1 as device1
from device2 import Device2 as device2

device1 = device1()
device2 = device2()
engine = Engine()


def do():
    '''contains the code thats also run with read and write (logic func)'''
    device1.movex()
    device2.movex()

def declareVars():
    '''in here declare your Variables to the valueDict Dictionary'''
    engine = Engine()

    engine.addVariables(device1.var1)
    engine.addVariables(device1.var2)
    engine.addVariables(device2.var1)
    engine.addVariables(device2.var2)


#runs Program
declareVars()
engine.run(do,0.3,engine.valueDict)