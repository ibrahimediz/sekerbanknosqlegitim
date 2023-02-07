import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
#db = client["abdullah"]
#col = db["musteriler"]
########### delete_one
# sorgu = {"adi":{"$eq":"ABDULLAH"}}
# sonuc = col.delete_one(sorgu)
# print(sonuc.deleted_count)





########### delete_many
# sorgu = {"adi":{"$eq":"ABDULLAH"}}
# sonuc = col.delete_many(sorgu)
# print(sonuc.deleted_count)




#################################################

with client:
    db=client.abdullah
    res = db.Musteriler.find_one()
    print(res["_id"])
    sorgu = {"_id":{"$eq":res["_id"]}}
    sonuc = db.Musteriler.delete_one(sorgu)



