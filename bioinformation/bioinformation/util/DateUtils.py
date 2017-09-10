# coding:utf-8
import time;
def getDate():
    year=time.localtime().tm_year;
    month1=time.localtime().tm_mon;
    day1=time.localtime().tm_mday;
    month=""
    day=""
    if month1<10:
        month="0"+str(month1);
    else:
        month=str(month1);
    if day1<10:
        day="0"+str(day1);
    else:
        day=str(day1);
    return str(year)+"-"+month+"-"+day;
    