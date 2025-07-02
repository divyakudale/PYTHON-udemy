#immutable, diff data types

#empty
tuple1 = ()
print(tuple1)

#integer
tuple2 = (1, 2, 3)
print(tuple2)

#heterogenous
tuple3 = (101, "divya", 2000.00, "HR dept")
print(tuple3)

#nested 
tuple4 = ("points", [1,3,5], (7, 9, 11))
print(tuple4)

#tuple packing -- without ()
tuple5 = 100, 'kudale', 778.98, 'fghb'
print(tuple5)

#unpacking tuple
empid, empname, empsal, empdept = tuple5
print(empid)
print(empname)
print(empsal)
print(empdept)
print(type(tuple5))

#acess elements
tuple6 = 'a', 'e', 'i', 'o', 'u'
print(tuple6)
print(tuple6[0])
print(tuple6[2])
print(tuple6[4])

tuple7 = ('points', [1,2,2], (3,45,7))
print(tuple7)
print(tuple7[0][3])
print(tuple7[1][2])
print(tuple7[2][0])

#slice tuple
tuple8 = ('d', 'i', 'v', 'y', 'a')
print(tuple8[1:3])
print(tuple8[:4])
print(tuple8[2:])
print(tuple8[:])

#immutable elements
tuple9 = ('w', 'e', 'l', 'c', 'o', 'm', 'e')
print(tuple9)
#tuple9[2] = 'x' #error
tuple9 = ('g', 'o', 'o', 'd', 'b', 'y', 'e')
print(tuple9)

#concatenate
print(tuple9 + tuple8)
print(('divya',)*5)

#delete
#elements from tuple cannot be deleted , we can delete entire tuple
del tuple9
#print(tuple9) #nameerror

#methods COUNT, INDEX
tuple10 = ('h','e', 'l', 'l', '0o')
print(tuple10)
print(tuple10.count('l'))
print(tuple10.index('e'))

#operations # memebership -- IN , NOT IN
tuple11 = ('w', 'e', 'l', 'c', 'o', 'm', 'e', 'divya')
print(tuple11)
print('l' in tuple11)
print('x' in tuple11)
print('l' not in tuple11)
print('s' not in tuple11)

#iterate
for i in tuple11:
    print("letter is->" , i)
    
#built-in functions
tuple12 = 22,54,5,65,334,66,83
print(max(tuple12))
print(min(tuple12))
print(sorted(tuple12))
print(len(tuple12))
