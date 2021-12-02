#!/usr/bin/env python
# coding: utf-8

import ast
from datetime import datetime
from datetime import time
from datetime import timedelta


# this function extracts metadata about each crn from database.txt
def extract_course_data(crns):
    d_final = {}
    file = open('database.txt', 'r')
    f = file.readlines()
    course_dict = {}
    for c in crns:
        for line in f:
            if (c in line):
                course_dict = ast.literal_eval("{" + line + "}")
                for key, value in course_dict.items():
                    d_final[key] = value
    return d_final


# In[3]:


# generate_daily_agenda takes the course data and organizes it by day in a dictionary
def generate_daily_agenda(days):
    for item in crns.keys():
        if(len(crns[item][2]) > 1):
          for letter in crns[item][2]:
            # Storing time and location in a list 'temp' and appending it to dictionary 'days'
            temp = []
            temp.append(crns[item][1])
            temp.append(crns[item][0])
            days[letter].append(temp)
        else:
            temp = []
            temp.append(crns[item][1])
            temp.append(crns[item][0])
            days[crns[item][2]].append(temp)


# In[4]:


# convert_times_and_sort_days takes the days dictionary, and converts times after 12 pm to double digits
# it also sorts the classes by the times in ascending order
def convert_times_and_sort_days(days, sorted_days):
    for key, val in days.items():
      for item in val:
        if ("PM" in item[0] and (not("AM" in item[0]))):
          new_time = ""
          if(int(item[0][:2]) < 12):
            new_start_time = str(int(item[0][:2]) + 12)
            new_end_time = str(int(item[0][10:12]) + 12)
            #print(new_start_time, new_end_time)
            new_time = new_start_time + item[0][2:10] + new_end_time + item[0][12:]
            item[0] = new_time
        if (item[0].startswith('12') and item[0].rfind('01')!= -1):
            new_end_time = str(int(item[0][10:12]) + 12)
            new_time = new_end_time + item[0][12:]
            item[0] = item[0][0:10] + new_time
    for key, val in days.items():
      val = sorted(val, key=lambda x: x[0])
      sorted_days[key] = val


# returns differece between start and end times
def timeDiff(end_time,start_time):
    timeDiff = end_time - start_time
    return timeDiff


# converts all the times in sorted_days to date time objects and populates classes_datetime
def convert_to_datetime(classes_datetime):
    datetime_object = datetime.strptime
    for key, val in sorted_days.items():
      for item in val:
        start_end = item[0].split(" ") 
        start = datetime.strptime(start_end[0][:-2], "%H:%M")
        end = datetime.strptime(start_end[2][:-2], "%H:%M")
        classes_datetime[key].append([item[1], start, end]);


# creates a dictionary called back_to_back with the following format:
# {M: [[class 1, class 2, time between class 1 & 2],[class 2, class 3, time between class 2 & 3] ]}
def organize_classes(back_to_back, classes_datetime):
    for key, val in classes_datetime.items():
        i = 0
        while i < len(val) - 1:
            class_pair = []
            item = val[i]
            following_item = val[i + 1]
            class_pair.append(item[0])
            class_pair.append(following_item[0])
            class_pair.append((following_item[1] - item[2]))
            back_to_back[key].append(class_pair)
            i = i + 1


# In[8]:


crnsInput = {'59821', '75111', '73308', '75272', '48924', '70667', '62829', '57971'}
crns = extract_course_data(crnsInput)


# In[9]:


crns


# In[10]:


days = {"M" : [], "T" : [], "W": [], "R": [], "F" : []}
generate_daily_agenda(days)


# In[11]:


days


# In[12]:


sorted_days = {}
convert_times_and_sort_days(days, sorted_days)


# In[13]:


sorted_days


# In[14]:


classes_datetime = {"M" : [], "T" : [], "W": [], "R": [], "F" : []}
convert_to_datetime(classes_datetime)


# In[15]:


classes_datetime


# In[16]:


back_to_back = {"M" : [], "T" : [], "W": [], "R": [], "F" : []}
organize_classes(back_to_back, classes_datetime)


# In[17]:


back_to_back


# In[ ]:




