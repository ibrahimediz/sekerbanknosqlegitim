
from pprint import pprint
import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
##### match sort
db = client["sample_airbnb"]
col = db["listingsAndReviews"]

match= {"$match":{"bedrooms":{"$gt":3}}}
sort={"$sort":{"bedroom":pymongo.DESCENDING}}
limit={"$limit":5}
pipeline = [match,sort,limit]
sonuclar = col.aggregate(pipeline)
for item in sonuclar:
    print(item["bedrooms"],item["listing_url"])

"""
Egzersiz
sample_airbnb database içindeki listingsAndReviews koleksiyonu içerisinde bulunan dökümanlardan
yatak sayısı (bedrooms) 3 ten yüksek olan kayıtların  listing_url ve bedrooms başlıklarını ekrana yazdırınız.
"""