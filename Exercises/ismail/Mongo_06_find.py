import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
db = client["korkmazDb"]
col = db["musteriler"]
#res = col.find_one()
#print(res)

kayitlar = col.find({},{"_id":0,"adi":1,"soyadi":1})

for kayit in kayitlar:
    print(kayit)