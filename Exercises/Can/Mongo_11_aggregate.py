"""
SELECT 
isim,
count(islemtipi) as islemsayisi
FROM 
kayitlar
WHERE isim = 'tamamlandi'
group by isim
order by islemsayisi
"""

from pprint import pprint
import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
###### match sort
#db = client["sample_mflix"]
#col = db["movies"]

#match= {
#        "$match":{
#            "title":"A Star Is Born"
#            }
#    }
##        "$sort":{
#sorting =    {
#            "year":pymongo.ASCENDING
#        }
#    }
#limit = {"$limit":2}
#pipeline = [match,sorting,limit]
#sonuclar = col.aggregate(pipeline)
#for item in sonuclar:
#    print(item["year"])



"""
Egzersiz
sample_airbnb database içindeki listingsAndReviews koleksiyonu içerisinde bulunan dökümanlardan
yatak sayısı (bedrooms) 3 ten yüksek olan kayıtların  listing_url ve bedrooms başlıklarını ekrana yazdırınız.
"""
db = client["sample_airbnb"]
col = db["listingsAndReviews"]
#####-------------------matches
matches = {"$match":{"bedrooms":{"$eq":5}}}
#####-------------------sort
sorts = {"$sort":{"bedrooms":pymongo.DESCENDING}}
#####-------------------limit
limits = {"$limit":5}
#####-------------------group
groups = {"$group":{
    "_id":"$bedrooms",
    "count":{"$count":{}},
    "avg":{"$avg":"$price"},
    }
}
#####--------------------- sort of group
sortsofgrp = {"$sort":{"_id":-1}}
#####-------------------aggregate
for item in col.aggregate([matches,groups]):
    print(item)


"""
Egzersiz
sample_airbnb database içindeki listingsAndReviews koleksiyonu içerisinde 
bulunan dökümanlardan bedrooms alanına göre gruplanan verilerde 
ortalama fiyat (price) değerini ekrana yazdıran python programını yazınız.
$avg kullanılabilir
5 odalı evlerin ortama fiyatı nedir?

"""