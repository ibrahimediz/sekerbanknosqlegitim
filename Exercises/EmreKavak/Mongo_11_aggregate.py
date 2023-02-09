import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")

db = client["sample_airbnb"]
col = db["listingsAndReviews"]
matches= [{"$match":{"bedrooms":{"$gte":3}}}]
#sorts = [{"$sort":{"bedrooms":pymongo.ASCENDING}}]
sonuclar = col.aggregate([matches,sorts])
for item in sonuclar:
    print(item["listing_url"],item["bedrooms"])