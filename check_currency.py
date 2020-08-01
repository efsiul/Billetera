import requests

class Check_currency:
    
   
    COINMARKET_API_KEY = "d4e571f9-65a3-46c7-af2b-310417d2e144"
    headers = {'Accepts': 'application/json','X-CMC_PRO_API_KEY': COINMARKET_API_KEY}   
    
    def __init__(self):
        self._monedas=()
        self._monedas_dict={}
        self._ENDPOINT = "https://api.binance.com"
        
    
    def _url(self, api):
        point= self._ENDPOINT + api
        return point
    
    def get_price(self, cripto):
        price=requests.get(self._url("/api/v3/ticker/price?symbol="+cripto+"USDT")).json()
        return price['price']
    
    def check_coin(self):
        data=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()
        for cripto in data["data"]:
            self._monedas_dict[cripto["symbol"]]=cripto["name"]
        self._monedas = self._monedas_dict.keys()
        
    def esmoneda(self, cripto):
        return cripto in self._monedas
