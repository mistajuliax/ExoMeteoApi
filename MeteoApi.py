import web
import json
import requests
import re

from dotenv import load_dotenv
load_dotenv()


#r = requests.get('https://api.openweathermap.org/data/2.5/weather?zip=35000,fr&appid=5ed01d65b56978f73d7aaa52dc47682f')
#print(r.json())


#routing
urls = (
    '/weather?', 'Weather',
    '/(.*)', 'Zipcode'
)


#config
url = "https://api.openweathermap.org/data/2.5/weather?q="
city = "rennes"
country = "fr"

apikey = "5ed01d65b56978f73d7aaa52dc47682f"

app = web.application(urls, globals())


class Weather:
    def GET(self):
        web.header('Content-type', 'application/json')
        params = re.findall('([a-zA-Z]*)=([a-zA-Z0-9]*)', web.ctx.query)
        print(params)
        data = requests.get(url + city + ',' + country + '&appid=' + apikey)
        w = {
            'temperature': data.get('main')('temp'),
            'weather': data.get('weather').get(0).get('main'),
            'temperature min ': data.get('main').get('temp_min'),
            'temperature max': data.get('main').get('temp_max')
        }
        return json.dumps(w)


class Zipcode:
    def GET(self, param):
        return 'Invalid Regular expression'
    # def __init__(self, params, rep):
    #     if len(params) == 5:
    #         rep.status = '200 ok'
    #     else:
    #         raise Exception('Zipcode is too short')


if __name__ == "__main__":
    app.run()
