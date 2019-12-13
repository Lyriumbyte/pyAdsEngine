from TcAds.Variable import Variable as Variable
from TcAds.Engine import Engine as Engine
from TcAds.Plc import Plc as Plc


engine = Engine()

#TwinCAT_Projekt1.Untitled1.MAIN.intWert000

var1 = Variable('MAIN.intWert000')
var1.writeValue = 13
plc = Plc()


var2 = Variable('MAIN.intWert006')
var2.writeValue = 99


var3 = Variable('MAIN.intWert018')
var3.writeValue = 978

engine.addVariables(var1)
engine.addVariables(var2)
engine.addVariables(var3)


plc.blockUpdateValues()


plc.blockWriteValues()





