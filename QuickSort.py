import random 

my_list = [3,36,6,9,12,1,2,9,7,8,60,21,66,90]

def sort(my_list):
	if len(my_list) <= 1:
		return my_list

	r = random.choice(my_list)
	my_list.remove(r)
	small_list = []
	big_list = []

	for x in my_list:
		if x < r:
			small_list.append(x)
		if x >= r:
			big_list.append(x)
	
	return sort(small_list) + [r] + sort(big_list)

print(sort(my_list))

