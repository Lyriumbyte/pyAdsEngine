class Variable:

    # constructor
    def __init__(self, name):
        self.__name = name
    '''
    Vars
    '''
    __name = str()

    # Handle
    __indexGroup = int()
    __indexOffset = int()

    # Values
    __objValue = object()
    __previousValue = object()
    __writeValue = object()

    isDirty = bool()

# Updates Value if a value is allready there
    def updateValue(self, newObjValue):
        if self.__objValue != None:
            self.__previousValue = self.__objValue
        self.__objValue = newObjValue

    '''
    Getter/Setter + Properties
    '''

    # Getter, Setter Property for Name
    def __getName(self):
        return self.__name

    def __setName(self, name):
        self.__name = name

    name = property(__getName, __setName)

    # Getter, Setter Property for Indexgroup
    def __getIndexGroup(self):
        return self.__indexGroup

    def __setIndexGroup(self, indexGroup):
        self.__indexGroup = indexGroup

    indexGroup = property(__getIndexGroup, __setIndexGroup)

    # Getter, Setter Property for Indexoffset
    def __getIndexOffset(self):
        return self.__indexOffset

    def __setIndexOffset(self, indexOffset):
        self.__indexOffset = indexOffset

    indexOffset = property(__getIndexOffset, __setIndexOffset)

    # Getter, Setter Property for objValue
    def __getObjValue(self):
        return self.__objValue

    def __setObjValue(self, objValue):
        self.__objValue = objValue

    objValue = property(__getObjValue, __setObjValue)

    # Getter, Setter Property for prevValue
    def __getPrevValue(self):
        return self.__previousValue

    def __setPrevValue(self, prevValue):
        self.__previousValue = prevValue

    previousValue = property(__getPrevValue, __setPrevValue)

    # Getter, Setter Property for WriteValue
    def __getWriteValue(self):
        return self.__writeValue

    def __setWriteValue(self, writeValue):
        self.__writeValue = writeValue

    writeValue = property(__getWriteValue, __setWriteValue)
