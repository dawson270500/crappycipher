import random

def split(word):##simple string splitter
	return [char for char in word]

class CrapCiph:
	def ciph(inp):##CIpher input
		seed = random.randint(100, 99999999)

		letters = split(inp)
		out = ""

		for x in letters:
			out = out + str(ord(x)*seed) + "-"

		return (str(out)+str(seed))

	def unciph(inp):##Uncipher input
		workon = inp

		nums = []
		out = ""

		for x in workon:
			if(x=="-"):
				nums.append(out)
				out = ""
			else:
				out = out+x

		nums.append(out)
		letters = ""
		
		seed = nums[len(nums)-1]
		nums.remove(seed)
		seed = int(seed)
		for x in nums:
			letters = letters +chr(int(int(x)/seed))

		return letters