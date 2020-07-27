#Error checking method for an input:

while x != y and z != y and m != y:
    c = input('testing')
    


#Closest number snippet
myNumber = 7
myList = [1, 5, 10, 19]

closestNumber = min(myList, key=lambda x:abs(x-myNumber))
print(closestNumeber)


#How to find where a list is
mylist = [21, 5, 8, 52, 21, 87]
item = 8

#search for the item
index = mylist.index(item)

print('The index of', item, 'in the list is:', index)