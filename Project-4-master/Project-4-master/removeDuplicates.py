import argparse
try:
	if __name__ == '__main__':

		parser = argparse.ArgumentParser(description="Remove duplicate characters")
		parser.add_argument('--lst', type=str, nargs='+', help = "code to remove duplicate characters")
		args = parser.parse_args()
		thelistIneed = args.lst
		
		
		finallist=[]
		resultlist=[]
		def killduplicates(duplist):
			
			for word in duplist:
				x = set()
				mylist = []
				for ch in word:
					if ch not in x:
						x.add(ch)
						mylist.append(ch)
				finallist.append(mylist)
			

				def convert(s):
					str1=""
					return(str1.join(s))

			for lst in finallist:
				resultlist.append(convert(lst))
			print(resultlist)
				

	killduplicates(thelistIneed)
except TypeError: 
	print("You have entered the incorrect data type. Please try a string.")

except:	
	print("You have thrown an error! Please try again.")

