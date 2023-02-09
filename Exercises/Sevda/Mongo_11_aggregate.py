from pprint import pprint
import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
##### match sort
db = client["sample_mflix"]
col = db["movies"]

match= {
        "$match":{
            "title":"A Star Is Born"
            }
    }
sorting =    {
        "$sort":{
            "year":pymongo.ASCENDING
        }
    }
limit = {"$limit":2}
pipeline = [match,sorting,limit]
sonuclar = col.aggregate(pipeline)
for item in sonuclar:
    print(item["year"])



"""
Egzersiz
sample_airbnb database içindeki listingsAndReviews koleksiyonu içerisinde bulunan dökümanlardan
yatak sayısı (bedrooms) 3 ten yüksek olan kayıtların  listing_url ve bedrooms başlıklarını ekrana yazdırınız.
"""
db = client["sample_airbnb"]
col = db["listingsAndReviews"]
#####-------------------matches
matches = {"$match":{"bedrooms":{"$gt":5}}}
#####-------------------sort
# sorts = {"$sort":{"bedrooms":pymongo.DESCENDING}}
#####-------------------limit
limits = {"$limit":5}
#####-------------------group

########## UNWIND
groups = {"$group":{
    "_id":"$bedrooms",#### {""}
    "ortalama_fiyat":{"$avg":"$price"}
    }
}
#####--------------------- sort of group
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