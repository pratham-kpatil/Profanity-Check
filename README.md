# Profanity-Check

## Introduction

This project finds the profane words from a given scentence and reports the degree of
profanity and censored text

## Requirement
- Create conda environment
  ```bash
  conda create -n profanity_check python
  conda activate profanity_check
  ```
  
 - Clone the repository
    ```bash 
    git clone https://github.com/pratham-kpatil/Profanity-Check.git 
    cd Profanity-Check
 
 - Install requirements
    ```bash
    pip install -r requirements.txt
    
    
## Usage
 
- For single scentence
   ```bash
    python main.py --scentence ${your scentence} --print
   ```
  
 - For csv file
   ```bash 
    python main.py --csv_file ${path to csv_file} --print --save_path ${path to save output as csv}
   ```
  Use --print only when you want to print censored text in output
  
  Use --save_path only when you want to save output as csv
 ## Assumptions
  
  - Config file is generated with fake data to test the code
  - Fake input csv file is generated in csv_data folder tp test code
  - The csv file should contain a column named "scentences" which will have scentences 
  stored in it.
