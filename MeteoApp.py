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
    #'/weather', 'Weather',
    '/zipcode=([0-9]{5})', 'Zipcode'
    #'/w?.*', 'zipcode'
)

app = web.application(urls, globals())


def tempdata(data):
    data = f"{str(data)} degré" if data in [1, 0, -1] else f"{str(data)} degrés"
    return data


def checkzip(zip):
    return zip if len(zip) == 5 else "zipcode is not valid"


class Zipcode:
    def GET(self, zipcode):
        web.header('Content-type', 'application/json')
        web.header('charset', 'utf-8')

        req = requests.get(config.url + checkzip(zipcode) + ',' + config.country + '&appid=' + apikey)

        jdata = req.json()
        #print(jdata)
        k = 275
        weather = str(jdata["weather"][0]["main"])

        temperature = tempdata(round(float(jdata["main"]["temp"]) - k))
        tempmin = tempdata(round(float(jdata["main"]["temp_min"]) - k))
        tempmax = tempdata(round(float(jdata["main"]["temp_max"]) - k))

        # temperature = round(float(jdata["main"]["temp"]) - k)
        # if temperature == 1 or temperature == 0 or temperature == -1:
        #     temperature = str(temperature) + " degré"
        # else:
        #     temperature = str(temperature) + " degrés"
        #
        # tempmin = round(float(jdata["main"]["temp_min"]) - k)
        # if tempmin == 1 or tempmin == 0 or tempmin == -1:
        #     tempmin = str(tempmin) + " degré"
        # else:
        #     tempmin = str(tempmin) + " degrés"
        #
        # tempmax = round(float(jdata["main"]["temp_max"]) - k)
        # if tempmax == 1 or tempmax == 0 or tempmax == -1:
        #     tempmax = str(tempmax) + " degré"
        # else:
        #     tempmax = str(tempmax) + " degrés"

        w = {
            'weather': weather,
            'temperature': temperature,
            'tempMin': tempmin,
            'tempMax': tempmax
        }
        return json.dumps(w)

    # def GET(self):
    #     print(web.ctx.query)
    #     params = re.findall('([a-zA-Z]*)=([a-zA-Z0-9]{5})', web.ctx.query)
    #     if len(params) == 5:
    #         for key, value in params:
    #             if key == 'zip':
    #                 zipcode = params[0][1]
    #                 print(zipcode)
    #                 return zipcode
        # else:
        #     return 'Zipcode is not valid'


# class Zipcode:
#     # def __init__(self, zipcode):
#     #     self.zipcode = zipcode
#
#     def GET(self):
#         print(web.ctx.query)
#         params = re.findall('([a-zA-Z]*)=([a-zA-Z0-9]{5})', web.ctx.query)
#         if len(params) == 5:
#             for key, value in params:
#                 if key == 'zip':
#                     zipcode = params[0][1]
#                     #print(zipcode)
#                     return zipcode
#         else:
#             return 'Zipcode is not valid'

    # def GET(self):
    #     print(web.ctx.query)
    #     params = re.findall('([a-zA-Z]*)=([a-zA-Z0-9]{5)
    #             if key == 'zip':
    #                 zipcode = params[0][1]
    #                 print(zipcode)
    #                 return zipcode
    #     else:
    #         return 'Zipcode is not valid'

if __name__ == "__main__":
    app.run()
