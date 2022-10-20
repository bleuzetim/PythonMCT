import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def geef_naam(titel,x_as,y_as):
    plt.title(titel)
    plt.x

def histogram(data,x,y,title=''):
    sns.histplot(data=data, x=x,y=y)
    title = f'Graafiek van {x} en {y}'
    plt.title(title)

def get_bins(df,kolom):
    rang = df[kolom].max()-df[kolom].min()
    bins = (rang/(np.sqrt(df[kolom].count())))
    bins = np.arange(df[kolom].min(), df[kolom].max(), bins)
    return bins

def distplot(df,kolom):
    bins = get_bins(df,kolom)
    sns.distplot(x=df[kolom], bins=bins, kde=False)
    plt.title(f'Grafiek van {kolom}')
    plt.show()
     
