#Closest number
myNumber = 7
myList = [1, 5, 10, 19]

closestNumber = min(myList, key=lambda x:abs(x-myNumber))
print(closestNumeber)