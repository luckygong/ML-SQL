import sys

sys.path.insert(0, 'parser/')

from parser import parser

def execute(command):
	"""
	Used to parse and execute an ML-SQL command supplied by the user. 
	This function is meant to exported for use in other modules.
	"""
	myparser = parser()
	result = myparser.parseString(command)
	print(result)


def repl(parser):
	"""
	Used to create a read-evaluate-print-loop sequence for the ML-SQL langauge.
	This function will continually parse and execute user input from command
	line until the word exit is typed. 
	"""
	print("Initializing Parser...")
	myparser = parser()
	
	print("ML-SQL Parser is ready for use")

	while True:
		command = input(">")
		if command.lower() == "exit":
			print("Exiting ML-SQL")
			break
		else:
			result = myparser.parseString(command)
			print(result)

if __name__ == "__main__":
	repl(parser)
