#Automatically run searchCLI and PeptideShaker

###REQUIREMENTS###

	#Modules: sys, glob, subprocess, linecache, shutil, math, random, argparse, os
	#files: mgf spectra file, .par file setup via SearchGUI
	#Modify script to specify location of PeptideShaker and SearchGUI .jar files and versions 3.2.13 on SearchGUI and 1.16.4 for PeptideShaker

'''
usage: search_shaker_auto.py input_spectra.mgf SearchGUI.par
'''

import sys, subprocess, os, time

#start = time.clock()

###.jar locations
SearchGUI = '/stor/home/rgarge/SearchGUI-3.2.13' + '/SearchGUI-3.2.13.jar'
PeptideShaker = '/stor/home/rgarge/PeptideShaker-1.16.4' + '/PeptideShaker-1.16.4.jar'


###Get input files
mgf_file = sys.argv[1]
par_file = sys.argv[2]


###Create file structure
current_path = os.getcwd()

sample = mgf_file.split('.')[0]
out_path = current_path + '/' + sample
if not os.path.exists(out_path):
	os.makedirs(out_path)
	os.makedirs(out_path + '/log')
	os.makedirs(out_path + '/peptide_shaker')
	os.makedirs(out_path + '/peptide_shaker/reports')


###Run SearchCLI (We used X!Tandem, OMSSA and MS-GF+. You may want to add/delete search engines as required)
cmd = ['java', '-cp', SearchGUI, 'eu.isas.searchgui.cmd.SearchCLI', 
		'-spectrum_files', '"' + mgf_file + '"', 
		'-output_folder', '"' + out_path + '"', 
		'-id_params', '"' + par_file + '"',
		'-log', '"' + out_path + '/log' + '"',
		'-xtandem', '1', 
		'-msgf', '1', 
		'-omssa', '1',
		'-output_option', '3',
		'-threads', '25'
]

print('Running SearchCLI on %s\n' % mgf_file)
process = subprocess.Popen(cmd)
process.wait()

###Run PeptideShaker
cmd2 = ['java', '-cp', PeptideShaker, 'eu.isas.peptideshaker.cmd.PeptideShakerCLI', 
		'-experiment', 'AltOrfSearch',
		'-sample', mgf_file.split('.')[0],
		'-replicate', '0',
		'-identification_files', '"' + out_path + '/' + mgf_file.split('.')[0] + '.omx, ' + out_path + '/' + mgf_file.split('.')[0] +'.msgf.mzid, ' + out_path + '/' + mgf_file.split('.')[0] + '.t.xml,' + '"',
		'-spectrum_files', '"' + mgf_file + '"',
		'-id_params', '"' + par_file + '"',
		'-out', '"' + out_path + '/peptide_shaker/' + sample + '.cpsx' + '"'
]

print('Running PeptudeShaker on %s\n' % mgf_file)
process2 = subprocess.Popen(cmd2)
process2.wait()

###Copy mgf file into PeptideShaker directory since the program is dumb and can't locate the mgf file via command line. It says you can but provides no documentation of the command to do that.
cmd3 = ['cp', mgf_file, out_path + '/peptide_shaker']
process3 = subprocess.Popen(cmd3)
process3.wait()


###Generate PeptideShaker Reports
cmd4 = ['java', '-cp', PeptideShaker, 'eu.isas.peptideshaker.cmd.ReportCLI',
		'-in', '"' + out_path + '/peptide_shaker/' + sample + '.cpsx' + '"',
		'-out_reports', '"' + out_path + '/peptide_shaker/reports' + '"',
		'-reports', '"3,5,7"'
]
process4 = subprocess.Popen(cmd4)
process4.wait()
#print('Done in %f seconds' % (time.clock() - start))

