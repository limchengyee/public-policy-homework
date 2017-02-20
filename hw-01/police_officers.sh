#!/bin/bash

# How many police officers are there?
echo "Police Officers in Chicago"
cat salaries.csv |
    grep -i "police officer" |    # grep for police officers
    wc -l                          # count 'em with wc!
      
