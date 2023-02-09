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
# ##### match sort
# db = client["sample_mflix"]
# col = db["movies"]

# match= {
#         "$match":{
#             "title":"A Star Is Born"
#             }
#     }
# sorting =    {
#         "$sort":{
#             "year":pymongo.ASCENDING
#         }
#     }
# limit = {"$limit":2}
# pipeline = [match,sorting,limit]
# sonuclar = col.aggregate(pipeline)
# for item in sonuclar:
#     pprint(item["year"])





db = client["sample_airbnb"]
col = db["listingAndReviews"]
match= {"$match":{"bedrooms":{"gt":3 } }}
sorts = {"$sort":{"bedrooms":PYMONGO.DESC}}
limits = {"$limit":5}
for item in col.aggregate([matches,sorts,limits]):
 print(item["listing_url"],item["bedrooms"])
