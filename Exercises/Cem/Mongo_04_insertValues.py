import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
dbName = "Cem"
db=client[dbName]
colName = "MUSTERILER"
col=db[colName]
liste = [{
    "adi":"Cem",
    "soyadi":"CEM",
    "tel":"5554635",
    "email":"cem@cemgoktas.com"
},{
    "adi":"Cem",
    "soyadi":"Gkts",
    "tel":"5554636",
    "email":"cem@cem.com"
}
] # çoklu döküman
res = col.insert_many(liste) #### insertmany ile birden fazla dökümanı koleksiyona ekleyebiliriz.
print(*client.list_database_names(),sep="\n")
print("-"*30)
print(*db.list_collection_names(),sep="\n")
print(res.inserted_ids) # [ObjectId('63da565bc5840d76461dab23'), ObjectId('63da565bc5840d76461dab24')]