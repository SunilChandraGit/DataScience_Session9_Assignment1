import random
import pandas as pd
import calendar

sum=0
compMonth=1
count=0
 
#get all business days in year 2015
df = pd.DataFrame({'Date':pd.date_range("2015-01-01", "2015-12-31", freq='B')})

#generate random number for each business day and add to data frame
df['Value']=[random.randint(1, 999) for i in range(df['Date'].count())]

df['max'] = df.groupby(df['Date'].dt.quarter)['Value'].transform('max')

#find max in every quarter
for index, rows in df.iterrows():
    month=rows['Date'].date().month
    #print(str(month)+'\t'+str(compMonth)+'-'+str(count))
    if(month-compMonth==3 or (month==12 and count==23)):
        print('Quarter '+str(compMonth)+' '+str(sum))
        sum=rows['Value']
        compMonth=month
        count=1
    else:
        if(rows['Value']>sum):
            sum=rows['Value']
        count=count+1


    