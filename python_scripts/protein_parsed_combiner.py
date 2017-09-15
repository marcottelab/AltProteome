#This script takes in a folder of parsed protein reports (from protein_report_parser.py) and combine the doubful and confident into one file each with the fraction appended to each line

'''
Usage: protein_parsed_combiner.py parsed_report_directory
'''

import sys, glob

folder = sys.argv[1]

confident = glob.glob(folder + '*confident.txt')
doubtful = glob.glob(folder + '*doubtful.txt')

#confident parsing
with open('confident_alt_ORFs.txt', 'w') as conf_out:

	#get column headers
	with open(confident[0],'r') as get_col_headers:
		col_headers = get_col_headers.readline().rstrip()
	conf_out.write(col_headers + '\tFraction\n')

	for conf_file in confident: #iterate through files
		fraction = '_'.join(conf_file.split('/')[1].split('_')[1:7]) #grab fraction name
		with open(conf_file,'r') as conf_to_parse:
			next(conf_to_parse)
			for line in conf_to_parse:
				if line != '\n':
					conf_out.write(line.strip() + '\t' + fraction + '\n')


#doubtful parsing
with open('doubtful_alt_ORFs.txt', 'w') as doubt_out:

	#get column headers
	with open(doubtful[0],'r') as get_col_headers:
		col_headers = get_col_headers.readline().rstrip()
	doubt_out.write(col_headers + '\tFraction\n')

	for doubt_file in doubtful:
		fraction = '_'.join(doubt_file.split('/')[1].split('_')[1:7]) #grab fraction name

		with open(doubt_file,'r') as doubt_to_parse:
			next(doubt_to_parse)
			for line in doubt_to_parse:
				if line != '\n':
					doubt_out.write(line.strip() + '\t' + fraction + '\n')

