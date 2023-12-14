import requests

class AllCointsApiIO:
    def __init__(self):
        self.url = ""
        self.lista_criptos = []
        self.lista_no_criptos = []



    def getAllCoins(self, apikey):
        self.url = f"https://rest.coinapi.io/v1/assets/?apikey={apikey}"
        r = requests.get(self.url)
        if r.status_code != 200:
            raise Exception("Error en consulta codigo:{}".format(r.status_code))


        lista_general = r.json()
        

        for dic in lista_general:
            if dic["type_is_crypto"] == 1:
                self.lista_criptos.append(dic["asset_id"])
            else:
                self.lista_no_criptos.append(dic["asset_id"])


class Exchange:
    def __init__(self):
        self.rate = None
        

    def updateExchange(self):
        url = f"https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={APIKEY}"
        r = requests.get(url)

        respuesta = r.json()    

        if r.status_code == 200:
            print( "{:.2f}€".format(respuesta["rate"]))
            break
        else:
            print("error:", respuesta["error"])
