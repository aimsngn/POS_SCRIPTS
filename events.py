import csv
import os
import re

# Script: Employee Performance Tracker
# Description: This script tracks and analyzes customer signups made by employees based on POS logs.
# Date: August 2023

def extract_signups_from_logs():
    """ This function extracts the signup events from the log file (generated by my point-of-sale system), and returns it as a list.

    Returns:
        sign_ups_list: A list of dictionaries containing employee ID, sign-up date, customer ID, customer name, and customer phone number as keys.
    """
    sign_ups_list = []
   
    file_path = "../files/pos_logs.txt"
    file_path = os.path.abspath(file_path)
   
    # Opens the log file and analyzes it line by line
    with open(file_path, 'r') as log_file:
        for log in log_file:
            log = log.rstrip()
            
            # If it isn't a sign up event, which is a FINE log level, it skips.
            if "FINE" not in log:
                continue
            result = re.search(r"^\[(\d{4}-\d{2}-\d{2}) .+ Employee (\d+) .+ Customer ID: \[(\d+)\]\. Customer Phone: \[(\d+)\]. Customer Name: \[(.+)\]", log)
           
            if result is None:
                continue
           
            # Storing the extracted information into the list
            sign_ups_list.append({'Employee ID': result[2], 'Sign-up Date': result[1], 'Customer ID':result[3], 'Customer\'s Phone Number': result[4], 'Customer\'s First Name': result[5]})

    return sign_ups_list
   
   
def export_signups_events(sign_ups_list):
    """ This function exports the passed list into a csv file. 
        It genereates a new csv file, which summarizes all signup events.

    Args:
        sign_ups_list: The list of dictionaries from extract_signups_from_logs
    """
    
    # The csv header
    keys = ["Employee ID", "Sign-up Date", "Customer ID", "Customer's Phone Number", "Customer's First Name"]
    
    file_path = "../files/sign_up_events.csv"
    file_path = os.path.abspath(file_path)
   
    # Generates the CSV file
    with open(file_path, 'w', newline = '') as output_file: 
        writer = csv.DictWriter(output_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(sign_ups_list)


def count_signups_from_events():
    """ This function counts the number of sign-ups made by each employee from the exported CSV file

    Returns:
        signup_counts: A dictionary containing an employee's ID as the key and the count of the number of sign-ups they've made as the value.
    """
    signup_counts = {}
   
    file_path = "../files/sign_up_events.csv"
    file_path = os.path.abspath(file_path)
   
    # Opens the exported CSV file and analyzes it per row
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            employee_id = row['Employee ID']
            signup_counts[employee_id] = signup_counts.get(employee_id, 0) +1
    
    # This sorts the employee ID in ascending order
    signup_counts = {key: signup_counts[key] for key in sorted(signup_counts.keys())}
   
    return signup_counts
   
   
def export_employee_performance(signup_counts):
    """ This exports employees' performances into a text file. It also states the top performing employee.
        It generates a text file.

    Args:
        signup_counts: The employee ID and their respective signup counts from the count_signups_from_events function
    """
    file_path = "../files/employee_signup_performance"
    file_path = os.path.abspath(file_path)
   
    # Generates the file
    with open(file_path, 'w', newline = '') as file:
        top_performing_emp = max(signup_counts, key=signup_counts.get)
        top_performing_count = signup_counts[top_performing_emp]
        file.write("Employee " + str(top_performing_emp) + " has the highest signup count of " + str(top_performing_count) + "\n")
        
        for emp_id, count in signup_counts.items():
            file.write("Employee " + str(emp_id) + " made " + str(count) + " sign ups\n")


# Main script execution          
sign_ups = extract_signups_from_logs()
export_signups_events(sign_ups)
signup_counts = count_signups_from_events()
export_employee_performance(signup_counts)

