#%%
import json
import glob
import csv

from mongoengine import (
    connect,
)

from schemas import Dataset, Image, Tweet
#%%
connect(host="mongodb://root:SGG@localhost:27017/demo?authSource=admin")

# %%
tweets_ds = Dataset(
    name="tweets",
    content_type="TEXT",
    message="Please mark the tweet as positive/negative/neutral",
    label_type="CLASS",
    options=[
	  "Positive",
	  "Negative",
	  "Neutral"
    ]
).save()
#%%

with open("assets/tweets/tweets_sample.csv", newline='') as csvfile:
  tweets = csv.reader(csvfile) #, delimiter=' ', quotechar='|')
  for i, row in enumerate(tweets):
    t = Tweet(
      _id=i,
      dataset="tweets",
      tweet=row[5],
    ).save()
   
#%%
unsplash_ds = Dataset(
    name="unsplash",
    content_type="IMAGE",
    message="Please select the label that best describes what is being captured in this photograph.",
    label_type="CLASS",
    options=[
        "Animals (ground)",
	    "Birds",
        "Plants",
        "Sky",
        "Water",
	    "Mountains",
	    "Desert",
	    "Ice",
        "Landscape",
        "None / Unknown"
    ]
).save()

with open("assets/unsplash/unsplash.json") as f:
    images = json.load(f)

for img in images:
    Image(
        dataset=unsplash_ds,
        url=img["url"]
    ).save()

#%%
kitti_ds = Dataset(
    name="kitti_semantics",
    content_type="IMAGE",
    message="Please select the label that best describes what is being captured in this photograph.",
    label_type="GRID",
    options=[
        "Car",
        "Van",
        "Truck",
        "People",
        "Bike",
        "Motorbike",
        "Pedestrian crossing",
        "Monuments (external)",
    ]
).save()

raw = glob.glob("assets/kitti_semantics/*.png")
kitti_urls = [url[3:] for url in raw]
kitti_urls

#%%
for url in kitti_urls:
    Image(
        dataset=kitti_ds,
        url=url
    ).save()