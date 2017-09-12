x = 6
y = 2
z = 3
a = x + z + y
print(a)

def genRandBool():
	seed = ["eni", "menie", "minie", "moe", "catch", "a", "tiger", "by", "the", "toe"]
	bool retn = True
	for i in range(0, len(seed)):
		retn = !retn
	return retn 
	
