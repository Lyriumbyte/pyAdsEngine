from TcAds.Variable import Variable as Variable
from TcAds.Engine import Engine as Engine
from TcAds.Plc import plc as plc
plc = plc()

plc.plc.open()
plc.test('MAIN.intArray001',12)
plc.plc.close()

engine = Engine()

var1 = Variable("Test1")
var2 = Variable("Test2")
var3 = Variable("Test3")
var1.name = "Hans"
var1.indexOffset = 121
var1.writeValue = 5

engine.addVariable(var1)
engine.addVariable(var2)
engine.addVariable(var3)



print(var1)
#print(engine.valueDict[var1])
