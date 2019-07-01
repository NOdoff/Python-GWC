# A helper program for loading and saving data.
import json

# Change this string if you want to use a different file name for your data.
DATA_FILE = "data.json"

def load_data(filename=DATA_FILE):
	'''Loads json data from filename and returns python list or dictionary.'''
	try:
		file = open(filename, 'r')
	except IOError as e:
		print("Unable to open", filename)
		print(e)
		return None
	try:
		data = json.load(file)
	except:
		print("Unable to deserialize", filename)
		return None
	return data

def save_data(data, filename=DATA_FILE):
	'''Saves data into filename as a json.'''
	try:
		file = open(filename, 'w')
	except IOError as e:
		print ("Unable to write to", filename)
		print(e)
		return
	try:
		json.dump(data, file)
	except:
		print("Unable to serialize data.")