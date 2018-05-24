import random
import pandas as pd
import calendar
import datetime

#function to check if its months last business day
def is_business_day_end(date):
    
    #check if next day is month end date and a non-weekday
    enddate = pd.to_datetime(date) + pd.DateOffset(days=1)
    if(date.weekday()==4 and enddate.is_month_end and (enddate.weekday()==5 or enddate.weekday()==6)):
        return True
    
    #check if its month end day 
    if(date.is_month_end):
        return True
    
    return False

sum=0
count=0
compMonth=1

months=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
 
#get all business days in year 2015
df = pd.DataFrame({'Date':pd.date_range("2015-01-01", "2015-12-31", freq='B')})

#generate random number for each business day and add to data frame
df['Value']=[random.randint(1, 999) for i in range(df['Date'].count())]

print('Month\t\t\tAverage\n'+'-'*30)

#find sum of values of every month
for index, rows in df.iterrows():
    month=rows['Date'].date().month
    
    sum=sum+rows['Value']
    count=count+1
    
    if(is_business_day_end(rows['Date'])):
        print(months[rows['Date'].date().month-1].ljust(10)+'\t\t'+str(round(sum/count, 2)).ljust(10))
        sum=0
        count=0
        


    
