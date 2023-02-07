import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")


# with client:
#     db = client.sample_mflix
#     sorgu = {"year":{"$gt":1938}} # gt > , gte >= , lt <, lte <= ,eq =,ne !=, in [1,2,3], nin => not [1,2,3]
#     print(*db.musteriler.find(sorgu,{"_id":0,"adi":1}))
#     print(db.musteriler.count_documents(sorgu))

with client:
    db = client.sample_training
    coll_name = "companies"
    col = db[coll_name]
    sorgu = {"category_code":{"$eq":"social"}} # gt > , gte >= , lt <, lte <= ,eq =,ne !=, in [1,2,3], nin => not in [1,2,3]
    #print(*db.companies.find(sorgu,{"_id":0}))
    #print(db.companies.find_one())
    print(db.companies.count_documents(sorgu))