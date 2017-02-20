#!/bin/bash

# What are the most common names of police officers?
echo "Most common police officer names."
cat salaries.csv |
    grep -i "police officer" |          # grep police officers.
    cut -f2 -d, |                       # cut out their first names
    sed 's/\  //g' | sed 's/"//g' |     # get rid of quotes and leading spaces + sed find and replace
    cut -f1 -d " " |                    # choose the first field: cut
    sort -r | uniq -c | sort -n -r |    # do some sorting magic (sort/uniq)
    head -40                            # to pull off the top 40 (head)

# What do you notice about the names?  Ouff.
