from fachada import Fachada
from time import sleep
if __name__ == "__main__":
    print('***** Bienvenido *****')

    cocinero = Fachada()

    while(True):
        print('\n***************** \nSeleccione una opcion')
        print('1. Hacer una salchipapa')
        print('2. Cierre jornada laboral')
        print('3. Salir')

        try:
            opt = int(input('ingrese una opcion '))

            if (opt == 1):
                cocinero.hacer_salchipapa()
                print('\n\n **** SALCHIPAPA SALIENDO')
                sleep(1)
                print('\n\n **** SALCHIPAPA TERMINADA')

            if (opt == 2):
                print(cocinero.obtener_numero_platos())
                break

            if opt == 3:
                print('Adios')
                break

            if opt < 1 or opt > 2:
                print('*************')
                print('¡OPCIÓN INVALIDA!')
                print('*************')
                continue

        except ValueError:
            print("Error invalid option")
        
        continue 
            
        
