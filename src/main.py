from TcAds.Variable import Variable as Variable
from TcAds.Engine import Engine as Engine
from TcAds.Plc import Plc as Plc


engine = Engine()

#TwinCAT_Projekt1.Untitled1.MAIN.intWert000

var1 = Variable('MAIN.intWert000')
var1.objValue = 161
var1.datatype
plc = Plc()
plc.writeValue(var1)