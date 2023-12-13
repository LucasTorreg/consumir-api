import requests
#from .utils import *
from config import APIKEY

moneda_cripto = input("Ingrese una criptomoneda conocida: ").upper()
#APIKEY = "BFF0F841-A15B-4997-A1D0-2784C04BF223"


while moneda_cripto != "" and moneda_cripto.isalpha():
    #invocando el método get con la url específica
    url = f"https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={APIKEY}"
    r = requests.get(url)

    #ejercicio 1 cómo capturamos el rate
    respuesta = r.json()#obtener la respuesta en formato diccionario
    #print("rate: ", respuesta["rate"])

    #ejerciocio 2 cómo captura errores de petición http
    if r.status_code == 200:
        #print("rate: ", respuesta["rate"])
        print( "{:.2f}€".format(respuesta["rate"]))
        break

    else:
        print("error:", respuesta["error"])

    moneda_cripto = input("Ingrese una criptomoneda conocida: ").upper()


