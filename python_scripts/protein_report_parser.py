#This script takes in a protein report from peptide shaker and search for the alt_orfs and pull them out into a new file.

'''
Usage: protein_report_parser.py protein_report_file
'''

import sys, os

current_path = os.getcwd()

confident_alts = []
doubtful_alts = []

with open(sys.argv[1], 'r') as report_file: #open report fle
	col_headers = report_file.readline()
	for line in report_file: #iterate through lines
		line_split = line.strip().split('\t') #split tab delim line
		if line_split[1].startswith('NM') or line_split[1].startswith('XM'): #check if protein is from alt_orf set
			if line_split[-1] == 'Confident': #check if alt protein is confident
				confident_alts.append(line)
			else:
				doubtful_alts.append(line)

out_report_name_base = current_path + '/' + sys.argv[1].split('.')[0]


#confident output file
with open(out_report_name_base + '_confident.txt', 'w') as confident_out:
	confident_out.write(col_headers)
	for con in confident_alts:
		confident_out.write(con + '\n')

#doubtful output file
with open(out_report_name_base + '_doubtful.txt', 'w') as doubtful_out:
	doubtful_out.write(col_headers)
	for doubt in doubtful_alts:
		doubtful_out.write(doubt + '\n')

#stats and stats output file
confident_alts_num = len(confident_alts)
doubtful_alts_num = len(doubtful_alts)
total_alts = confident_alts_num + doubtful_alts_num
if not total_alts == 0:
	percent_conf = confident_alts_num / (doubtful_alts_num + confident_alts_num) * 100
else:
	percent_conf = 0


with open(out_report_name_base + '_stats.txt', 'w') as stats_out:
	stats_out.write('Total_Alt_ORFs\tConfident_Alt_ORFs\tDoubtful_Alt_ORFs\tPercent_Confident\n')
	stats_out.write(str(total_alts) + '\t' + str(confident_alts_num) + '\t' + str(doubtful_alts_num) + '\t' + str(percent_conf))


