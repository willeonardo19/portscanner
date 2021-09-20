#!/bin/python3
import sys
import socket
from datetime import datetime

##Banner
def banner():
    print("""

╭━━━╮╱╱╱╱╭╮╭━━━╮
┃╭━╮┃╱╱╱╭╯╰┫╭━╮┃
┃╰━╯┣━━┳┻╮╭┫╰━━┳━━┳━━┳━╮╭━╮╭━━┳━╮
┃╭━━┫╭╮┃╭┫┃╰━━╮┃╭━┫╭╮┃╭╮┫╭╮┫┃━┫╭╯
┃┃╱╱┃╰╯┃┃┃╰┫╰━╯┃╰━┫╭╮┃┃┃┃┃┃┃┃━┫┃
╰╯╱╱╰━━┻╯╰━┻━━━┻━━┻╯╰┻╯╰┻╯╰┻━━┻╯
╭╮╱╱╱╱╱╭━━┳━╮╭━┳━━╮╭━━━┳╮╱╱╭━━━┳━╮╱╭┳━━━┳╮╱╭┳━━━╮
┃┃╱╱╱╱╱╰┫┣┻╮╰╯╭┫╭╮┃┃╭━╮┃┃╱╱┃╭━╮┃┃╰╮┃┃╭━╮┃┃╱┃┃╭━━╯
┃╰━┳╮╱╭╮┃┃╱╰╮╭╯┃╰╯╰┫┃╱┃┃┃╱╱┃┃╱┃┃╭╮╰╯┃┃╱┃┃┃╱┃┃╰━━╮
┃╭╮┃┃╱┃┃┃┃╱╭╯╰╮┃╭━╮┃╰━╯┃┃╱╭┫╰━╯┃┃╰╮┃┃┃╱┃┃┃╱┃┃╭━━╯
┃╰╯┃╰━╯┣┫┣┳╯╭╮╰┫╰━╯┃╭━╮┃╰━╯┃╭━╮┃┃╱┃┃┃╰━╯┃╰━╯┃╰━━╮
╰━━┻━╮╭┻━━┻━╯╰━┻━━━┻╯╱╰┻━━━┻╯╱╰┻╯╱╰━┻━━╮┣━━━┻━━━╯
╱╱╱╭━╯┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
╱╱╱╰━━╯                                                                             
""")

## Realizar el escaneo de puertos
def escaneo(objetivo):
    try:
        if len(objetivo) == 2: ## Se valida que exista un parametro
            target = socket.gethostbyname(objetivo[1]) ## traducimos nuestro hostname a IPv4
            ## banner()
            print("PortScanner by Ixbalanque".center(25,"-"))
            print("Escaneando objetivo:. {}".format(target))
            print("Hora de inicio:. {}".format(datetime.now()))
            puertos = [] ## lista para guardar los puertos abiertos
            for port in range(1, 65536): ## Aca establecemos el rango de puertos que deseamos escanear
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) ##  IPV4 y puerto
                s.settimeout(0.5) ## Se establese 0.5 segundo para el timeout
                result = s.connect_ex((target, port))
                if result == 0: ## si la respuestqa es igual a 0, el puerto esta abierto
                    print("Puerto {} esta abierto".format(port)) ## imprimimos el puerto abierto
                    puertos.append(port) ## añadiimos el puerto abierto a la lista de puertos
                #else: ## si la respuesta es diferente a cero, el puerto esta cerrado
                #    print("Puerto {} esta cerrado".format(port))
                s.close() ## cerre de la conexion
            if len(puertos) > 0: ## se valida que existan puertos abiertos en la lista puertos
                txt = open("{}.txt".format(target), 'w') ## establecemos el archivo que contendra los puertos abiertos.
                for puerto in puertos:
                    txt.write(str(puerto)+"\n") ## se añade cada puerto en la lista al archivo.
                txt.close() ## cierre del archivo
            print("Escaneo finalizado:. {}".format(datetime.now()).center(25, "-")) ## mensaje de escaneo finalizado
            print("{} puerto(s) abierto(s).".format(len(puertos))) ## mensaje de puertos abiertos
            print("Se ha creado el archivo {}.txt".format(target)) ## mensaje del archivo creado, que contiene los puertos abiertos.
        else:
            print("Debes de ingresar la IP a escanear.") ## si no se añade un parametro, muestra el mensaje de ingresar IP
            print("Sintaxis: python3 portscanner.py <ip>") ## sintaxis del script.
    ## validación de excepciones
    except KeyboardInterrupt as error:
        print("\nSaliendo del escaneo")
        # print("Error:.{}".format(error))
    except socket.gaierror as error:
        print("No se pudo resolver el hostname. Asegurate de haber ingresado una IP.")
        # print("Error:.{}".format(error))
    except socket.error as error:
        print("No se puede conectar al objetivo.")
        # print("Error:.{}".format(error))


if __name__ == '__main__':
    escaneo(sys.argv)



