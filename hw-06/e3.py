# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 21:18:34 2016

@author: Lim Cheng Yee
"""

import pandas as pd 
import glob

y = []
for line in open("ELECTION_ID", "r"):
    x =line.strip().split()
    for i in x:
        y.append(int(i))

#split each line into year/el_id
year = y[::2]
elec = y[1::2] 

path =r'C:\cygwin64\home\Lim Cheng Yee\hw-6-limchengyee' # use your path
allFiles = glob.glob(path + "/*.csv")
frame = pd.DataFrame()
list_ = []
i = 0
for year in range(1924,2013,4):
    for file_ in allFiles:
        header = pd.read_csv(file_, nrows = 1).dropna(axis = 1)
        d = header.iloc[0].to_dict()

        df = pd.read_csv(file_, index_col = 0, thousands = ",", skiprows = [1])

        df.rename(inplace = True, columns = d) # rename to democrat/republican
        df.dropna(inplace = True, axis = 1)    # drop empty columns
        list_.append(df)
        df["Year"]=year
frame = pd.concat(list_, ignore_index=True)
