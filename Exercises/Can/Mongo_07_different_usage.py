import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
##db = client["sample_mflix"]
##col = db["movies"]

## with client:
##    db = client.sample_mflix
##    sorgu = {"year":{"$gt":1938}} # gt > , gte >= , lt <, lte <= ,eq =,ne !=, in [1,2,3], nin => not [1,2,3]
##    print(*db.movies.find(sorgu,{"_id":0,"adi":1,"soyadi":1}))
##    print(db.movies.count_documents(sorgu))
    
#####  regular expression

with client:
    db = client.sample_mflix
    sorgu = {"title":{"$regex":"^Z"}} # gt > , gte >= , lt <, lte <= ,eq =,ne !=, in [1,2,3], nin => not in [1,2,3]
    # print(*db.musteriler.find(sorgu,{"_id":0,"adi":1,"soyadi":1}))
    print(db.movies.count_documents(sorgu))


""" Egzersiz
Yukarıdaki kalıbı kullanarak
sample_mflix database i içinde yer alan movies koleksiyonunda yer alan dökümanlardan title bilgisi
Z ile başlayan dökümanları sayısı nedir
"""