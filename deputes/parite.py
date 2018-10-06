#! /usr/bin/env python3
# coding: utf-8

# Import du module

import analysis.csv as c_an
import analysis.xml as x_an
import argparse
import lg

#import pdb;pdb.set_trace()

def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("-e", "--extension", help="""Type of file to analyse. Is it a CSV or an XML?""")

    parser.add_argument("-d", "--datafile",
                        help="""CSV file containing pieces of information about the members of parliament""")

    return parser.parse_args()


def main():
    # Exécution de la fonction main() du module csv_analysis
    lg.basicConfig(level=lg.DEBUG)
    args = parse_arguments()

    try:

        datafile = args.datafile

        if datafile == None:

            raise Warning('You must indicate a datafile!')

        else:

            try:

                if args.extension == 'xml':

                    x_an.launch_analysis(datafile)

                elif args.extension == 'csv':

                    c_an.launch_analysis(datafile)

            except FileNotFoundError as e:

                lg.warning("Ow :( The file was not found. Here is the original message of the exception :", e)

            finally:

                lg.info('#################### Analysis is over ######################')

    except Warning as e:

        lg.warning(e)


if __name__ == "__main__":
    main()
