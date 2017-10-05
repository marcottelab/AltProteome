#!/bin/bash

############################################################
# This script parses all *Decoys_PSM_Reports.txt files in a directory to a single file containing every unique protein with unique PSMs
# 
############################################################

awk 'BEGIN {
    FS="\t"
    OFS=FS
    PROCINFO["sorted_in"] = "@ind_str_asc"
  }
  
  FNR == 1 {
    filecounter++
    split(FILENAME,splitted,"_")
    if (filecounter == 1)
      printf($2"\tTotalCount\tUniquePeptides")
    printf("\t%s_%s",splitted[3],splitted[7])
    next
  }
  #$2 ~ /\,/ && $24 /Confident/ {
  $2 !~ /,/ {
    prot_totals[$2] += 1
    prots[$2,filecounter] += 1
    if (peps_unique[$2,$3]++ == 0) {
        peps_uniq_counts[$2]++
      
    }
  }
  END {
    for (prot in prot_totals) {
      printf("\n%s\t%d\t%d", prot, prot_totals[prot], peps_uniq_counts[prot])
      for (i = 1; i<=filecounter; i++)
        printf("\t%d", prots[prot,i])
    }
  }' "$@"


#FNR == 2 {
#    if (filecounter == 1)
#      printf($1"\tTotalCount")
#    printf("\t%s",$3)
#    next
#  }
#  {
#    pep_totals[$1] += $3
#    peps[$1,filecounter] = $3
#  }
#  END {
#    for (pep in pep_totals) {
#      printf("\n%s\t%d", pep, pep_totals[pep])
#      for (i = 1; i<=filecounter; i++)
#        printf("\t%d", peps[pep,i])
#    }
#  }' "$@"
