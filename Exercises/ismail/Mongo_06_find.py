import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
db = client["korkmazDb"]
col = db["musteriler"]
res = col.find_one()
print(res)