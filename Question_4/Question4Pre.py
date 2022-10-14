#!/usr/bin/env python

'''
read_names.py
  Author(s): Leen Al-Jallad (1154729), Hamna Ahmed (1148915) and Ashmethaa Arulanantham(1072965)

  Project: Lab Assignment Week 4 Task 1 Script
  Date of Last Update: Feb 1, 2021.

  
      There are expected to be three fields:
          1. name
          2. sex (only F or M recorded in this US census data)
          3. number of people with this name

      This code will also count the number of names in each of the
      "F" and "M" categories, and print this out at the end.

      The file represents the names of people in the population
      for a particular year of birth in the United States of America.
      Officially it is the "National Data on the relative frequency
      of given names in the population of U.S. births where the individual
      has a Social Security Number".

     Commandline Parameters: 1
        argv[1] = initial year
        argv[2] = last year
        argv[3] = increment 

     References
        Name files from http://www.ssa.gov/OACT/babynames/limits.html
'''
#python Question4Pre.py conposcovidloc.csv

#
#   Packages and modules
#

# The 'sys' module gives us access to system tools, including the
# command line parameters, as well as standard input, output and error
import sys

# The 'csv' module gives us access to a tool that will read CSV
# (Comma Separated Value) files and provide us access to each of
# the fields on each line in turn

import csv
import urllib.request

INDEX_MAP_CASES = {
  
        "Row_ID" :  0,
        "Accurate_Episode_Date" :  1,
        "Case_Reported_Date" :  2,
        "Test_Reported_Date" :  3,
        "Specimen_Date" :  4,
        "Age_Group" :  5,
        "Client_Gender" :  6,
        "Case_AcquisitionInfo" :  7,
        "Outcome1" :  8,
        "Outbreak_Related" :  9,
        "Reporting_PHU_ID" :  10,
        "Reporting_PHU" :  11,
        "Reporting_PHU_Address" :  12,
        "Reporting_PHU_City" :  13,
        "Reporting_PHU_Postal_Code" :  14,
        "Reporting_PHU_Website" :  15,
        "Reporting_PHU_Latitude" :  16,
        "Reporting_PHU_Longitude" :  17}

#
# Define any "constants" for the file here.
# Names of constants should be in UPPER_CASE.
#
INDEX_MAP = {
        "MONTH" :  0,
        "GEOGRAPHY" :  1,
        "DURATION" :  2,
        "AGE GROUP" :  3,
        "Both sexes" :  4,
        "Male" :  5,
        "Female" :  6 }

def main(argv):
    #
    #Main function in the script. Putting the body of the
    #script into a function allows us to separate the local
    #variables of this function from the global constants
    #declared outside.
    #

    #
    #   Check that we have been given the right number of parameters,
    #   and store the single command line argument in a variable with
    #   a better name
    #

  if len(argv) != 2:

        # we exit with a zero when everything goes well, so we choose
        # a non-zero value for exit in case of an error

    print("Usage: read_file.py <file name> <number of names>")
        # we exit with a zero when everything goes well, so we choose
        # a non-zero value for exit in case of an error

    sys.exit(1)

  positiveCasesFile = argv[1]

  try:
      fh = open(positiveCasesFile, encoding="utf-8-sig")

  except IOError as err:
        # Here we are using the python format() function.
        # The arguments passed to format() are placed into
        # the string it is called on in the order in which
        # they are given.
      print("Unable to open file '{}' : {}".format(
                positiveCasesFile, err), file=sys.stderr)
      sys.exit(1)

    #
    # Create a CSV (Comma Separated Value) reader based on this
    # open file handle.  We can use the reader in a loop iteration
    # in order to access each line in turn.
    #
  data_reader = csv.reader(fh)

  positiveCaseList = []
  PHU = "Toronto Public Health"
  for row in data_reader:
    if PHU == row[INDEX_MAP_CASES["Reporting_PHU"]]:
      positiveCaseList.append(row[INDEX_MAP_CASES["Case_Reported_Date"]])
  
  region = "TORONTO"

  url = 'https://data.ontario.ca/api/3/action/datastore_search?q=' + region + '&resource_id=e760480e-1f95-4634-a923-98161cfb02fa'
  with urllib.request.urlopen(url) as url:
    fileobj = url.read()
  
  icuList = str(fileobj).split("[")
  newlist = icuList[2].split('"')

  dateList = []

  newICUList = []
  for row in range(len(newlist)):
    dateUsed = False
    if newlist[row] == "date":
      icuDate = newlist[row + 2]

      datePart = icuDate.split("-")
      month = datePart[0] + "-" + datePart[1]
      for x in range(len(dateList)):
        if dateList[x].startswith(month):
          dateUsed = True

      if dateUsed == False:
        dateList.append(month)

      hosiptalization = newlist[row + 13]
      hosiptalization = hosiptalization.replace(":", "")
      hosiptalization = hosiptalization.replace(",", "")
      newICUList.append([icuDate, hosiptalization])

  f = open("month.txt", "w+")
  for x in range(len(dateList)):
    text = dateList[x] + "\n"
    f.write(text)
  f.close
  
  for y in range(len(dateList)):
    positiveCaseList.sort()
    first = True
    total = 0

    textName = dateList[y] + ".txt"
    f = open(textName,"w+")
    f.write("Case Type,Date,Total Number Of Cases\n")
    for x in range(len(positiveCaseList)):
      if positiveCaseList[x].startswith(dateList[y]):
        if first:
          oldDate = positiveCaseList[x]
          first = False
        if oldDate != positiveCaseList[x]:
          f.write("Covid," + oldDate + "," + str(total) + "\n")
          total = 0
          oldDate = positiveCaseList[x]
        total = total + 1

    newICUList.sort()
    for x in range(len(newICUList)):
      if newICUList[x][0].startswith(dateList[y]):
        newDate = newICUList[x][0].split("T")
        f.write("Hospitalizations," + newDate[0] + "," + newICUList[x][1] + "\n")
    
    f.close()

  print("Files were created.")

##
## Call our main function, passing the system argv as the parameter
##  
main(sys.argv)
#
#   End of Script