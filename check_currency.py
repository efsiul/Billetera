
import json
import csv
import requests

class Check_currency:
    
    def __init__(self):
        self._monedas=[]
        self._monedas_dict={}
        self.url = 'https://api.coinmarketcap.com/v1/ticker/'
        self.parameters ={'start':'1','limit':'5000', 'convert':'USD' }
        self.COINMARKET_API_KEY = "d4e571f9-65a3-46c7-af2b-310417d2e144"
        self.headers = {'Accepts': 'application/json',  'X-CMC_PRO_API_KEY': self.COINMARKET_API_KEY} 
    
    def data_json(self):
        data=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest", headers=self.headers, params=self.parameters)        
        data=data.json()
        return data
    
    def get_price(self, coin):
        datos=[]
        data=self.data_json()
        for cripto in data['data']:
            if cripto['symbol'] == coin:
                datos=cripto['quote']
                return datos['USD']['price']
            
    
    def check_coin(self):
        data=self.data_json()
        for cripto in data["data"]:
            self._monedas.append(cripto["symbol"])
        monedas = tuple(self._monedas)
        return (monedas)  
        
    def name_symbol_price(self):
        lis= list(csv.reader(open('monedas.csv', 'r')))
        for data in lis:
            if len(data)==0:
                continue
            else:
                print((data[1], data[2], data[5]))

            
    def _save(self):
        data=self.data_json()
        with open('monedas.csv','w') as csvfile:
            writer=csv.writer(csvfile)
            writer.writerow(('id','name', 'symbol','slug', 'date_added','price'))
            for value in data['data']:
                writer.writerow((value['id'], value['name'], value['symbol'], value['slug'],value['date_added'], value['quote']['USD']['price']))       
            
    def esmoneda(self, cripto):
        return cripto in self.check_coin()
