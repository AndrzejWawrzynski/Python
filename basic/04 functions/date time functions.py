import time
import datetime

ticks = time.time()
print(ticks)

timeData = time.localtime()
print(timeData)
print(timeData.tm_year)

timeData = time.localtime(10)
print(timeData)
print(timeData.tm_year)

result = time.asctime(time.localtime())
print(result)

timeData = time.localtime()
print(time.strftime("%d/%m%Y %H:%M:%S", timeData))

timeStr = "17:23:45 08.12.2021"
timeData = time.strptime(timeStr, "%H:%M:%S %d.%m.%Y")
print(timeData)


i = 0

while i < 5:
    time.sleep(0.0001)
    print(time.asctime(time.localtime()))
    i += 1

timeStart = time.perf_counter()

time.sleep(0.3)

timeEnd = time.perf_counter()

print("Code took :", (timeEnd - timeStart), "seconds")

dateTimeObj = datetime.datetime.now()
print(dateTimeObj)
# print(dir(dateTimeObj))

dateTimeObj = datetime.datetime(2025, 4,10, 22,59,59)

print("date(): ", dateTimeObj.date())
print("time(): ", dateTimeObj.time())
print("timestamp(): ", dateTimeObj.timestamp())
print("today(): ", dateTimeObj.today())
print("year(): ", dateTimeObj.year)
print("month(): ", dateTimeObj.month)
print("day(): ", dateTimeObj.day)
print("hour(): ", dateTimeObj.hour)
print("minute(): ", dateTimeObj.minute)
print("second(): ", dateTimeObj.second)

print("format :", dateTimeObj.strftime("%H:%M:%S %d/%B/%Y"))
dateTimeObj = datetime.datetime.now()
print("format :", dateTimeObj.strftime("%H:%M:%S %d/%m/%Y"))

dateTime1 = datetime.datetime(2025,1,1, 23,59,59)
dateTime2 = datetime.datetime(2030,1,1, 23,59,59)

print(dateTime2 > dateTime1)
print(dateTime2 < dateTime1)

dateTime1 = datetime.date(2025,1,1)
dateTime2 = datetime.date(2027,1,1)

print( dateTime1 > dateTime2)
print( dateTime1 < dateTime2)



