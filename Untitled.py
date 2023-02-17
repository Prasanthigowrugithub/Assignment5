#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Challenge 3: Implement the Complete Student Class
class Student:
    def _init(self,name,_RollNmber):  #private properties
        self._name=_name
        self._RollNumber=_RollNmber
        print(f"name  : {self._name} \nrollno : {_RollNmber}")

    def setName(self,name): 
        self.__name=name
    def getName(self):
        return self.__name
    def setRollNumber(self,Rollnumber):
        self.__RollNumber=Rollnumber
    def getRollNumber(self):
        return self.__RollNumber
obj=Student("sia",67)
(obj.setName("kim"))
(obj.setRollNumber(7))
print((obj.getName()))
print((obj.getRollNumber()))

