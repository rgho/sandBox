# Unfunctional version:
 
names = ['Mary', 'Isla', 'Sam']
 
'''
for i in range(len(names)):
names[i] = hash(names[i])
 
print names # => [6306819796133686941, 8135353348168144921, -1228887169324443034]
'''
 
# Rewrite the code above as a map
new_names = map(hash, names)
print new_names

# Expected answer: [6306819796133686941, 8135353348168144921, -1228887169324443034]


# EX 2
people = [{'name': 'Mary', 'height': 160},
{'name': 'Isla', 'height': 80},
{'name': 'Sam'}]
 
"""
height_total = 0
height_count = 0
for person in people:
if 'height' in person:
height_total += person['height']
height_count += 1
 
if height_count > 0:
average_height = height_total / height_count # => 120
"""
 
# Rewrite the code above using map, reduce and filter
people_with_heights = filter(lambda x:"height" in x,people)
height_total = reduce(lambda a,x:a+x["height"],people_with_heights,0)
height_avg = reduce(lambda a,x:a+x["height"],people_with_heights,0)/len(people_with_heights)

# print height_total
# print height_avg
# print people

# Expected answer: 120

# UNTESTED
def rishi_reduce(input_function, input_list, initialize_answer):
	answer = initialize_answer
	for input_item in input_list:
		answer = input_function(answer,input_item)
	return answer



"""
def rule_sequence(s, rules):
for rule in rules:
s = rule(s)
if s == None:
break
 
return s
"""

# def zero(s):
# 	if s[0] == "0":
# 		return s[1:]
 
# def one(s):
# 	if s[0] == "1":
# 		return s[1:]

# def apply_function(func, param):
# 	return func(param)

# def rule_sequence(input_string, match_seq):
# 	# print input_string 
# 	# print match_seq
# 	# print "==="
# 	if match_seq == []: return input_string[0:]
# 	if apply_function(input_string, match_seq[0]) != None:
# 		return rule_sequence(input_string[1:],match_seq[1:])
		


 
# print rule_sequence('0101', [zero, one, zero])
# # => 1
 
# print rule_sequence('0101', [zero, zero])
# # => None

# with for loops
def pipeline_each(dictionary,functions_list):
	for item in dictionary:
		for func in functions_list:
			dictionary[item] = apply_function(func, item)

	return dictionary


# lambda item: item

