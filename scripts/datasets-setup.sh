#!/bin/sh
<<<<<<< HEAD
# preparing `kitti` dataset
unzip -d assets/kitti_semantics/ kitti_semantics.zip
rm kitti_semantics.zip

# preparing `tweets` dataset
=======
# kitti
unzip -d assets/kitti_semantics/ kitti_semantics.zip
rm kitti_semantics.zip

# tweets
>>>>>>> datasets-2
pip install pandas
python py_scripts/sample_csv.py 2000 tweets.csv tweets_sample.csv
mkdir assets/tweets
mv tweets_sample.csv assets/tweets/
rm tweets.csv

<<<<<<< HEAD
# loading into `MongoDB`
pip install mongoengine
python server/db/datasets_loading.py
=======
# loading into MongoDB
cd server/db
python datasets_loading.py
cd ../../
>>>>>>> datasets-2
