import pandas as pd
import numpy as nm

df=pd.read_csv("India Agriculture Crop Production.csv")
df.head()

df.sort_values(['Production'], ascending= False,axis=0,inplace=True)
df_top5=df.head()
df_top5=df_top5['Production'].transpose()


import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
df_top5.plot(kind='area')

plt.title('India Agriculture Crop Production')
plt.ylabel('Number of crops')
plt.xlabel('Years')
plt.show()

import matplotlib as mpl
import matplotlib.pyplot as plt
df_top5.plot(kind='hist')

plt.title('India Agriculture Crop Production')
plt.ylabel('Number of crops')
plt.xlabel('Years')
plt.show()

df.sort_values(['Production'], ascending= False,axis=0,inplace=True)
df_top5=df.head()
df_top5=df_top5['Production'].transpose()

df.set_index('Country', inplace=True)
df.columns = list(map(str, df.columns))
df.describe()
years=list(map(str ,range(1980,2014)))

Albania=df.loc['Albania',years]
Albania.index= Albania.index.map(int)
Albania.plot(kind='line')
plt.title('Immigration from Albenia')
plt.xlabel('Number of immigration')
plt.ylabel('Years')
# plt.text(2000, 6000, '2010 Earthquake') # see note below
plt.show()

df_YEIN=df.loc[['China','India'],years]
df_YEIN=df_YEIN.transpose()
df_YEIN.index= df_YEIN.index.map(int)
df_YEIN.plot(kind='line')
plt.ylabel("Number of immigrants")
plt.xlabel('Years')
plt.title("Immigartions from China to India")
plt.show()

#comparision of the trend of top 5 countries

df.head()
df_sort=df.sort_values(by = 'Total', ascending= False)
df_sort.head()

df.sort_values(['Production'], ascending= False,axis=0,inplace=True)
df_top5=df.head()
df_top5=df_top5['Production'].transpose()

top_5_names=df_sort.index[0:5]
df_top5=df.loc[top_5_names,years]
df_top5=df_top5.transpose()
df_top5.index=df_top5.index.map(int)
df_top5.plot(kind='line',figsize=(14,8))
plt.title('\nImmigration from top 5 companies \n')
plt.ylabel('\n Number of immigrants\n')
plt.xlabel('\n Years \n')
plt.show()

df_top5.plot(kind='area',figsize=(20,12),alpha=0.6,stacked=True)
plt.title("Immigration from top five countries")
plt.ylabel("Number of immigrants")
plt.xlabel("Years")
plt.show()

count,bin_edges=np.histogram(df['2013'])

df['2013'].plot(kind="hist", bins = 60, figsize=(8, 5), xticks=bin_edges)
plt.title("Histogram of immigration from 195 different countries")
plt.ylabel("Number of Countries")
plt.xlabel("Number of Immigrants")

df_t=df.loc[["India","China","Germany","Russian Federation"],years].transpose()
df_t.head()

count,bin_edges=np.histogram(df_t,10)
df_t.plot(kind="hist",figsize=(10,8),
          alpha=0.5,
          color=['darksalmon', 'darkslateblue', 'mediumseagreen'],
         xticks=bin_edges)
#Scatter plot
df_top5.plot(
    kind="scatter"
    x="Years"
    y="Total"
)
plt.title('Total immigrant population in Canada')
plt.xlabel("Year")
plt.ylabel("Number of immigrant")
