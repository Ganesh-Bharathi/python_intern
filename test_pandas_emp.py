import unittest
from pandas_emp import Employee
import pandas as pd

data = pd.read_csv('D:/time_entry_weekly.csv')

class Test_Pandas_emp(unittest.TestCase):

    def test_activity_summary(self):
        ob = Employee(data, "Senthil Palanisamy")
        self.assertEqual(ob.calc_activity_summary(), {'Coding & Unit Testing': 13.123, 'Planning & Management': 3.9, 'Training': 0.417, 'Design & Analysis Review': 2.809, 'Research & Exploration': 10.13, 'Documentation': 5.576})

if __name__ == "__main__":
    unittest.main()