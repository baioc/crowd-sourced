from mongoengine import connect
import json
import os

connect(host="mongodb://root:SGG@localhost:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false")

from models.instance import Instance

folder_path_to_json = f"{os.path.abspath('.')}/shared/json/Tripix/"

json_files = os.listdir(folder_path_to_json)

for json_file in json_files:
    with open(f'{folder_path_to_json}/{json_file}', mode='r', encoding='utf-8') as file:
        data = json.loads(file.read())
        instance = Instance(dataset=data["dataset"], 
            url=data["url"], 
            labels=data["labels"], 
            text=data["text"], 
            text_url=data["text_url"]
        )
        instance.save()