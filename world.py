import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Loading the dataset
df=pd.read_csv('world-data-2023.csv')
print(df.head())
print(df.info())

df.drop(columns=['Abbreviation'], inplace=True)
df.drop(columns='Longitude', inplace=True)
df.drop(columns='Latitude', inplace=True)
print(df.columns)

print(df.duplicated().sum())
print(df.isna().sum())

#Percentange of the missing values
null_mean = (df.isna().mean()*100).round(2)
print("Percentage of Null Elements in Each Column is:")
print(null_mean)

#Checking for values that might affect the Analysis
df_num = df.select_dtypes(include=[np.number])
df_cat = df.select_dtypes(include =[object])
print(df_num.head().T)
print(df_cat.describe().T)

print("Column data types are:", df.dtypes)
#Before converting numeric columns to floats, remove the units of measures($, %) and commas 
comma_cols=[]
percent_cols=[]
dollar_cols=[]
for col in df.columns:
    if df[col].dtype=="object":
        if df[col].str.contains(",").any():
            comma_cols.append(col)
        elif df[col].str.contains("%").any():
            percent_cols.append(col)
        elif df[col].str.contains("$").any():
            dollar_cols.append(col)
 
for col in percent_cols:
    df[col]=df[col].str.replace("%","")            

for col in dollar_cols:
    df[col]=df[col].str.replace("$","")
    
for col in comma_cols:
    df[col]=df[col].str.replace(",","")

df["GDP"]=df["GDP"].str.replace("$","")                                        

#Converting numerical values from objects to floats
for col in df.columns:
    if df[col].dtype=="object":
        if col == 'Density\n(P/Km2)'or col =='Land Area(Km2)'or col =='Armed Forces size'or col =='Co2-Emissions'or col =='CPI'or col =='GDP'or col =='Population'or col =='Urban_population'or col =='Agricultural Land( %)'or col =='CPI Change (%)'or col =='Forested Area (%)'or col =='Gross primary education enrollment (%)'or col =='Gross tertiary education enrollment (%)'or col =='Out of pocket health expenditure'or col =='Population: Labor force participation (%)'or col =='Tax revenue (%)'or col =='Total tax rate' or col =='Unemployment rate' or col =='Gasoline Price' or col =='Minimum wage':
            df[col]=df[col].astype("float64")
            
print(df.dtypes)            

#Top 20 most populated countries
country_population =df[["Country","Population"]].dropna().sort_values(by="Population",ascending=False).reset_index()

highest_populated=country_population[["Country","Population"]].head(20).reset_index().drop("index",axis=1)
print(highest_populated)

least_populated=country_population[["Country","Population"]].tail(20).reset_index().drop("index",axis=1)
print(least_populated)

#Vizualizing the results
#highest_populated.sort_index(ascending=True).set_index("Country").plot(kind="bar",color="#0F2539",legend=False)
#plt.xticks(rotation=90)

#plt.title("Top 20 Populated Countries")
#plt.xlabel("Population")
#plt.ylabel("Country")
#plt.show()

#least_populated.sort_index(ascending=False).set_index("Country").plot(kind="bar",color="#0F2539",legend=False)
#plt.xticks(rotation=90)

#plt.title("Bottom 20 Populated Countries")
#plt.xlabel("Country")
#plt.ylabel("Population")
#plt.show()

#Top 20 and Bottom 20 country's GDP
country_gdp=df[["Country","GDP"]].dropna().sort_values(by="GDP",ascending=False).reset_index()

highest_gdp=country_gdp[["Country", "GDP"]].head(20).reset_index().drop("index",axis=1)
print(highest_gdp)

plt.title("Top 20 Countries With Highest GDP")
plt.xlabel("Country")
plt.ylabel("GDP")
plt.show()

lowest_gdp=country_gdp[["Country", "GDP"]].tail(20).reset_index().drop("index",axis=1)
print(lowest_gdp)
