class Engine:

    from TcAds.Plc import Plc as Plc
    import time

    valueDict = {}
    plc = Plc()

    def __init__(self):
        pass

    

    def addVariables(self, variable):
        """Adds variable """
        self.valueDict[variable.name] = variable
    

    def __str__(self):
        return self.valueDict

    def run(self, logic_func, sleepDuration, varList):
        self.plc.prepare()
        """runs function given as postional argument and blockWrite and blockRead with given list"""
        while 1:
            self.plc.blockWriteValues(varList)
            self.plc.blockUpdateValues(varList)
            logic_func()
            self.time.sleep(sleepDuration)
        self.plc.close()
            