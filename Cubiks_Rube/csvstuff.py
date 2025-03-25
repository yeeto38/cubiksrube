import csv
import os
import numpy as np
from universal import resource_path

def csvwriter(time, scramble):
    with open (resource_path('times.csv'), 'a+') as csvfile:
        csvwriting = csv.writer(csvfile)
        csvwriting.writerow([time, scramble])

def file_exists():
# Check if times.csv exists, if not create it with headers
    prevsolves = np.zeros(12)
    if not os.path.exists(resource_path('times.csv')):
        with open(resource_path('times.csv'), 'w') as csvfile:
            csv.writer(csvfile)
    with open(resource_path('times.csv'), 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            prevsolves = np.roll(prevsolves, 1)
            prevsolves[0] = float(row[0])
    return prevsolves