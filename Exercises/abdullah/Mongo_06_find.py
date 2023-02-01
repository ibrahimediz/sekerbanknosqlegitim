import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
db = client["abdullah"]
col = db["musteriler"]
kayitlar = col.find({},{"_id":0,"adi":1,"soyadi":1})
for kayit in kayitlar:
    print(kayit)
