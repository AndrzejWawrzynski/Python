import requests

coinsList = None

def getCointlist():
    global coinsList
    # {'id': '0-mee', 'symbol': 'ome', 'name': 'O-MEE', 'platforms': {'ethereum': '0xbd89b8d708809e7022135313683663911826977e'}}
    response = requests.get("https://api.coingecko.com/api/v3/coins/list?include_platform=true")
    if response.ok == True:
        print("response ok")
        data = response.json()
        print(data[3])
        print(len(data))
        coinsList = data

def findCoinBySymbol(symbol):
    symbol = symbol.lower().strip()
    for coin in coinsList:
        if coin["symbol"] == symbol:
            return coin
    else:
        return None
    
getCointlist()

btcData = findCoinBySymbol("btc")
print(btcData)

