#!C:\Program Files\Python36\python.exe
import os
import cgi
import random
from htmlMethods import *
from database import *

form = cgi.FieldStorage()

htmlMethods.printHeader("Search Result")
cityCount = Database().findCityCount()
cityList = Database().getCities()
positionList = Database().searchKeywordInternshipPositions("an")

counter = 0
htmlMethods.printTableHeader()
for city in cityList:
    checkFlag = 0
    cityName = city[1]
    print("""
    <body>

    <h2>%s</h2>

    <table>
    <tr>
        <th>Software Company</th>
        <th>Position Name</th>
        <th>Description</th>
        <th>Expectations</th>
        <th>Deadline</th>
    </tr>""" % cityName)

    for position in positionList:
        if(position[6] == cityName):
            print("""<tr>""")
            print('<td><a href="companydetails.py?company='+position[0]+'">'+position[1]+'</a></td>')
            print("""<td>%s</td>""" % position[2])
            print("""<td>%s</td>""" % position[3])
            print("""<td>%s</td>""" % position[4])
            print("""<td>%s</td>""" % position[5])
            print("""<tr>""")
            checkFlag = 1
    if not checkFlag:
        print("""<tr>""")
        print("""<td>No Position Available</td>""" )
        print("""<td> </td>""" )
        print("""<td> </td>""" )
        print("""<td> </td>""" )
        print("""<td> </td>""" )
        print("""<tr>""")
    print("""
    </table>

    </body>""")
            
print("""<input type="submit" value="Main Page" onclick="window.location='index.py';"/>""")

htmlMethods.endBodyAndHtml()

