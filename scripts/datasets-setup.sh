#!/bin/sh
# preparing `kitti` dataset
unzip -d assets/kitti_semantics/ kitti_semantics.zip
rm kitti_semantics.zip

# preparing `tweets` dataset
pip install pandas
python py_scripts/sample_csv.py 2000 tweets.csv tweets_sample.csv
mkdir assets/tweets
mv tweets_sample.csv assets/tweets/
rm tweets.csv

# loading into `MongoDB`
pip install mongoengine
python server/db/datasets_loading.py