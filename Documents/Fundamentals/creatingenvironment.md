### Mac Linux için environment oluşturma
* python3 -m venv env
#### Aktivasyon için
* source env/bin/activate
### Windows
* python -m venv env
#### Aktivasyon için
* env/Scripts/activate
###### kurulu olan kütüphane listesini alabilmek için
* pip freeze > requirements.txt
###### Listeden kurulum yapabilmek için
* pip install -r requirements.txt
###### MONGO DB için ###################
pip install pymongo