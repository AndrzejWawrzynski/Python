import requests


title = "List_of_national_capitals"
response = requests.get("https://wikitable2json.vercel.app/api/"+title+"?table=0")

if response.ok:
    print("OK!")
    data = response.json()

# print(data) 

z = 0
for i in data:
    # print(i)
    z += 1
    if z > 20: break
    if len(i) >= 3:
        for i, n in i.items():
            print(i ,":", n)
        print("-----------")  
      

# {'City/Town': 'Abu Dhabi', 
# 'Country/Territory': 'United Arab Emirates', 
# 'Continent': 'Asia', 
# 'Notes': ''},




