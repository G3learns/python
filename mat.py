aLsit = [100, 200, 300, 400, 500]
print(aLsit[::-1])

list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]
list3=[]
for i,j in zip(list1,list2):
    list3.append(i+j)
print(list3)

aList = [1, 2, 3, 4, 5, 6, 7]
print([x*x for x in aList])

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
print([x+y for x in list1 for y in list2])

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for i,j in zip(list1,list2[::-1]):
    print(i,j)

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list2=list(filter(None,list1))
print(list2)

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2]+=[7000]
print(list1)

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list1[2][1][2].extend("hij")
print(list1)

list1 = [5, 10, 15, 20, 25, 50, 20]
num=list1.index(20)
list1[num]=200
print(list1)

list1 = [5, 20, 15, 20, 25, 50, 20]
c=list1.count(20)
if c!=0:
    for i in range(0,c):
        list1.remove(20)
print(list1)