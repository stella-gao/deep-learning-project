#!/bin/bash
remove='2'
cut -d, -f$remove --complement 100.csv > 100_1.csv
tr , " " < 100_1.csv > 100_2.txt
