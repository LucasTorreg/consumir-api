respuesta={
"time": "2023-12-11T13:26:15.0000000Z",
"asset_id_base": "BTC",
"asset_id_quote": "EUR",
"rate": 39204.65040504416
}

#print(respuesta['rate'])
#print( respuesta.get('rate') )

errores= {
"error": "You didn't specify API key or it is incorrectly formatted. You should do it in: query string parameter `apikey`,  in http header named `X-CoinAPI-Key`,  in http header named `Authorization` or  as part of URL /apikey-YOUR-API-KEY/"
}

#print(errores["error"])

prueba= "rolando"
#print(  prueba.upper() )

print(prueba.isalpha())#True