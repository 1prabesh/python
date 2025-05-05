# %%
import pandas as pd
import glob

# %%
# to see if csv is present in that folder
for csv in glob.glob('*.csv'):
    print(csv)

# %%
# function to read csv on loop
def read_csv(file_to_read):
    return pd.read_csv(file_to_read)

#function to read and merg all csv at once
def extract_ndread():
    newdataframe=[]
    for csvs in glob.glob('*.csv'):
        print(f'working with {csvs}')
        df=read_csv(csvs)
        newdataframe.append(df)
    combinedata=pd.concat(newdataframe,ignore_index=True)
    return combinedata
    
file=extract_ndread()
print(file)

# %%
newfile=file.to_excel('combinedfile.xlsx')

# %%



