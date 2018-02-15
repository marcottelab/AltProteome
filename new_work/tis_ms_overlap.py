#This script checks for overlapping accessions in both files and prints them.

import sys
in_file=sys.argv[1]
ref_file=sys.argv[2]
acc_nums=set()
acc_num_in_both = []
with open(in_file, "r") as input_file:
	next(input_file)
	for line in input_file:
		line=line.split("\n")
		acc_nums.add(line[0])

#print acc_nums 

with open(ref_file, "r") as ref_data:
	next(ref_data)
	for line in ref_data:
		line=line.split("\n")
		#print(line[1])
		if line[0] in acc_nums:
			acc_num_in_both.append(line[0])

with open('tis_ms_out.txt', "w") as output_file:
	output_file.write('MS_TIS_Overlap\n')
	for entry in range(len(acc_num_in_both)):
		output_file.write(acc_num_in_both[entry]+'\n')

print len(acc_num_in_both)