import requests

for i in range(0, 100):
    if i %2 == 1:
        response = requests.get('http://10.10.166.237:8000/api/{}'.format(str(i)))
        print(str(i) + " : " + str(response.status_code))
        print(response.text)
