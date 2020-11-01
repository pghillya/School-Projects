import argparse
try:
	if __name__ == '__main__':
		parser = argparse.ArgumentParser(description="")
		parser.add_argument('--lst', type=int, nargs='+', action="append", help = "Compute squares of each int in multiple int lists")
		args=parser.parse_args()
		thelistIneed = args.lst 
		
		def getsquare(lsts):
			square=0
			emptylist = []
			
			for lst in lsts:
				index=0
				for integer in lst:
					lst[index] = integer*integer
					index+=1
					
				print(lst)

		getsquare(thelistIneed)
except TypeError: 
	print("Please make sure you are entering lists of integers")
except:
	print("You have thrown an error. Please make sure your input is similar to 'python multiple.py --lst int1, int2... --lst int1, int2...'")

