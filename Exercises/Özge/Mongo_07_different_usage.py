import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")


'''with client:
    db = client.sample_mflix
    sorgu = {"year":{"$gt":1938}} # gt > , gte >= , lt <, lte <= ,eq =,ne !=, in [1,2,3], nin => not [1,2,3]
    #print(*db.movies.find(sorgu,{"_id":0,"title":1}))
    print(db.movies.count_documents(sorgu))'''
    

# with client:
#     db = client.sample_mflix
#     sorgu = {"title":{"$regex":"^Z"}}
#     print(db.movies.count_documents(sorgu))


""" Egzersiz
Yukarıdaki kalıbı kullanarak
sample_training database i içinde yer alan companies koleksiyonunda yer alan dökümanlardan category_code bilgisi
social ile olan dökümanların sayısı nedir
Mongo_07_different_usage
"""


with client:
    db = client.sample_training
    sorgu = {"category_code":{"$regex":"^social"}} 
    print(db.movies.count_documents(sorgu))