# simple script to sample rows from a CSV file
# Example:
# python sample_csv.py 1000 mydata.csv mydatasample.csv
#%%
import pandas as pd
import sys

#%%
n = int(sys.argv[1])
source = sys.argv[2]
dest = sys.argv[3]

tweets = pd.read_csv(source)
tweets.sample(n).to_csv(dest)