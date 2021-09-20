
import requests

names_list = ['Captain America', 'Hulk', 'Thanos']
url = "https://superheroapi.com/api/2619421814940190/search/"
def heroes_int(names_list, url):
    url_list = []
    heroes_dict = {}
    for i_id in names_list:
        url_list.append(url + i_id)
    for hero in url_list:
        response = requests.get(hero)
        names = response.json()['results'][0]['name']
        intelligence = int(response.json()['results'][0]['powerstats']['intelligence'])
        heroes_dict[names] = intelligence
    return print(f'Самым умным супергероем оказался - {max(heroes_dict)}')


heroes_int(names_list, url)    

