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
╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
"""+red)
print (lgreen+bold+" Developer: Misha Korzhik \n"+clear)
print (yellow+bold+"   Tool Version: v1.1 \n"+clear)

ip = args.target

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = lgreen+bold+"[$]"
        b = cyan+bold+"[$]"
        print (a, " <Victim:", data['query'])
        print(red+"[>]———————-–————–——[<]"+red)
        print (b, " <Status:", data['status'])
        print(red+"[>]——————-————-–———[<]"+red)
        print (a, " <Continent:", data['continent'])
        print(red+"[>]——————-————-–———[<]"+red)
        print (b, " <ContinentCode:", data['continentCode'])
        print(red+"[>]——————-————-–———[<]"+red)
        print (a, " <Country:", data['country'])
        print(red+"[>]———-———————-–———[<]"+red)
        print (b, " <CountryCode:", data['countryCode'])
        print(red+"[>]——————-—————————[<]"+red)
        print (a, " <Region:", data['region'])
        print(red+"[>]——————-—————————[<]"+red)
        print (b, " <Country:", data['country'])
        print(red+"[>]——-–————————-———[<]"+red)
        print (a, " <CountryCode:", data['countryCode'])
        print(red+"[>]——-–————————-———[<]"+red)
        print (b, " <Region:", data['region'])
        print(red+"[>]————————————-–——[<]"+red)
        print (a, " <RegionName:", data['regionName'])
        print(red+"[>]————————————-–——[<]"+red)
        print (b, " <City:", data['city'])
        print(red+"[>]——————-————-–———[<]"+red)
        print (a, " <Zip code:", data['zip'])
        print(red+"[>]——————-————-–———[<]"+red)
        print (b, " <Latitude:", data['lat'])
        print(red+"[>]———-–-———–———-——[<]"+red)
        print (a, " <Longitude:", data['lon'])
        print(red+"[>]——————-————-–———[<]"+red)
        print (b, " <Time Zone:", data['timezone'])
        print(red+"[>]———-–-———–———-——[<]"+red)
        print (a, " <Offset:", data['offset'])
        print(red+"[>]———-–-———–———-——[<]"+red)
        print (b, " <Currency:", data['currency'])
        print(red+"[>]——————-————-–———[<]"+red)
        print (a, " <ISP:", data['isp'])
        print(red+"[>]———-–-———–———-——[<]"+red)
        print (b, " <Org:", data['org'])
        print(red+"[>]——————-————-–———[<]"+red)
        print (a, " <AS:", data['as'])
        print(red+"[>]———-–-———–———-——[<]"+red)
        print (b, " <AsName:", data['asname'])
        print(red+"[>]——————-————-–———[<]"+red)
        print (a, " <Device:", data['mobile'])
        print(red+"[>]———-–-———–———-——[<]"+red)
        print (b, " <Proxy:", data['proxy'])
        print (" "+yellow)

except KeyboardInterrupt:
        print ('Quiting Utility! Bye Bye, Have a nice day!'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[-]"+" Please check your internet connection!"+clear)
sys.exit(1)
