from TcAds.Variable import Variable as Variable
from TcAds.Engine import Engine as Engine
from TcAds.Plc import plc as plc

import device1 as Device1
import device2 as Device2

engine = Engine()

d1 = Device1.Device1()
d2 = Device2.Device2()

engine.addVariables(d1.getVariables()) #todo addVariables (plural, Liste, Array)
engine.addVariables(d2.getVariables())

#engine.updateHandle() #todo updateHandles


























plc = plc()



plc.plc.open()
plc.writeIntByName('MAIN.intWert001',12)
plc.plc.close()



var1 = Variable("Test1",int())
var2 = Variable("Test2",str())
var3 = Variable("Test3",bool())
var1.name = "Hans"
var1.indexOffset = 121
var1.writeValue = True
var1.datatype = str()



engine.addVariables(var1)
engine.addVariables(var2)
engine.addVariables(var3)



print(var1)
#print(engine.valueDict[var1])
