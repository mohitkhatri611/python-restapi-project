import requests

URL="http://127.0.0.1:8000"

#Get auth token
def get_token():
    url= f"{URL}/api/auth/"
    response = requests.post(url, data={'username': 'admin',
                                        'password': 'admin'})

    return response.json()
    #print(response.json()) #use json insted of .text #json() is safe


def get_data():
    #using this we wll get data using request.
    url= f"{URL}/api/users_list/"
    header={'Authorization': f'Token {get_token()}'}
    response = requests.get(url, headers = header)
    emp_data= response.json()
    for e in emp_data:
        print(e)


def create_new(count):
    #this is usefull if you have data in excel and you want to import the data into database.
    #you can do that in batch.
    url= f"{URL}/api/users_list/"
    header = {'Authorization': f'Token {get_token()}'}
    data ={
        "name": f"AARYAN SHARMA {count}",
        "employee_id": f"HQ000{count}",
        "ranking": 2.4 ,
        "age": {count},
          }
    response = requests.post(url, data =data, headers = header)
    print(response.text)


def edit_data(employee_id):
    #to update the data
    url= f"{URL}/api/users_list/{employee_id}/"
    header = {'Authorization': f'Token {get_token()}'}
    data ={
        "name": "wow666",
        "ranking": 3.5 ,
        "age": 55,
          }
    response = requests.put(url, data =data, headers = header)
    print(response.text,response.status_code)

def delete_data(employee_id):
    url= f"{URL}/api/users_list/{employee_id}/"
    header = {'Authorization': f'Token {get_token()}'}
    response = requests.delete(url, headers = header)
    print(f"{employee_id} deleted ",response.status_code)


for e in range(21):
    if e >4:
        delete_data(e)
    #204 return means successfuly deleted, 404 means that user doesn't exit

#get_data()

# for e in range(20):
#     create_new(e)

#edit_data(5)