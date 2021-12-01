from datetime import datetime
from datetime import time
from datetime import timedelta

def timeDiff(end_time,start_time):
    timeDiff = end_time - start_time
    return timeDiff


def getSchedule(input):
    

    crns = {"58056" : ['302 Transportation Building', '09:00AM - 10:50AM', 'M'],
        "70107" : ['112 Gregory Hall', '12:00PM - 12:50PM', 'MW'],
        "38783" : ['8 ACES Lib, Info & Alum Ctr', '02:00PM - 03:20PM', 'TR'],
        "29825" : ['122 Bevier Hall', '10:00AM - 11:20AM', 'MW'],
        "29785" : ['4029 Campus Instructional Facility', '10:00AM - 10:50AM', 'MWF'],
        "68954" : ['149 National Soybean Res Ctr', '09:00AM - 09:50AM', 'M'],
        "62727" : ['325 David Kinley Hall', '01:00PM - 02:50PM', 'MWF']
    }

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

## TODO
def parseBackToBack(schedule):
    pass

def getTravelTime(parsed_):
    pass 