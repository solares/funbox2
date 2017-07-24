#!/usr/bin/python
import os
from helpers import ensureFolder, ensureVersionFolder
from constants import appRepos, assetRepos, buildRepos, tick

from subprocess import call

def bash(*args):
    cmd = " ".join(args)
    call(cmd, shell=True)


def crushArt(version):
    print "Crushing art to %s"%version

def crushAudio(platform):
    print "Crushing audio for %s"%platform

def link(version):
	print "Linking %s version assets"%version

