class Variable():

    def __init__(self):
        pass

############
# Vars
############
    name = str()
    indexGroup = int()
    indexOffset = int()
    objValue = object()
    previousValue = object()
    writeValue = object()
    isDirty = bool()

    def updateValue (self,newObjValue):
        if self.objValue != None:
            self.previousValue = self.objValue
        self.objValue = newObjValue

    def toString(self):
        str(self.name+","+str(self.objValue))
   

