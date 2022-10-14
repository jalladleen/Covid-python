#!/usr/bin/env python

'''
dictionary_array_example.py
  Author(s): Leen Al-Jallad (1154729), Hamna Ahmed (1148915), Ashmethaa Arulanantham(1072965)

  Project: Milestone  Script (Iteration 0)
  Date of Last Update: March 13, 2021.

  Functional Summary
      dictionary_array_example.py demonstrates how we can
      use a "dictionary" to look up indices by name

     Commandline Parameters: 1
        argv[0] = data file
'''
#python Question2.py conposcovidloc.csv response_framework.csv

#Producing the txt: python Question2.py conposcovidloc.csv response_framework.csv  >  Question2.txt

#Running the graphOne: python plotQuestion2.py Question2.txt graphOne.pdf

#
#   Packages and modules
#

# The 'sys' module gives us access to system tools, including the
# command line parameters, as well as standard input, output and error
import sys

import urllib.request


#
# Define any "constants" for the file here.
# Names of constants should be in UPPER_CASE.
#
# This is a dictionary -- a data structure that associates
# values (in this case integers) with names.


def main(argv):
    '''
    Load a data file and print out the columns matching the selected
    indices
    '''
    PHU = "Peel_Public_Health" #the user needs to indicate the city's name as the second line argument 


    url = 'https://data.ontario.ca/api/3/action/datastore_search?q='+PHU+'&resource_id=ce9f043d-f0d4-40f0-9b96-4c8a83ded3f6'
    with urllib.request.urlopen(url) as url:
      fileobjstatus = url.read()

    listStatus = str(fileobjstatus).split("[")
    newListStatus = listStatus[2].split('"')

    row_number_zone = 0 # Variable for counting the number of rows that indicate the Ontario COVID-19 zones in the file
    row_number_case = 0 # Variable for counting the number of rows  that indicate the Confirmed positive cases of COVID19 in Ontario in the file
    listZone = [] # This list that will contain the zone/state, the starting date of the status and the ending date of that status
    listCase = [] # This list that will contain the positive cases in that zone 
    
    # This will be looping through the data to read the zones in the region and identify the starting and the ending date of that status. 
    for row in range(len(newListStatus)):
        if newListStatus[row] == "Status_PHU":
            listZone.append([newListStatus[row + 6], newListStatus[row + 10], newListStatus[row + 2]])
            row_number_zone += 1

    # This will be looping through the data to read the cases in the region.    
    for row in range(len(newListCases)):
        if newListCases[row] == "Case_Reported_Date":
            listCase.append(newListCases[row + 2])
            row_number_case += 1
    print(listCase)
    listCase.sort() #sort the list in alpha order
    
    new_row_number_zone = row_number_zone
    for row in range(row_number_zone):
      earliestCommonDate = ""
      oldestCommonDate = ""
      for rowTwo in range(row_number_zone):
        if(row != rowTwo):
          if(listZone[row][0] < listZone[rowTwo][0]) and (listZone[row][1] > listZone[rowTwo][1]):
            if(listZone[rowTwo][2] != listZone[row][2]):
              listZone[rowTwo][2] = listZone[rowTwo][2] + " and " + listZone[row][2]

            if(earliestCommonDate == ""):
              earliestCommonDate = listZone[rowTwo][0]
            elif(earliestCommonDate > listZone[rowTwo][0]):
              earliestCommonDate = listZone[rowTwo][0]
          
            if(oldestCommonDate == ""):
              oldestCommonDate = listZone[rowTwo][1]
            elif(oldestCommonDate < listZone[rowTwo][1]):
              oldestCommonDate = listZone[rowTwo][1]
      
      if(earliestCommonDate != ""):
        Date = earliestCommonDate.split('-')
        Day = Date[2].split('T')
        Day[0] = int(Day[0]) - 1
        tempLastDay = listZone[row][1]
        listZone[row][1] = Date[0] + "-" + Date[1] + "-" + str(Day[0]) + "T" + Day[1]
      
      if(oldestCommonDate != ""):
        Date = oldestCommonDate.split('-')
        Day = Date[2].split('T')
        Day[0] = int(Day[0]) + 1
        if(Day[0] < 10):
          newDate = Date[0] + "-" + Date[1] + "-0" + str(Day[0]) + "T" + Day[1]
        else:
          newDate = Date[0] + "-" + Date[1] + "-" + str(Day[0]) + "T" + Day[1]
        listZone.append([newDate, tempLastDay, listZone[row][2]])
        new_row_number_zone = new_row_number_zone + 1

        
    #GOOD CODE   
    zoneCases = []

    for rowZone in range(new_row_number_zone):
      tempZoneStartDate = listZone[rowZone][0].split('-')
      tempZoneEndDate = listZone[rowZone][1].split('-')
      tempEndDay = tempZoneEndDate[2].split('T')
      tempStartDay = tempZoneStartDate[2].split('T')
      numberOfCases = 0
      #row_number_case
      for rowCase in range(row_number_case):
        tempCaseDate = listCase[rowCase].split('-')
        # print(tempCaseDate)

        if (tempZoneStartDate[0] <= tempCaseDate[0] and tempCaseDate[0] <= tempZoneEndDate[0]):
          if (tempZoneStartDate[0] != tempZoneEndDate[0]):
            if (tempZoneStartDate[1] <= tempCaseDate[1] and tempCaseDate[0] == tempZoneStartDate[0]):
              if tempZoneStartDate[1] == tempCaseDate[1]:
                if(tempStartDay[0] <= tempCaseDate[2]):
                  numberOfCases = numberOfCases + 1
              elif tempZoneEndDate[1] == tempCaseDate[1]:
                if(tempEndDay[0] >= tempCaseDate[2]):
                  numberOfCases = numberOfCases + 1
              else:
                numberOfCases = numberOfCases + 1

            elif (tempCaseDate[1] <= tempZoneEndDate[1] and tempCaseDate[0] == tempZoneEndDate[0]):
              if tempZoneStartDate[1] == tempCaseDate[1]:
                if(tempStartDay[0] <= tempCaseDate[2]):
                  numberOfCases = numberOfCases + 1
              elif tempZoneEndDate[1] == tempCaseDate[1]:
                if(tempEndDay[0] >= tempCaseDate[2]):
                  numberOfCases = numberOfCases + 1
              else:
                numberOfCases = numberOfCases + 1

          elif (tempZoneStartDate[1] <= tempCaseDate[1] and tempCaseDate[1] <= tempZoneEndDate[1]):
            if tempZoneStartDate[1] == tempCaseDate[1]:
              if(tempStartDay[0] <= tempCaseDate[2]):
                numberOfCases = numberOfCases + 1
            elif tempZoneEndDate[1] == tempCaseDate[1]:
              if(tempEndDay[0] >= tempCaseDate[2]):
                numberOfCases = numberOfCases + 1
            else:
              numberOfCases = numberOfCases + 1
      
      zoneCases.append([listZone[rowZone][0], listZone[rowZone][1], listZone[rowZone][2], numberOfCases])
    zoneCases.sort()
    print("Status,Number Of Cases")
    for rowZone in range(len(zoneCases)):
      dateOne = zoneCases[rowZone][0].split('T')
      dateTwo = zoneCases[rowZone][1].split('T')
      status = zoneCases[rowZone][2] + " (" + dateOne[0] + " to " + dateTwo[0] +")"
      print("%s,%d" % (status, zoneCases[rowZone][3]))
    
    #
    #   End of Function
    #
    
##
## Call our main function, passing the system argv as the parameter
##
main(sys.argv)


#
#   End of Script
#
