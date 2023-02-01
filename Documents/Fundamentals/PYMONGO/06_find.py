import pymongo
client = pymongo.MongoClient("mongodb+srv://dbuser:dbuser123@cluster0.fjttryf.mongodb.net/?retryWrites=true&w=majority")
db = client["ediz"]
col = db["musteriler"]
# kayitlar = col.find()
# döküman içerisindeki farklı başlıkları nasıl alabiliriz.
kayitlar = col.find({},{"_id":0,"adi":1,"tel":1})
#              sart,hangi başlık
for kayit in kayitlar:
    print(kayit)


""" Egzersiz
Biraz önce kayıt yapmış olduğunuz dökümanları sadece adı ve soyadı gözükecek şekilde find fonksiyonunu kullanarak
listeleyiniz.
Egzersizi Mongo_06_find.py dosyası içerisine yazabilirsiniz.
""" 