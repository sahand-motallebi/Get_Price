import requests
import json
import pyttsx3

class coinDesk:
    def get_btc_price():
        engine = pyttsx3.init()
        price = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        data = json.loads(price.text)
        btc_price = data['bpi']['USD']['rate']
        btc_price = btc_price.replace(',', '')
        engine.say("btc_price = {}".format(btc_price))
        engine.runAndWait()
        with open('price1.txt','w',encoding='utf-8') as f:
            for price in btc_price:
                f.write(price)

        return btc_price



print(coinDesk.get_btc_price())




