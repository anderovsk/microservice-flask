import requests
url = 'http://localhost:5000'

def req_get(url, endpoint):
    res = requests.get(url+endpoint)
    print(res.status_code)
    print(res.content)

def req_post(url, endpoint, data):
    res = requests.post(url+endpoint, json=data)
    print(res.status_code)
    print(res.content)

data = {
    "user":"joao",
    "username":"jao",
    "password":"JaoEMariete",
    "email":"jao.dow@gmail.com",
    "isadmin":"true"    
    }
req_post(url, '/singup', data)

#req_get(url, '/getuser/anderovsk')