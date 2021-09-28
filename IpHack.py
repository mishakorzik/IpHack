import argparse
import requests
import json
import sys
import os
from sys import argv

parser = argparse.ArgumentParser()

parser.add_argument ("-t", help= "target/host IP address", type=str, dest='target', required=True )

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
print (yellow+bold+"      Developer: Misha Korzhik "+clear)
print (yellow+bold+"        Tool Version: v1.1 \n"+clear)

ip = args.target
inf = "?fields=asname,reverse,mobile,proxy,hosting,offset,currency,continent"
inf1 = "/json/"

api = "http://ip-api.com/json/"
api1 = "http://ipwhois.app/json/"
api2 = "http://edns.ip-api.com/json/"
api3 = "https://ipapi.co/"

try:
        data = requests.get(api+ip).json()
        data1 = requests.get(api1+ip).json()
        data2 = requests.get(api+ip+inf).json()
        data3 = requests.get(api2+ip).json()
        data4 = requests.get(api3+ip+inf1).json()
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
        print (a, "[Offset]:", data2['offset'])
        print (a, "[Utc offset]:", data4['utc_offset'])
        print (a, "[Currency]:", data2['currency'])
        print (a, "[Continent]:", data2['continent'])
        print (a, "[Country iso3]:", data4['country_code_iso3'])
        print (a, "[Country area]:", data4['country_area'])
        print (a, "[Cuntry population]:", data4['country_population'])
        print (a, "[Phone]:", data1['country_phone'])
        print (a, "[Mobile]:", data2['mobile'])
        print (a, "[Hosting]:", data2['hosting'])
        print (a, "[Proxy]:", data2['proxy'])
        print (" "+lgreen)
        print (a, "[DNS Server]:", data2['proxy'])
        print (a, "[Geolocation]:", data3['geo'])
        print (a, "[Requests]:", data1['completed_requests'])
        print (" "+yellow)

except KeyboardInterrupt:
        print ('Quiting Utility! Bye Bye, Have a nice day!'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[-]"+" Please check your internet connection!"+clear)
        print (red+"[-]"+" Error code: 106 DNS server refused to connect!"+clear)
        print (red+"[-]"+" Error code: 404 Not Found! No internet!"+clear)
sys.exit(1)
