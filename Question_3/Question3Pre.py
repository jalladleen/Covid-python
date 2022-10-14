#!/usr/bin/env python

'''
Question3Pre.py
  Author(s): Leen Al-Jallad (1154729), Hamna Ahmed (1148915) and Ashmethaa Arulanantham(1072965)
'''
#python Question3Pre.py unemployment.csv


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

  unemplymentFile = argv[1]


  age_range = ["15", "15-64", "15-19", "20-24", "25-44", "45-54", "55-64", "65"]


  validAgeGroup = False
  year = 0
  repeat = False
  
  for n in range(len(age_range)):
    tempList = []
    try:
      fh = open(unemplymentFile, encoding="utf-8-sig")

    except IOError as err:
          # Here we are using the python format() function.
          # The arguments passed to format() are placed into
          # the string it is called on in the order in which
          # they are given.
        print("Unable to open file '{}' : {}".format(
                  unemplymentFile, err), file=sys.stderr)
        sys.exit(1)

      #
      # Create a CSV (Comma Separated Value) reader based on this
      # open file handle.  We can use the reader in a loop iteration
      # in order to access each line in turn.
      #
    data_reader = csv.reader(fh)
    
    for row in data_reader: 
          age_group = row[INDEX_MAP["AGE GROUP"]]
          age_group_list = age_group.split(" ")

          for x in range(len(age_group_list)):
            if age_group_list[x] == str(age_range[n]):
              validAgeGroup = True

          month = row[INDEX_MAP["MONTH"]]
          power = 3
        
          for i in range(len(month)):
            if month[i].isdigit():
              year = year + int(month[i]) * (10 ** power);
              power = power - 1
          
          if year > 2017  and  validAgeGroup and row[INDEX_MAP["DURATION"]] == "Total unemployed" and row[INDEX_MAP["GEOGRAPHY"]] == "Total, Ontario regions":
            for y in range(len(tempList)):
              if month == tempList[y][1]:
                repeat = True
            
            if year > 2019 and repeat == False:
              tempList.append(["Covid", month, row[INDEX_MAP["Both sexes"]]])
            elif repeat == False:
              tempList.append(["Pre Covid", month, row[INDEX_MAP["Both sexes"]]])
          
          validAgeGroup = False
          year = 0
          repeat = False

    textName = age_range[n] + ".txt"
    f = open(textName,"w+")
    f.write("Time Interval,Date,Unemployment\n")
    for x in range(len(tempList)):
      f.write(tempList[x][0] + "," + tempList[x][1] +","+ tempList[x][2]+"\n")
    f.close()
  
  print("Finished creating the files.")
  

##
## Call our main function, passing the system argv as the parameter
##  
main(sys.argv)
#
#   End of Script
#by