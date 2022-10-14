#!/usr/bin/env python

'''
read_names.py
  Author(s): Leen Al-Jallad (1154729) and Ashmethaa Arulanantham(1072965)
  and Hamna Ahmed (1148915)
  Earlier contributors(s): Andrew Hamilton-Wright, Deborah Stacey

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
#python Question4.py
#python plotQuestion4.py 2020-04.txt Question4.pdf

#
#   Packages and modules
#

# The 'sys' module gives us access to system tools, including the
# command line parameters, as well as standard input, output and error
import sys

def main(argv):

  valid = True
  userInput = ""

  fp = open("month.txt", "r")
  lines = fp.readlines()
  
  dates = []
  for line in lines:
    dates.append(line.strip())

  month = ""
  while valid:
    print("Select one of the given months:")
    for x in range(len(dates)):
      text = str(x+1) + ". " + dates[x]
      print(text)
    userInput = input("Enter an month: ")
    textName = userInput + ".txt"

    if int(userInput) > 0 and int(userInput) <= len(dates):
      valid = False
      month = dates[int(userInput) - 1]
    else:
      print("Invalid entry. Try again!\n")


  textName = month + ".txt"
  f = open(textName,"r")
  print("\n-------------------------------------------------------------")
  print("REQUESTED DATA")
  print("-------------------------------------------------------------")
  print(f.read())
  f.close()

  print("Information is stored in " +textName)

##
## Call our main function, passing the system argv as the parameter
##  
main(sys.argv)
#
#   End of Script