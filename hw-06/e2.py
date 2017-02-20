# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 21:18:04 2016

@author: Lim Cheng Yee
"""
import csv 

y = []
for line in open("ELECTION_ID", "r"):
    x =line.strip().split()
    for i in x:
        y.append(int(i))
print(x)
#split each line into year/el_id
year = y[::2]
elec = y[1::2] 

num = 0 
for i in elec:
    addr = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/".format(i)
    resp = requests.get(addr)
    #write them into a file
    file_name = str(year[num])+".csv"
    num += 1 
    with open(file_name, "w") as out:
        out.write(resp.text)
