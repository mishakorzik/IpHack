red='\e[1;31m'
default='\e[0m'
yellow='\e[0;33m'
orange='\e[38;5;166m'
green='\033[92m'

clear
sleep 1
echo -e "$yellow  ___                 __         .__  .__                 "
echo -e "$yellow |   | ____   _______/  |______  |  | |  |   ___________  "    
echo -e "$yellow |   |/    \ /  ___/\   __\__  \ |  | |  | _/ __ \_  __ \ "    
echo -e "$yellow |   |   |  \___  \  |  |  / __ \|  |_|  |_\  ___/|  | \/ "    
echo -e "$yellow |___|___|  /____  > |__| (____  /____/____/\___  >__|    "
echo -e "$yellow          \/     \/            \/               \/        "
echo ""
echo -e "$orange [INFO] $yellow Tool Name: IpHack  "
echo -e "$orange [INFO] $yellow Developer: Misha Korzhik " 
echo -e "$orange [INFO] $yellow License  : Apache License 2.0 "  " 


which git > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[Git].............................[ SUCCESFUL ]"
sleep 1.5
else
echo -e "$red[~]-[Git]..........................[ FAILED ]"
sleep 1.5
echo -e "$yellow[!][Installing Module Git...]"
apt install git 
fi

which python > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[Python]..........................[ SUCCESFUL ]"
sleep 1.5
else
echo -e "$red[~]-[Python].......................[ FAILED ]"
sleep 1.5
echo -e "$yellow[!][Installing Module Python...]"
apt install python > /dev/null
apt install python
apt install python2
apt install python3
pkg install pip
pkg install pip2
pip2 install --upgrade pip
fi

which lolcat > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "$green[+]-[lolcat]..........................[ SUCCESFUL ]"
sleep 1.5
else
echo -e "$red[~]-[lolcat].......................[ FAILED ]"
sleep 1.5
echo -e "$yellow[!][Installing Module lolcat...]"
apt install lolcat
fi

echo -e "$green[>]—————[Succesful Intslled]
