import csv
import os
import re

def extract_signups_from_logs():
    sign_ups_list = []
   
    file_path = "../files/pos_logs.txt"
    file_path = os.path.abspath(file_path)
   
    with open(file_path, 'r') as log_file:
        for log in log_file:
            log = log.rstrip()
            if "FINE" not in log:
                continue
            result = re.search(r"^\[(\d{4}-\d{2}-\d{2}) .+ Employee (\d+) .+ Customer ID: \[(\d+)\]\. Customer Phone: \[(\d+)\]. Customer Name: \[(.+)\]", log)
           
            if result is None:
                continue
           
            sign_ups_list.append({'Employee ID': result[2], 'Sign-up Date': result[1], 'Customer ID':result[3], 'Customer\'s Phone Number': result[4], 'Customer\'s First Name': result[5]})


    return sign_ups_list
   
def export_signups_events(sign_ups_list):
    keys = ["Employee ID", "Sign-up Date", "Customer ID", "Customer's Phone Number", "Customer's First Name"]
   
    file_path = "../files/sign_up_events.csv"
    file_path = os.path.abspath(file_path)
   
    with open(file_path, 'w', newline = '') as output_file: #by default newline character is \n
        writer = csv.DictWriter(output_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(sign_ups_list)

def count_signups_from_events():
    signup_counts = {}
   
    file_path = "../files/sign_up_events.csv"
    file_path = os.path.abspath(file_path)
   
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            employee_id = row['Employee ID']
            signup_counts[employee_id] = signup_counts.get(employee_id, 0) +1
   
    signup_counts = {key: signup_counts[key] for key in sorted(signup_counts.keys())}
   
    return signup_counts
   
def export_employee_performance(signup_counts):
   
    file_path = "../files/employee_signup_performance"
    file_path = os.path.abspath(file_path)
   
    with open(file_path, 'w', newline = '') as file:
        top_performing_emp = max(signup_counts, key=signup_counts.get)
        top_performing_count = signup_counts[top_performing_emp]
        file.write("Employee " + str(top_performing_emp) + " has the highest signup count of " + str(top_performing_count) + "\n")
   
        for emp_id, count in signup_counts.items():
            file.write("Employee " + str(emp_id) + " made " + str(count) + " sign ups\n")


           
sign_ups = extract_signups_from_logs()
export_signups_events(sign_ups)
signup_counts = count_signups_from_events()
export_employee_performance(signup_counts)

