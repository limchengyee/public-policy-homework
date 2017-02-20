#!/usr/bin/env python
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# solution should hold the final answer
solution = 0
df = pd.read_csv("chicago_crime.csv", index_col = 'ID')
pd.read_csv("chicago_crime.csv")
solution = df.groupby('Ward').count().sort_values(by = 'Case Number', ascending = False).index[0]
