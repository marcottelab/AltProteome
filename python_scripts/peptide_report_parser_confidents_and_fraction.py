#This script takes in a directory containing peptide reports from peptide shaker and determine number of confident, unique peptides identified.
#It outputs a file that shows the peptide by accession and the number of times it was seen confidently.

'''
Usage: peptide_report_parser_confident.py peptide_report_file_directory/
'''

import sys, glob

folder = sys.argv[1]

reports = glob.glob(folder + '*Peptide_Report.txt')

confident_peptides = 0
peptides_set = {}

for report in reports:
	fraction_name = '_'.join(report.split('_')[4:-4])
	print(fraction_name)
	with open(report,'r') as report_file:
		next(report_file)
		for line in report_file:
			line_split = line.strip().split('\t') #split tab delim line
			if line_split[-1] == 'Confident': #check if peptide is confident
				if not line_split[1] in peptides_set:
					peptides_set[line_split[1]] = [1,fraction_name]
					confident_peptides += 1
				else:
					peptides_set[line_split[1]][0] += 1
					peptides_set[line_split[1]].append(fraction_name)

print peptides_set
#print confident_peptides
#print('%i Confident Peptides identified' % confident_peptides)

#with open(folder[:-1] + '_unique_confident_peptides_fractions.txt', 'w') as out_file:
#	out_file.write('peptide\tcount\tFractions\n')
#	for key in peptides_set:
#		#out_file.write('%s\t%i\n' % (key, peptides_set[key]))
#		out_file.write(key + '\t' + str(peptides_set[key][0]) + '\t' + '\t'.join(peptides_set[key][1:]) + '\n')#