set1 = {1,2,34,56,8,87}
print(set1)

#mixed datatypes
set2 = {11,"divya",(52,98,5)}
print(set2)

#no duplicate allowed
set3 = {11,22,3,44,4,6,6,22}
print(set3)

#not mutable
#set4 ={1,2,34,[3,4]}  #TypeError: unhashable type: 'list'
#print(set4)   

#we can make set form list using set method
set5 = set([1,2,3,4,5])
print(set5)
print(type(set5))

#list from set
list1 = list({1,2,4,56,7,32,6})
print(list1)
print(type(list1))

#operations on set
set6 = {11,33,44,55,66}
print(set6)

#does not support indexing
#set[0]

#add element
set6.add(77)
print(set6)
#add multiple elements
set6.update([88,99,22])
print(set6)
#add list and set
set6.update([111,222],{333,445,555})
print(set6)

#remove and discard
set6.discard(8)  #no error if discard element which is not present
set6.discard(445)
#set6.remove(90)  ##key error
set6.remove(111) 
print(set6)

#pop method
#print(set6.pop())
#print(set6.pop())
set6.pop()
set6.pop()
print(set6)

#clear
set6.clear()
print(set6)

#set operations

#union |
set7 ={1,2,3,4,5}
set8={4,5,6,7,8,9}
print(set7,set8)
print(set7|set8)
print(set7.union(set8))
print(set8|set7)
print(set8.union(set7))

#intersection & 
print(set7 & set8)
print(set7.intersection(set8))
print(set8&set7)
print(set8.intersection(set7))

#set difference -
print(set7 - set8)
print(set7.difference(set8))
print(set8-set7)
print(set8.difference(set7))

#symmetric difference ^
print(set7 ^ set8)
print(set7.symmetric_difference(set8))
print(set8 ^ set7)
print(set8.symmetric_difference(set7))

# set membership
set9 = {0, 1, 2, 3, 4, 5}
print(2 in set9)
print(6 in set9)
print(2 not in set9)
print(6 not in set9)

#iterate through set
for letter in set("welcome"):
    print(letter)

#built-in function wiht set
print(len(set9))
print(min(set9))
print(max(set9))
print(sorted(set9))

#frozenset
# its a neew class that has characteristics of a set, but its elements cannot be changed once assigned 
set10 = frozenset([1,2,3,4])
set11 = frozenset([3,4,5,6])
print(set10)
print(set11)
print(set10.difference(set11))
print(set10.union(set11))
print(set1.intersection(set11))
print(set10.symmetric_difference(set11))

