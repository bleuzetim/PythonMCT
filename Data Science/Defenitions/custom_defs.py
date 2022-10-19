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
    if xlabel!='':
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
    if xlabel!='':
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


def catplot(data,x,kind,y='',xlabel='',ylabel='',xticks=[],xtickss=[]):
    if y=='':
        sns.catplot(data=data, x=x,kind=kind)
        title = f'Grafiek van {x}'
    else:
        sns.catplot(data=data, x=x, y=y,kind=kind)
        title = f'Grafiek van {x} en {y}'
    if xlabel!='':
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
    if xticks != []:
        plt.xticks(xticks,xtickss)    
    plt.title(title)
    plt.show()
    
