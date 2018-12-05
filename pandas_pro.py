import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import timedelta

# data = pd.read_csv('D:/time_entry_weekly.csv')


class Project:

    def __init__(self, data, proname):
        self.data = data
        self.proname = proname
        self.employee = data[data["Project"] == proname]["User"]
        self.tags = data[data["Project"] == proname]["Tags"]
        self.produration = data[data["Project"] == proname]["Duration"]
        self.emp_amt ={"Dhivakar Kanagaraj":500, "Harshvardhan Suresh":400, "Senthil Palanisamy":300, "Shivaraj Magadi":350}
        self.pro_data = data[data["Project"] == proname][["User", "Tags", "Duration"]].copy()
        self.u_employee = list((self.pro_data["User"].value_counts()).index)
        self.u_dur = []

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
        # print(dur[2])
        dur_hr = dur[2] / 3600
        return dur_hr
        # a = self.dur[1] / 60
        # self.dur[0] += a
        # self.dur[1] = self.dur[1] % 60
        # a = self.dur[2] / 3600
        # self.dur[0] += a
        # self.dur[2] = self.dur[2] % 3600

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
                dur[k] += Project.duration(i)[k]
        # print(dur)
        dur_hr = Project.con_to_hr(dur)
        return dur_hr
        # print(dur_hr)

    def calc_activity_summary(self):
        dic = {}
        final_dict = {}
        tem_set = set()
        em_dic = []
        for emp in self.u_employee:
            tag_dur = {}
            tag_dur1 = {}
            b = list(self.pro_data[self.pro_data["User"] == emp]["Tags"])
            dura = list(self.pro_data[self.pro_data["User"] == emp]["Duration"])
            d = []
            for j in dura:
                d.append(Project.con_to_hr(Project.duration(j)))
            for (k, l) in zip(b, d):
                if k not in tag_dur1:
                    tag_dur1[k] = [l]
                else:
                    tag_dur1[k].append(l)
            for m in tag_dur1.keys():
                a = sum(tag_dur1[m])          # SC_AS_P1
                tag_dur[m] = a
            em_dic.append(tag_dur)

        # keys as unique tags
        for x in em_dic:
            tem_set.update(set(x.keys()))
        for i in tem_set:
            final_dict[i] = []

        # final dict with key as tags and duration as values.
        # Can be displayed in dataform after transpose
        for p in final_dict.keys():
            for q in em_dic:
                final_dict[p].append(q[p] if p in q else "---")
        f_table = pd.DataFrame(data=final_dict)
        f_table.index = self.u_employee
        print('*'*25 + "ACTIVITY SUMMARY" + '*'*25)
        print(f_table.T)

    def cal_employee_summary(self):
        # pro_data = data[data["Project"] == proname][["User", "Duration"]].copy()
        # f_table1 = (pro_data["User"].value_counts())
        # print(f_table1)
        # self.u_employee = list((self.pro_data["User"].value_counts()).index)
        emp_v_time = {}
        for i in self.u_employee:
            dur_of_emp = (list(self.pro_data[self.pro_data["User"]==i]["Duration"]))
            # print(dur_of_emp)
            tdur_of_emp = Project.tduration(dur_of_emp)
            # print("Hours of emp:",tdur_of_emp)
            self.u_dur.append(tdur_of_emp)
        # print(temp)
        emp_v_time["Hours Spent"] = self.u_dur
        f_table1 = pd.DataFrame(emp_v_time)
        f_table1.index = self.u_employee
        print('*'*25 + "EMPLOYEE SUMMARY" + '*'*25)
        print(f_table1)                                                 # SC_AS_P1
        # print("Uni dur: ",self.u_dur)
        # print(emp_v_time)
        # f_table1.loc[:,'Duration'] = temp
        # print(f_table1)
        # print(plt.bar(u_employee, temp))

    def disp_bar_chart(self):
        # print("Uni employee: ",self.employee)
        # print("Uni dur: ",self.u_dur)
        t_emp_amt = []
        emp_v_amt = {}
        t_emp_amt = [self.emp_amt[i] * j for i, j in zip(self.u_employee, self.u_dur)]
        for i, j in zip(self.u_employee, t_emp_amt):
            emp_v_amt[i] = j
        # f_table = pd.DataFrame(emp_v_amt)
        plt.bar(self.u_employee, t_emp_amt)
        # print(f_table)
        # print(t_emp_amt)
        # print(emp_v_amt)
            
        # print(temp_amt)