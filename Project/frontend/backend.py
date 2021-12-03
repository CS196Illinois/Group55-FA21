from datetime import datetime
from datetime import time
from datetime import timedelta
import ast
import string
import requests
import json

def timeDiff(end_time,start_time):
    timeDiff = end_time - start_time
    return timeDiff


def getSchedule(input):
    

    # crns = {"58056" : ['302 Transportation Building', '09:00AM - 10:50AM', 'M'],
    #     "70107" : ['112 Gregory Hall', '12:00PM - 12:50PM', 'MW'],
    #     "38783" : ['8 ACES Lib, Info & Alum Ctr', '02:00PM - 03:20PM', 'TR'],
    #     "29825" : ['122 Bevier Hall', '10:00AM - 11:20AM', 'MW'],
    #     "29785" : ['4029 Campus Instructional Facility', '10:00AM - 10:50AM', 'MWF'],
    #     "68954" : ['149 National Soybean Res Ctr', '09:00AM - 09:50AM', 'M'],
    #     "62727" : ['325 David Kinley Hall', '01:00PM - 02:50PM', 'MWF']
    # }

    days = {"M" : [], "T" : [], "W": [], "R": [], "F" : []}
    for item in input:
        
        for letter in crns[item][2]:
        #M
            temp = []
            temp.append(crns[item][1])
            temp.append(crns[item][0])
            days[letter].append(temp)
        
    # TODO: find out what this does
    # for key, val in days.items():
    #     for item in val:
    #         if "PM" in item[0]:
    #             new_time = ""
    #             if(int(item[0][:2]) < 12):
    #                 new_start_time = str(int(item[0][:2]) + 12)
    #                 new_end_time = str(int(item[0][10:12]) + 12)
    #                 print(new_start_time, new_end_time)
    #                 new_time = new_start_time + item[0][2:10] + new_end_time + item[0][12:]
    #                 item[0] = new_time

    for key, val in days.items():
        for item in val:
            datetime_object1 = datetime.strptime(item[0][:7], '%I:%M%p')
            datetime_object2 = datetime.strptime(item[0][10:17], '%I:%M%p')
            new_temp = str(datetime_object1)[11:] + " " + str(datetime_object2)[11:]
            item[0] = new_temp
    
    print(days)
    back_to_back = {"M" : [], "T" : [], "W": [], "R": [], "F" : []}
    for key, val in days.items():
        val = sorted(val, key = lambda x: x[0])
        #   print(key, val)
        
        back = []
        for item in val:
            start_end = item[0].split(" ")
            back.append([datetime.strptime(start_end[0], "%H:%M:%S"), datetime.strptime(start_end[1], '%H:%M:%S'), item[1]])

        # [endtime, end_location, start_time_of_next_class, next_locatiion]
        #   print(back)
    
        for n in range(0, len(back)-1):
            temp = []
            threshhold = timedelta(minutes = 20)
            if timeDiff(back[n+1][0], back[n][1]) < threshhold:
            
        #       print(timeDiff(back[n+1][0], back[n][1]))
                temp.append([back[n][2], back[n+1][2]])
        #       print(temp)
            if temp:
                back_to_back[key] += temp

    #print(back_to_back)
    # for i in range (0, len(location_check)):  
    return(back_to_back)

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


# generate_daily_agenda takes the course data and organizes it by day in a dictionary
def generate_daily_agenda(crns):
    days = {"M" : [], "T" : [], "W": [], "R": [], "F" : []}
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
    return days

# convert_times_and_sort_days takes the days dictionary, and converts times after 12 pm to double digits
# it also sorts the classes by the times in ascending order
def convert_times_and_sort_days(days):
    sorted_days = {}
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
    return sorted_days


# returns differece between start and end times
def timeDiff(end_time,start_time):
    timeDiff = end_time - start_time
    return timeDiff



# converts all the times in sorted_days to date time objects and populates classes_datetime
def convert_to_datetime(sorted_days):
    classes_datetime = {"M" : [], "T" : [], "W": [], "R": [], "F" : []}
    datetime_object = datetime.strptime
    for key, val in sorted_days.items():
      for item in val:
        start_end = item[0].split(" ") 
        start = datetime.strptime(start_end[0][:-2], "%H:%M")
        end = datetime.strptime(start_end[2][:-2], "%H:%M")
        classes_datetime[key].append([item[1], start, end]);
    return classes_datetime

# creates a dictionary called back_to_back with the following format:
# {M: [[class 1, class 2, time between class 1 & 2],[class 2, class 3, time between class 2 & 3] ]}
def organize_classes(classes_datetime):
    back_to_back = {"M" : [], "T" : [], "W": [], "R": [], "F" : []}
    for key, val in classes_datetime.items():
        i = 0
        while i < len(val) - 1:
            class_pair = []
            item = val[i]
            following_item = val[i + 1]
            class_pair.append(item[0])
            class_pair.append(item[2])
            class_pair.append(following_item[0])
            class_pair.append(following_item[1])
            class_pair.append((following_item[1] - item[2]))
            back_to_back[key].append(class_pair)
            i = i + 1
    return back_to_back
    
def finalClasses(crnsInput):
    crns = extract_course_data(crnsInput)
    days = generate_daily_agenda(crns)
    sorted_days = convert_times_and_sort_days(days)
    classes_datetime = convert_to_datetime(sorted_days)
    back_to_back = organize_classes(classes_datetime)
    return back_to_back

def parseBackToBack(schedule):
    # schedule is back_to_back
    back_to_back_sliced = {"M" : [], "T" : [], "W": [], "R": [], "F" : []}
    for key, val in schedule.items():
        temp_sliced = []
        for clash in val:
            translation_table = str.maketrans('', '', string.digits)
            temp_sliced.append([clash[0].translate(translation_table).strip() + " UIUC", clash[2].translate(translation_table).strip() + " UIUC", clash[1], clash[3], clash[4]])
        back_to_back_sliced[key] += temp_sliced
    print(back_to_back_sliced)
    return back_to_back_sliced

def sendRequest(back_to_back_sliced):
    for key,val in back_to_back_sliced.items():
        if val:
            for item in val:
                url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + item[0] + "&destinations=" + item[1] + "&key=&mode=walking"
                print(item[0])
                print(item[1])
                print(url)
                payload={}
                headers={}
                response = requests.request("GET", url, headers=headers, data=payload)
                try:
                    print(response.text)
                    print(response.json()["rows"][0]["elements"][0]["duration"]["text"])
                    item.append(response.json()["rows"][0]["elements"][0]["duration"]["text"])
                except KeyError:
                    pass
    return back_to_back_sliced
            #print(response.json()["rows"][0]["elements"][0]["duration"]["text"])

def convertDateTime(datetime_object):
    return datetime_object.strftime("%H:%M")
    
                

def finalOutput(back_to_back_sliced):
    final = {"M" : [], "T" : [], "W": [], "R": [], "F" : []}
    for key, val in back_to_back_sliced.items():
        if val:
            for item in val:
                output = "You have to go from " + item[0][:-5] + " to " + item[1][:-5] + " at " + convertDateTime(item[2]) + " in " + item[5]
                final[key].append(output)
    print(final)
    return final
