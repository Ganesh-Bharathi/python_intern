from pandas_emp import Employee
from pandas_pro import Project
import pandas as pd

data = pd.read_csv('D:/time_entry_weekly.csv')
emp_list = list(dict.fromkeys(list(data["User"])))
pro_list = list(dict.fromkeys(list(data["Project"])))
# print(emp_list)

def start():
    flag = 1
    a = int(input("1 for pro and 2 for emp"))
    if a == 1:
        while flag == 1:
            b = input("Enter pro name")
            if b in pro_list:
                flag = 0
                ob = Project(data, b)
                ob.calc_activity_summary()
                ob.cal_employee_summary()
                ob.disp_bar_chart()
            else:
                print("No Project found. Enter again")
    elif a ==2:
        b = input("Enter emp name")
        if b in emp_list:
            ob = Employee(data, b)
            ob.calc_activity_summary()
            ob.cal_project_summary()
            ob.disp_bar_chart()
        else:
            print("No Employee found")
    else:
        print("Wrong entry")
        start()
        
start()