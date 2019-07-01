# A program to analyze data collected in the surver.
import data_helper

def find_average_year():
	# Load the data using the appropraite function from the data_helper module,
	# and search through it to find the average age of respondants.
	# Return that value.
	data = data_helper.load_data('list_of_responses.json')
	total_year = 0
	for response in data:
		total_year+= response['year']
	return total_year/len(data)
	pass

def num_month_counts():
	month_counts = {
	'december':0,
	'january':0,
	'february':0,

	'march':0,
	'april':0,
	'may':0,

	'june':0,
	'july':0,
	'august':0,

	'september':0,
	'october':0,
	'november':0,

	}
	data = data_helper.load_data('list_of_responses.json')
	for response in data:
		month= response['month']

	return month_counts 
	# Load the data using the appropriate function from the data_helper module,
	# and search through it to find the number of unique and complete responses
	# you have.
