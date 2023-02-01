import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
#print(*client.list_database_names(),sep="\n")

for item in client.list_database_names():
    db = client[item]
    print("---",item,"---")
    print("#"*30)
    print(*db.list_collection_names(),sep="\n")
    print("#"*30)