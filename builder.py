import time
import os

# establish a welcome message system and provide user with options
welcome_msg = [
'Hi, I\'m Bob, your personal notes builder.',
'Here are your command options below:',
'type \'bob adds\' to begin a new notes entry for the day',
'type \'bob lists\' for a list of all journal entries',
'type \'bob deletes\' to decide which notes to throw away',
'type \'exit\' to leave bob'
]

# give user the welcome message iteration
for msg in welcome_msg:
	print(msg)
	# time.sleep(2)

def exit():
	print('Bob says bye...')
	return 

def bob_adds():
	Y = 'Y'
	N = 'N'
	feedback = input('Do you have a title in mind for this new note? [Y/n] ')
	if feedback == Y.lower():
		return give_note_title()
	elif feedback == N.lower():
		return create_note()
	else:
		return reroute()

def give_note_title():
	note_title = input('Enter new note title: ')
	if note_title != '':
		create_note(note_title=note_title)
	else:
		print(note_title)

def create_note(note_title=None):
	if not note_title:
		note_title = 'bob_' + str(time.time())	
	f = open('./notes/' + str(note_title) + '.txt', 'w+')
	print('{} successfully created!'.format(note_title))
	print('Navigating to new file: {} ...'.format(note_title))
	f.close()
	choose()

def bob_lists():
	if os.listdir("./notes") == []:
		print('You don\'t have any notes yet!')
	else:
		idx = 1
		for file in os.listdir("./notes"):
			print('{} -- {}'.format(idx, file))
			idx += 1
	choose()

def bob_deletes():
	print('Deleting notes now...')

def choose():
	waiting = input('what will bob do for you today? ')
	if waiting == 'bob adds':
		bob_adds()
	elif waiting == 'bob lists':
		bob_lists()
	elif waiting == 'bob deletes':
		bob_deletes()
	elif waiting == 'exit':
		exit()
	else:
		print('Bob can\'t find the command \'{}\'. Try again.'.format(waiting))
		choose()

def reroute():
	return choose()

choose()



