import os
import ConfigParser
from constants import requiredFolders
from helpers import bash

def read(inifile):
	config = ConfigParser.RawConfigParser(allow_no_value=True)
	config.optionxform = str # this makes options case-sensitive
	config.readfp(open(inifile))
	for section in config.sections():
		print (section)
	return config

def setupFolders():
    for folder in requiredFolders:
        if not os.path.exists(folder):
            bash("mkdir", folder)

def addFolderToPath():
	bash("export PATH=$PATH:$PWD")


def setup():
	setupFolders()
	addFolderToPath()
