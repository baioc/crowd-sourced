#%%
import json
import glob
import csv

#%%
glob.glob("../assets/kitti_semantics/*.png")
#TODO: parse strings and load into MongoDB

# %%
# TODO: directly load into MongoDB, instead of printing
with open("../assets/tweets/tweets.csv", newline='') as csvfile:
  tweets = csv.reader(csvfile) #, delimiter=' ', quotechar='|')
  for row in tweets:
    #fields = row.split(",")
    print(row[5])
   
#%%
with open("../assets/unsplash/unsplash.json") as f:
    d = json.load(f)
    print(d)
#TODO: load `d` into MongoDb

# %%
from pymongo import MongoClient

mongo = MongoClient("mongodb://root:SGG@mongo:27017")

db = mongo["demo"]

coll = db["unsplash"]

#%%
x = coll.insert_many(d)
# %%