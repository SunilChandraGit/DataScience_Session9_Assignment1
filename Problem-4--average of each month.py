import random
import pandas as pd
import calendar
import datetime

sum=0
count=0
compMonth=1
 
#get all business days in year 2015
df = pd.DataFrame({'Date':pd.date_range("2015-01-01", "2015-12-31", freq='B')})

#generate random number for each business day and add to data frame
df['Value']=[random.randint(1, 999) for i in range(df['Date'].count())]

print('Month\tAverage\n'+'-'*15)

#find sum of values of every month
for index, rows in df.iterrows():
    month=rows['Date'].date().month
    if(month==compMonth):
        sum=sum+rows['Value']
        count=count+1
    else:
        print(str(rows['Date'].date().month-1)+'\t'+str(sum/count))
        sum=rows['Value']
        count=1
        compMonth=month
        
print(str(rows['Date'].date().month)+'\t'+str(sum/count))


    