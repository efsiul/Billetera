
import os
from csv import *
from datetime import *


def run():
    transaction = Transactions()
    now = datetime.now()
    fecha = now.strftime('%d/%m/%Y Hora: %H:%M:%S')
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
    with open('transacciones.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue  
    run()