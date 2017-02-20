#!/bin/bash

# We have several questions about
# the time distribution of first
# degree murders.  Let's make an
# 'intermediate' file with just
# that information.

cat chicago_crime.csv |
    grep -i "FIRST DEGREE MURDER" |     # grep out the first degree murders
    cut -f3 -d, > murder_dates.txt |    # use cut to select the date (3rd field, divided by ",")
    cat murder_dates.txt

echo "Murders by hour of day."
cat murder_dates.txt |                  # cat murder_dates.txt |
    sed 's/\:..:..//g' |                # use sed to find minutes and seconds, and remove them.
    cut -f2,3 -d " " |                  # cut out only the times -- the 2nd field, delimited by spaces.
    sed 's/12 AM/00 AM/g' |             # we'll sort it, so we want 12AM to come before 01AM, use sed to replace 12 with 00
    sort -n | uniq -c |                 # sort it and count (uniq) the results
    sort -nr |                          # resort based on the frequency,
    head -1                             # and print the worst one.

echo "Worst month for murders."
cat murder_dates.txt |
    cut -f1 -d / |                      # cut, delimiting on "/" to grab the month (1st field)
    sort -n | uniq -c | sort -n -r      # sort them, then count (uniq -c)

echo "Bloodiest single day."
cat murder_dates.txt |
    cut -f1 -d " " |                     # we just want the dates, no times
    sort -n | uniq -c |                  # sort and count
    uniq -c | sort -nr | head -1         # reverse sort and take the top one (or, of course, sort and take the last)

echo "Murders by place."
cat chicago_crime.csv |
    grep -i "FIRST DEGREE MURDER" |     # Use grep to grab the first degree murders
    cut -f 8 -d , |                     # use cut to select the place field.
    sort | uniq -c |                    # sort it so that you can count (uniq).
    sort -n -r                          # then (reverse) sort  _that_, to order by the common places.
