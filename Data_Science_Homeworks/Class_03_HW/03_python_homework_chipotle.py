'''
Python Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''

'''
BASIC LEVEL
PART 1: Read in the file with csv.reader() and store it in an object called 'file_nested_list'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
      https://docs.python.org/2/library/csv.html
'''
import csv
file_nested = []
with open('chipotle.tsv' , mode = 'rU') as file_nested_list:
	file_nested_list = csv.reader(file_nested_list,delimiter='\t')
	for row in file_nested_list:
		file_nested.append(row)
#print(file_nested)

'''
BASIC LEVEL
PART 2: Separate 'file_nested_list' into the 'header' and the 'data'.
'''
header = file_nested[0]
#print(header)
data = file_nested[1:]
#print(data)
'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!
'''
addition = []
for order in data:
	addition.append(float(order[4][1:-1])*float(order[1]))
#print(round(sum(addition)/len(data),2))

#average cost of an order is $8.49

'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like Izze.
'''
'''
unique_sodas = []
for sodas in data:
	if(sodas[2] == "Canned Soda" or sodas[2] == "Canned Soft Drink"):
		unique_sodas.append(sodas[3])
print(set(unique_sodas))
'''
#set(['[Lemonade]', '[Dr. Pepper]', '[Diet Coke]', '[Nestea]', '[Mountain Dew]', '[Diet Dr. Pepper]', '[Coke]', '[Coca Cola]', '[Sprite]'])

'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''
'''
number_of_toppings=[]
burrito_list=[]
for burrito in data:
	if("Burrito" in burrito[2].split(" ")):
		burrito[3] = burrito[3].split(",")
		number_of_toppings.append(len(burrito[3]))
		burrito_list.append(burrito[2])
print(sum(number_of_toppings)/len(burrito_list))
average number of toppings is 5
'''



'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''

for chips in data:
	if("Chips" in chips[2]):
		#print chips[2]
		chips_dict = dict(zip(chips[2],chips[1]))
		print chips_dict

#BONUS: Think of a question about this data that interests you, and then answer it!