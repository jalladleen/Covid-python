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
#python Question2Pre.py conposcovidloc.csv response_framework.csv

#
#   Packages and modules
#

# The 'sys' module gives us access to system tools, including the
# command line parameters, as well as standard input, output and error
import sys

import csv


#
# Define any "constants" for the file here.
# Names of constants should be in UPPER_CASE.
#
# This is a dictionary -- a data structure that associates
# values (in this case integers) with names.
INDEX_MAP_STATE = {
        "Reporting_PHU" :  0,
        "Rporting_PHU_id" :  1,
        "Status_PHU" :  2,
        "start_date" :  3,
        "end_date" :  4,
        "PHU_url" :  5 }

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
    if len(argv) != 3:
        print("Usage: dictionary_selection_example.py <data file>>")

        # we exit with a zero when everything goes well, so we choose
        # a non-zero value for exit in case of an error
        sys.exit(1)

    filename_Cases = argv[1]
    filname_Zone = argv[2]


    #
    # Open the name data input file1 (Confirmed positive cases of COVID19 in Ontario).  The encoding argument
    # indicates that we want to handle the BOM (if present)
    # by simply ignoring it.
    #
    try:
        fh_Cases = open(filename_Cases, encoding="utf-8-sig")
    except IOError as err:
        # Here we are using the python format() function.
        # The arguments passed to format() are placed into
        # the string it is called on in the order in which
        # they are given.
        
        print("Unable to open file '{}' : {}".format(
                filename_Cases, err), file=sys.stderr)
        sys.exit(1)
    #
    # Create a CSV (Comma Separated Value) reader based on this
    # open file handle.  We can use the reader in a loop iteration
    # in order to access each line in turn.
    #
    
    data_reader_cases = csv.reader(fh_Cases)
    
    
    #
    # Open the name data input file2 (Ontario COVID-19 zones:). The encoding argument
    # indicates that we want to handle the BOM (if present)
    # by simply ignoring it.
    
    try:
        fh_Zone = open(filname_Zone, encoding="utf-8-sig")
    except IOError as err:
        print("Unable to open file '{}' : {}".format(
                filname_Zone, err), file=sys.stderr)
        sys.exit(1)

    data_reader_zone = csv.reader(fh_Zone)

    listZone = [] # This list that will contain the zone/state, the starting date of the status and the ending date of that status
    listCase = [] # This list that will contain the positive cases in that zone 
    
    # This will be looping through the data to read the zones in the region and identify the starting and the ending date of that status. 
    for row in data_reader_zone: 
        reporting_PHU = row[INDEX_MAP_STATE["Reporting_PHU"]]
        if reporting_PHU.startswith("Peel Public Health"):
            listZone.append([row[INDEX_MAP_STATE["start_date"]] , row[INDEX_MAP_STATE["end_date"]], row[INDEX_MAP_STATE["Status_PHU"]]])

    f = open("status.txt","w+")
    for x in range(len(listZone)):
      f.write(listZone[x][0] + "," + listZone[x][1] +","+ listZone[x][2]+"\n")
    f.close()
    
    # This will be looping through the data to read the cases in the region.    
    for row in data_reader_cases:
        reporting_PHU = row[INDEX_MAP_CASES["Reporting_PHU"]] 
        if reporting_PHU.startswith("Peel Public Health"):
            listCase.append(row[INDEX_MAP_CASES["Case_Reported_Date"]])

    f = open("cases.txt","w+")
    for x in range(len(listCase)):
      f.write(listCase[x] +"\n")
    f.close()

    print("Created files.")

main(sys.argv)