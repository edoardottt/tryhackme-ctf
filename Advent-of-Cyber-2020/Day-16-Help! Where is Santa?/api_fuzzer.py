import requests

TARGET_API = "HERE YOUR TARGET_IP"

for i in range(0, 100):
    if i %2 == 1:
        response = requests.get('http://' + TARGET_API + ':8000/api/{}'.format(str(i)))
        print(str(i) + " : " + str(response.status_code))
        print(response.text)
