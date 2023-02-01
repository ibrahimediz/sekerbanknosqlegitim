import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")

dbName = "EmreKavak"
for item in client.list_database_names():
    if item == dbName:  
        print("Veritabanı zaten var")
    db = client[dbName] 

collectionName = "Musteriler"
for item in db.list_collection_names():
    if item == collectionName:
        print("Koleksiyon zaten var")
    col = db[collectionName] 


