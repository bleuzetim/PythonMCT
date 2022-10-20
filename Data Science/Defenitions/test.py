from custom_defs import *
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

#df = pd.read_csv('riemen.csv')

#boxplot(df,'Geslacht','Heupomtrek','Heupomtrek','Sex')  werkt
#sns.histplot(x=df[df['Geslacht']=='M']['Heupomtrek'])
#plt.show()

#histogram('',df[df['Geslacht']=='M']['Heupomtrek'],'','Grafiek van ','Heupomtrek','Aantal') werkt

df = pd.read_csv('penguins_preprocessed.csv')

catplot(df,'Sex','','count','Sex','Aantal','Staafdiagram mannen vs vrouwen',[0,1],['man','vrouw'])
plt.show()
t = input('g ')