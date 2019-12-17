
from TcAds.Variable import Variable as Variable
import pyads


class Device2():
    var1 = Variable('MAIN.intWert021',pyads.PLCTYPE_INT)
    var2 = Variable('MAIN.intWert020',pyads.PLCTYPE_INT)
    var3 = Variable('Main.intWert019',pyads.PLCTYPE_INT)

    def __init__(self):
        pass


    def movex(self):
        #does stuff
        if self.var1.Value<59:
            self.var1.Value=self.var1.Value+1
        elif self.var2.Value<59:
            self.var2.Value=self.var2.Value+1
            self.var1.Value = 0
        else:
            self.var3.Value = self.var3.Value+1
            self.var2.Value = 0

        