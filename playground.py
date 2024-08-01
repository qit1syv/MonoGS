import json

path = "/home/curobot/dev_lib/MonoGS/result/perc_segment-anything-2/2024-07-31-14-20-41/plot/trj_final.json"

with open(path, "r") as f:
    data = json.load(f)
print(len(data["trj_id"]))