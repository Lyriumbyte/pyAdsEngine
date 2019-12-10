class Variable:

    #constructor
    def __init__(self, name):
        self.name = name
    '''
    Vars
    '''
    name = str()

    #Handle
    indexGroup = int()
    indexOffset = int()

    #Values
    objValue = object()
    previousValue = object()
    writeValue = object()
    
    isDirty = bool()

#Updates Value if a value is allready there
    def updateValue (self,newObjValue):
        if self.objValue != None:
            self.previousValue = self.objValue
        self.objValue = newObjValue

    
   

