import pymongo
client3 = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")


#with client:
#    db=client.Sevda
#    sorgu = {"yas":{"gte":0}}
#    kolonlar={"_id":0,"adi":1}
#    print(*db.Musteriler.find(sorgu,{"_id":0,"adi":1}))

# with client2:
#     db=client2.sample_mflix
#     #sart={"year":{"$gt":1938}}
#     #print(*db.movies.find(sart,{}))
#     sart={"title":{"$regex":"^Z"}}
#     print(*db.movies.find(sart,{}))
#     print(db.movies.count_documents(sart))

with client3:
    db=client3.sample_training
    sart={"category_code":{"$regex":"^social"}}    
    print(db.companies.count_documents(sart))