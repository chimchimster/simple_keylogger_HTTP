import requests


def save_keys():
    data = input()
    if data:
        requests.post('http://localhost:8080/', data=data.encode('utf-8'))


if __name__ == '__main__':
    while True:
        save_keys()