# VIS 198 Assignment 1 - Lawrence Chit
# NOT COMPLETE NOT COMPLETE NOT COMPLETE NOT COMPLETE NOT COMPLETE NOT COMPLETENOT COMPLETE NOT COMPLETE NOT COMPLETE

import json
import numpy

file1 = "/Users/AUNG/Documents/School/VIS 198/json1"
file2 = "/Users/AUNG/Documents/School/VIS 198/json2"
file3 = "/Users/AUNG/Documents/School/VIS 198/json3"
file4 = "/Users/AUNG/Documents/School/VIS 198/json4"

# Convert json files to dictionaries
json1_file = open(file1)
json1_string = json1_file.read()
json1_data = json.loads(json1_string)[0]
print(json1_data['datapoints'][0] + " target: " + json1_data['target'])


json2_file = open(file2)
json2_string = json2_file.read()
json2_data = json.loads(json2_string)[0]
print(json2_data['datapoints'][0] + " target: " + json2_data['target'])

json3_file = open(file3)
json3_string = json3_file.read()
json3_data = json.loads(json3_string)[0]
print(json3_data['datapoints'][0] + " target: " + json3_data['target'])

json4_file = open(file4)
json4_string = json4_file.read()
json4_data = json.loads(json4_string)[0]
print(json4_data['datapoints'][0] + " target: " + json4_data['target'])




