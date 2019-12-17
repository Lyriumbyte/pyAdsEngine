
from TcAds.Variable import Variable as Variable



class Device2():
    var1 = Variable('MAIN.intWert021')
    var2 = Variable('MAIN.intWert020')

    def __init__(self):
        pass


    def movex(self):
        #does stuff
        if self.var1.Value<25:
            self.var1.Value=self.var1.Value+1
            self.var2.Value=self.var2.Value+1
        else:
            self.var1.Value = 0

        