import json
import time
from PyQt5.QtWidgets import QFileDialog

#from memory_profiler import profile
class fileclass:
    def func(str):
        print(str)

    def sum(a, b):
        print(a+b)

    def sub(a, b):
        print(a-b)
    def getInput(self,filename):
        boolean=False
        dictionary = {}
        lst=[]
        file = open(filename, "r")
        string = file.read()
        string = string.split('\n')
        count = 0
        jsonS = ""
       # print("here")
       # print(string)
      #  print("here")
        
        for str in string:
            if (str.find(":") != -1 or str.find("{") != -1 or str.find("}") != -1):
                boolean=True
                if (str.find("{") != -1):
                    count = count + 1
                if (str.find("}") != -1):
                    count = count - 1
                jsonS = jsonS + str
                if (count == 0):
                    dictionary = json.loads(jsonS)
                    for i in dictionary:
                        dictionary.update({i : dictionary[i]})
            else:
               # print(lst)
                boolean=False
                lst.append(int(str))
        if (boolean):
            return boolean, dictionary,filename
        else:
            return boolean, lst,filename
    def main():
        boolean=False
        dictionary = {}
        lst=[]
        file = open("filing.txt", "r")
        string = file.read()
        string = string.split('\n')
        count = 0
        jsonS = ""
        for str in string:
            if (str.find(":") != -1 or str.find("{") != -1 or str.find("}") != -1):
                boolean=True
                if (str.find("{") != -1):
                    count = count + 1
                if (str.find("}") != -1):
                    count = count - 1
                jsonS = jsonS + str
                if (count == 0):
                    dictionary = json.loads(jsonS)
                    for i in dictionary:
                        print("")
            else:
                boolean=False
                lst.append(int(str))

  