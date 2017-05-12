#This script takes in a directory containing peptide reports from peptide shaker and the output from combined_protein_parsed_unique_checker.py and return the unique peptides from each report file.
#THe script will then output a file containing all these peptides.
'''
Usage: peptide_report_parser_confident.py peptide_report_file_directory protein_list_file
'''

import sys, glob

folder = sys.argv[1]

reports = glob.glob(folder + '*Peptide_Report.txt')

proteins_to_search = set()
with open(sys.argv[2], 'r') as protein_list_file:
	next(protein_list_file)
	for line in protein_list_file:
		proteins_to_search.add(line.split('\t')[0])


check = 0

with open(sys.argv[2].split('.')[0] + '_peptides_list.txt', 'w') as out_file:
	for report in reports:

		fraction = '_'.join(report.split('/')[1].split('_')[1:7]) #grab fraction name
		with open(report,'r') as report_file:
			if check == 0:
				header = report_file.readline()
				out_file.write(header.rstrip() + '\tfraction\n')
				check = 1
			for line in report_file:
				line_split = line.rstrip().split('\t') #split tab delim line
				if not ';' in line_split[1]:
					if line_split[1] in proteins_to_search:
						if line_split[-1] == 'Confident': #check if protein is confident
							out_file.write(line.rstrip() + '\t' + fraction + '\n')
				else:
					possible_proteins = line_split[1].split(';')
					for pos_prot in possible_proteins:
						pos_prot = pos_prot.strip()
						if pos_prot in proteins_to_search:
							if line_split[-1] == 'Confident': #check if protein is confident
								out_file.write(line.rstrip() + '\t' + fraction + '\n')
							break

						
	
	
	
	
	
