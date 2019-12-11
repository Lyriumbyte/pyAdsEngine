from TcAds.Variable import Variable as Variable
from TcAds.Engine import Engine as Engine

engine = Engine()

var1 = Variable("Test1")
var2 = Variable("Test2")
var3 = Variable("Test3")

engine.addVariable(var1)
engine.addVariable(var2)
engine.addVariable(var3)

'''
var1.name = "Hans"
var1.indexOffset = 121
print(var1.name)
var1.writeValue = 5
'''

print(var1)
print(engine.valueDict)

