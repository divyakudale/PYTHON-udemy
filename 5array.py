arr = [10, 20, 30, 40, 50]
print(arr)

print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])

print(arr[-1])
print(arr[-2])

brands = ["Coke", "Apple", "Google", "Microsoft", "Toyota"]
print(brands)

#length of array
num_brands = len(brands)
print(num_brands)

#add elements to array
brands.append("Intel")
brands.append("lenovo")
brands.append("lv")
print(brands)


#remove elements from array
colors = ["red", "voilet", "blue", "indigo", "Purple", "pink", "green"]
print(colors)

del colors[3]
print(colors)

colors.remove("green")
print(colors)

colors.pop(1) 
print(colors)
colors.pop(0)
print(colors)


#modify elements of array 
fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
print(fruits)

fruits[2] = "Watermelon"
print(fruits)
fruits[-1] = "Guava"
print(fruits)

#concatenate 2 arrays using + operator
concat = [1, 2, 3]
print(concat)
result = concat + [4, 5, 6]
print(result)

#repeat elements in array
repeat = ["a"]
print(repeat)
result = repeat * 5
print(result)


#slicing array
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
print(numbers[1:5])
print(numbers[:8])
print(numbers[5:])
print(numbers[-1:-6])
print(numbers[-8:])


#declare and define multidimentional array
matrix = [[1,2], [3,4], [5,6], [7,8]]
print(matrix)
print(matrix[0])
print(matrix[3])
print(matrix[2][1])
print(matrix[3][0])