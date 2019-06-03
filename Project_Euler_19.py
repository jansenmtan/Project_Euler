#-*-coding:utf8;-*-
#qpy:3
#qpy:console
from time import sleep
months = {0:(31,"January"),
          1:(28,"February"),
          2:(31,"March"),
          3:(30,"April"),
          4:(31,"May"),
          5:(30,"June"),
          6:(31,"July"),
          7:(31,"August"),
          8:(30,"September"),
          9:(31,"October"),
          10:(30,"November"),
          11:(31,"December"),
          }
weekdays = {0:"Monday",
            1:"Tuesday",
            2:"Wednesday",
            3:"Thursday",
            4:"Friday",
            5:"Saturday",
            6:"Sunday",
            }

#date is formatted as [year,month,day]
date = [1901,1,1]
end_date = [2000,12,31]
weekday = 1
count = 0

flag = 0
while True:
    for month in range(date[1] - 1,12):
        if all([date[0] % 4 == 0,
                date[0] % 400 != 0,
                month % 12 == 1,]):
            days_in_month = [i for i in range(date[2] + 1,30)]
        else:
            days_in_month = [i for i in range(date[2] + 1,months[month][0] + 1)]
        #print(days_in_month)
        #sleep(1)
        for day in days_in_month:
            if date[2] == 1 and weekday % 7 == 6:
                count += 1
            date[2] = day
            weekday += 1
            #print(date)
            if date == end_date:
                flag = 1
                break
        
        date[2] = 1
        weekday += 1
        
        if flag == 1:
            break
        
        date[1] = month + 2
    
    if flag == 1:
        break
    
    date[0] += 1
    date[1] = 1
    date[2] = 1
    weekday += 1
print(count)