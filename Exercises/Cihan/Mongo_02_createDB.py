import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")

dbName = "ciaydin"
db = client[dbName]## ciaydin isimli client oluştur

#print(*client.list_database_names(),sep="\n")

collectionName = "sample_123"
col = db[collectionName]## sample123 isimli collection oluştur

##print(*client.list_database_names(),sep="\n")## list of Clients
##print(*db.list_collection_names(),sep="\n")## list of collections