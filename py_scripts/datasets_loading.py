#%%
import json
import glob
import csv

from mongoengine import (
    connect,
    Document,
    StringField,
    IntField,
    ListField,
    ReferenceField,
    DictField
)

#%%
connect(host="mongodb://root:SGG@localhost:27017/demo?authSource=admin")

class Dataset(Document):
    name = StringField(primary_key=True)
    content_type = StringField(required=True, choices=["IMAGE", "TEXT"])
    message = StringField(required=True)
    label_type = StringField(required=True, choices=["CLASS", "LABEL", "GRID"])
    options = ListField(StringField())


class Image(Document):
    dataset = ReferenceField(Dataset, required=True)
    url = StringField(required=True, unique_with="dataset")
    labels = DictField(StringField)

class Tweet(Document):
    _id = IntField(primary_key=True)
    dataset = ReferenceField(Dataset, required=True)
    tweet = StringField(required=True) #, unique_with="dataset")
    labels = DictField(StringField)


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

with open("../assets/tweets/tweets.csv", newline='') as csvfile:
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

with open("../assets/unsplash/unsplash.json") as f:
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

raw = glob.glob("../assets/kitti_semantics/*.png")
kitti_urls = [url[3:] for url in raw]
kitti_urls

#%%
for url in kitti_urls:
    Image(
        dataset=kitti_ds,
        url=url
    ).save()