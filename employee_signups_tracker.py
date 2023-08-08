import re
import os

def search_level_events(file_path):
    level_pattern = input("\nType in log level (e.g., INFO, FINE): ")
    level_pattern = level_pattern.upper()
    logs_level = []
   
    with open(file_path, 'r') as log_file:
        for log in log_file:
            if level_pattern not in log:
                continue
           
            result = re.search(r'\b{}\b'.format(level_pattern), log)
            if result:
                logs_level.append(log)


    print("\n---------------------------------------------------------------------------------")
    if not logs_level:
        print("Level not found. Available levels include: Warning, Info, Config, Fine, Finer")
    for log_level in logs_level:
        print(log_level, end = '')
    print("---------------------------------------------------------------------------------\n")
     
     
def search_message_events(file_path):
    message_pattern = input("\nEnter log message (e.g., new transaction): ")
    message_list_pattern = message_pattern.split()
    found_messages = []
   
    with open(file_path, 'r') as log_file:
        for log in log_file:
            if all(re.search(r': .*{}.*'.format(message.lower()), log.lower()) for message in message_list_pattern):
                found_messages.append(log)


    print("\n---------------------------------------------------------------------------------")
    if not found_messages:
        print("No messages found.")
    else:
        for message in found_messages:
            print(message, end = '')
    print("---------------------------------------------------------------------------------\n")




def main():
    loop = True
    initial_query = False
    file_path = "../files/pos_logs.txt"
    file_path = os.path.abspath(file_path)
   
    while loop:
        try:
            answer = int(input("\nEnter Selection.\n1: Search an event based on its log level.\n2: Search an event based on its log message.\n--> "))
            if  0 < answer < 3:
                if answer == 1:
                    search_level_events(file_path)
                if answer == 2:
                    search_message_events(file_path)
               
                initial_query = True
        except ValueError:
            continue
   
        if initial_query == False:
            continue
       
        while True:
            try:
                loop_answer = int(input("Another search query?\n1: Yes.\n2: No.\n--> "))
                if 0 < loop_answer < 3:
                    if loop_answer == 1:
                        loop = True
                        break
                    else:
                        loop = False
                        break
                else:
                    print("")
                           
            except ValueError:
                print("")
           
   
main()
