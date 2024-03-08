import requests
import json

URL1 = "http://127.0.0.1:8000/get_student/"
URL2= "http://127.0.0.1:8000/student_create/"
URL3 = "http://127.0.0.1:8000/update_student/"
URL4 = "http://127.0.0.1:8000/student_delete/"
def get_student(id = None):
    data = dict()
    if id:
        data['id'] = id
    json_data = json.dumps(data)
    r = requests.get(url=URL1, data=json_data)
    # print(r.text)
    data = r.json()
    print('python data: ',data)
    

def post_data():
    data = {
        'name':'Vijay',
        'roll':304,
        'city':'Majalgaon'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL2,data=json_data)
    data = r.json()
    print(data)


def update_student():
    data ={
        'id':1,
        'roll':384,
        'name':'ajay mehhata',
        'city':'parli vaidhyanath'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL3,data=json_data)
    # print(r.text)
    data = r.json()
    print(data)


def delete_student(id):
    try:
        r = requests.delete(url=URL4 + f"{id}/")
        r.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        print("Student deleted successfully")
    except requests.exceptions.HTTPError as e:
        print("Failed to delete student:", e)


    


# post_data()
# get_student()
# update_student()
delete_student(1)
    

