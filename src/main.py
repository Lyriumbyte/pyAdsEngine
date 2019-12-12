from TcAds.Variable import Variable as Variable
from TcAds.Engine import Engine as Engine
from TcAds.Plc import plc as plc
plc = plc()



plc.plc.open()
plc.writeIntByName('MAIN.intWert001',12)
plc.plc.close()

engine = Engine()

var1 = Variable("Test1",int())
var2 = Variable("Test2",str())
var3 = Variable("Test3",bool())
var1.name = "Hans"
var1.indexOffset = 121
var1.writeValue = True
var1.datatype = str()



engine.addVariable(var1)
engine.addVariable(var2)
engine.addVariable(var3)



print(var1)
#print(engine.valueDict[var1])
