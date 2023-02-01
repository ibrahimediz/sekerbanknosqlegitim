import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
dbName = "ozgesenkul"
db = client[dbName] 
colName = "musteriler"
col = db[colName] 



""" Egzersiz
1. kendi adınıza bir veritabanı oluşturmak için gereken kodu yazınız
2. bu veritabanı içerisinde musteriler adında bir koleksiyon oluşturalım
Egzersizi MongoDB_02_createDB.py dosyası içerisinde yazabilirsiniz.
""" 