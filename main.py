import requests
import json
intitle = input('Введите ваш вопрос: ')


a = requests.get('https://api.stackexchange.com/2.3/search?order=desc&sort=activity&intitle='+intitle+'&site=stackoverflow')

b = a.json()


for i in range(5):
    print(b["items"][i]["link"])
