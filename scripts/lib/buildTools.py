#!/usr/bin/python
import os
from helpers import ensureFolder, ensureVersionFolder, bash
from constants import appRepos, assetRepos, buildRepos, tick


def build(args):
    cmd = " ".join(args)
    print "Building with './build.py %s'"%cmd

def link(version):
    print "Linking skins for %s"%version

def uploadConfig(product):
    print "Uploading %s config to Amazon S3"%product
