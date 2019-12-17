import pyads


class Plc():
    __plc = pyads.Connection('127.0.0.1.1.1', 851) #local connection

    def __init__(self):
        pass

    def prepare(self):
        '''opens connection'''
        self.__plc.open()
    
    def close(self):
        ''' closes connection'''
        self.__plc.close()
    
    def __writeValue(self,variable):

        if self.__plc.is_open:
            #Writes
            
            self.__plc.write_by_name(variable.name,variable.writeValue, variable.datatype)
            variable.isDirty = False


    def __readValue(self, variable):
        
        if self.__plc.is_open:
            
            #reads
             return self.__plc.read_by_name(variable.name, variable.datatype)
 
      
    def __updateValues(self, variable):
        
        if self.__plc.is_open:

            newValue = self.__readValue(variable)
            variable.updateValue(newValue)



    def blockWriteValues(self, varList):

        if self.__plc.is_open:

            #for loop through list with variable entries
            for x in varList:

                #checks if there are unsaved changes
                if varList[x].isDirty:
                    self.__writeValue(varList[x])


       
    def blockUpdateValues(self, varList):

        if self.__plc.is_open:

            #for loop through list with variable entries
            for x in varList:

                self.__updateValues(varList[x])

