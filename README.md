# Employee Performance Tracker & Log Search Utility

This repository contains two scripts: `employee_performance.py` and `events_query.py`

The `employee_performance.py` script is used as a **Employee Performance Tracker** based on customer signups, while the `events_query.py` script is used as a **Log Search Utility** that makes queries based on log levels or log messages.

## Table of Contents

- [Employee Performance Tracker](#employee-performance-tracker)
  - [Description](#description)
  - [Usage](#usage)
  - [Functions](#functions)
- [Log Search Utility](#log-search-utility)
  - [Description](#description-1)
  - [Usage](#usage-1)
  - [Functions](#functions-1)
- [File Structure](#file-structure)

<a name="employee-performance-tracker"></a>
## Employee Performance Tracker

<a name="description"></a>
### Description

The **Employee Performance Tracker** script processes customer sign-up events from a log file that is generated by my point-of-sale (POS) system. It provides insights into employee performance based on their sign-up activities. You can find my POS system in here: https://github.com/aimsngn/POS. 

This script generates two files, which are currently ignored by the .gitignore file due to their frequent updates.
  - `employee_signup_performance.txt`
      - A text file containing a summary and analysis of employees' performances.
      - It counts how many customers' an employee has registered.
  - `sign_up_events.csv`
      - A CSV file that contains a summary and quick overview of all signup events from the log file.
      - It contains: Employee ID, Sign-up Date, Customer ID, Customer's Phone Number, Customer's First Name

***To showcase these files, I've included a `sample_employee_signup_perf.txt` and a `sample_sign_up_events.csv`***

<a name="usage"></a>
### Usage

1. Ensure you have the appropriate log file. I have included a sample log file in this repository, which is a snipped copy of my POS' log file.

2. You may have to change file paths within the script.

3. Run the script by executing the main script file: `employee_performance_tracker.py`.

<a name="functions"></a>
### Functions

1. The script extracts sign-up events from POS logs using `extract_signups_from_logs()`.

2. Extracted sign-up events are exported into a CSV file using `export_signups_events(sign_ups_list)`.

3. The script counts sign-ups for each employee from the exported CSV file using `count_signups_from_events()`.

4. Employee performance data is exported to a text file using `export_employee_performance(signup_counts)`.

<a name="log-search-utility"></a>
## Log Search Utility

<a name="description-1"></a>
### Description

The **Log Search Utility** script allows users to search for particular log events within a given log file. Users can make queries based on either log level or log message. While the script is currently tailored to work with log files generated by my POS system, it can seamlessly adapt to operate with other types of files as well.

<a name="usage-1"></a>
### Usage

1. Ensure you have the appropriate log file. I have included a sample log file in this repository, which is a copy of my POS' log file.

2. You may have to change file paths within the script.

3. Run the script by executing the main script file: `log_search_utility.py`.

<a name="functions-1"></a>
### Functions

1. Users are prompted to select the type of query: log level or log message.

2. If log level is chosen, the script searches and displays logs matching the specified level using `search_level_events(file_path)`.

3. If log message is chosen, the script searches and displays logs containing all specified keywords using `search_message_events(file_path)`.

4. After each search, users can choose to perform another query or exit the program.

<a name="file-structure"></a>
## File Structure

POS_SCRIPTS/

├── employee_performance_tracker.py
  
├── log_search_utility.py
  
├── sample_logs.txt (A sample log file that is used by the scripts)
  
├── sample_employee_signup_performance.txt (Not auto-generated; It's used to showcase the ignored file by git)
  
├── sample_sign_up_events.csv (Not auto-generated; It's used to showcase the ignored file by git)
  
│
  
└── files/ (Ignored using .gitignore)
      
``      └─── sign_up_events.csv (Auto-generated)
      
``      └─── employee_signup_performance.txt (Auto-generated)


