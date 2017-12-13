#!/usr/bin/python
import os
from helpers import bash

# TODO move these to INI
skins_path = "assets/funenglish-skins/scripts"
app_path = "apps/funenglish"

def crush(product, version):
    print "Crushing %s skin version %s"%(product, version)
    # change to skin folder 
    # print (os.getcwd())
    os.chdir(skins_path)
    bash("./build.sh", product, version)

def link(version):
    print "Linking %s version assets"%version
    dest_path = os.path.realpath(app_path)
    os.chdir(skins_path)
    bash("./link.sh", version, dest_path)

