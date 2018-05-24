import random
import pandas as pd
import calendar

max=0
maxDate='2015-01-01'
quarter=1

#function to check whether given date is quarters end date or not
def is_business_quarter_end(date):
    enddate = pd.to_datetime(date) + pd.DateOffset(days=1)
    
    #check if next day is quarter end date and a non-weekday
    if(date.weekday()==4 and enddate.is_quarter_end and (enddate.weekday()==5 or enddate.weekday()==6)):
        return True
    
    #check if its quarter end
    if(date.is_quarter_end):
        return True
    
    return False
 
#get all business days in year 2015
df = pd.DataFrame({'Date':pd.date_range("2015-01-01", "2015-12-31", freq='B')})

#generate random number for each business day and add to data frame
df['Value']=[random.randint(1, 999) for i in range(df['Date'].count())]

#print the header
print('Quarter\tDate\t\t\tMaxValue\n'+'-'*40)

#find max in every quarter
for index, rows in df.iterrows():
    
    if(rows['Value']>max):
        max=rows['Value']
        maxDate=rows['Date']
    
    if(is_business_quarter_end(rows['Date'])):
        print(str(quarter)+'\t'+str(maxDate)+'\t'+str(max))
        max=0
        quarter=quarter+1
    
