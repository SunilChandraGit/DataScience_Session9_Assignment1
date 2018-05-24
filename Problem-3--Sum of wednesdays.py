import random
import pandas as pd

sum=0
 
#get all business days in year 2015
df = pd.DataFrame({'Date':pd.date_range("2015-01-01", "2015-12-31", freq='B')})

#generate random number for each business day and add to data frame
df['Value']=[random.randint(1, 999) for i in range(df['Date'].count())]

#find sum of values of every wednesday
for index, rows in df.iterrows():
    if(rows['Date'].date().weekday()==2):
        sum=sum+rows['Value']

#print final sum
print('Sum of values for every wednesday : ' +str(sum))

    