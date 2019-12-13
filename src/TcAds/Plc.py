import pyads

class Plc():
    __plc = pyads.Connection('127.0.0.1.1.1', 851) #local connection

    def __init__(self):
        pass

    def writeIntByName(self,name,value):
        self.__plc.open()
        self.__plc.write_by_name(str(name),value,pyads.PLCTYPE_INT)
        self.__plc.close()

    def writeValue(self,variable):
        self.__plc.open()
        
        #self.__plc.write_by_name(variable.name,variable.objValue, pyads.PLCTYPE_UINT)
        print(variable.datatype)
        if isinstance(variable.objValue,bool):
            self.__plc.write_by_name(variable.name,variable.objValue, pyads.PLCTYPE_BOOL)

        elif isinstance(variable.objValue,str):
             self.__plc.write_by_name(variable.name,variable.objValue, pyads.PLCTYPE_STRING)

        elif isinstance(variable.objValue,int):
            self.__plc.write_by_name(variable.name,variable.objValue, pyads.PLCTYPE_INT)


        self.__plc.close()

    