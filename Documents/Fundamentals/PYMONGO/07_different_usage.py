import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")


with client:
    db = client.ediz
    sorgu = {"$and":[{"yas":{"$eq":None}},{"email":{"$regex":"/@$/"}}]} # gt > , gte >= , lt <, lte <= ,eq =,ne !=, in [1,2,3], nin => not in [1,2,3]
    print(*db.musteriler.find(sorgu,{"_id":0,"adi":1,"soyadi":1}))
    print(db.musteriler.count_documents(sorgu))


    
""" Egzersiz
Yukarıdaki kalıbı kullanarak
sample_mflix database i içinde yer alan movies koleksiyonunda yer alan dökümanlardan year bilgisi
1938 den sonra olanları listeleyen sorguyu yazınız
"""

#####  regular expression

# with client:
#     db = client.ediz
#     sorgu = {"adi":{"$regex":"Ö^"}} # gt > , gte >= , lt <, lte <= ,eq =,ne !=, in [1,2,3], nin => not in [1,2,3]
#     # print(*db.musteriler.find(sorgu,{"_id":0,"adi":1,"soyadi":1}))
#     print(db.musteriler.count_documents(sorgu))


""" Egzersiz
Yukarıdaki kalıbı kullanarak
sample_mflix database i içinde yer alan movies koleksiyonunda yer alan dökümanlardan title bilgisi
Z ile başlayan dökümanları sayısı nedir
"""




""" Egzersiz
Yukarıdaki kalıbı kullanarak
sample_training database i içinde yer alan companies koleksiyonunda yer alan dökümanlardan category_code bilgisi
social ile olan dökümanların sayısı nedir
Mongo_07_different_usage
"""
