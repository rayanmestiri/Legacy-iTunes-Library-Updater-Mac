#!/bin/bash
str=""
argCount=0
for thing in "$@"
do
	if [ $argCount -eq 0 ]
	then	
		str=${thing}
	else
		str+=" "${thing}
	fi
	argCount=$((argCount+1))
done

osascript ~/Library/Scripts/Folder\ Action\ Scripts/addFolderAction.scpt "$str"