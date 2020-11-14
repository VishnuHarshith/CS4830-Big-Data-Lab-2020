
#!/usr/bin/env python

import pyspark
import sys

if len(sys.argv) != 3:
  raise Exception("Exactly 2 arguments are required: <inputUri> <outputUri>")

inputUri= sys.argv[1]
outputUri= sys.argv[2]

def transform_it(data):
	date, time, ID = data.split(" ")
	hr, min, sec = time.split(":")
	hr = int(hr)
	if hr in range(0,7):
		return '0-6'
	elif hr in range(7,13):
		return '6-12'
	elif hr in range(13,19):
		return '12-18'
	elif hr in range(19,25):
		return '18-24'
sc = pyspark.SparkContext()
interval = sc.textFile(sys.argv[1])
interval_1 = interval.Map(transform_it)
interval_2 = interval_1.map(lambda time_gap: (time_gap, 1)).reduceByKey(lambda count1, count2: count1 + count2)
interval_2.saveAsTextFile(sys.argv[2])
