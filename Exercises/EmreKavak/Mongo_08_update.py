import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
db = client["EmreKavak"]
col = db["musteriler"]


result = col.find()
for item in result:
    yenideger = {"$set":{"adi":item["adi"].upper()}}
    col.update_one(result, yenideger)
    