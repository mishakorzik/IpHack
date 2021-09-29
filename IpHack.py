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
inf = "?fields=status,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,mobile,proxy,hosting,query"
inf1 = "/json/"

api = "http://ip-api.com/json/"
api1 = "http://ipwhois.app/json/
api2 = "https://ipapi.co/"
try:
        data1 = requests.get(api1+ip).json()
        data2 = requests.get(api+ip+inf).json()
        data3 = requests.get(api2+ip+inf1).json()
        sys.stdout.flush()
        a = lgreen+bold+"[>]"
        print (a, "[Status]:", data2['status'])
        print (a, "[Victim]:", data2['query'])
        print (a, "[Type]:", data1['type'])
        print (a, "[ISP]:", data2['isp'])
        print (a, "[Org]:", data2['org'])
        print (a, "[As]:", data2['as'])
        print (a, "[City]:", data2['city'])
        print (a, "[Region]:", data2['region'])
        print (a, "[RegionName]:", data2['regionName'])
        print (a, "[Country]:", data2['country'])
        print (a, "[CountryCode]:", data2['countryCode'])
        print (a, "[Country Type]:", data1['country_neighbours'])
        print (a, "[Latitude]:", data1['latitude'])
        print (a, "[Longitude]:", data1['longitude'])
        print (a, "[Time zone]:", data2['timezone'])
        print (a, "[Zip code]:", data2['zip'])
        print (a, "[Offset]:", data2['offset'])
        print (a, "[Utc offset]:", data3['utc_offset'])
        print (a, "[Currency]:", data2['currency'])
        print (a, "[Continent]:", data2['continent'])
        print (a, "[Country iso3]:", data3['country_code_iso3'])
        print (a, "[Country area]:", data3['country_area'])
        print (a, "[Cuntry population]:", data3['country_population'])
        print (a, "[Phone]:", data1['country_phone'])
        print (a, "[Mobile]:", data2['mobile'])
        print (a, "[Hosting]:", data2['hosting'])
        print (a, "[Proxy]:", data2['proxy'])
        print (a, "[DNS Server]:", data2['proxy'])
        print (a, "[Requests]:", data1['completed_requests'])

except KeyboardInterrupt:
        print ('Quiting Utility! Bye Bye, Have a nice day!'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[-]"+" Please check your internet connection!"+clear)
        print (red+"[-]"+" Error code: 106 DNS server refused to connect!"+clear)
        print (red+"[-]"+" Error code: 404 Not Found! No internet!"+clear)
sys.exit(1)
