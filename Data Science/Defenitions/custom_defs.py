import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def geef_naam(titel,x_as,y_as):
    plt.title(titel)
    plt.x

def boxplot(data,x,y='',xlabel='',ylabel=''):
    if y=='':
        sns.boxplot(data=data,x=x)
        title = f'Grafiek van {x}'
    else:
        sns.boxplot(data=data, y=y,x=x)
        title = f'Grafiek van {x} en {y}'
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def histogram(data,x,y='',title='',xlabel='',ylabel=''): 
    if y=='':         
        sns.histplot(data=data, x=x)
        title = f'Grafiek van {x}'
        pass
    else:
        sns.histplot(data=data, x=x, y=y)
        title = f'Grafiek van {x} en {y}'
        pass
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def bins(df,kolom):
    rang = df[kolom].max()-df[kolom].min()
    bins = (rang/(np.sqrt(df[kolom].count())))
    bins = np.arange(df[kolom].min(), df[kolom].max(), bins)
    return bins

def distplot(df,kolom):
    bins = bins(df,kolom)
    sns.distplot(x=df[kolom], bins=bins, kde=False)
    plt.title(f'Grafiek van {kolom}')
     
