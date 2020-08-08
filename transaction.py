import csv
from check_currency import *

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
        
        
    def typeTransaction(self, code, typeT, date, coin, count):
        price=Check_currency()
        precio=price.get_price(coin)
        valor=count*float(precio)   
        
        monto_accom=float(self._accomulator(8))
        num_Transaccion=int(self._accomulator(0))
        if typeT=="receives":
            mont=monto_accom+valor
            transa=num_Transaccion+1
            
        elif typeT=="send":
            mont=self.monto_accom+((-1.0)*valor)
            transa=self.num_Transaccion+1
        
        self.addTransaction(transa, typeT, code, date, coin, precio, count, valor, mont)
        
    def addTransaction(self, transa, typeT, code, date, coin, precio, count, valor, mont):
        transaction=Transaction(transa, typeT, code, date, coin, precio, count, valor, mont)
        self._transactions.append(transaction)
        self._save()
    
    def _accomulator(self,i):
        lis= list(csv.reader(open('transacciones.csv', 'r')))
        lon=(len(lis))
        return lis[lon-2][i]
        
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
        print('valor operado {}'.format(transaction.value))
        print('Monto a la fecha {}'.format(transaction.amount))
        print('*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*')
        
    
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
