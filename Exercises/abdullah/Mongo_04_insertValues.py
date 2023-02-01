import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
dbName = "abdullah"
db=client[dbName]
colName = "musteriler"
col=db[colName]
liste = [{
    "adi":"abdullah",
    "soyadi":"hamarat",
    "tel":"555",
    "email":"a@gmail.com"
},{
    "adi":"Sezen",
    "soyadi":"hamarat",
    "tel":"556",
    "email":"szn@gmail.com"
}
] # çoklu döküman
res = col.insert_many(liste) #### insertmany ile birden fazla dökümanı koleksiyona ekleyebiliriz.
print(*client.list_database_names(),sep="\n")
print("-"*30)
print(*db.list_collection_names(),sep="\n")
print(res.inserted_ids) # [ObjectId('63da565bc5840d76461dab23'), ObjectId('63da565bc5840d76461dab24')]