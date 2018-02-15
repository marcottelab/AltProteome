# This script reads the altorf fasta and tis_ms_out file and returns the output of the experimentally validated altorfs in a fasta format.
import sys
#import re
from Bio import SeqIO


altorfseqs_file=sys.argv[1]
expt_altorfs_file=sys.argv[2]
#ref_seq_file= sys.argv[3]
altorf_dict={}
ref_seq_dict={}
val_altorf=set()
#full_dict={}

#Makes a dict of the fasta header and corresponding sequence

for line in SeqIO.parse(altorfseqs_file, 'fasta'):
	altorf_dict[str(line.id)]= str(line.seq)
#print altorf_dict

for line in SeqIO.parse(ref_seq_file, 'fasta'):
	ref_seq_dict[str(line.id)]= str(line.seq)
#print len(ref_seq_dict)

#Makes a set of entries that need to be searched against the dictionary

with open(expt_altorfs_file, "r") as in_file2:
	next(in_file2)
	for line in in_file2:
		line=line.split("\n")
		val_altorf.add(line[0])
#print val_altorf

#Makes a dictionary with the filtered orfs

clean_dict={key:value for key,value in altorf_dict.items() if key in val_altorf}

#print len(clean_dict)
#full_dict.update(ref_seq_dict)
#full_dict.update(clean_dict)
#print len(full_dict)

#Writes it out to fasta format

with open('reduced_altorf_set.fasta', 'w') as out_file:
	for key,value in clean_dict.items():
		out_file.write(">" + key + "\n" + value + "\n")

#with open('Hs_ref_red_altorf_database.fasta', 'w') as output_file:
#	for key,value in full_dict.items():
#		output_file.write(">" +  key + "\n" + value + "\n")
