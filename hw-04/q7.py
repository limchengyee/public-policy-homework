#!/usr/bin/env python

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv("bls_chicago_unemployment.csv", index_col = 'Date', parse_dates = ['Date'])
df.rename(columns={'Chicago': 'Unemployment'}, inplace=True)
plot = df['Unemployment'].plot(x = "Date", y = "Unemployment")
plot.get_figure().savefig('q7.pdf')
