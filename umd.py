#!/usr/bin/env python

import urllib2
import json
import time

url = []
days = ["MW", "TuTh", "F", "MWF"]
time = time.strftime('%I%p')
building = 'CSI'
room = '1115'


bldg_ans = (raw_input("Default building is CSI. Do you want to change this? (y/n) ")).lower()
if bldg_ans == 'y':
    building = (raw_input("Enter new 3-letter building code. ")).upper()
room_ans = (raw_input("Default room is 1115. Do you want to change this? (y/n) ")).lower()
if room_ans == 'y':
    room = (raw_input("Enter new room number. ")).upper()

url.append('http://api.umd.io/v0/courses/sections?')        
if building:
    url.append('building=')
    url.append(building)
if room:
    url.append('&room=')
    url.append(room)
if time:
    url.append('&start_time>=')
    url.append(time)
final = ''.join(url) 

print(final)
json_obj = urllib2.urlopen(final)
sections = json.load(json_obj)

#print(data)
for section in sections:
    print section['instructors'];
