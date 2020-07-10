import requests
from config import HOST
def login_test(username,password):
    url = f'{HOST}/api/mgr/loginReq'
    payload = {'username': username, 'password': password}
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    res = requests.post(url, data=payload, headers=header)
    print(res.text)
    print(res.headers)
    return res.json()


if __name__ == "__main__":
    login_test('auto','sdfsdfsdf')

