import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
dbName = "Cem"
db=client[dbName]
colName = "MUSTERILER"
col=db[colName]
sozluk = {
    "adi":"Cem",
    "soyadi":"Göktaş",
    "tel":"5554445544",
    "email":"cem@cem.com"
}
res = col.insert_one(sozluk) #### insertOne
print(*client.list_database_names(),sep="\n")
print("-"*30)
print(*db.list_collection_names(),sep="\n")

