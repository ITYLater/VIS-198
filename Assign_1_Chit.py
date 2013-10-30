# VIS 198 Assignment 1 - Lawrence Chit
# NOT COMPLETE NOT COMPLETE NOT COMPLETE NOT COMPLETE NOT COMPLETE NOT COMPLETENOT COMPLETE NOT COMPLETE NOT COMPLETE

iimport json
import numpy

file1 = "/Users/AUNG/Documents/School/VIS 198/Assignment 1/json1"
file2 = "/Users/AUNG/Documents/School/VIS 198/Assignment 1/json2"
file3 = "/Users/AUNG/Documents/School/VIS 198/Assignment 1/json3"
file4 = "/Users/AUNG/Documents/School/VIS 198/Assignment 1/json4"

# Convert json files to dictionaries
json1_file = open(file1)
json1_string = json1_file.read()
json1_data = json.loads(json1_string)[0]
#print json1_data['datapoints'][0], " by: ", json1_data['target']  

json2_file = open(file2)
json2_string = json2_file.read()
json2_data = json.loads(json2_string)[0]
#print json2_data['datapoints'][0], "by: ", json2_data['target']

json3_file = open(file3)
json3_string = json3_file.read()
json3_data = json.loads(json3_string)[0]
#print json3_data['datapoints'][0], "by: ", json3_data['target']

json4_file = open(file4)
json4_string = json4_file.read()
json4_data = json.loads(json4_string)[0]
#print json4_data['datapoints'][0], "by: ", json4_data['target']

json1_writes = numpy.array(json1_data['datapoints'])
json2_writes = numpy.array(json2_data['datapoints'])
json3_writes = numpy.array(json3_data['datapoints'])
json4_writes = numpy.array(json4_data['datapoints'])

avg1_wpm = json1_writes[0:7,0].mean()
avg2_wpm = json2_writes[0:7,0].mean()
avg3_wpm = json3_writes[0:7,0].mean()
avg4_wpm = json4_writes[0:7,0].mean()

print "average writes per minute: ", avg1_wpm, " from: ", json1_data['target']
print "average writes per minute: ", avg2_wpm, " from: ", json2_data['target']
print "average writes per minute: ", avg3_wpm, " from: ", json3_data['target']
print "average writes per minute: ", avg4_wpm, " from: ", json4_data['target']

avg1_wph = json1_writes[0:49,0].mean()
avg2_wph = json2_writes[0:49,0].mean()
avg3_wph = json3_writes[49:98,0].mean()
avg4_wph = json4_writes[41:89,0].mean()

print '\n'

print "average writes per hour: ", avg1_wph, " from: ", json1_data['target']
print "average writes per hour: ", avg2_wph, " from: ", json2_data['target']
print "average writes per hour: ", avg3_wph, " from: ", json3_data['target']
print "average writes per hour: ", avg4_wph, " from: ", json4_data['target']

avg1_wpd = json1_writes[0:343,0].mean()
print avg1_wpd

#Problem encountered. Key 'datapoints' includes string "None"

type(json2_writes) #Type is ndarray, how to manipulate?

#Will not work, because 0 is still read in as a string
#json1_string.replace("None", "0")
#json2_string.replace("None", "0")
#json3_string.replace("None", "0")
#json4_string.replace("None", "0")




