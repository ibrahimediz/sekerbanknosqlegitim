from pprint import pprint
import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
# ##### match sort
# db = client["sample_airbnb"]
# col = db["listingsAndReviews"]

# match= {"$match":{"bedrooms":{"$gt":3}}}
# sort={"$sort":{"bedroom":pymongo.DESCENDING}}
# limit={"$limit":5}
# pipeline = [match,sort,limit]
# sonuclar = col.aggregate(pipeline)
# for item in sonuclar:
#     print(item["bedrooms"],item["listing_url"])

"""
Egzersiz
sample_airbnb database içindeki listingsAndReviews koleksiyonu içerisinde bulunan dökümanlardan
yatak sayısı (bedrooms) 3 ten yüksek olan kayıtların  listing_url ve bedrooms başlıklarını ekrana yazdırınız.
"""

db = client["sample_airbnb"]
col = db["listingsAndReviews"]
#####-------------------matches
matches = {"$match":{"bedrooms":{"$eq":5}}}
#####-------------------group
groups = {"$group":{
    "_id":"$bedrooms",
    "average":{"$avg":"$price"}
    }
}

sortsofgrp = {"$sort":{"_id":-1}}
matchesofgrp = {"$match":{"_id":{"$eq":5}}}
#####-------------------aggregate
for item in col.aggregate([groups,sortsofgrp,matchesofgrp]):
    print(item)

"""
Egzersiz
sample_airbnb database içindeki listingsAndReviews koleksiyonu içerisinde bulunan dökümanlardan
bedrooms alanına göre gruplanan verilerde ortalama fiyat (price) değerini ekrana yazdıran python programını yazınız.
$avg kullanılabilir
5 odalı evlerin ortama fiyatı nedir?

"""