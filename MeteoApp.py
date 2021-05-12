import web
import requests
import json
import config
import re

import os
from dotenv import load_dotenv
load_dotenv()

# apikey
apikey = os.getenv('APIKEY')

# routing
urls = (
    '/weather?', 'Weather',
    #'/zipcode=([0-9]{5})', 'Zipcode'
    '/w?.*', 'Zipcode'
)

app = web.application(urls, globals())


class Weather:
    def GET(self):
        web.header('Content-type', 'application/json')

        req = requests.get(config.url + config.zipcode + ',' + config.country + '&appid=' + apikey)
        jdata = req.json()

        weather = str(jdata["weather"][0]["main"])
        temperature = round(float(jdata["main"]["temp"]))
        tempmin = round(float(jdata["main"]["temp_min"]))
        tempmax = round(float(jdata["main"]["temp_max"]))

        w = {
            'weather': weather,
            'temperature': temperature,
            'tempMin': tempmin,
            'tempMax': tempmax
        }
        return json.dumps(w)


# class Zipcode:
#     def GET(self):
#         #print(web.ctx.query)
#         params = re.findall('([a-zA-Z]*)=([a-zA-Z0-9]{5})', web.ctx.query)
#         for key, value in params:
#             if key == 'zipcode':
#                 zipcode = value
#             else:
#                 raise Exception('Zipcode is not valid')
#         return zipcode

        # if len(params) == 5:
        #     rep.status = '200 ok'
        #     return params
        # else:
        #     raise Exception('Zipcode is not valid')


# class Params:
#     def get_param_from_url(self, url, param_name):
#         params = [i.split("=")[-1] for i in url.split("?", 1)[-1].split("&") if i.startswith(param_name + "=")][0]
#         return str(params)
#
#
# zipcode = Params()

if __name__ == "__main__":
    app.run()
