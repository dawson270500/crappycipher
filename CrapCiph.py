import sys
import random

def split(word):##simple string splitter
	return [char for char in word]

arg = sys.argv##getting arugments
if(len(arg) == 1):
	print("No arugments given, -h for more info")##nothing given

else:
	todo = arg[1]##getting command
	
	if(todo == "ciph" and len(arg) > 2):##cipher
		seed = random.randint(100, 99999999)

		letters = split(arg[2])
		out = ""

		for x in letters:
			y = ord(x)
			out = out + str(y*seed) + "-"

		print(str(out)+str(seed)+"-")

	elif(todo == "unciph" and len(arg) > 2):##uncipher
		workon = arg[2]

		nums = []
		out = ""

		for x in workon:
			if(x=="-"):
				nums.append(out)
				out = ""
			else:
				out = out+x

		letters = ""
		seed = nums[len(nums)-1]
		nums.remove(seed)
		seed = int(seed)
		for x in nums:
			letters = letters +chr(int(int(x)/seed))

		print(letters)

	elif(todo == "-h"):##help
		print("Commands:\n\tciph - Used to cipher a word or string, ciph <string>\n\tunciph - Used to uncipher a word, unciph <cipher>")
	
	else:##Not a command
		print("Invalid Arugment, -h for more info")