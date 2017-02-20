#!/usr/bin/env python
import pandas as pd

# these will be useful later
import numpy  as np
from matplotlib import pyplot as plt

# solution should hold the final answer
df = pd.read_csv("chicago_crime.csv", index_col = 'ID')
crime_arrest = df[["Primary Type", "Arrest"]]
crime_arrest[df['Arrest']].groupby('Primary Type').count().sort_values(by = 'Arrest', ascending = False).head(5)
solution = crime_arrest[df['Arrest']].groupby('Primary Type').count().sort_values(by = 'Arrest', ascending = False).index[0]
