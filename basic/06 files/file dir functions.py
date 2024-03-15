import os
import shutil

scriptData = os.path.dirname(__file__)

fh = open(scriptData + "/test.txt", "w", encoding="utf-8")
fh.write("Dane ęąśćłó")
fh.close()

if not os.path.exists(scriptData + "/newTest.txt"):
    os.rename(scriptData + "/test.txt", scriptData + "/newTest.txt")

print(os.path.getsize(scriptData + "/newTest.txt"))
print(os.path.isfile(scriptData + "/newTest.txt"))
print(os.path.isdir(scriptData + "/newTest.txt"))
print(os.path.isdir("./basic"))

if os.path.exists(scriptData + "/subDir"):
    os.rmdir(scriptData + "/subDir")

if not os.path.exists(scriptData + "/subDir"):
    os.mkdir(scriptData + "/subDir")

if os.path.exists(scriptData + "/newTest.txt"):
    os.remove(scriptData + "/newTest.txt")

print("current working directory :", os.getcwd())
os.chdir(scriptData)
print("current working directory :", os.getcwd())

if not os.path.exists("data-copy.dat"):
    shutil.copyfile("data.dat", "data-copy.dat")