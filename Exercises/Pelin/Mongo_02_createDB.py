import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
dbName= "Pelin"
for item in client.list_database_names():
    db=client[dbName]
##print(*client.list_database_names(),sep="\n")
collectionName = "Musteriler"
for item in db.list_collection_names():
    col=db[collectionName]
