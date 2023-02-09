import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")

db = client["sample_airbnb"]
col = db["listingsAndReviews"]
matches= [{"$match":{"bedrooms":{"$eq":3}}}]
#sorts = [{"$sort":{"bedrooms":pymongo.ASCENDING}}]

groups = {"$group":{
    "_id":"$bedrooms",
    "count":{"$count":{}},
    "average":{"$avg":"$price"}
    }
}
sonuclar = col.aggregate([groups])
for item in sonuclar:
    print(item)