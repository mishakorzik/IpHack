import argparse
import requests
import json
import sys
import os
from sys import argv

parser = argparse.ArgumentParser()

parser.add_argument ("-v", help= "target/host IP address", type=str, dest='target', required=True )

args = parser.parse_args()

#colors
red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

#banner
print (red+"""
██╗██████╗░██╗░░██╗░█████╗░░█████╗░██╗░░██╗
██║██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░██╔╝
██║██████╔╝███████║███████║██║░░╚═╝█████═╝░
██║██╔═══╝░██╔══██║██╔══██║██║░░██╗██╔═██╗░
██║██║░░░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗
╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝"""+red)
print (lgreen+bold+"      Developer: Misha Korzhik "+clear)
print (yellow+bold+"        Tool Version: v1.1 \n"+clear)

ip = args.target

api = "http://ip-api.com/json/"
api1 = "http://ipwhois.app/json/"

try:
        data = requests.get(api+ip).json()
        data1 = requests.get(api1+ip).json()
        sys.stdout.flush()
        a = lgreen+bold+"[>]"
        print (a, "[Status]:", data['status'])
        print(red+"[+]————————————————————[+]"+red)
        print (a, "[Victim]:", data['query'])
        print(red+"[+]————————————————————[+]"+red)
        print (a, "[HostName]:", data['hostname'])
        print(red+"[+]————————————————————[+]"+red)
        print (a, "[Type]:", data1['type'])
        print(red+"[+]————————————————————[+]"+red)
        print (a, "[ISP]:", data['isp'])
        print(red+"[+]———-———————————–————[+]"+red)
        print (a, "[Org]:", data['org'])
        print(red+"[+]———-———————————–————[+]"+red)
        print (a, "[Query]:", data['query'])
        print(red+"[+]———-———————————–————[+]"+red)
        print (a, "[As]:", data['as'])
        print(red+"[+]—-————————————-–————[+]"+red)
        print (a, "[City]:", data['city'])
        print(red+"[+]————————————————————[+]"+red)
        print (a, "[Region]:", data['region'])
        print(red+"[+]—————————————–-–————[+]"+red)
        print (a, "[RegionName]:", data['regionName'])
        print(red+"[+]——————————–-–———————[+]"+red)
        print (a, "[Country]:", data['country'])
        print(red+"[+]———-——————————–—————[+]"+red)
        print (a, "[CountryCode]:", data['countryCode'])
        print(red+"[+]–——————————-————————[+]"+red)
        print (a, "[Country Type]:", data1['country_neighbours'])
        print(red+"[+]————————————————————[+]"+red)
        print (a, "[Latitude]:", data1['latitude'])
        print(red+"[+]——-———————————-—–———[+]"+red)
        print (a, "[Longitude]:", data1['longitude'])
        print(red+"[+]————-——–————————–———[+]"+red)
        print (a, "[Time zone]:", data['timezone'])
        print(red+"[+]————————————————————[+]"+red)
        print (a, "[Zip code]:", data['zip'])
        print(red+"[+]————————————————————[+]"+red)
        print (a, "[Phone]:", data1['country_phone'])
        print(red+"[+]————————————————————[+]"+red)
        print (a, "[Requests]:", data1['completed_requests'])
        print(red+"[+]————————————————————[+]"+red)
        print (" "+yellow)

except KeyboardInterrupt:
        print ('Quiting Utility! Bye Bye, Have a nice day!'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[-]"+" Please check your internet connection!"+clear)
sys.exit(1)
