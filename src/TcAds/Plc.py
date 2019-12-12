import pyads

class plc():
    plc = pyads.Connection('127.0.0.1.1.1', 851) #local connection

    def __init__(self):
        pass

    def writeIntByName(self,name,value):
        self.plc.write_by_name(str(name),value,pyads.PLCTYPE_INT)