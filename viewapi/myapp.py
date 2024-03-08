import requests
import json


# URL1 = "http://127.0.0.1:8000/get_student/"
URL2= "http://127.0.0.1:8000/create_student/"
# URL3 = "http://127.0.0.1:8000/update_student/"
def get_student(id=None):
    URL1 = "http://127.0.0.1:8000/get_student/"
    data = dict()
    if id:
        URL1 = URL1+f'{id}/'
    r = requests.get(url=URL1)
    # print(r.text)
    data = r.json()
    print('python data: ',data)
    


def post_data():
    data = {
        'name':'ram',
        'roll':12,
        'city':'PUne'
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL2,data=json_data,headers=headers)
    data = r.json()
    print(data)


def update_student():
    data ={
        'id':8,
        'roll':528,
        'name':'shankar',
        'city':'Gujarat'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL3,data=json_data)
    # print(r.text)
    data = r.json()
    print(data)


post_data()
get_student()
# update_student()
    

