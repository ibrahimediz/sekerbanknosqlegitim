# import pymongo as pym
# cli =  pym.MongoClient()
# from pymongo import MongoClient as mgc,message as msg
# cli = mgc()
"""
SELECT fun, profit FROM real_world WHERE relatinal=false
"""

import os
os.chdir("./Exercises")
print(os.listdir())
for item in os.listdir():
    open(f"{item}/Mongo_01_Fundamentals.py","a")
