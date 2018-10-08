#! /usr/bin/env python3
# coding: utf-8

import os
from SetOfParliamentMembers import SetOfParliamentMembers

def main():
    launch_analysis('current_mps.csv')

"""
def launch_analysis(data_file):
    directory = os.path.dirname(__file__)  # we get the right path.

    path_to_file = os.path.join(directory, "../data",
                                data_file)  # with this path, we go inside the folder `data` and get the file.

    with open(path_to_file, "r") as f:
        preview = f.readline()

    print("Yeah! We managed to read the file. Here is a preview: {}".format(preview))
"""

def launch_analysis(data_file, by_party = False, info = False):

    sopm = SetOfParliamentMembers("All MPs")

    sopm.data_from_csv(os.path.join("data",data_file))

    sopm.display_chart()

    if info:
        print(sopm)


    if by_party:

        for party, s in sopm.split_by_political_party().items():

            s.display_chart()


if __name__ == "__main__":
    main()
