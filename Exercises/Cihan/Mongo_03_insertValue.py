import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")

dbName = "ciaydin"
db=client[dbName]

colName = "sample_123"
col=db[colName]

sozluk = {
    "adi":"Ali",
    "soyadi":"Veli",
    "tel":"5554950",
    "email":"ali@veli.com"
}

res = col.insert_one(sozluk) #### insertOne ile tekbir kayıt koleksiyona kaydedildi.
#print(*client.list_database_names(),sep="\n")
#print("-"*30)
#print(*db.list_collection_names(),sep="\n")
print(res.inserted_id) # 

