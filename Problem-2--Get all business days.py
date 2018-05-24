import random
import pandas as pd
 
#get all business days in year 2015
df = pd.DataFrame({'Date':pd.date_range("2015-01-01", "2015-12-31", freq='B')})

#generate random number for each business day and add to data frame
df['Value']=[random.randint(1, 999) for i in range(df['Date'].count())]

#print dataframe
df
    
