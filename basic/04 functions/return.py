
def addNumbers(a,b,c):
    return a + b + c

def sumListElements(listData):
    if len(listData) == 0:
        print("Pusta lista")
        return None
    result = 0
    for i in listData:
        result += i
    return result

print(sumListElements([]))
print(sumListElements([1,2,3]))
print(sumListElements([1,2,3,4,5]))
print(sumListElements({1:15,2:10,3:11,4:4,5:50}))

def printList(listData):
    if len(listData) <= 3:
    # funkcja konczy dzialanie
    # jesli lista ma mniej niz
    # 3 elementy
        return

    print(listData)
    # return na koncu jest opcjonalne
    # jesli nie zwracana jest
    # konkretna wartosó
    return

printList(["a","b","c"])
printList(["a","b","c","d","e"])


def printList2(listData):
    if len(listData) == 0:
        return
    for i in listData:
        print(i)

printList2([])
printList2([6,7,8])
