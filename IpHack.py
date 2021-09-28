import argparse
import requests
import json
import sys
import os
from sys import argv

parser = argparse.ArgumentParser()

parser.add_argument ("-v", help= "

--[ Retrieve IP Geolocation information from: ip-api.com, ipwhois.app
--[ Donate IpHack: https://www.donationalerts.com/r/misha_korzhik
--[ Copyright (c) 2019-2020 mishakorzhik

Target/host IP address: --victim, -v
Update system IpHack: --update, -u
View more commands: --help,   -h
About information: --info,  -a", type=str, dest='target', required=True )

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
        print (a, "[Victim]:", data['query'])
        print (a, "[Type]:", data1['type'])
        print (a, "[ISP]:", data['isp'])
        print (a, "[Org]:", data['org'])
        print (a, "[Query]:", data['query'])
        print (a, "[As]:", data['as'])
        print (a, "[City]:", data['city'])
        print (a, "[Region]:", data['region'])
        print (a, "[RegionName]:", data['regionName'])
        print (a, "[Country]:", data['country'])
        print (a, "[CountryCode]:", data['countryCode'])
        print (a, "[Country Type]:", data1['country_neighbours'])
        print (a, "[Latitude]:", data1['latitude'])
        print (a, "[Longitude]:", data1['longitude'])
        print (a, "[Time zone]:", data['timezone'])
        print (a, "[Zip code]:", data['zip'])
        print (a, "[Phone]:", data1['country_phone'])
        print (a, "[Requests]:", data1['completed_requests'])
        print (" "+yellow)

except KeyboardInterrupt:
        print ('Quiting Utility! Bye Bye, Have a nice day!'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[-]"+" Please check your internet connection!"+clear)
sys.exit(1)
