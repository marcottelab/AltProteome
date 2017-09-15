#Checks for overlaps between the 2 outputs produced by combined_protein_parsed_unique_checker.py 
#

import sys
in_file=sys.argv[1]
ref_file=sys.argv[2]
acc_nums=set()
acc_num_in_both = []
with open(in_file, "r") as input_file:
	next(input_file)
	for line in input_file:
		line=line.split("\t")
		acc_nums.add(line[0])

#print(acc_nums)
with open(ref_file, "r") as ref_data:
	next(ref_data)
	for line in ref_data:
		line=line.split("\t")
		#print(line[1])
		if line[0] in acc_nums:
			acc_num_in_both.append(line[0])

print acc_num_in_both			