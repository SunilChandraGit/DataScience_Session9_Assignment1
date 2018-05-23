import pandas as pd

#create initial given dataframe
df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})

#initialize a list for adding distance to 0
Y=[]

#variable to keep track of distance to nearest zero
inc=0

#loop to get distance from 0 for each element and append to Y
for i in range(10):
    if(df['X'][i]==0):
        inc=0
    Y.append(inc)
    inc=inc+1

#add Y as Y column in existing dataframe
df['Y']=Y

#print dataframe
df