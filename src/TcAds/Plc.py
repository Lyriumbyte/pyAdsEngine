import pyads
from TcAds.Engine import Engine as Engine

engine = Engine()

class Plc():
    __plc = pyads.Connection('127.0.0.1.1.1', 851) #local connection

    def __init__(self):
        pass

    '''def writeIntByName(self,name,value):
        self.__plc.open()
        self.__plc.write_by_name(str(name),value,pyads.PLCTYPE_INT)
        self.__plc.close()'''

    def writeValue(self,variable):
        # opens connection
        self.__plc.open()
        
        #Writes Bool
        if isinstance(variable.objValue,bool):
            self.__plc.write_by_name(variable.name,variable.writeValue, pyads.PLCTYPE_BOOL)
            variable.isDirty = False

        #Writes String
        elif isinstance(variable.objValue,str):
             self.__plc.write_by_name(variable.name,variable.writeValue, pyads.PLCTYPE_STRING)
             variable.isDirty = False

        #Writes Integer
        elif isinstance(variable.objValue,int):
            self.__plc.write_by_name(variable.name,variable.writeValue, pyads.PLCTYPE_INT)
            variable.isDirty = False

        #closes connection
        self.__plc.close()

    def __readValue(self, variable):
        #opens connection
        self.__plc.open()

        #returns Bool
        if isinstance(variable.objValue,bool):
            return self.__plc.read_by_name(variable.name, pyads.PLCTYPE_BOOL)
        
        #returns String
        if isinstance(variable.objValue,str):
            return self.__plc.read_by_name(variable.name, pyads.PLCTYPE_STRING)
        
        #returns Integer
        if isinstance(variable.objValue,int):
           return self.__plc.read_by_name(variable.name, pyads.PLCTYPE_INT)
            


        #closes connection
        self.__plc.close()

    def updateValues(self, variable):
        #opens connection
        self.__plc.open()

        newValue = self.__readValue(variable)
        variable.updateValue(newValue)
        engine.addVariables(variable)


        #closes connection
        self.__plc.close()