from pprint import pprint
import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
##### match sort
db = client["sample_airbnb"]
col = db["listingsAndReviews"]

match= { "$match":{"bedrooms":{"$gt":3}}}


#limit = {"$limit":2}
pipeline = [match]
sonuclar = col.aggregate(pipeline)
for item in sonuclar:
    pprint(item["listing_url"])
