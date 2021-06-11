#!/bin/sh
# kitti
unzip -d assets/kitti_semantics/ kitti_semantics.zip
rm kitti_semantics.zip

# tweets
pip install pandas
python py_scripts/sample_csv.py 2000 tweets.csv tweets_sample.csv
mkdir assets/tweets
mv tweets_sample.csv assets/tweets/
rm tweets.csv

# loading into MongoDB
cd server/db
python datasets_loading.py
cd ../../