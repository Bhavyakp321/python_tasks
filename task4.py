import random

def generate_emp_details(no_emp_generate):
     cities = ["Kormangala", "HSR Layout", "Ballary", "Mumbai", "Chennai", "Nellore", "Gurgaon", "Hyderabad"]

     for i in range(no_emp_generate):
         emp_id = random.randint(1,9999)
         emp_location = random.choice(cities)
         emp_salary = random.randint(20000,150000)
         yield {
            "Emp Id": emp_id,
            "Emp Location": emp_location,
            "Emp Salary": emp_salary
        }

def main():
    no_emp_generate = int(input("Enter the Number of employee details to Generate: "))

    emp_detail = generate_emp_details(no_emp_generate)

    print("*****EMPLOYEE DETAILS*****")
    
    for employee in emp_detail:
        for key, value in employee.items():
            print(key + ":", value)
        print()

main()

    
