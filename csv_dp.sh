#!/bin/bash
remove='2'
cut -d, -f$remove --complement profile_database_100.csv > 100_1.csv
awk -F, -vOFS="," '{for (i=2; i<=NF; i++) { $i=(i-1)":"$i}}1' 100_1.csv > 100_2.csv
tr , " " < 100_2.csv > 100_3.txt




