add=lambda x,y:x+y
print(add(45,45))#addition

s=lambda x:x*x
print(s(10))#squares

number=[1,2,3,4,5]#mapping
squares=list(map(lambda x:x*x,number))
print(squares)

number=[10,20,30,40,50]#filter
even=list(filter(lambda x:x%2==0,number))
print(even)

cube = lambda x: x ** 3#cube
results = list(map(cube, [1, 3, 5, 8, 12]))
print(results)  



