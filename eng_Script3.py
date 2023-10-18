# William Eng
# weng2@oakland.edu
# Email information retrieval

import re
import os
import shelve

# email_pattern = re.compile(r'''(
#     Email:\s[a-zA-Z0-9._%+ -]+ # username
#     @ # @ symbol
#     [a-zA-Z0-9. -]+ # domain name
#     (\.[a-zA-Z]{2 ,4}) # dot-something
#     )''', re.VERBOSE)

email_pattern = re.compile(r'Email: ([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-zA-Z]{2,4})')
name_pattern = re.compile(r'Name: (.*)')

def save_to_shelf(email_dict, shelf_file):
    shelf_file = shelve.open('email_info')
    for k,v in email_dict.items():
        shelf_file[k] = v
    shelf_file.close()
    return True

def read_from_shelf(shelf_file):
    shelf_file = shelve.open('email_info')
    print("Potential users: {}".format(list(shelf_file.keys())))
    print("The email list is: {}".format(list(shelf_file.values())))
    shelf_file.close()
    return True

client_dictionary = {}
my_files = os.listdir(path ='./potential_clients')
print("******Potential Clients******")
print(("(file size, file name)").center(30))
total = 0
for file in my_files:
    file_size = os.path.getsize(os.path.join('./potential_clients', file))
    # print(str(file_size) + "\t" + file)
    print((str(file_size).rjust(5)).center(10) + "\t" + ((file).ljust(5)).center(10))
    total += file_size
    with open(os.path.join('./potential_clients', file), 'r') as f:
        content = f.read()
        name = name_pattern.search(content).group(1)
        try:
            email = email_pattern.search(content).group(1)
            # print(email)
        except AttributeError:
            email = "N/A"
            # print(email)
        if email != "N/A":
            client_dictionary[name] = email
    f.close()
# print(client_dictionary)
print("***Total size of items: " + str(total) + "***")
save_to_shelf(client_dictionary, 'email_info')
read_from_shelf('email_info')