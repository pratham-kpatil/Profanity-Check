import argparse
import json
import os

import pandas as pd

from degree_of_profinity import Profanity


def main():
    parser = argparse.ArgumentParser(description='Calcualte Degree of Profanity')
    parser.add_argument("--scentence", action='store', 
                        help='Enter a string or scentence to check profanity score')
    parser.add_argument("--csv_file", action='store',
                        help='Enter input csv file path')
    parser.add_argument("--save_path", action='store',
                        help='Enter path to where you want to save output csv file')
    parser.add_argument("--print", action='store_true',
                        help='Add this argument to see censored text')
    args = parser.parse_args()

    profanity = Profanity()

    if args.scentence:
        profanity.calculate_degree_of_profanity(args.scentence)  # check degree of profanity of a scentence
        profanity.print_output(args.print) # print the output
        
    
    if args.csv_file:

        try:
            if not os.path.exists(args.csv_file):
                raise FileNotFoundError("Error while reading csv or invalid csv file path")
            
            #read csv file
            data = pd.read_csv(args.csv_file) 
            assert ('scentences' in data.columns), 'Please use csv with target column named as scentences'

            # take all the scentences in csv file
            scentences = data['scentences']

            for idx, scentence in  enumerate(scentences):
                profanity.calculate_degree_of_profanity(scentence) # check degree of profanity of a scentence
            profanity.print_output(args.print) # print the output

            if args.save_path:
                profanity.save_output_csv(args.csv_file, args.save_path)   # save output of the csv file
        
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()