import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
dbName = "ediz"
db=client[dbName]
colName = "musteriler"
col=db[colName]



# update_many
#yenideger = {"$set":{"adi":"ediz@ibrahimediz.com"}}
#sorgu = {"yas":{"$gt":0}}
#result = col.find(sorgu,{})
#    print(item)
#for item in result:
#guncelleme = col.update_many(sorgu, yenideger)
#result = col.find(sorgu,{})
#for item in result:
#    print(item)
#print(guncelleme.modified_count)

""" Egzersiz
Kendi veritabanı ve koleksiyonunda duran dökümanda adi alanındaki bilgiyi 
tümünü büyük harf yapacak şekilde değiştirelim
Mongo_08_update.py dosyası içerisine egzersizinizi yapabilirsiniz.
"""

with client:
    db = client.ediz
    liste = db.musteriler.find()
    for item in liste:
        print(item["_id"])
        sorgu = {"_id":{"$eq":item["_id"]}}
        yenideger = {"$set":{"adi":item["adi"].upper()}}
        guncelle = db.musteriler.update_one(sorgu, yenideger)
