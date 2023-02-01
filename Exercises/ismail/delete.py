import pymongo
myclient = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")

#myclient = pymongo.MongoClient("mongodb://localhost:27017/")

print("List of databases before deletion\n--------------------------")
for x in myclient.list_database_names():
  print(x)
  
#delete database named 'organisation'
db = myclient["korkmazBd"]
col = db["musteriler"]
col.delete_many({})
db.drop_collection("musteriler")
myclient.drop_database("korkmazBd")
print("\nList of databases after deletion\n--------------------------")
for x in myclient.list_database_names():
  print(x)