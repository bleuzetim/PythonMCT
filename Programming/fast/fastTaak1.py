import pandas as pd
import random
import math
import seaborn as sns
import matplotlib.pyplot as plt

d = pd.read_csv("data/fast_groepen_opgave2.csv")

def maak_groepen(klassen , grootte : int,gesplitst : bool):
    totaal = len(d['klasgroep'].to_list())
    lmct = []
    lmit =[]
    for i in l:
        if 'MCT' in i:
            lmct.append(i)
    else: lmit.append(i)
    gemixt = input('Mogen de groepen gemengd zijn tussen zowel MCT als MIT [J:ja,N:nee]')
    if 'MIT' in klassen:
        
        
    l = {}
    n = []
    for i in range(len(d['klasgroep'].to_list())):
        n.append(i)
    for o in range(((len(d['klasgroep'].to_list())-1)//grootte)):
        for p in range(grootte): 
            rand = random.choice(n)
            n.remove(rand)
            if o in l.keys():
                l[o].append(d['voornaam'][rand]+ ' ' + d['familienaam'][rand])
            else:
                l[o] = []
                l[o].append(d['voornaam'][rand]+ ' ' + d['familienaam'][rand])

    for a in range(len(d['klasgroep'].to_list())-(grootte*(((len(d['klasgroep'].to_list())-1)//grootte)))):
            rand = random.choice(n)
            n.remove(rand)
            if a!=0:
                l[o+0].append(d['voornaam'][rand]+ ' ' + d['familienaam'][rand])
            else:
                l[o+a] = []
                l[o+a].append(d['voornaam'][rand]+ ' ' + d['familienaam'][rand])

    for m in l.keys():
        print(l[m])



count = 0 
l=[]

for i in (d['klasgroep'].to_list()):
    if i not in l:
        l.append(i)
        count+=1
lmct = []
lmit =[]
for i in l:
    if 'MCT' in i:
        lmct.append(i)
    else: lmit.append(i)


MCT = d[d['klasgroep']=='MCT'].klasgroep
for i in lmct:
    print(d[d['klasgroep']==i].klasgroep)
print('--------')
for i in lmit:
    print(d[d['klasgroep']==i].klasgroep)
print(lmit)
print(lmct.index('1MCT3'))
print(lmct[3])
print(len(d['klasgroep'].to_list()))







