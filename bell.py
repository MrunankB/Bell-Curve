import pandas as pd
import plotly.figure_factory as ff
import csv

df = pd.read_csv('csv.csv')
fig = ff.create_distplot([df['Avg Rating'].tolist()],[ 'Mobile Brand'], show_hist = False)
fig.show()
