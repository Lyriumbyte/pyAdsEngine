#todo
from TcAds.Variable import Variable as Variable
import pyads


class Device1:
    var1 = Variable('MAIN.intWert000',pyads.PLCTYPE_INT)
    var2 = Variable('MAIN.intWert001',pyads.PLCTYPE_INT)

    def __init__(self):
        pass



    def movex(self):
        #does stuff
        if self.var1.Value<50:
            self.var1.Value = self.var2.Value+1
            self.var2.Value = self.var2.Value+1
        else:
            self.var1.Value = 0
            self.var2.Value = 0
            

