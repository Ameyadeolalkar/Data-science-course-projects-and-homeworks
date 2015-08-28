#https://gist.github.com/justmarkham/16734d16ef493041843a

print("This is done using for loop")

movies = ['tt0111161', 'tt1856010', 'tt0096694', 'tt0088763', 'tt1375666']
for i in movies:
	print(i[2:len(i)])

print("This is done using list comprehension")


print([i[2:len(i)] for i in movies])


print("sum of all numbers")

numbers = sum([int(i[2:]) for i in movies])
print(numbers)