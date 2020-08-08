import os
import csv
from datetime import *
from transaction import *

def run():
    transaction = Transactions()
    now = datetime.now()
    fecha = now.strftime('%d/%m/%Y Hora: %H:%M:%S')
    
    with open('transacciones.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            try:                                                                                                #Como los datos se guardan en el csv dejando una liena de espacio, al buscar en row[0],row[1],row[2]....row[8] sacara error
                transaction.addTransaction(row[0], row[1], row[2],row[3],row[4],row[5],row[6],row[7],row[8])     #por lo que la linea hay una lista vacia y no hay indices en el la lista row. Por ello se genera una excepción  
            except IndexError:                                                                                  #haciendo que el programa siga, y salte a la siguiente linea.
                continue
    
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
                        |   6 - Salir del programa                                                          |
                        |***********************************************************************************|
                        \n''')
            
        if option == '1':
            print('''
                        |*********************************************|
                        |             RECIBIR CANTIDAD                |         
                        |*********************************************|
                    \n''')
            coin = str(input("Indique la moneda que va a recibir: "))
            count = float(input('Indique la cantidad de dinero que desea recibir: '))
            code = input('Indique el codigo de quien envia: ')
            transaction.typeTransaction(code, "receives", fecha, coin, count)
                
            os.system("pause")
                
        elif option == '2':
            print('''
                        |*********************************************|
                        |             TRANSFERIR MONTO                |         
                        |*********************************************|
                    \n''')
                
            transaction._accomulator(1)
            os.system("pause")
                
        elif option == '3':
            print('''
                        |*********************************************|
                        |         MOSTRAR BALANCE DE MONEDA           |         
                        |*********************************************|
                    \n''')
            os.system("pause")
        elif option == '4':
            print('''
                        |*********************************************|
                        |           MOSTRAR BALANCE GENERAL           |         
                        |*********************************************|
                    \n''')
            os.system("pause")
        elif option == '5':
            print('''
                        |*********************************************|
                        |     MOSTRAR HISTORICO DE TRANSACCIONES      |        
                        |*********************************************|
                    \n''')
            transaction.show_all()
            os.system("pause")
                
        elif option == '6':
            print('Saliendo...')
            break
        else:
            print("OPCIÓN INVALIDA, MARQUE UNA DE LAS OPCIONES DEL MENÚ")
            os.system("pause")
                

if __name__ == '__main__':  
    run()