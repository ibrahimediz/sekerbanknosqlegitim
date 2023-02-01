import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")


with client:
    db = client.sample_mflix
    sorgu = {"year":{"$gt":1938}} # gt > , gte >= , lt <, lte <= ,eq =,ne !=, in [1,2,3], nin => not [1,2,3]
    #print(*db.movies.find(sorgu,{"_id":0,"title":1}))
    print(db.movies.count_documents(sorgu))
    

with client:
    db = client.sample_mflix
    sorgu = {"title":{"$regex":1938}}
    
""" Egzersiz
Yukarıdaki kalıbı kullanarak
sample_mflix database i içinde yer alan movies koleksiyonunda yer alan dökümanlardan year bilgisi
1938 den sonra olanları listeleyen sorguyu yazınız
"""