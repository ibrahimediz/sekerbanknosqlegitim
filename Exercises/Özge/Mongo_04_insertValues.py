import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
dbName = "ozge"
db=client[dbName]
colName = "musteriler"
col=db[colName]
liste = [{
    "adi":"Özge",
    "soyadi":"Şenkul",
    "tel":"5555555",
    "email":"ozge@senkul.com"
},{
    "adi":"Ege",
    "soyadi":"Şenkul",
    "tel":"5550000",
    "email":"ege@senkul.com"
}
] # çoklu döküman
res = col.insert_many(liste) #### insertmany ile birden fazla dökümanı koleksiyona ekleyebiliriz.
print(*client.list_database_names(),sep="\n")
print("-"*30)
print(*db.list_collection_names(),sep="\n")
print(res.inserted_ids) # [ObjectId('63da565bc5840d76461dab23'), ObjectId('63da565bc5840d76461dab24')]