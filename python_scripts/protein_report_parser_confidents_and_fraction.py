#This script takes in a directory containing protein reports from peptide shaker and determine number of confident, unique proteins identified.
#It outputs a file that shows the protein by accession and the number of times it was seen confidently.

'''
Usage: protein_report_parser_confident.py protein_report_file_directory/
'''

import sys, glob

folder = sys.argv[1]

reports = glob.glob(folder + '*Protein_Report.txt')

confident_proteins = 0
proteins_set = {}

for report in reports:
	fraction_name = '_'.join(report.split('_')[4:-4])
	print(fraction_name)
	with open(report,'r') as report_file:
		next(report_file)
		for line in report_file:
			line_split = line.strip().split('\t') #split tab delim line
			if line_split[-1] == 'Confident': #check if protein is confident
				if not line_split[1] in proteins_set:
					proteins_set[line_split[1]] = [1,fraction_name]
					confident_proteins += 1
				else:
					proteins_set[line_split[1]][0] += 1
					proteins_set[line_split[1]].append(fraction_name)

print proteins_set

print('%i Confident Proteins identified' % confident_proteins)

with open(folder[:-1] + '_unique_confident_proteins_fractions.txt', 'w') as out_file:
	out_file.write('protein\tcount\tFractions\n')
	for key in proteins_set:
		#out_file.write('%s\t%i\n' % (key, proteins_set[key]))
		out_file.write(key + '\t' + str(proteins_set[key][0]) + '\t' + '\t'.join(proteins_set[key][1:]) + '\n')