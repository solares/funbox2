#!/usr/bin/python
import os
from helpers import ensureFolder, ensureVersionFolder, bash
from constants import appRepos, assetRepos, buildRepos, tick

# TODO move these to INI
path_to_app = "apps/funenglish"

def build(args):
    script_path = os.path.join(path_to_app, "scripts", "build")
    os.chdir(script_path)
    args.insert(0, "python build.py")
    bash(*args)

def publish(args):
	pass

def uploadConfig(product):
    print "Uploading %s config to Amazon S3"%product

# shows the current status of the the project
def status():
	# first show branch and commit of the principal app repo
	bash("git", "-C", path_to_app, "status")
