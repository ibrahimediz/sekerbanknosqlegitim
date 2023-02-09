import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")

db = client["sample_mflix"]
col = db["movies"]
# col.index_information() indexlerin listesi
print(col.find().explain()["executionStats"])
indeks = [
    ("countries",pymongo.TEXT),("year",pymongo.ASCENDING)
]
col.create_index(
    indeks,
    name="indexULKEYIL",
    default_language="english",
    unique=True
    )

