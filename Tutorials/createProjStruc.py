from datetime import date, timedelta
import sys

sdate = date(2021, 1, 4)   # start date
edate = date(2021, 2, 1)   # end date

delta = edate - sdate       # as timedelta

students = [
"Adjaye",
"Francesco",
"Jonas",
"Juliette",
"Marco",
"Timon",
"Yogi"
]


def printProgressReport():
    f = open("ProgressReport_CRAPy.md", "w")

    f.write("# Progress report of the CRAPy project\n\n")

    for i in range(delta.days + 1):
        day = sdate + timedelta(days=i)
        f.write(day.strftime("\n## Progress: %A %d %B, %Y")+"\n")
        for name in students:
            f.write("\n#### " + name +":\n\n")

    f.close()

def printProgressReportContent():
    f = open("ProgressReport_Table_CRAPy.md", "w")

    f.write("# Project Daily Progress Report\n\n## Table of Content\n\n")


    for i in range(delta.days + 1):
        day = sdate + timedelta(days=i)
        f.write("[**Daily Report - {} : {}**](https://github.com/Jonastjep/CRAPy/blob/master/ProgressReport_CRAPy.md#progress-{}-{}-{}-{})\n\n".format(day.strftime("%d/%m/%Y"),day.strftime("%A %d %B, %Y"),day.strftime("%A").lower(),day.strftime("%d"),day.strftime("%B").lower(),day.strftime("%Y")))

    f.close()
