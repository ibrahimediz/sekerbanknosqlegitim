import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
dbName = "candb"
db=client[dbName]
colName = "sefer"
col=db[colName]
sozluk = {
    "seferno":"001",
    "kaptan":"murat",
    "rota":"1-2-3-5-1",
    "tarih":"20230201"
}
res = col.insert_one(sozluk) #### insertOne
print(*client.list_database_names(),sep="\n")
print("-"*30)
print(*db.list_collection_names(),sep="\n")