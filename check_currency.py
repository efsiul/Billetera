import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

class Check_currency:
    
    def __init__(self):
        self._monedas=[]
        self._monedas_dict={}
        self._monedas2=[]
        self._ENDPOINT = "https://api.binance.com"
        self.url = 'https://api.coinmarketcap.com/v1/ticker/'
        self.parameters ={'start':'1','limit':'5000', 'convert':'USD' }
        self.COINMARKET_API_KEY = "d4e571f9-65a3-46c7-af2b-310417d2e144"
        self.headers = {'Accepts': 'application/json',  'X-CMC_PRO_API_KEY': self.COINMARKET_API_KEY} 


    
    def _url(self, api):
        point= self._ENDPOINT + api
        return point
    
    def get_price(self, cripto):
        price=requests.get(self._url("/api/v3/ticker/price?symbol="+cripto+"USDT")).json()
        return price['price']
    
    def get_price2(self, coin):
        datos=[]
        data=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest", headers=self.headers, params=self.parameters)        
        data=data.json()
        for cripto in data['data']:
            if cripto['symbol'] == coin:
                datos=cripto['quote']
                return datos['USD']['price']
            
    
    def check_coin(self):
        data=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest", headers=self.headers, params=self.parameters).json()
        for cripto in data["data"]:
            self._monedas2.append(cripto["symbol"])
        monedas = tuple(self._monedas2)
        return (monedas)  
            
    def check_price(self,coin,element):
        respuesta=requests.get(self.url+coin+'/')    
        resp_json=respuesta.json()
        print(resp_json[element])
        
    
    
            #self._monedas_dict[cripto["symbol"]]=cripto["name"]
        #self._monedas = self._monedas_dict.keys()
    
        
    def esmoneda(self, cripto):
        return cripto in self.check_coin()
