from TcAds.Variable import Variable as Variable
from TcAds.Engine import Engine as Engine
from TcAds.Plc import Plc as Plc


engine = Engine()

#TwinCAT_Projekt1.Untitled1.MAIN.intWert000

var1 = Variable('MAIN.intWert000')
var1.writeValue = 161
plc = Plc()
plc.writeValue(var1)
plc.updateValues(var1)

var2 = Variable('MAIN.intWert008')
plc.updateValues(var2)


print(engine.valueDict[var1.name])
print(engine.valueDict[var2.name])