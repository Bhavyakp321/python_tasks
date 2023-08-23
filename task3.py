import re
import os

def valid_ip(user_input):
    pattern = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    return re.search(pattern,user_input)

def ping(user_input):
    return os.system('ping -n 8 {}'.format(user_input))

def write_file1(user_input):
    with open("ValidIP_details.txt","a") as file:
        file.write(user_input + '\n')

def write_file2(user_input):
    with open("InvalidIP_details.txt","a") as file:
        file.write(user_input + '\n')
    

def main():
    while True:
        user_input = input("Enter the IP Address:")

        if valid_ip(user_input):
            ping(user_input)
            write_file1(user_input)
            print({user_input}, "is Valid IP address")
        else:
            write_file2(user_input)
            print({user_input}, "is Invalid IP address")

        choice = input("Do you want to continue? (yes/no): ").lower()
        if choice == 'no':
            f1 = open("ValidIP_details.txt","r")
            content = f1.read()
            print('List of Pinging IPs: ',content)
            f1.close()
            
            f2 = open("InvalidIP_details.txt","r")
            contents = f2.read()
            print('List of Not Pinging IPs: ',contents)
            f2.close()
            break

main()






