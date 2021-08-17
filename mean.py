import pandas as pd



df = pd.read_csv("data.csv")
data = df["Height(Inches)"].tolist()

sum = 0

for g in data:
    sum = sum + g

print(sum)

number = len(data)
print(number)

average = sum/number
print(average)

