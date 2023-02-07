import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
db = client["ediz"]
col = db["musteriler"]

########### delete_one
# sorgu = {"adi":{"$eq":"İBRAHIM"}}
# sonuc = col.delete_one(sorgu)
# print(sonuc.deleted_count)
########### delete_many
# sorgu = {"adi":{"$eq":"İBRAHIM"}}
# sonuc = col.delete_many(sorgu)
# print(sonuc.deleted_count)


""" 
Egzersiz
Kendi veritabanı ve koleksiyonunda duran bir dökümanın id sini alınız ve bu id bilgisini kullarak kaydı siliniz.
Mongo_09_delete.py dosyası içerisine gerekli kodları yazabilirsiniz.
"""
