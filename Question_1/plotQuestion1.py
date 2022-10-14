#!/usr/bin/env python

'''
plotQuestion1.py
  Author(s): Leen Al-Jallad (1154729), Hamna Ahmed (1148915) and Ashmethaa Arulanantham(1072965)

  Project: Lab Assignment 4 Script
  Date of Last Update: Dec 26, 2020.

  Functional Summary
      create_name_plot.py reads a CSV file and saves
      a plot based on the data to a PDF file.

     Commandline Parameters: 2
        sys.argv[0] = name of file to read
        sys.argv[1] = name of graphics file to create
'''

#python plotQuestion1.py QuestionOakville.txt graphTwo.pdf Oakville 2020 09

#
#   Packages and modules
#
import sys

# pandas is a (somewhat slow) library to do complicated
# things with CSV files. We will use it here to identify
# data by column
import pandas as pd

# seaborn and matplotlib are for plotting.  The matplotlib
# library is the actual graphics library, and seaborn provides
# a nice interface to produce plots more easily.
import seaborn as sns
from matplotlib import pyplot as plt


def main(argv):

    '''
    Create a plot using ranks
    '''

    #
    #   Check that we have been given the right number of parameters,
    #
    #   Check that we have been given the right number of parameters,
    #   and store the single command line argument in a variable with
    #   a better name
    #
    if len(argv) != 3:
        print("Usage:",
                "create_name_plot.py <data file> <graphics file>")
        sys.exit(-1)

    csv_filename = argv[1]
    graphics_filename = argv[2]


    #
    # Open the data file using "pandas", which will attempt to read
    # in the entire CSV file
    #
    try:
        csv_df = pd.read_csv(csv_filename)

    except IOError as err:
        print("Unable to open source file", csv_filename,
                ": {}".format(err), file=sys.stderr)
        sys.exit(-1)


    # A this point in the file, we begin to do the plotting

    # We must get the figure before we plot to it, or nothing will show up.
    # The matplotlib "figure" is the data environment that we are drawing
    # our plot into.  The seaborn library will draw onto this figure.
    # We don't see seaborn directly refer to "fig" because it is internally
    # drawing on "the current figure" which is the same one we are
    # referencing on this line.
    fig = plt.figure(figsize = (20, 30))

    text = csv_filename.split(".")
    textPart  = text[0].split("_")
    graphTitle = textPart[0] + ": " + textPart[1]
    plt.title(graphTitle, fontsize = 100)

    # sns.set(font_scale = 5)
    sns.set(font_scale = 2)
    sns.barplot(x = "Positive COVID-19 Cases", y = "School's Name",  data = csv_df)
    
    # print(csv_df['Positive COVID-19 Cases'].min(), csv_df['Positive COVID-19 Cases'].max())

  
    plt.xlabel("Positive COVID-19 Cases", size = 80, labelpad=70)
    plt.ylabel("School's Name", size = 80, labelpad=70)

    txt = "Minimum amount of cases: " + str(csv_df['Positive COVID-19 Cases'].min()) + "\nMaximum amount of cases: " + str(csv_df['Positive COVID-19 Cases'].max())
    plt.figtext(0.5, 0.01, txt, wrap = True, horizontalalignment='center', fontsize=20)

    # Now we can save the matplotlib figure that seaborn has drawn
    # for us to a file
    fig.savefig(graphics_filename, bbox_inches="tight")


    # Uncomment this line to show the figure on the screen.  Note
    # that in repl.it, you may not be able to close the figure (it may
    # be too big for your screen) so you will have to press [CTRL]-C
    # in order to stop your program in order to be able to run commands
    # in your shell again.
    # plt.show()

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
