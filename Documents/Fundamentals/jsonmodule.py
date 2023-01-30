# sozluk = {"adi":"İbrahim","soyadi":"Ediz","Tel":112222331}
# #####.     key:value
# sozluk["adi"]
########## JSON 2 PYTHON ############
# sozluk = '{"adi":"İbrahim","soyadi":"Ediz","Tel":112222331}'
# import json
# y = json.loads(sozluk)
# print(y["adi"])
########## PYTHON 2 JSON ############
# sozluk = {"adi":"Şekerbank","soyadi":"T.A.Ş.","Tel":112222331,"Yas":25}
# y = json.dumps(sozluk,indent=4)
# print(y)
#################################################
import json 
sozluk = {
    "isim":"Ali",
    "yas":40,
    "evli":False,
    "bosandi":False,
    "cocuk":("Mehmet","Ayşe"),
    "arabalar":[
        {"model":"BMW 230","hp":2000},
        {"model":"Ford KUGA","hp":2000},
    ]
}

sonuc = json.dumps(sozluk,indent=4,sort_keys=True)
print(sonuc,file=open("deneme.json","w",encoding="UTF-8"))