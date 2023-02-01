import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
dbName = "ornek"
for item in client.list_database_names():
    if item == dbName:  # önceden var olup olmadığı kontrol ediliyor
        print("Veritabanı zaten var")
    db = client[dbName] ## veritabanı oluşturuluyor
print(*client.list_database_names(),sep="\n")
collectionName = "ornekKoleksiyon"
for item in db.list_collection_names():
    if item in collectionName: # önceden var olup olmadığı kontrol ediliyor
        print("Koleksiyon zaten var")
    col = db[collectionName] ## koleksiyon oluşturuluyor
print(*client.list_database_names(),sep="\n")
print(*db.list_collection_names(),sep="\n")

""" Egzersiz
1. kendi adınıza bir veritabanı oluşturmak için gereken kodu yazınız
2. bu veritabanı içerisinde musteriler adında bir koleksiyon oluşturalım
Egzersizi MongoDB_02_createDB.py dosyası içerisinde yazabilirsiniz.
""" 