# from datetime import datetime
import requests

currency = "USD"

response = requests.get("https://v6.exchangerate-api.com/v6/a429228c5b0d12bd1240f87a/latest/"+ currency)

"""
# timestamp
ts = 1617295943.17321

# convert to datetime
dt = datetime.fromtimestamp(ts)
print("The date and time is:", dt)

# output 2021-04-01 22:22:23.173210
"""

if response.ok == True:
    data = response.json()
    rates = data["conversion_rates"]
    base = data["base_code"]
    date = data["time_last_update_utc"]
   
    
    print("Data: ", date)
    print("base currency: ", base)

    # print(rates)

    for key in rates:
        print(key + ": ", rates[key])


