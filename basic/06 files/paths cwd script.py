import os

print("Absolute path to script file :", __file__)
scriptDid = os.path.dirname(__file__)
print("---------")
print("Absolute path to script directory :", scriptDid)
print("---------")
pathToFile = scriptDid + "/newFile.txt"
print("Path to file :", pathToFile)
print("---------")


fh = open(scriptDid + "/newFile.txt", "w")
fh.write("content!")
fh.close()