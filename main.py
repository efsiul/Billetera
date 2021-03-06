import os
import csv
from datetime import *
from transaction import *
from check_currency import *

def run():
    transaction = Transactions()
    check=Check_currency()
    now = datetime.now()
    fecha = now.strftime('%d/%m/%Y Hora: %H:%M:%S')
    check._save()
    #Abrimos el documento transacciones.csv y lo copiamos a en la lista que trabajaremos, para seguir la secuencia
    with open('transacciones.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            try:                                                                                                #Como los datos se guardan en el csv dejando una liena de espacio, al buscar en row[0],row[1],row[2]....row[8] sacara error
                transaction.addTransaction(row[0], row[1], row[2],row[3],row[4],row[5],row[6],row[7],row[8])    #por lo que la linea hay una lista vacia y no hay indices en el la lista row. Por ello se genera una excepción  
            except IndexError:                                                                                  #haciendo que el programa siga, y salte a la siguiente linea.
                continue    
    
    #Elaboración del Menú de opciones
    while True:
        option = input('''
                        |***********************************************************************************|
                        |                           BIENVENIDO A SU BILLETERA                               |
                        |                                                                                   |
                        |   Elija una de las siguientes opciones, digitando el número correspondiente:      |
                        |                                                                                   |
                        |   1 - Recibir cantidad                                                            |
                        |   2 - Transferir monto                                                            |
                        |   3 - Mostrar balance de moneda                                                   |
                        |   4 - Mostrar balance general                                                     |
                        |   5 - Mostrar historico de transacciones                                          |
                        |   6 - Conocer valor al día de criptomonedas                                       |
                        |   7 - Salir del programa                                                          |
                        |***********************************************************************************|
                        \n''')
            
        if option == '1':
            print('''
                        |*********************************************|
                        |          1-   RECIBIR CANTIDAD              |         
                        |*********************************************|
                    \n''')
            coinR = str(input("Indique la moneda que va a recibir: ")).upper()
            if check.esmoneda(coinR):
                count = float(input('Indique la cantidad de moneda que le van a transferir: '))
                code = input('Indique el codigo de quien envia: ')
                transaction.typeTransaction(code, "receives", fecha, coinR, count)
                print("Moneda recibida, transacción registrada")
            else:
                print("Lo sentimos, no reconocemos esa moneda")
            os.system("pause")
                
        elif option == '2':
            print('''
                        |*********************************************|
                        |         2-    TRANSFERIR MONTO              |         
                        |*********************************************|
                    \n''')
            
            coinS = str(input("Indique la moneda que va a enviar: ")).upper()
            if transaction.count_coin(coinS)>0:
                if check.esmoneda(coinS):
                    count = float(input('Indique la cantidad de moneda que desea transferir: '))
                    code = input('Indique el codigo de quien le desea enviar: ')
                    transaction.typeTransaction(code, "send", fecha, coinS, count)                
                    print("Moneda enviada, transacción registrada")
                else:
                    print("Lo sentimos, no reconocemos esa moneda")
            else:
                print("Lo sentimos, no tiene suficiente {} para realizar envios".format(coinS))
            os.system("pause")
            
        elif option == '3':
            print('''
                        |*********************************************|
                        |     3-  MOSTRAR BALANCE POR CRIPTOMONEDA    |         
                        |*********************************************|
                    \n''')
            coin =str(input("Indique la moneda que quiere consultar: ")).upper()
            if check.esmoneda(coin):
                valueCoin=transaction.value_coin(coin)
                print("Hasta la fecha usted tiene un balance de {}, en la moneda {}".format(valueCoin,coin))
            else:
                print("Lo sentimos, no reconocemos esa moneda")
            os.system("pause")
            
        elif option == '4':
            print('''
                        |*********************************************|
                        |       4-    MOSTRAR BALANCE GENERAL         |         
                        |*********************************************|
                    \n''')
            transaction.summary_coin()
            os.system("pause")
            
        elif option == '5':
            print('''
                        |*********************************************|
                        |  5-   MOSTRAR HISTORICO DE TRANSACCIONES    |        
                        |*********************************************|
                    \n''')
            transaction.show_all()
            os.system("pause")
            

        elif option == '6':
            print('''
                        |*********************************************|
                        |   6-  CONOCER VALOR AL DÍA DE CRIPTOMONEDA  |         
                        |*********************************************|
                    \n''')
            check.name_symbol_price()
            os.system("pause")
            
        elif option == '7':
            print('Saliendo...')
            break
        else:
            print("OPCIÓN INVALIDA, MARQUE UNA DE LAS OPCIONES DEL MENÚ")
            os.system("pause")
                


#Se indica al programa desde donde comenzar
if __name__ == '__main__':  
    run()