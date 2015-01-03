#!/usr/bin/python

from pyItunes import *
from os.path import isfile
from os.path import expanduser
from os.path import dirname
from os.path import realpath
from subprocess import call

home = expanduser("~")
pwd = dirname(realpath(__file__))

scriptFile = pwd+'/removeFromiTunes.scpt'

l = Library(home+'/Music/iTunes/iTunes Music Library.xml')
filesToDelete = []

for id, song in l.songs.items():
	location = song.location
	if location is not None:
		location = '/'+location
		if not isfile(location):
			name = song.name
			filesToDelete.append(name)
print filesToDelete
args = ''
filesLen = len(filesToDelete)
if filesLen > 0:
	for i, val in enumerate(filesToDelete):
		val = val.replace(' ', '\\ ')
		if (i >= 0 and i < filesLen and filesLen > 1):
			args += val + ' '
		else:
			args += val

	cmd = "osascript '" + scriptFile +"' " + args
	print cmd
	call(cmd, shell=True)