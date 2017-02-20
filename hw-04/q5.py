#!/usr/bin/env python

# solution should hold the final answer
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv("chicago_schools.csv", usecols = ["ISBE_ID", "PARCC Proficiency (%)", "College Ready (%)", "Low Income (%)"], index_col="ISBE_ID")
df.dropna(inplace = True)
c = df[df.index.str.contains("C")]
c.median()
nc = df[df.index.str.contains("C") == False]
nc.median()

# Charter schools perform better in college redainess and PARCC proficiencies than non-charter schools.
# The medians for college readiness is 14.4% in charter schools and 5.4% in non-charter schools.
# The medians for PARCC proficiency is 10.7% in charter schools and 3.0% in non-charter schools.
# Both charter and non-charter schools serve comparable fractions of disadvantaged students, with 94.2% and 92.8% low income students respectively.
