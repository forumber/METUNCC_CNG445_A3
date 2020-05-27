#!C:\Program Files\Python36\python.exe
import os
import cgi
import random
import http.cookies as Cookie  
from htmlMethods import *
from database import *
#from searchKeywordMain import keywordToSearch
form = cgi.FieldStorage()
keywordToSearch = "Test Position"
htmlMethods.printHeader("PreviousPositions")
cityCount = Database().findCityCount()[0][0]
cityList = Database().getCities()
positionList = Database().searchKeywordInternshipPositions(keywordToSearch)

counter = 0
print("""<head>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>""")
while(counter < cityCount):
    checkFlag = 0
    cityName = cityList[counter][0]
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
        if(position[5] == cityName):
            print("""<tr>""")
            print("""<td>%s</td>""" % position[0])
            print("""<td>%s</td>""" % position[1])
            print("""<td>%s</td>""" % position[2])
            print("""<td>%s</td>""" % position[3])
            print("""<td>%s</td>""" % position[4])
            print("""<tr>""")
            checkFlag = 1
    if(checkFlag<1):
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
    counter+=1
            
print("""
    <input type="submit" value="Go Back" onclick="window.location='searchKeywordMain.py';"/>""")
print("""
    <input type="submit" value="Main Menu" onclick="window.location='index.py';"/>""")

htmlMethods.endBodyAndHtml()

