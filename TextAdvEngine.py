def TextAdventure(tafile):
	"""Runs interactive textadventure from text file in folder.
	
	Text adventure is stored as a dictionary.
		Key = Path string, or string of 1/2/3 decisions taken thusfar (starting = 'start')
		Value[0] = Scenario prompt
		Value[1:] = Decision possibilities
	
	PreC: tafile is string containing text file name"""
	
	tadict = dict()
	
	# Splice text file to dictionary
	# Open file and read all to string
	with open(tafile, 'r') as f:
		full = f.read()
	# Separate file string into lines by newlines (\n)
	lines = full.split('\n')
	# Separate each line into key/value by separator (|)
	for line in lines:
		linesep = line.split('|')
		tadict[linesep[0]] = linesep[1:]
		
	path = 'start'

	while True:
		if not path in tadict:
			print
			print 'This path has never been taken. You decide what\'s next!'
			# Solicit a new scenario prompt
			scenario = raw_input('Set the scene and prompt a decision >> ')
			new = [scenario]
			# Solicit a user-chosen number of decisions
			numchoices = input('How many decisions: >> ')
			for x in range(numchoices):
				choicetext = raw_input('Give me a choice >> ')
				new.append(choicetext)
			
			# Add it to the ta dictionary
			tadict[path] = new
			
			# Create a string to write to the file
			filestr = path
			for item in new:
				filestr = filestr + '|' + item
			filestr = filestr + '\n'
			# Write the new string to file
			with open(tafile, 'a') as f:
				f.write(filestr)
			
		# Print the secnario prompt and decision possibilities
		print
		current = tadict[path]
		print current[0]
		for i in range(1, len(current)):
			print str(i) + '. ' + current[i]
		
		# Solicit user choice and update decision string
		choice = raw_input('What do you do? Type your choice number >> ')
		
		if path == 'start':
			path = choice
		else:
			path += choice
		
		
if __name__ == '__main__':
	thefile = raw_input('File name >> ')
	TextAdventure(thefile)