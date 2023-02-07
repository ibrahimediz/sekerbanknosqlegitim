import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")


# update_one
# sorgu = {"yas":{"$gt":40}}
# yenideger = {"$set":{"email":"ediz@ibrahimediz.com"}}
# col.update_one(sorgu, yenideger)
# result = col.find(sorgu,{})
# for item in result:
#     print(item)


# update_many
# sorgu = {"yas":{"$gt":40}}
# yenideger = {"$set":{"email":"ediz@ibrahimediz.com"}}
# result = col.find(sorgu,{})
# for item in result:
#     print(item)
# guncelleme = col.update_many(sorgu, yenideger)
# result = col.find(sorgu,{})
# for item in result:
#     print(item)
# print(guncelleme.modified_count)

""" Egzersiz
Kendi veritabanı ve koleksiyonunda duran dökümanda adi alanındaki bilgiyi tümünü büyük harf yapacak şekilde değiştirelim
Mongo_08_update.py dosyası içerisine egzersizinizi yapabilirsiniz.
"""

with client:
    db = client.abdullah
    liste = db.musteriler.find()
    for item in liste:
        print(item["_id"])
        sorgu = {"_id":{"$eq":item["_id"]}}
        yenideger = {"$set":{"adi":item["adi"].upper()}}
        guncelle = db.musteriler.update_one(sorgu, yenideger)
        print(guncelleme)


