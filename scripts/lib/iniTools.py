import os
import ConfigParser
from constants import requiredFolders
from helpers import ensureFolder, bash

def read(inifile):
	config = ConfigParser.RawConfigParser(allow_no_value=True)
	config.optionxform = str # this makes options case-sensitive
	config.readfp(open(inifile))
	for section in config.sections():
		print (section)
	return config

def setupFolders(cwd):
    for folder in requiredFolders:
    	ensureFolder(cwd, folder)

def addFolderToPath(cwd):
	bash("export PATH=$PATH:%s"%cwd)

def setup(cwd):
	setupFolders(cwd)
	addFolderToPath(cwd)
