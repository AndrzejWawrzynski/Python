import requests

currency = "USD"

response = requests.get("https://v6.exchangerate-api.com/v6/a429228c5b0d12bd1240f87a/latest/"+ currency)

if response.ok == True:
    data = response.json()
    rates = data["conversion_rates"]
    base = data["base_code"]
    date = data["time_last_update_utc"]
   
    print("Data: ", date)
    print("base currency: ", base)

    for key in rates:
        print(key + ": ", rates[key])


