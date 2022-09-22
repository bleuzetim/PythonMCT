import pandas as pd

d = pd.read_csv("fast_groepen_opgave2.csv")

count = 0 
l=[]

for i in (d['klasgroep'].to_list()):
    if i not in l:
        l.append(i)
        count+=1
        
        
print(l)
print(count)
