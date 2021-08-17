import pandas as pd
import statistics


df = pd.read_csv("data.csv")
data = df["Height(Inches)"].tolist()

mode = statistics.mode(data)
print(mode)