import pandas as pd

data = pd.read_excel(r"C:\Users\stufs\Desktop\Git\GUI-tic-tac-toe\main\data.xlsx")
d = list(data["A"])
a = {}
sum = 0
for obj in d:
    if obj not in list(a.keys()):
        a.update({obj: 0})
for obj in d:
    for key in list(a.keys()):
        if obj == key:
            a[key] += 1
for key in list(a.keys()):
    sum += a[key]
print(a)
print(sum)