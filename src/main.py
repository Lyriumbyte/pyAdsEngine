from TcAds import Variable  as Engine
from TcAds import Engine  as TcAds

TcAds.Variable = Engine.Variable

var1 = TcAds.Variable("Test")

TcAds.Engine.valueDict [var1.name] = [var1.indexOffset, var1.indexGroup]


'''
var1.name = "Hans"
var1.indexOffset = 121
print(var1.name)
var1.writeValue = 5
'''

print(TcAds.Engine.valueDict)

print(var1)
