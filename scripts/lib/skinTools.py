#!/usr/bin/python
import os
from helpers import ensureFolder, ensureVersionFolder
from constants import appRepos, assetRepos, buildRepos, tick

from subprocess import call

def bash(*args):
    cmd = " ".join(args)
    call(cmd, shell=True)

def crush(product, version):
    print "Crushing %s skin version %s"%(product, version)

def link(version):
	print "Linking %s version assets"%version

