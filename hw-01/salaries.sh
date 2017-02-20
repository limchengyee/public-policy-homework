#!/bin/bash

# SORT CHICAGO SALARIES

# start the party!!
echo "Top 10 Salaries in Chicago"
cat salaries.csv | 
    grep '\$' |               # keep only lines with dollar signs.
    sed 's/\$//g' |           # remove the dollar signs.
    sed "s/\"//g" |           # remove the quotes
    sort -t, -k 5 -n -r |     # sorting is the best.
    head -10 | column -s, -t  # clean it up


