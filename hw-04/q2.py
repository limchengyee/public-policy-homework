#!/usr/bin/env python
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# solution should hold the final answer
df = pd.read_csv("chicago_crime.csv", index_col = 'ID')
primary_arrest = df[["Primary Type", "Arrest"]]
solution = primary_arrest.groupby('Primary Type').mean().sort_values(by ='Arrest', ascending = False).index[0]
