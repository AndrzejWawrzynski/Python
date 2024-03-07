import requests

currency = "PLN"

response = requests.get("https://v6.exchangerate-api.com/v6/a429228c5b0d12bd1240f87a/latest/"+ currency)
# codes = requests.get("https://v6.exchangerate-api.com/v6/a429228c5b0d12bd1240f87a/codes")

if response.ok:
    data = response.json()
    rates = data["conversion_rates"]
    base = data["base_code"]
    date = data["time_last_update_utc"]
   
    print("Data: ", data)
    print("base currency: ", base)

    for key in rates:
        print(key + ": ", rates[key])

# data2 = codes.json()
# codeCountry = data2["supported_codes"]
# for i in codeCountry:
#     print(i)