import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")


with client:
    db = client.sample_mflix
    sorgu = {"title":{"$gt":1938}} 
    ##print(*db.movies.find(sorgu,{"_id":0,"year":1,"soyadi":1}))
    print(db.movies.count_documents(sorgu))
    


    

