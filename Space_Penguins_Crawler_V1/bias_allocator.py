import json
import re

with open('master_list.json', 'r') as file:
    master_list = json.load(file)


def leaning_reconv(leaning):
    if leaning < -8:
        return "Left"
    elif leaning < -4:
        return "Center left"
    elif leaning <= 4:
        return "Center"
    elif leaning <= 8:
        return "Center right"
    else:
        return "Right"


def reliability_reconv(reliability):
    if reliability < 3:
        return "Low"
    elif reliability < 7:
        return "Mixed"
    else:
        return "High"


def assess_url(url):
    clean_url = re.search(r'(?:https?:\/\/)?(?:www\.)?(.+?)\/?$', url).group(1)
    matches = []
    for sublist in master_list:
        for item in master_list[sublist]:
            if item["url"] == clean_url:
                matches.append(item)
    out = {"reliability": [], "leaning": []}
    if len(matches) == 1:
        if "reliability" in matches[0].keys():
            out["reliability"] = [{"rating": reliability_reconv(matches[0]["reliability"]),
                                   "source": matches[0]["source"]}]
        if "leaning" in matches[0].keys():
            out["leaning"] = [{"rating": leaning_reconv(matches[0]["leaning"]),
                               "source": matches[0]["source"]}]
    if len(matches) > 1:
        reliability_count = 0
        reliability_total = 0
        leaning_count = 0
        leaning_total = 0
        for item in matches:
            if "reliability" in item.keys():
                reliability_count += 1
                reliability_total += item["reliability"]
                out["reliability"].append({"rating": reliability_reconv(item["reliability"]),
                                           "source": item["source"]})
            if "leaning" in item.keys():
                leaning_count += 1
                leaning_total += item["leaning"]
                out["leaning"].append({"rating": leaning_reconv(item["leaning"]), "source": item["source"]})
        if reliability_count > 1:
            out["reliability"].append({"rating": reliability_reconv(reliability_total / reliability_count),
                                       "source": "MEAN_VALUE"})
        if leaning_count > 1:
            out["leaning"].append({"rating": leaning_reconv(leaning_total / leaning_count), "source": "MEAN_VALUE"})
    return out

list_handles = {}

import csv

with open('sample2.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    for record in reader:
        handle, url = record[0], record[1]
        list_handles[handle] = url

def assess_handle(handle):
    return assess_url(list_handles[handle])