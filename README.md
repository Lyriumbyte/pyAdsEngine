# PyAdsEngine
## TcAds
### Variable
Contains following Variables:
- Name
- indexGroup
- indexHandle
- Object Value
- Write Value
- Previous Value

Function Update Value:

`if self.__objValue != None:`   
` self.__previousValue = self.__objValue`   
` self.__objValue = newObjValue`    
Saves Value in Previous Value and new Value in Value

### Engine
Contains Dictionary with Values   
Function addVariables: Adds Variables to Dictionary   
Function run: Parameters:                     
- logic_func: runs given function
- sleepDuration: Sleeping time
- varList: writes and updates given List if you don't use the dictionary

write all values from given list   
updates list   
runs given function  
sleeps

### Plc
opens connection to TwinCat   
write a single value (bool, int and string)   
reads a single value   
writes all values   
reads all values
## Example
### Machine
do: where you can declare which device code you want to run   
addVariables: where you can add your variables to the dictionary   
main: runs addVarables and engine.run
### Device1
device example
### Device2
device example