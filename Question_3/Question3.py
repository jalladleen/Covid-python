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
#python Question3.py
#python plotQuestion3.py 15-64.txt 15-64.pdf


#
#   Packages and modules
#

# The 'sys' module gives us access to system tools, including the
# command line parameters, as well as standard input, output and error
import sys


def main(argv):


  age_range = ["15", "15-64", "15-19", "20-24", "25-44", "45-54", "55-64", "65"]
  
  validInput = True
  userInput = ""

  while validInput:
    print("Choose an age group using the values 1 to 8")
    print("1. 15+")
    print("2. 15-64")
    print("3. 15-19")
    print("4. 20-24")
    print("5. 25-44")
    print("6. 45-54")
    print("7. 55-64")
    print("8. 65+")
    userInput = input("Enter a value: ")
    if (int(userInput) > 0) and (int(userInput) < 9):
      validInput = False
    else:
      print("Invalid input try again!\n")

  print("\n-------------------------------------------------------------")
  print("REQUESTED DATA")
  print("-------------------------------------------------------------")
  textName = age_range[int(userInput) - 1] + ".txt"
  f = open(textName,"r")
  print(f.read())
  f.close()

  print("Information is stored in " + textName)
  

##
## Call our main function, passing the system argv as the parameter
##  
main(sys.argv)
#
#   End of Script
#by