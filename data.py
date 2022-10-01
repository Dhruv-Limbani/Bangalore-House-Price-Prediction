import json
with open("columns.json",'rb') as f:
    locs = json.load(f)

locations = locs['locations']
print(locations,len(locations))