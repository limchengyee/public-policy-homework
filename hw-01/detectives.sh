#!/bin/bash

# How many police detectives are there?
echo "Police Detectives in Chicago"
cat salaries.csv |
    grep -i "detective" |   # grep for employees 'assigned as detective'
    wc -l                   # count 'em with wc!
