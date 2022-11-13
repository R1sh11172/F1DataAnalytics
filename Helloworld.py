import numpy as np
import pandas as pd


def get_dataframe(csvFile="races.csv"):
  return pd.read_csv(csvFile)


#import pandas as pd
#my_csv = pd.read_csv(filename)
#column = my_csv.column_name
# you can also use my_csv['column_name']


def get_driver_lap_times():
  df = get_dataframe()
  minidf = df[['raceId', 'year', 'name']]
  print(minidf.raceId)
  pass

get_driver_lap_times()