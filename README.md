# Profanity-Check

## Introduction

This project finds the profane words from a given scentence and reports the degree of
profanity and censored text

## Requirement
- Create conda environment
  ```bash
  conda create -n profanity_check python
  ```
  
 - Clone the repository
    ```bash 
    git clone https://github.com/pratham-kpatil/Profanity-Check.git 
    cd profanity-check
 
 - Install requirements
    ```bash
    pip install -r requirements.txt
    
    
## Usage
 
- For single scentence
  ```bash
  python main.py --scentence ${your scentence} --print
  
 - For csv file
  ```bash 
  python main.py --csv_file ${path of csv_file} --print
  
  ## Assumptions
  
  - The csv file should contain a column named "scentences" which will have scentences 
  stored in it.
