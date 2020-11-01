import argparse
try:
	def averagefunction(lst):
		average = sum(lst) / len(lst)
		print(average)

	if __name__=='__main__':
		
		parser = argparse.ArgumentParser(description="Code to accept list of numbers and calculate average")
		
		parser.add_argument('--lst',type=int, nargs='+', help="add number")
		
		args = parser.parse_args()
		
		thelistIneed = args.lst
		
		averagefunction(thelistIneed)
	
		print("average: " + str(average))
except:
	print("you have thrown an error. Please make sure your input follows syntax: 'python average.py --lst 1 2 3 4...'")
