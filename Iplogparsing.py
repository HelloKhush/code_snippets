import re
import csv
from collections import Counter
import os
#file = 'logs'
#location='/Users/khushboo.singh/Downloads/pythonproject/test/logparsing/'
#path = os.path.join(location, file)
#print('++++++++++++++')

def reader(filename):
    with open(filename) as f:
        log = f.read()
    
    regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    ip_list = re.findall(regexp,log)
    
    return ip_list

def count(ip_list):
    counter_ip = Counter(ip_list)
    return counter_ip

def outputcsv(counter_ip):
    with open('output.csv', mode = 'w') as csvfile:
        writercsv = csv.writer(csvfile)
        header = ['IP', 'Frequency']
        
        writercsv.writerow(header)
        
        for item in counter_ip:
            writercsv.writerow((item, counter_ip[item]))
            
if __name__ == "__main__":

    outputcsv(count(reader('logs')))
