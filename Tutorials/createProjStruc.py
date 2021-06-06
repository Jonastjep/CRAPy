from datetime import date, timedelta
import sys

sdate = date(2021, 6, 7)   # start date
edate = date(2021, 6, 30)   # end date

delta = edate - sdate       # as timedelta

students = [
"Chris",
"Gabriel",
"Justus",
"Linus",
"Lucas",
"Marc",
"Milan",
"Timon",
"Xavier"
]


def printProgressReport():
    f = open("PROGRESS:REPORT.md", "w")

    f.write("# Progress report of the CRAPy project\n\n")

    for i in range(delta.days + 1):
        day = sdate + timedelta(days=i)
        f.write(day.strftime("\n## Progress: %A %d %B, %Y")+"\n")
        for name in students:
            f.write("\n#### " + name +":\n\n")

    f.close()

def printProgressReportContent():
    f = open("PROGRESS:REPORT:TABLE.md", "w")

    f.write("# Project Daily Progress Report\n\n## Table of Content\n\n")


    for i in range(delta.days + 1):
        day = sdate + timedelta(days=i)
        f.write("[**Daily Report - {} : {}**](https://github.com/Jonastjep/CRAPy/blob/master/PROGRESS:REPORT.md#progress-{}-{}-{}-{})\n\n".format(day.strftime("%d/%m/%Y"),day.strftime("%A %d %B, %Y"),day.strftime("%A").lower(),day.strftime("%d"),day.strftime("%B").lower(),day.strftime("%Y")))

    f.close()
