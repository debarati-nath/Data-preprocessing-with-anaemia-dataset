#Importing libraries
import pandas as pd
from sklearn.preprocessing import LabelBinarizer
import matplotlib.pyplot as plt
import seaborn as sns

#Load dataset from the personal computer
datafeatures = pd.read_csv('C:/Users/Tuli/Downloads/Combine.csv')

#Apply mapping
datafeatures['Prevalence of anaemia in pregnant women (aged 15-49) (%)'] = list(map(lambda x: x.split('[')[0].rstrip(' '), \
                                                                                    datafeatures['Prevalence of anaemia in pregnant women (aged 15-49) (%)']))
datafeatures['Number of women of reproductive age (aged 15-49 years) with anaemia (thousands)'] = list(map(lambda x: x.split('[')[0].rstrip(' '), \
                                                                                    datafeatures['Number of women of reproductive age (aged 15-49 years) with anaemia (thousands)']))
datafeatures['Prevalence of anaemia in non-pregnant women (aged 15-49) (%)'] = list(map(lambda x: x.split('[')[0].rstrip(' '), \
                                                                                    datafeatures['Prevalence of anaemia in non-pregnant women (aged 15-49) (%)']))
datafeatures['Number of non-pregnant women (aged 15-49 years) with anaemia (thousands)'] = list(map(lambda x: x.split('[')[0].rstrip(' '), \
                                                                                    datafeatures['Number of non-pregnant women (aged 15-49 years) with anaemia (thousands)']))
datafeatures['Prevalence of anaemia in pregnant women (aged 15-49) (%)'] = list(map(lambda x: x.split('[')[0].rstrip(' '), \
                                                                                    datafeatures['Prevalence of anaemia in pregnant women (aged 15-49) (%)']))
datafeatures['Number of pregnant women (aged 15-49 years) with anaemia (thousands)'] = list(map(lambda x: x.split('[')[0].rstrip(' '), \
                                                                                datafeatures['Number of pregnant women (aged 15-49 years) with anaemia (thousands)']))
datafeatures['Prevalence of anaemia in children aged 6–59 months (%)'] = list(map(lambda x: x.split('[')[0].rstrip(' '), \
                                                                                    datafeatures['Prevalence of anaemia in children aged 6–59 months (%)']))
datafeatures['Number of children aged 6–59 months with anaemia (thousands)'] = list(map(lambda x: x.split('[')[0].rstrip(' '), \
                                                                                    datafeatures['Number of children aged 6–59 months with anaemia (thousands)']))
datafeatures['Prevalence of anaemia in women of reproductive age (aged 15-49) (%)'] = list(map(lambda x: x.split('[')[0].rstrip(' '), \
                                                                                    datafeatures['Prevalence of anaemia in women of reproductive age (aged 15-49) (%)']))


#Use LabelBinarizer for 'Country' coloumn
binary = LabelBinarizer()
binary.fit(datafeatures['Country'])
transformed = binary.transform(datafeatures['Country'])
country_df = pd.DataFrame(transformed)

country_df['ColumnA'] = country_df[country)df.columns[0:]].apply(
    lambda x: ''.join(x.dropna().astype(str)),
    axis=1)
country_df.drop(country_df[country_df.columns[0:192]], axis=1)


#Display datadeatures
datafeatures.head()

#Save as csv
datafeatures.to_csv("C:/Users/Tuli/Downloads/combine_edited.csv")

#Read csv file
datafeatures = pd.read_csv('C:/Users/Tuli/Downloads/combine_edited.csv')
datafeatures.shape

#Dataframe
datafeatures=pd.DataFrame(datafeatures)
datafeatures=datafeatures.iloc[:,1:]
datafeatures.head()

for col in datafeatures.columns:
    datafeatures['Prevalence of anaemia in women of reproductive age (aged 15-49) (%)'] = datafeatures['Prevalence of anaemia in women of reproductive age (aged 15-49) (%)'].astype(float)
    datafeatures['Prevalence of anaemia in non-pregnant women (aged 15-49) (%)'] = datafeatures['Prevalence of anaemia in non-pregnant women (aged 15-49) (%)'].astype(float)
    datafeatures['Number of women of reproductive age (aged 15-49 years) with anaemia (thousands)'] = datafeatures['Number of women of reproductive age (aged 15-49 years) with anaemia (thousands)'].astype(float)
    datafeatures['Prevalence of anaemia in pregnant women (aged 15-49) (%)'] = datafeatures['Prevalence of anaemia in pregnant women (aged 15-49) (%)'].astype(float)
    datafeatures['Number of non-pregnant women (aged 15-49 years) with anaemia (thousands)'] = datafeatures['Number of non-pregnant women (aged 15-49 years) with anaemia (thousands)'].astype(float)
    datafeatures['Number of pregnant women (aged 15-49 years) with anaemia (thousands)'] = datafeatures['Number of pregnant women (aged 15-49 years) with anaemia (thousands)'].astype(float)
    datafeatures['Number of children aged 6–59 months with anaemia (thousands)'] = datafeatures['Number of children aged 6–59 months with anaemia (thousands)'].astype(float)
    datafeatures['Prevalence of anaemia in children aged 6–59 months (%)'] = datafeatures['Prevalence of anaemia in children aged 6–59 months (%)'].astype(float)

#Drop the coloumns
datafeatures.drop(['Country','Year'], axis = 1 ,inplace=True)

#Normalize
datafeatures = (datafeatures - datafeatures.min()) / (datafeatures.max() - datafeatures.min())

#Correlation
corrmatrix = datafeatures.corr()
topcorrfeatures = corrmatrix.index
plt.figure#(figsize=(16,16))
g=sns.heatmap(datafeatures[topcorrfeatures].corr(), annot=True, cmap="Spectral")
plt.show()



