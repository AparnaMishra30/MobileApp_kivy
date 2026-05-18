import requests

BASE_URL = "http://192.168.100.29:5000"


def login_api(loginid, password):

    url = f"{BASE_URL}/login"

    payload = {
        "loginid": loginid,
        "password": password
    }

    response = requests.post(url, json=payload)

    return response.json()


def chat_api(message):

    url = f"{BASE_URL}/chat"

    payload = {
        "message": message
    }

    response = requests.post(url, json=payload)

    return response.json()


def target_api(usercode):

    url = f"{BASE_URL}/target/{usercode}"

    response = requests.get(url)

    return response.json()