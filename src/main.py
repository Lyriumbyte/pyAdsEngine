from TcAds import Variable  as Engine

var1 = Engine.Variable("Test")

var1.name = "Hans"
print(var1.name)
var1.writeValue = 5


print(var1)