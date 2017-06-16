#!/bin/bash
remove='2'
cut -d, -f$remove --complement profile_database_350.csv > 350_1.csv
awk -F, -vOFS="," '{for (i=2; i<=NF; i++) { $i=(i-1)":"$i}}1' 350_1.csv > 350_2.csv
tr , " " < 350_2.csv > 350_3.txt




