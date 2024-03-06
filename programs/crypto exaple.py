import requests

currency = "pln"
coinsList = None

def getCointlist():
    global coinsList
    # {'id': '0-mee', 'symbol': 'ome', 'name': 'O-MEE', 'platforms': {'ethereum': '0xbd89b8d708809e7022135313683663911826977e'}}
    response = requests.get("https://api.coingecko.com/api/v3/coins/list?include_platform=true")
    if response.ok:
        print("response ok")
        data = response.json()
        print(data[3])
        print("Ilosc kryptowalut :", len(data))
        coinsList = data

def findCoinBySymbol(symbol):
    # {'id': '0-mee', 'symbol': 'ome', 'name': 'O-MEE', 'platforms': {'ethereum': '0xbd89b8d708809e7022135313683663911826977e'}}
    symbol = symbol.lower().strip()
    for coin in coinsList:
        if coin["symbol"] == symbol:
            return coin
    else:
        return None
    
def getCoinLastMarketData(coinId):
    # {'0-mee': {'pln': 0.00034951, 'pln_market_cap': 0.0, 'pln_24h_vol': 108761.99399090643, 'pln_24h_change': -14.402285796243792, 'last_updated_at': 1709744598}}
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids="+coinId+"&vs_currencies="+currency+"&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true")
    if response.ok:
        data = response.json()
        return data
    else:
        return None

def getCoinPriceInCurrency(coinId, currency):
    currency = currency.lower().strip()
    marketData = getCoinLastMarketData(coinId)
    return marketData[coinId][currency]


getCointlist()

btcData = findCoinBySymbol("btc")
print(btcData)


marketData = getCoinLastMarketData(btcData["id"])
print(marketData)

coinPrice = getCoinPriceInCurrency(btcData["id"], currency)
print("Coin price in " + currency + " :", coinPrice) # Coin price in pln : 0.00034958

print("\nWitamy w crypto exchange")

while True:
    cryptoSymbolToBuy  = input("Wybierz symbol krypto do kupienia np btc lub exit aby zakonczyc :")
    if cryptoSymbolToBuy == "exit" : break

    coinData = findCoinBySymbol(cryptoSymbolToBuy)
    if coinData == None:
        print("Nie ma takiej waluty")
        continue
    coinPrice = getCoinPriceInCurrency(coinData["id"], currency)
    print("Cena " + str(coinData["id"]), coinPrice, currency)

    moneyToBuyCrypto = float(input("Ile chcesz przeznaczyc na zakup :"))
    boughtCrypto = moneyToBuyCrypto / coinPrice

    print("\nGratulacje kupiles " + str(boughtCrypto) + " " + cryptoSymbolToBuy + "\n")
