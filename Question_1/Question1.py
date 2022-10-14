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
#Running code: python Question1.py
#Running the graphOne: python plotQuestion1.py Question1.txt graphOne.pdf



#
#   Packages and modules
#

# The 'sys' module gives us access to system tools, including the
# command line parameters, as well as standard input, output and error
import sys

import urllib.request

# command line parameters, as well as standard input, output and error
# import urllib.request


def main(argv):
    valid = True
    userInput = ""
    userDate = ""

    while valid:
      userInput = input("Enter a city: ")
      url = 'https://data.ontario.ca/api/3/action/datastore_search?q='+userInput+'&resource_id=8b6d22e2-7065-4b0f-966f-02640be366f2'
      with urllib.request.urlopen(url) as url:
        fileobj = url.read()
      
      temp = str(fileobj).split('[')
      newList = temp[2].split('"')
      userDate = input("Enter a date in this format YYYY-MM: ") #the date much be expressed as a year then space then the month 
      row_number = 0
      schoolList = [] #the list will contain the school cases in a certain month 
      
      for row in range(len(newList)):

          if newList[row] == "reported_date":

            isDate = newList[row + 2].startswith(userDate)
            #checking if the reported date matches the user's input (true/filename_activeCases)
            if isDate:
                #if the user's input matches the data on the data list from the file 
                school = newList[row + 14] #identify the school's name
                cases = newList[row + 27]
                cases = cases.replace(":", "")
                cases = cases.replace(",", "")
                
                # attach the data of the school's names and the number of the cases 
                schoolList.append([school, cases]) #append the school's data into the list
                row_number += 1 #loop over each row 
      if len(schoolList) != 0:
        valid = False
      else:
        print("Invalid entry try again!")

    schoolList.sort() #sort the list in alphabetical order for the school's names 
    #splits the data output by spaces for readible data 
    old_school =  schoolList[0][0]#used as a variable to indicate the name of the school the data is being selected for within the loop 

  
    finalSchoolList = []
    cases = 0

    for row in range(row_number): # total cases removes names cases go back to zero after new school on list
      school = schoolList[row][0]

      if school != old_school:
        finalSchoolList.append([cases, old_school])
        cases = 0;  
        old_school = schoolList[row][0]

      cases = cases + int(schoolList[row][1]) #counting the number of the total cases for each school in the list 
    
    finalSchoolList.append([cases, old_school]) #adding the final data of schools to the list
    finalSchoolList.sort() #sorting it on the list to be outputed with spaces 

    #writes information into a Question1.txt
    textname = userInput + "_" + userDate + ".txt"
    f = open(textname,"w+")
    f.write("Positive COVID-19 Cases,School's Name\n")
    for row in range(len(finalSchoolList)):
      f.write(str(finalSchoolList[row][0]) + "," + str(finalSchoolList[row][1]) + "\n")
    f.close()

    print("File is created\nLook at the file named "+ textname)

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
