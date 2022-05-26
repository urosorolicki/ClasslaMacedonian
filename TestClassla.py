import classla
import cyrtranslit
import csv
from setuptools import find_packages, setup
import pandas as pd



cyrtranslit.to_cyrillic('mk')

with open("TestAlgolija.csv") as f, open("TestClasslaMakedonski.csv", "w") as w:
    lines = list(f)
    w.write(lines[0])
    
def generate_dec_f2f(f1, f2):
   with open(f1, 'r', encoding='utf8') as TestAlgolija:
        with open(f2, 'w', encoding='utf8', newline='') as TestClasslaMakedonski:
            csvwriter = csv.writer(TestClasslaMakedonski)
                
            print()
                    
f1 = "/Users/ladmin/Desktop/TestAlgolija.csv"
f2 = "/Users/ladmin/Desktop/TestClasslaMakedonski.csv"
generate_dec_f2f(f1, f2)                    