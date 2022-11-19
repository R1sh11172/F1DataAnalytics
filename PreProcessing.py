import numpy as np
import pandas as pd

def get_status(csvFile="status.csv"):
    return pd.read_csv(csvFile)
def get_results(csvFile="results.csv"):
    return pd.read_csv(csvFile)
def get_qualifying(csvFile="qualifying.csv"):
    return pd.read_csv(csvFile)
def get_races(csvFile="races.csv"):
    return pd.read_csv(csvFile)
def get_pit_stops(csvFile="pit_stops.csv"):
    return pd.read_csv(csvFile)
def get_drivers(csvFile="drivers.csv"):
    return pd.read_csv(csvFile)
def get_constructors(csvFile="constructors.csv"):
    return pd.read_csv(csvFile)

statusDf = get_status()
resultsDf = get_results()[['raceId', 'driverId', 'constructorId', 'fastestLapTime', 'fastestLapSpeed', 'rank', 'statusId']]
qualifyingDf = get_qualifying()[['raceId', 'driverId', 'constructorId', 'position', 'q1', 'q2','q3']]
racesDf = get_races()[['raceId', 'name']]
pitStopsDf = get_pit_stops()[['raceId', 'driverId', 'stop', 'lap', 'time', 'duration']]
driversDf = get_drivers()[['driverId', 'driverRef']]
constructorsDf = get_constructors()[['constructorId', 'name']]
