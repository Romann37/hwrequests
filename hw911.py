from pprint import pprint
import requests

def charahter(url1, url2, url3):
    print("интелект Капитан Америка")
    response = requests.get(url1, timeout=5)
    text1 = response.json()
    int_cap = text1.get('intelligence')
    print(int_cap)
    #pprint(text1)
    print("интеллект Халк")
    response = requests.get(url2, timeout=5)
    text1 = response.json()
    int_hulk = text1.get('intelligence')
    print(int_hulk)
    #pprint(text1)
    print("интеллект Танос")
    response = requests.get(url3, timeout=5)
    text1 = response.json()
    int_tanos = text1.get('intelligence')
    print(int_tanos)
    #pprint(text1)
    listprint = []
    listprint.append(int_cap)
    listprint.append(int_hulk)
    listprint.append(int_tanos)
    print(f"самый умный супергерой: {max(listprint)}")
url1 = "https://superheroapi.com/api/2619421814940190/149/powerstats/get"
url2 = "https://superheroapi.com/api/2619421814940190/332/powerstats/get"
url3 = "https://superheroapi.com/api/2619421814940190/665/powerstats/get"
heroes = charahter(url1, url2, url3)
    

