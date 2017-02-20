#!/usr/bin/env python

# slope and error should hold the final answer
import pandas as pd
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

df = pd.read_csv("chicago_crime.csv")
pw = df[['Primary Type', 'Ward']]
weapon = pw[pw["Primary Type"]=="WEAPONS VIOLATION"].groupby("Ward").count()
weapon.rename(columns={'Primary Type': 'Weapon'}, inplace=True)
homicide = pw[pw["Primary Type"]=="HOMICIDE"].groupby("Ward").count()
homicide.rename(columns={'Primary Type': 'Homicide'}, inplace=True)
merged = pd.concat([homicide, weapon], axis=1)
merged.dropna(inplace = True)

slope, intercept, r_value, p_value, std_err = stats.linregress(merged["Weapon"], merged["Homicide"])
slope = slope
error = std_err
