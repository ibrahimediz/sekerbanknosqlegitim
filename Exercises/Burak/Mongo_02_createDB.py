import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
dbName = "Burak"
db = client[dbName]
collectionName = "MUSTERILER"
for item in db.list_collection_names():
    if item in collectionName: 
        print("Koleksiyon zaten var")
    col = db[collectionName] 

