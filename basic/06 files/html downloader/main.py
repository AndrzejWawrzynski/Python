import os, sys
import urllib.parse
import validators
import requests

print("Number of arguments: ", len(sys.argv))
print("Arguments list :", sys.argv)

url = "https://duckduckgo.com"
if len(sys.argv) > 1:
    url = sys.argv[1]

print("Website to download :", url)

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)
print("Current working dir :", os.getcwd())

if not os.path.exists("./websites"):
    os.mkdir("websites")

paresdUrl = urllib.parse.urlparse(url)
print(paresdUrl)

valiFlag = validators.url(url)
if valiFlag:
    print("Url :", url, "is valid")
else:
    print("Url :", url, "is invalid")
    raise Exception("Bad URL!")

response = requests.get(url, allow_redirects=True)
if response.ok == True:
    print("Response ok from server from url :", url)

