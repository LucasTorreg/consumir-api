from appcoints.config import APIKEY
from appcoints.model import *
from appcoints.view import *

class AppCoinsController:

    def executeProgram(self):
        #consulta de todas las monedas
        allcoint = AllCointsApiIO()#creando objeto
        viewTools = Views()#creando objetos
        allcoint.getAllCoins(APIKEY)   

        viewTools.viewListCoins(allcoint=allcoint)
        ########################################################################
        moneda_cripto = viewTools.insertCoin()

        while moneda_cripto != "" and moneda_cripto.isalpha():
            if moneda_cripto in allcoint.lista_criptos:
                exchange = Exchange(moneda_cripto)
                try:
                    exchange.updateExchange(APIKEY)
                    viewTools.viewRateExchange(exchange)
                except ModelError as error:
                    viewTools.getError(error)

            moneda_cripto = viewTools.insertCoin()