import requests

moneda_cripto = input("Ingrese una criptomoneda conocida: ").upper()
apikey="BFF0F841-A15B-4997-A1D0-2784C04BF223"


#invocando el método get con la url específica
url = f"https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={apikey}"
r = requests.get(url)

#ejercicio 1 cómo capturamos el rate
respuesta = r.json()#obtener la respuesta en formato diccionario
#print("rate: ", respuesta["rate"])

#ejerciocio 2 cómo captura errores de petición http
if r.status_code == 200:
    print("rate: ", respuesta["rate"])

else:
    print("error:", respuesta["error"])

"""
print("código http de respuesta:", r.status_code)
print("cabecera:", r.headers["content-type"])
print("encoding:", r.encoding)
print("respuesta en string", r.text)
print("respuesta en json", r.json())
"""
