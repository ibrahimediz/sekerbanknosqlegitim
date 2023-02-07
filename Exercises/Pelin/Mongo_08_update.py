with client:
    db = client.Pelin
    liste = db.musteriler.find()
    for item in liste:
        print(item["_id"])
        sorgu = {"_id":{"$eq":item["_id"]}}
        yenideger = {"$set":{"adi":item["adi"].upper()}}
        guncelle = db.musteriler.update_one(sorgu, yenideger)