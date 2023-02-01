import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")


# with client:
#     db = client.ediz
#     sorgu = {"yas":{"$gt":40}} # gt > , gte >= , lt <, lte <= ,eq =,ne !=, in [1,2,3], nin => not in [1,2,3]
#     print(*db.musteriler.find(sorgu,{"_id":0,"adi":1,"soyadi":1}))
#     print(db.musteriler.count_documents(sorgu))


    
""" Egzersiz
Yukarıdaki kalıbı kullanarak
sample_mflix database i içinde yer alan movies koleksiyonunda yer alan dökümanlardan year bilgisi
1938 den sonra olanları listeleyen sorguyu yazınız
"""

#####  regular expression

with client:
    db = client.ediz
    sorgu = {"adi":{"$regex":"^Ö"}} # gt > , gte >= , lt <, lte <= ,eq =,ne !=, in [1,2,3], nin => not in [1,2,3]
    # print(*db.musteriler.find(sorgu,{"_id":0,"adi":1,"soyadi":1}))
    print(db.musteriler.count_documents(sorgu))


""" Egzersiz
Yukarıdaki kalıbı kullanarak
sample_mflix database i içinde yer alan movies koleksiyonunda yer alan dökümanlardan title bilgisi
Z ile başlayan dökümanları sayısı nedir
"""