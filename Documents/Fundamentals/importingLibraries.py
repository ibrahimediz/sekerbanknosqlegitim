# import pymongo as pym
# cli =  pym.MongoClient()
# from pymongo import MongoClient as mgc,message as msg
# cli = mgc()
"""
SELECT fun, profit FROM real_world WHERE relatinal=false
"""

# import os
# os.chdir("./Exercises")
# print(os.listdir())
# for item in os.listdir():
#     open(f"{item}/Mongo_02_createDB.py","a")

########## Çalıştır #############
import subprocess as sub
import os
os.chdir("./Exercises")
print(os.listdir())
for item in os.listdir():
    dosya = open(f"{item}/Mongo_02_createDB.py","r")
    if dosya.read() !=  "":
        print("#"*20,f"{item}","#"*20)
        res = sub.run(["python",f"{item}/Mongo_02_createDB.py"],stderr=sub.PIPE,text=True)
        print(res)