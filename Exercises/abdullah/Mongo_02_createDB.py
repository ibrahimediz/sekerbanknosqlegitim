import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
dbName = "abdullah"
db=client[dbName]
colName="musteriler"
col=db[colName]
sozluk={
    "adi":"abdullah",
      "soyadi":"hamarat",
        "tel":"555",
          "email":"a@gmail.com"
}
res=col.insert_one(sozluk)
print(*client.list_database_names(),sep="\n")
print("-"*30)
print(*db.list_collection_names(),sep="\n")
print(res.inserted_id)
