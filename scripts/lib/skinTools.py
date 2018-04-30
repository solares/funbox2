#!/usr/bin/python
import os
from helpers import ensureFolder, ensureVersionFolder, bash, now
from constants import appRepos, assetRepos, buildRepos, tick, warn, error, displacementFolder


# TODO move these to INI
skins_path = "assets/funenglish-skins/scripts"
app_path = "apps/funenglish"
path_to_club = "club"

# if a folder is in the way, it gets moved to a time-stamped folder in __displaced__ on the app root
def displace(name, target, location):

    # first, ensure that the target exists
    if not os.path.exists(target):
        print error + "  Target %s doesn't exist!"%target
        print "Try one of these:"
        listArtPaths()
        return


    # if it's a link, kill it
    if os.path.islink(location):
        bash("rm", location)

    # if a folder, move it out the way
    if os.path.exists(location):

        # create __displaced if not done so yet
        displaced = os.path.join(app_path, displacementFolder)
        if not os.path.exists(displaced):
            bash("mkdir", displaced)

        # move folder into displaced folder with datetime 
        displaced = os.path.join(app_path, displacementFolder, "%s-%s"%(name, now()))
        print warn + "  Moving %s folder to %s"%(location, displaced)
        bash("mv", location, displaced)

    # create the link
    bash("ln -sf", target, location) 
    bash("ls -al", location)

# ensure there's a skins folder in app_path
ensureFolder(app_path, "skins")

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

def linkClub(folderName):
	print "Linking %s skin assets"%folderName
	club_path = os.path.realpath(path_to_club)
	clubLink = os.path.join(club_path, folderName)
	clubLocation = os.path.join(app_path, "skins")
	displace("skins", clubLink, clubLocation)