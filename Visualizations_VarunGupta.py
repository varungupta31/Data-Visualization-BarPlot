# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 18:30:54 2021

@author: varun
"""

#Importing the required libraries

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
from plotly.offline import plot
#Importing the dataset

df = pd.read_csv('housing.csv')

df.describe
#This tells us that there are 20,640 values in the data and 10 features.

df.info()

#The columns present in the data are : 
    
"""
 1   latitude            
 2   housing_median_age  
 3   total_rooms         
 4   total_bedrooms      
 5   population          
 6   households          
 7   median_income       
 8   median_house_value  
 9   ocean_proximity  
 
1. longitude: A measure of how far west a house is; a higher value is farther west

2. latitude: A measure of how far north a house is; a higher value is farther north

3. housingMedianAge: Median age of a house within a block; a lower number is a newer building

4. totalRooms: Total number of rooms within a block

5. totalBedrooms: Total number of bedrooms within a block

6. population: Total number of people residing within a block

7. households: Total number of households, a group of people residing within a home unit, for a block

8. medianIncome: Median income for households within a block of houses (measured in tens of thousands of US Dollars)

9. medianHouseValue: Median house value for households within a block (measured in US Dollars)

10. oceanProximity: Location of the house w.r.t ocean/sea
"""
#checking the variety of the label
print(df['ocean_proximity'].value_counts())

"""
<1H OCEAN     9136
INLAND        6551
NEAR OCEAN    2658
NEAR BAY      2290
ISLAND           5
Name: ocean_proximity, dtype: int64
"""

#extracting required columns -- Housing Price and house location.
df_final = df.iloc[:,[8,9]].copy()

df_final.head()

#creating a list of average prices by location
prices = []

#checking the information of individual location.
prices.append(df_final[df_final['ocean_proximity']=='<1H OCEAN'].describe().loc['mean'][0])

prices.append(df_final[df_final['ocean_proximity']=='INLAND'].describe().loc['mean'][0])

prices.append(df_final[df_final['ocean_proximity']=='NEAR OCEAN'].describe().loc['mean'][0])

prices.append(df_final[df_final['ocean_proximity']=='NEAR BAY'].describe().loc['mean'][0])

prices.append(df_final[df_final['ocean_proximity']=='ISLAND'].describe().loc['mean'][0])


#rounding up to 3 decimal places
prices = [round(num,3) for num in prices]

locations = ['<1H OCEAN','INLAND','NEAR OCEAN','NEAR BAY','ISLAND']

#Data is prepared.

#Plotting Using MATPLOTLIB

plt.figure(figsize=(24,12))
plt.bar(x=locations,height = prices,width = 0.8,
        edgecolor='red',tick_label = locations,hatch='\\')
for index,data in enumerate(prices):
    plt.text(x=index-0.2 , y =data+3000 , s=f"{data}$" , fontdict=dict(fontsize=20))
plt.tick_params(axis='both',labelsize=20)
plt.xlabel('Location of Property',labelpad=10,fontsize=15,backgroundcolor='yellow',fontweight='medium')
plt.ylabel('Mean House Value($)',labelpad=15,fontsize=15,backgroundcolor='yellow',fontweight='medium')
plt.title("Average Housing Prices In California By Location",fontsize=30,fontweight='medium')
ax = plt.axes()
ax.set_facecolor('orange')
plt.savefig('my')


## Data Plotting Using  plotly
df_plotly = pd.DataFrame({
    'Location':locations,
    'Average Price':prices})
fig = px.bar(df_plotly,x="Location",y="Average Price",title="Average Housing Prices in California By Location",color="Average Price")
plot(fig)


## NOTE: The plotly plot will launch on the localhost, in a web browser.
