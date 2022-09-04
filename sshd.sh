#!/usr/bin/bash
cd /etc/ssh

# Assign the filename
filename="sshd_config"
 # Take the search string
# Assign the filename
#read -p "Enter the search string: " search
search=22
# Take the replace string
read -p "Enter the Port number: " replace
#echo $replace
#if [[$replace -gt 1024] && [$replace -lt 65536]]; then
	#echo $replace
	if [[ $search != "" && $replace != "" ]]; then
        sed -i "s/$search/$replace/" $filename
	exit
	su Hadir
	fi
#else
#	echo "invalid port number please enter a number > 1024 and <65536" 
#fi

