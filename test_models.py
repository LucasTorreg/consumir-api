from appcoints.model import AllCointsApiIO
from appcoints.config import APIKEY

def test_allcoint():
    listas = AllCointsApiIO()#creando objeto de la clase AllCointsApiIO
    listas.getAllCoins(APIKEY)#llamando al método getAllCoins()
    assert listas != None#True
    cantidad = len(listas.lista_criptos) + len(listas.lista_no_criptos)
    assert cantidad == 18521#True