'''
Lesson on file reading using Airline Safety Data
https://github.com/fivethirtyeight/data/tree/master/airline-safety
'''

# read the whole file at once, return a single string (including newlines)
# 'rU' mode (read universal) converts different line endings into '\n'
#f = open('airlines.csv', mode = 'rU')
#file_string = f.read()
#print(file_string)
# use a context manager to automatically close your file

# read the file into a list (each list element is one row)
#with open('airlines.csv', mode = 'rU') as f:
#	file_list = []
#	for row in f:
#		file_list.append(row)
# do the same thing using a list comprehension
#file_list_1 = []
#file_list_1.append(row for row in f)
# side note: splitting strings

# split each string (at the commas) into a list

# do the same thing using the csv module
import csv
with open('airlines.csv', mode = 'rU') as f:
	file_list = [row for row in csv.reader(f)]
#print(file_list)
# separate the header and data
header = file_list[0]
data = file_list[1:]
#print(data)

#EXERCISES:

'''1. Create a list containing the average number of incidents per year for each airline.
Example for Aer Lingus: (2 + 0)/30 = 0.07
Expected output: [0.07, 2.73, 0.23, ...]'''
average = []
for outer_list in data:
	#average.append(float(outer_list[2])+float(outer_list[5])/30)
	average.append(round((int(outer_list[2])+int(outer_list[5]))/float(30),2))
print(average)



'''2. Create a list of airline names (without the star).
Expected output: ['Aer Lingus', 'Aeroflot', 'Aerolineas Argentinas', ...]'''
airline_names = []
for outer_list in data:
	airline_names.append(outer_list[0])
'''for names in airline_names:
	if names.endswith('*'):
		#print(names[:-1])
	else:
		#print(names)'''

'''3. Create a list (of the same length) that contains 1 if there's a star and 0 if not.'''
#Expected output: [0, 1, 0, ...]
'''for names in airline_names:
	if names.endswith('*'):
		print('1')
	else:
		print('0')'''
'''4. BONUS: Create a dictionary in which the key is the airline name (without the star)
   and the value is the average number of incidents.
Expected output: {'Aer Lingus': 0.07, 'Aeroflot': 2.73, ...}'''


'''A few extra things that will help you with the homework'''


# 'set' data structure is useful for gathering unique elements

# 'in' statement is useful for lists

# 'in' is useful for strings (checks for substrings)

# 'in' is useful for dictionaries (checks keys but not values)

# 'count' method for strings counts how many times a character appears
