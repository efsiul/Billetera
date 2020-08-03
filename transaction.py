import csv
from check_currency import *
class Monto:
    def __init__(self, amount=0.0, trans=0):
        self.__amount=amount
        self.__trans=trans
    
    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, amount):
        self.__amount=self.__amount+amount
    
    @property
    def trans(self):
        return self.__trans
    
    @trans.setter
    def trans(self,conse):
        self.__trans=conse
    

class Transaction:
    
    def __init__(self,trans, typeT, code, date, coin, price , count, value, amount):
        self.trans=trans
        self.typeT=typeT
        self.code=code
        self.date=date
        self.coin=coin
        self.price=price
        self.count=count
        self.value=value
        self.amount=amount



class Transactions:
    def __init__(self):
        self._transactions=[]
    
    def __consecutive(self, conse):
        cons=Monto()
        tempo=cons.trans
        cons.trans=tempo+conse
        
        
    def typeTransaction(self, code, typeT, date, coin, count):
        price=Check_currency()
        precio=price.get_price(coin)
        valor=count*float(precio)   

        monto=Monto()
        if typeT=="receives":
            mont=monto.amount=valor
            self.__consecutive(1)
            transa=monto.trans
            
            
        elif typeT=="send":
            mont=monto.amount=(-1.0)*valor
            self.__consecutive(1)
            transa=monto.trans
            
        transaction=Transaction(transa, typeT, code, date, coin, precio, count, valor, mont)
        self._transactions.append(transaction)
        self._save()
    
    def show_all(self):
        for i in self._transactions:
            self._print_transaction(i)
    
    def _print_transaction(self,transaction):
        print('*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*')
        print('Transacción número: {}'.format(transaction.trans))
        print('Tipo de Transacción: {}'.format(transaction.typeT))
        print('Codigo usuario para transferencia: {}'.format(transaction.code))
        print('Fecha: {}'.format(transaction.date))
        print('Moneda: {}'.format(transaction.coin))
        print('Precio de la moneda: {}'.format(transaction.price))
        print('cantidad a operar: {}'.format(transaction.count))
        print('valor de operado {}'.format(transaction.value))
        print('Monto a la fecha {}'.format(transaction.amount))
        print('*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*')
        
    
    def delete(self,code):
        for indx, transaction in enumerate(self._transactions):
            if transaction.trans==trans:
                del self._transactions[indx]
                self._save()
                break
    
    def search(self, code):
        for transaction in self._transactions:
            if transaction.code==code:
                self._print_transaction(transaction)
                break
        else:
            self._not_found()
            
    def _not_found():
        print('************************************')
        print('Transacción no encontrada')
        print('************************************')
            
    def _save(self):
        with open('transacciones.csv','w') as f:
            writer=csv.writer(f)   
            writer.writerow(('N° Trans', 'Tipo Transaccion', 'Codigo Usuario','Fecha', 'Moneda', 'Precio Moneda', 'Cantidad', 'Valor Transado','Monto Acomulado'))
            for trans in self._transactions:
                writer.writerow((trans.trans, trans.typeT, trans.code, trans.date, trans.coin, trans.price, trans.count, trans.value, trans.amount))
