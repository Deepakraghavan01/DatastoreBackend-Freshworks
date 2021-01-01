import time
import json
from os import path,getcwd
datas={}
filesize = 1024*3 
valuesize = 16*1024*1024
class Ds:
    def __init__(self,L=getcwd()): #getcwd is used to get the current working directory
        self.loc = L
        if(path.isdir(self.loc)): #check the directory exist or not
            try:
                self.filename = "\\"+input("enter the file name")+".json"
                fileds = open(str(self.loc)+self.filename,"x")
                fileds.write(json.dumps(datas)) #write the data in json format in that file
                print("1)create file \n 2)Read file \n 3) Delete file")
            except:
                print("file name already exist")
        else:
            print("File directory not exist")
    def Create(self,key,value,time_sec=0):
        if key in datas: # checks whether the key in dictionary or not
            print("the key is already exist")
        else:
            if key.isalpha():
                if(len(key)>32): #check the length of the key character
                    print("enter the key character less than 32")
                else:
                    if(len(datas)<filesize and value <= valuesize): #To validate the file is less than 1GB and the json value must be less than or equal to 16KB
                        time_stamp = time_sec
                        if time_sec!=0:
                            time_stamp = int(time.time())+time_sec  
                        datas[key] = [value,time_stamp]
                        print("data is successfully created")
                    else:
                        print("Memory size exceed")
            else:
                print("enter the key in only alphabet")
    def Read(self,key):
        if key in datas:
            values = datas[key]
            if values[1] < int(time.time()) and values[1]!=0: #checks the time-to-live property
                print("Time_to_live for the key is expired")
            else:
                print(str(key)+":"+str(values[0]))  #for returning the JSON format
        else:
            print("key does not exist")
    def Delete(self,key):
        if key in datas:
            values = datas[key]
            if values[1] < int(time.time()) and values[1]!=0:
                print("Time-to-live for the key is expired")
            else:
                del datas[key]
                print("The key has been deleted!")
        else:
            print("Key does not exist")
D = Ds()
