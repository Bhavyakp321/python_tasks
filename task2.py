import re

def valid_email(user_input):
    pattern = "^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
    return re.search(pattern,user_input)

def write_file(user_input):
    with open("email_list.txt","a") as file:
        file.write(user_input + '\n')

def main():
    while True:
        user_input = input("Enter the email:")

        if valid_email(user_input):
            write_file(user_input)
            print("Email is valid and saved successfully.")
        else:
            print("Invalid email address. Please enter a valid email.")

        continue_choice = input("Do you want to continue? (yes/no): ").lower()
        if continue_choice == 'no':
            file = open("email_list.txt","r")
            contents = file.read()
            print("List of Email ID's:")
            print(contents)
            file.close()
            break

main()
