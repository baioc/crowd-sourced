#%%
import requests
import json
import os
# %%
# Params
# for info on available params:
# https://unsplash.com/documentation#get-a-topic
topic = "nature"
n_images = 100
orientation = "landscape"
order_by = "popular"

# access key
key = "Ye_-eyGujb_ub1gSiT7KjHKO516Sq_jW7QVCvqYgbjM"

# api-endpoint
URL = f"https://api.unsplash.com/topics/{topic}/photos"
  
# defining a params dict for the parameters to be sent to the API
PARAMS = {
	"per_page": n_images,
	"orientation": orientation,
	"order_by": order_by,
	"client_id": key,
}
  
# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)
  
# extracting data in json format
data = r.json()
data = [{
	"id": sample["id"],
	"url": sample["urls"]["regular"]
	} for sample in data
]
  
#%%  
filename = "assets/unsplash/unsplash.json"
os.makedirs(os.path.dirname(filename), exist_ok=True)

with open(filename, 'w') as f:
    json.dump(data, f)