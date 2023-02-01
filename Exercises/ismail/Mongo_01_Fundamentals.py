import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
print(*client.list_database_names(),sep="\n")

dbName = "korkmazDb"
for item in client.list_database_names():
    if item == dbName: 
        print("Veritabanı zaten var")
    db = client[dbName] 
print(*client.list_database_names(),sep="\n")
collectionName = "korkmazKoleksiyon"
for item in db.list_collection_names():
    if item in collectionName: 
        print("Koleksiyon zaten var")
    col = db[collectionName]
print(*client.list_database_names(),sep="\n")
print(*db.list_collection_names(),sep="\n")
