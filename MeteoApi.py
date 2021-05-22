import web
import json
import requests
import re
import config
import os
import dotenv
from dotenv import load_dotenv
load_dotenv()
from furl import furl
f = furl("/weather?zipcode='(./*){5}'")
print(f.args['zipcode'])


import urllib.parse as urlparse
#from urllib.parse import urlparse
from urllib.parse import parse_qs


apikey = os.environ.get("APIKEY")
#routing
urls = (
    '/weather?', 'Weather',
    '/(.*)', 'Zipcode'
)


app = web.application(urls, globals())

url = 'localhost:8080/weather?zipcode=[(./*){5}]'
parsed = urlparse.urlparse(url)
print(parse_qs(parsed.query)['zipcode'])


# parsed = urlparse("localhost:8080/weather?zipcode=/")
# zipcode = parsed.query.get

# class Weather:
#     def GET(self):
#         web.header('Content-type', 'application/json')
#         req = requests.get(config.url + zipcode +  ',' + config.country + '&appid=' + apikey)
#         jdata = req.json()
#
#         w = {}
#         w["weather"] = str(jdata["weather"][0]["main"])
#         w["temperature"] = round(float(jdata["main"]["temp"]))
#         w["tempMin"] = round(float(jdata["main"]["temp_min"]))
#         w["tempMax"] = round(float(jdata["main"]["temp_max"]))
#
#         return json.dumps(w)


# class Zipcode:
#
#     def GET(self, params,rep):
#         params = re.findall('([a-zA-Z]*)=([a-zA-Z0-9]*)', web.ctx.query)
#         return 'Invalid Regular expression'
#
#         if len(params) == 5:
#             rep.status = '200 ok'
#             return params
#         else:
#             raise Exception('Zipcode is not valid')
#
#     def getZipcode(self,zip):
#         params = '/(.*){5}'
#         return zip(self)


if __name__ == "__main__":
    app.run()
