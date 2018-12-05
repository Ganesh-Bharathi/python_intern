import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import timedelta
import json

# data = pd.read_csv('D:/time_entry_weekly.csv')


class Employee:

    def __init__(self, data, empname):
        self.data = data
        self.empname = empname
        self.project = data[data["User"] == empname]["Project"]
        self.tags = data[data["User"] == empname]["Tags"]
        self.empduration = data[data["User"] == empname]["Duration"]
        self.pro_amt ={"SC_AS_P1":500, "SC_EP_P1":400, "SL_Bees":300, "SL_KYC":350}
        self.emp_data = data[data["User"] == empname][["Project", "Tags", "Duration"]].copy()
        self.u_project = list((self.emp_data["Project"].value_counts()).index)
        self.u_dur = []
        self.dict = {}

    def display(self):
        print("EMPLOYEES:")
        print(self.employee)
        print("TAGS:")
        print(self.tags)
        print("DURATION:")
        print(self.produration)

    # get [h, m, s] and returns everything in hour
    def con_to_hr(dur):
        # print(dur)
        dur[0] = dur[0] * 3600
        dur[1] = dur[1] * 60
        dur[2] = dur[0] + dur[1] + dur[2]
        dur_hr = dur[2] / 3600
        return dur_hr

    # gets duration in str and returns in list[h,m,s]
    def duration(dur_str):
        return (list(map(int, [j for j in dur_str.split(':')])))

    # gets a list of dur in str and returns hours by summing all durations
    def tduration(dura):
        # if dura == None:
        #     dura = self.produration
        dur = [0, 0, 0]
        # print("Hours in fun",dura)
        for i in dura:
            for k in range(3):
                dur[k] += Employee.duration(i)[k]
        # print(dur)
        dur_hr = Employee.con_to_hr(dur)
        return dur_hr
        # print(dur_hr)

    def calc_activity_summary(self):
        tags = list(self.tags)
        duration_str = list(self.empduration)
        duration_int = []
        f_dict = {}
        temp = {}
        for i in duration_str:    
            duration_int.append(Employee.con_to_hr(Employee.duration(i)))
        for i, j in zip(tags, duration_int):
            if i not in f_dict:
                f_dict[i] = [j]
            else:
                f_dict[i].append(j)
        for i in f_dict.keys():
            temp[i] = round(sum(f_dict[i]), 3)
        # print('*'*25 + "ACTIVITY SUMMARY" +'*'*25)
        return temp
        print(temp)

    def cal_project_summary(self):
        project = list(self.project)
        duration_str = list(self.empduration)
        duration_int = []
        f_dict = {}
        temp = {}
        for i in duration_str:    
            duration_int.append(Employee.con_to_hr(Employee.duration(i)))
        for i, j in zip(project, duration_int):
            if i not in f_dict:
                f_dict[i] = [j]
            else:
                f_dict[i].append(j)
        for i in f_dict.keys():
            temp[i] = round(sum(f_dict[i]), 3)
        self.dict = temp
        print('*'*25 + "PROJECT SUMMARY" +'*'*25)
        # return temp
        print(temp)

    def disp_bar_chart(self):
        duration_str = list(self.empduration)
        tdur_of_emp = Employee.tduration(duration_str)
        for i in self.u_project:
            dur_of_pro = (list(self.emp_data[self.emp_data["Project"]==i]["Duration"]))
            tdur_of_pro = Employee.tduration(dur_of_pro)
            self.u_dur.append(tdur_of_pro)
        self.u_dur.append(tdur_of_emp)

        # print("Uni employee: ",self.project)
        # print("Uni dur: ",self.u_dur)
        t_pro_amt = []
        pro_v_amt = {}
        t_pro_amt = [self.pro_amt[i] * j for i, j in zip(self.u_project, self.u_dur)]
        for i, j in zip(self.u_project, t_pro_amt):
            pro_v_amt[i] = j
        # f_table = pd.DataFrame(emp_v_amt)
        plt.show(block = False)
        plt.bar(self.u_project, t_pro_amt)
        # print(f_table)
        # print(t_emp_amt)
        # print(emp_v_amt)
            
        # print(temp_amt)

    def wriye_report_json(self):
        print("self dict in json:",self.dict)
        with open('panda_assignment.txt', 'w') as out:  
            json.dump(self.dict, out)
        print("Json fule written")