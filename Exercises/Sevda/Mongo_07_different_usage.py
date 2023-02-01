import pymongo
client2 = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")


#with client:
#    db=client.Sevda
#    sorgu = {"yas":{"gte":0}}
#    kolonlar={"_id":0,"adi":1}
#    print(*db.Musteriler.find(sorgu,{"_id":0,"adi":1}))

with client2:
    db=client2.sample_mflix
    #sart={"year":{"$gt":1938}}
    #print(*db.movies.find(sart,{}))
    sart={"title":{"regex"}}
    print(db.movies.count_documents(sart))