import subprocess   # first we will import the subprocess module
import os
from chardet import detect

def get_encoding(file):
    with open(file,'rb') as f:
        data = f.read()
    return detect(data)['encoding']

data = subprocess.check_output(['netsh','wlan','show','profiles']).decode(get_encoding).split('\n') # now we will store the profiles data in the "data" variable by
                                                                                               # running the 1st cmd command using subprocess.check_output
profiles =  [i.split(":")[1][1:-1] for i in data  if "All User Profile" in i]  # now we will store the profile by converting them to list

# using  for loop in python we re checking and printing the Wifi
# passwords  if they  are avaiable using the 2nd cmd command
for i in profiles:
    # running the 2nd cmd command to check  passwords
    results = subprocess.check_output(['netsh','wlan','show','profile',i,'key = clear']).decode(get_encoding).split('\n')
    # storing passwords after converting them to list
    results = [j.split(":")[1][1:-1]  for j in results if " Key Content" in j]
    # printing the profiles(wifi name) with their passwords using
    # try and except
try:
    print("{:<30} | {:<}".format(i,results[0]))
except IndexError:
    print("{:<30} | {:<}".format(i, ""))
except subprocess.CalledProcessError:
    print("{:<30} | {:<}".format(i, "ENCODING ERROR"))
print("")