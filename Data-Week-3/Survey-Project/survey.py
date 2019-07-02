# A program that conducts a survey and stores the response data.
import pprint
import data_helper

def conduct_survey():
	'''
	Allows the user to give multiple survey responses, saving the responses in
	a list. Returns the list.
	'''
	responses =[]
	responses.append(data_helper.load_data('list_of_responses.json'))
	print(responses)
	yesA = ['yes', 'y', 'ok', 'o.k.', 'okay']
	noA = ['no', 'n']
	# while start_survey in yesA:
	# 	start_survey = input("Would you like to start the survey?\n")
	# 	start_survey = start_survey.lower()
	# 	print("Okay, let's jump into it!")
	# 	response_of_current_person = get_survey_response()
	# 	responses.append(response_of_current_person)

	while True:
		start_survey = input("Would you like to start the survey?\n")
		start_survey = start_survey.lower()
		if(start_survey in noA):
			break

		print("Okay, let's jump into it!")
		response_of_current_person = get_survey_response()
		responses.append(response_of_current_person)





	print('Thanks for your time!')
	# Your code here! Ask the user if they'd like to take the survey. If they
	# say yes, use the get_survey_response() function to get their response.
	# allow them to continue submitting responses until they say they are done.
	# Append each response to the responses list.
	# (Hint: what kind of loop do you use when you don't know how many times
	# it will iterate?)


	# Keep this line of code at the end.
	return responses

def get_survey_response():
	'''
	Prompts the user to answer survey questions. Saves their responses in a
	dictionary, and returns the dictionary.
	'''
	response = {}
	true = ['true', 't']
	false = ['false', 'f']
	response['name'] = input("What is your name?\n")
	response['month'] = input('What month were you born?\n')
	while True:
		response['day'] = input('What day were you born?\n')
		try:
			response['day'] = int(response['day'])
			break
		except ValueError:
			print("Please enter a number!")
	while True:
		response['year'] = input('What year were you born?\n')
		try:
			response['year'] = int(response['year'])
			break
		except ValueError:
			print("Please enter a number!")

	response['chicken'] = input('Do you like chicken or beef more? Type none or both if you want\n')


	youOrSpo = input('You like or use Youtube more than Spotify. True or False\n').lower()

	if(youOrSpo in true):
		response['Youtube over Spotify'] = True
	elif(youOrSpo in false):
		response['Youtube over Spotify'] = False

	while True:
		response['float'] = input('What is your favorite decimal?\n')
		try:
			response['float'] = float(response['float'])
			break
		except ValueError:
			print("Please enter a number!")
	response['favorite color'] = input('What is your favorite color?\n')
	response['hobby'] = input('What is your hobby?\n')
	response['books or sports'] = input('Do you like books or sports more? Type none or both if you want\n')

	# Your code here! Prompt the user to answer questions, and save their
	# responses in the dictionary.


    # Keep this line of code at the end.
	return response

def show_response():
	resp = conduct_survey()
	data_helper.save_data(resp, 'list_of_responses.json')
	pprint.pprint(resp)

def main():
    # Put code to test here
	show_response()
# __name__ is the variable of the name of the program
#__main__ is the name of the program only when its run in the file it was created and not imported
if __name__ == '__main__':
	main()
