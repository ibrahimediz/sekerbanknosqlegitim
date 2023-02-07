import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")


"""with client:
    db = client.sample_mflix
    sorgu = {"year":{"$gte":1938}} 
    #print(*db.movies.find(sorgu,{"_id":0}))
    print(db.movies.count_documents(sorgu))"""

"""with client:
    db = client.sample_mflix
    sorgu = {"title":{"$regex":"^Z"}} 
    print(*db.movies.find(sorgu,{"_id":0}))
    print(db.movies.count_documents(sorgu))"""

with client:
    db = client.sample_training
    sorgu = {"category_code":{"$regex":"^social"}} 
    # print(*db.companies.find(sorgu,{"_id":0}))
    print(db.companies.count_documents(sorgu))