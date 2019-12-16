import pyads


class Plc():
    __plc = pyads.Connection('127.0.0.1.1.1', 851) #local connection

    def __init__(self):
        pass

    
    def __writeValue(self,variable):
        # opens connection
        self.__plc.open()
        
        #Writes Bool
        if isinstance(variable.Value,bool):
            self.__plc.write_by_name(variable.name,variable.writeValue, pyads.PLCTYPE_BOOL)
            variable.isDirty = False

        #Writes String
        elif isinstance(variable.Value,str):
             self.__plc.write_by_name(variable.name,variable.writeValue, pyads.PLCTYPE_STRING)
             variable.isDirty = False

        #Writes Integer
        elif isinstance(variable.Value,int):
            self.__plc.write_by_name(variable.name,variable.writeValue, pyads.PLCTYPE_INT)
            variable.isDirty = False

        #closes connection
        self.__plc.close()

    def __readValue(self, variable):
        #opens connection
        self.__plc.open()

        #returns Bool
        if isinstance(variable.Value,bool):
            return self.__plc.read_by_name(variable.name, pyads.PLCTYPE_BOOL)
        
        #returns String
        if isinstance(variable.Value,str):
            return self.__plc.read_by_name(variable.name, pyads.PLCTYPE_STRING)
        
        #returns Integer
        if isinstance(variable.Value,int):
           return self.__plc.read_by_name(variable.name, pyads.PLCTYPE_INT)
            


        #closes connection
        self.__plc.close()

    def __updateValues(self, variable):
        #opens connection
        self.__plc.open()

        newValue = self.__readValue(variable)
        variable.updateValue(newValue)


        #closes connection
        self.__plc.close()

    def blockWriteValues(self, varList):

        #opens connection
        self.__plc.open()

        #for loop through list with variable entries
        for x in varList:

            #checks if there are unsaved changes
            if varList[x].isDirty:
                self.__writeValue(varList[x])


        #closes connection
        self.__plc.close()

    def blockUpdateValues(self, varList):

        #opens connection
        self.__plc.open()

        #for loop through list with variable entries
        for x in varList:

            self.__updateValues(varList[x])


        #closes connection
        self.__plc.close()