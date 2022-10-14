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
#python Question1.py schoolsactivecovid.csv Markham 2020 09


#
#   Packages and modules
#

# The 'sys' module gives us access to system tools, including the
# command line parameters, as well as standard input, output and error
import sys

# command line parameters, as well as standard input, output and error
import urllib.request



#
# Define any "constants" for the file here.
# Names of constants should be in UPPER_CASE.
#
# This is a dictionary -- a data structure that associates
# values (in this case integers) with names.
INDEX_MAP = {
        "collected_date" :  0,
        "reported_date" :  1,
        "school_board" :  2,
        "school_id" :  3,
        "school" :  4,
        "municipality" :  5,
        "comfirmed_student_cases" :  6,
        "comfirmed_staff_cases" :  7,
        "confirmed_unspecified_cases" :  8,
        "total_confirmed_cases" :  9 }


def main(argv):
    '''
    Load a data file and print out the columns matching the selected
    indices
    '''

    #
    #   Check that we have been given the right number of parameters,
    #   and store the single command line argument in a variable with
    #   a better name
    #
    if len(argv) != 4:
        print("Usage: Question1.py <data file>>")

        # we exit with a zero when everything goes well, so we choose
        # a non-zero value for exit in case of an error
        sys.exit(1)

    # filename_activeCases = argv[1] #the first command line argument is the file indicating the data for Schools with active COVID-19 cases

    # #
    # # Open the name data input file.  The encoding argument
    # # indicates that we want to handle the BOM (if present)
    # # by simply ignoring it.
    # #

    # try:
    #     fh = open(filename_activeCases, encoding="utf-8-sig")

    # except IOError as err:
    #     # Here we are using the python format() function.
    #     # The arguments passed to format() are placed into
    #     # the string it is called on in the order in which
    #     # they are given.
    #     print("Unable to open file '{}' : {}".format(
    #             filename_activeCases, err), file=sys.stderr)
    #     sys.exit(1)

    #
    # Create a CSV (Comma Separated Value) reader based on this
    # open file handle.  We can use the reader in a loop iteration
    # in order to access each line in turn.
    #
    # data_reader = csv.reader(fh)

    city = argv[1] #the user needs to indicate the city's name as the second line argument 
    url = 'https://data.ontario.ca/api/3/action/datastore_search?q='+city+'&resource_id=8b6d22e2-7065-4b0f-966f-02640be366f2'
    with urllib.request.urlopen(url) as url:
      fileobj = url.read()
      # print (fileobj)

    list = str(fileobj).split('[')
    newList = list[2].split('"')
    # print(list[2])
    # print(newList[33])
    # newList[34] = newList[34].replace(":", "")
    # newList[34] = newList[34].replace(",", "")
    # print(newList[34])

    date = argv[2] + "-" +argv[3] #the date much be expressed as a year then space then the month 
    row_number = 0
    length = len(newList)
    list = [] #the list will contain the school cases in a certain month 
    
    for row in range(length):

        # municipality = row[INDEX_MAP["municipality"]]
        # #getting the city
        if newList[row] == "reported_date":

          isDate = newList[row + 2].startswith(date)
          #checking if the reported date matches the user's input (true/filename_activeCases)
          if isDate:
              #if the user's input matches the data on the data list from the file 
              school = newList[row + 14] #identify the school's name
              cases = newList[row + 27]
              cases = cases.replace(":", "")
              cases = cases.replace(",", "")
              
              #idenitfy the nymber of cases in that school
              schoolCases = school + " " + cases;
              # attach the data of the school's names and the number of the cases 
              list.append(schoolCases) #append the school's data into the list
              row_number += 1 #loop over each row 
            
    list.sort() #sort the list in alphabetical order for the school's names 
 
    temp = list[0].split() #splits the data output by spaces for readible data 
    old_school = "" #used as a variable to indicate the name of the school the data is being selected for within the loop 
    for element in range(len(temp) - 1): #looping over the schools names in the lists 
      if element == 0:
        old_school = temp[element]
      else:
        old_school = old_school + " " + temp[element]
  
    finalSchoolList = []
    finalSchoolListLength = 1
    cases = 0

    for row in range(row_number):
      temp = list[row].split()
      school = ""
      for element in range(len(temp) - 1):
        if element == 0:
          school = temp[element]
        else:
          school = school + " " + temp[element]

      if school != old_school:
        finalSchoolList.append([cases, old_school])
        finalSchoolListLength = finalSchoolListLength + 1
        cases = 0;
        old_school = ""
        for element in range(len(temp) - 1):
          if element == 0:
            old_school = temp[element]
          else:
            old_school = old_school + " " + temp[element]

      cases = cases + int(temp[len(temp) - 1]) #counting the number of the total cases for each school in the list 
    
    finalSchoolList.append([cases, old_school]) #adding the final data of schools to the list
    finalSchoolList.sort() #sorting it on the list to be outputed with spaces 

    #print out the data in the form of School's Name , Positive COVID-19 cases 
    print("Positive COVID-19 Cases,School's Name")
    for row in range(finalSchoolListLength):
      print("%s,%s" %(finalSchoolList[row][0], finalSchoolList[row][1]))


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
