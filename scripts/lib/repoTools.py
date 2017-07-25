#!/usr/bin/python
# import string
import os
from helpers import ensureFolder, ensureVersionFolder, bash
from constants import appRepos, assetRepos, buildRepos, tick


# def getRepoName(platform, product):
# 	return "build-%s-%s"%(platform, string.lower(product))

# def wipeAndCopyIn(platform, product, sourceFolder):
# 	"""
# 	wipes the working copy of chosen build folder
# 	then copies content of source in
# 	"""
# 	f, existing = ensureFolder(builds, platform, product)
# 	os.chdir(f)
# 	# wipe all but the .hg folder 
# 	bash("find . -not -name '.hg*' -not -name '.' -not -name '..' -maxdepth 1 -exec rm -rf {} \;")
# 	# and copy in
# 	bash("cp -R %s/* %s"%(sourceFolder, f))
# 	return f

# def commitAndTag(platform, product, version):
# 	f = ensureFolder(builds, platform, product)
# 	os.chdir(f)
# 	bash("hg addremove --similarity 90")
# 	bash("hg commit -m", version)

# def tag(platform, product, version):
# 	f = ensureFolder(builds, platform, product)
# 	os.chdir(f)
# 	bash("hg tag ", version)

# def push(platform, product, version):
# 	f = ensureFolder(builds, platform, product)
# 	os.chdir(f)
# 	bash("hg push")



def updateRepo(repo, protocol="ssh"):
    path = os.path.join(repo["base"], repo["path"])
    path = os.path.normpath(path)
    f, ver = ensureVersionFolder(path)

    branch = repo["branch"]

    if ver:
    	print "%s  Found repo %s"%(tick, path)
        if ver == "hg":
        	bash("hg -R", path, "pull")
        	bash("hg -R", path, "update", branch)
        else:
            bash("git -C", path, "pull")
            bash("git -C", path, "checkout", branch)

    else:
    	name = repo["name"]
    	ver = repo["ver"]
    	# enter the folder and clone the repo
        url = "ssh://hg@bitbucket.org/solares/%s"%name
        if protocol == "https":
            url = "https://bitbucket.org/solares/%s"%name
        print "%s %s"%(tick, url)
    	bash(ver, "clone", url, path)
        if ver=="hg":
            bash("hg -R", path, "update", branch)
        else:
            bash("git -C", path, "checkout", branch)





# ensure all repos are in place and updated 
def updateAll():
    protocol = "ssh"
    for repo in appRepos:
        updateRepo(repo, protocol)

    for repo in assetRepos:
        updateRepo(repo, protocol)


