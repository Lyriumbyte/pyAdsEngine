
from TcAds.Variable import Variable as Variable
from TcAds.Engine import Engine as Engine
from TcAds.Plc import Plc as Plc
from Example.device1 import Device1 as device1
from Example.device2 import Device2 as device2

class Machine():

    device1 = device1()
    device2 = device2()
    engine = Engine()
    plc = Plc()


    def do(self):
        #What the variables should do
        self.device1.movex()
        self.device2.movex()




def addVariables():
    engine = Engine()

    #Add Variables here
    engine.addVariables(device1.var1)
    engine.addVariables(device1.var2)
    engine.addVariables(device2.var1)
    engine.addVariables(device2.var2)

def main(self):
    #runs code
    engine = Engine()
    addVariables()

    engine.run(self.do,0.3,engine.valueDict)

if __name__ == "__main__":
    main
