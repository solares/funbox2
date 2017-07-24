#!/usr/bin/python
import string
import os
from helpers import ensureFolder, ensureHgFolder

# contains commands for working with build repos

# assumes we are running from apps/funenglish/scripts/build

# platforms = ["apple", "android", "amazon"] # android=Google Play
platforms = ["apple", "android"] # android=Google Play
# platforms = ["apple"] # android=Google Play
# products = ["FE", "FEC", "FETV", "FS", "FSC", "FF", "FFC", "FG", "FGC", "FC", "FCC", "FECH"]
# products = ["FE", "FEC", "FS", "FSC", "FF", "FFC", "FG", "FGC", "FC", "FCC", "FECH"]
# products = ["FE", "FEC", "FETV"]
products = ["FECH"]

# apps/builds
# apps/builds/apple
# apps/builds/android

# apps/builds/apple/FE
# apps/builds/apple/FEC
# apps/builds/apple/FS
# apps/builds/apple/FSC
# ...

# apps/builds/android/FE
# apps/builds/android/FEC
# apps/builds/android/FS
# apps/builds/android/FSC
# ...

def getRepoName(platform, product):
	return "build-%s-%s"%(platform, string.lower(product))

def wipeAndCopyIn(platform, product, sourceFolder):
	"""
	wipes the working copy of chosen build folder
	then copies content of source in
	"""
	f, existing = ensureFolder(builds, platform, product)
	os.chdir(f)
	# wipe all but the .hg folder 
	bash("find . -not -name '.hg*' -not -name '.' -not -name '..' -maxdepth 1 -exec rm -rf {} \;")
	# and copy in
	bash("cp -R %s/* %s"%(sourceFolder, f))
	return f

def commitAndTag(platform, product, version):
	f = ensureFolder(builds, platform, product)
	os.chdir(f)
	bash("hg addremove --similarity 90")
	bash("hg commit -m", version)

def tag(platform, product, version):
	f = ensureFolder(builds, platform, product)
	os.chdir(f)
	bash("hg tag ", version)

def push(platform, product, version):
	f = ensureFolder(builds, platform, product)
	os.chdir(f)
	bash("hg push")


def ensureRepos(base=""):
	builds = os.path.join(base, "builds")
	builds = os.path.normpath(builds)
	ensureFolder(builds)
	# os.chdir(builds)
	for platform in platforms:
		ensureFolder(builds, platform)
		for product in products:
			f, existing = ensureHgFolder(builds, platform, product)
			repo = getRepoName(platform, product)
			os.chdir(f)
			print "-----------------------"
			if existing:
				print "Found %s. Pulling and updating..."%repo
				print "-----------------------"
				bash("hg pull -u")
				bash("hg summary")
			else:
				# enter the folder and clone the repo
				print "Cloning %s and updating..."%repo
				print "-----------------------"
				url = "ssh://hg@bitbucket.org/solares/%s"%repo
				bash("hg clone", url, ".")
				bash("hg update")
				bash("hg summary")


