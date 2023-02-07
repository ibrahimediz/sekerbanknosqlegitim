import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")

#####  Sort
# with client:
#     db = client.ediz
#     # ORDER BY adi DESC,soyadi ASC
#     # liste = db.musteriler.find({},{"_id":0,"adi":1,"soyadi":1}).sort("adi",pymongo.DESCENDING).sort("soyadi",pymongo.ASCENDING)
#     liste = db.musteriler.find({},{"_id":0,"adi":1,"soyadi":1}).sort([("adi",pymongo.DESCENDING),("soyadi",pymongo.ASCENDING)])
#     for item in liste:
#         print(item)
######## limit
with client:
    db = client.ediz
    liste = db.musteriler.find({},{"_id":0,"adi":1,"soyadi":1}).limit(4)
    for item in liste:
        print(item)