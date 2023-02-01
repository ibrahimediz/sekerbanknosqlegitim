import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
# print(*client.list_database_names(),sep="\n")
# db = client["sample_airbnb"]
# print(db.list_collection_names(),sep="\n")
dbName="ornek"
for item in client.list_database_names():
    if item==dbName:
        print("Veritabanı zaten var")
    db = client[dbName]
