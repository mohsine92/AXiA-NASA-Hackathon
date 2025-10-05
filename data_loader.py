# data_loader.py
import pandas as pd

def load_exoplanets(csv_path="data/prepared_exoplanets.csv"):
    df = pd.read_csv(csv_path)
    return df