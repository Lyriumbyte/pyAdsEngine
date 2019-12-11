class Engine:

    valueDict = {}

    def __init__(self):
        pass

    # def addValue(self, name, indexGroup, indexOffset, objValue, previousObjectValue, writeValue):
    #     self.valueDict[name] = [indexGroup, indexOffset,
    #                             objValue, previousObjectValue, writeValue]

    def addVariable(self, variable):
        """Add variable """
        self.valueDict[variable.name] = variable
