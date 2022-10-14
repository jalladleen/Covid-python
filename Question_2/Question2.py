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
#python Question2.py
#python plotQuestion2.py Question2.txt Question2.pdf


#
#   Packages and modules
#

# The 'sys' module gives us access to system tools, including the
# command line parameters, as well as standard input, output and error
import sys


def main(argv):

    row_number_zone = 0 # Variable for counting the number of rows that indicate the Ontario COVID-19 zones in the file
    row_number_case = 0 # Variable for counting the number of rows  that indicate the Confirmed positive cases of COVID19 in Ontario in the file
    listZone = [] # This list that will contain the zone/state, the starting date of the status and the ending date of that status
    listCase = [] # This list that will contain the positive cases in that zone 
    
    f = open("cases.txt","r")
    lines = f.readlines()
    for line in lines:
      listCase.append(str(line.strip()))
      row_number_case = row_number_case + 1
    f.close()

    f = open("status.txt","r")
    lines = f.readlines()
    for line in lines:
      temp = line.strip().split(",")
      listZone.append([str(temp[0]), str(temp[1]), str(temp[2])])
      row_number_zone = row_number_zone + 1
    f.close()

    listCase.sort() #sort the list in alpha order
    
    for row in range(row_number_zone): #first date
      earliestCommonDate = ""
      oldestCommonDate = ""
      for rowTwo in range(row_number_zone): #second date 0 - start date 1- end date 2- status name
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
        if(Day[0] < 10):
          listZone[row][1] = Date[0] + "-" + Date[1] + "-0" + str(Day[0]) + "T" + Day[1]
        else:
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


    zoneCases = []
    for rowZone in range(len(listZone)):
      tempStartDate = listZone[rowZone][0].split('T')
      tempEndDate = listZone[rowZone][1].split('T')
      numberOfCases = 0

      for rowCase in range(row_number_case):
        if (tempStartDate[0] <= listCase[rowCase] and listCase[rowCase] <= tempEndDate[0]):
          numberOfCases = numberOfCases + 1
      
      zoneCases.append([listZone[rowZone][0], listZone[rowZone][1], listZone[rowZone][2], numberOfCases])
  
    zoneCases.sort()
    f = open("Question2.txt","w+")
    f.write("Status,Number Of Cases\n")
    print("Status,Number Of Cases")
    for rowZone in range(len(zoneCases)):
      dateOne = zoneCases[rowZone][0].split('T')
      dateTwo = zoneCases[rowZone][1].split('T')
      status = zoneCases[rowZone][2] + " (" + dateOne[0] + " to " + dateTwo[0] +")"
      f.write(status + "," + str(zoneCases[rowZone][3]) + "\n")
      print(status + "," + str(zoneCases[rowZone][3]))
    f.close()

    print("\nInformation was stored in Question2.txt")


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
