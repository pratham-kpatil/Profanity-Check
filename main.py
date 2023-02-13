import argparse
import json
import os

import pandas as pd

from degree_of_profinity import Profanity


def main():
    parser = argparse.ArgumentParser(description='Calcualte Degree of Profanity')
    parser.add_argument("--scentence", action='store')
    parser.add_argument("--csv_file", action='store')
    parser.add_argument("--print", action='store_true')
    args = parser.parse_args()

    profanity = Profanity()

    if args.scentence:
        profanity.calculate_degree_of_profanity(args.scentence)
        profanity.print_output(args.print)
        
    
    if args.csv_file:
        try:
            if not os.path.exists(args.csv_file):
                raise FileNotFoundError("Error while reading csv or invalid csv file")
            
            data = pd.read_csv(args.csv_file) 
            assert ('scentences' in data.columns), 'Please use csv with target column named as scentences'


            scentences = data['scentences']

            for idx, scentence in  enumerate(scentences):
                profanity.calculate_degree_of_profanity(scentence)
            profanity.print_output(args.print)
        
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()