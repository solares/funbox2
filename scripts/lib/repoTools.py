#!/usr/bin/python
import os
from helpers import ensureFolder, ensureVersionFolder, bash
from constants import appRepos, assetRepos, buildRepos, tick, coronaPath

def fetchRepo(repo, protocol="ssh"):
    path = os.path.join(repo["base"], repo["path"])
    path = os.path.normpath(path)

    f, ver = ensureVersionFolder(path)

    if ver:
        print "%s Found %s repo at %s"%(tick, ver, path)
        if ver == "hg":
            bash("hg -R", path, "pull")
        else:
            bash("git -C", path, "fetch")

    else:
        name = repo["name"]
        ver = repo["ver"]
        # enter the folder and clone the repo
        url = "ssh://hg@bitbucket.org/solares/%s"%name
        if protocol == "https":
            url = "https://bitbucket.org/solares/%s"%name
        print "%s Cloning %s"%(tick, url)
        bash(ver, "clone", url, path)


def checkoutRepo(repo, protocol="ssh"):

    path = os.path.join(repo["base"], repo["path"])
    path = os.path.normpath(path)

    ver = repo["ver"]

    revision = repo["revision"]

    print "%s Checking out  %s"%(tick, revision)
    if ver == "hg":
    	bash("hg -R", path, "update", revision)
    else:
        bash("git -C", path, "checkout", revision)


# just for the main repo
def checkout(revision):
    protocol = "ssh"
    funRepo = appRepos[0] # todo fix later properly
    funRepo["revision"] = revision
    checkoutRepo(funRepo, protocol)





# ensure all repos are in place
def fetchAll():
    protocol = "ssh"
    for repo in appRepos:
        fetchRepo(repo, protocol)

    for repo in assetRepos:
        fetchRepo(repo, protocol)

    for repo in buildRepos:
        fetchRepo(repo, protocol)


def runApp():
    bash(coronaPath, "apps/funenglish")




# def getRepoName(platform, product):
#   return "build-%s-%s"%(platform, string.lower(product))

# def wipeAndCopyIn(platform, product, sourceFolder):
#   """
#   wipes the working copy of chosen build folder
#   then copies content of source in
#   """
#   f, existing = ensureFolder(builds, platform, product)
#   os.chdir(f)
#   # wipe all but the .hg folder 
#   bash("find . -not -name '.hg*' -not -name '.' -not -name '..' -maxdepth 1 -exec rm -rf {} \;")
#   # and copy in
#   bash("cp -R %s/* %s"%(sourceFolder, f))
#   return f

# def commitAndTag(platform, product, version):
#   f = ensureFolder(builds, platform, product)
#   os.chdir(f)
#   bash("hg addremove --similarity 90")
#   bash("hg commit -m", version)

# def tag(platform, product, version):
#   f = ensureFolder(builds, platform, product)
#   os.chdir(f)
#   bash("hg tag ", version)

# def push(platform, product, version):
#   f = ensureFolder(builds, platform, product)
#   os.chdir(f)
#   bash("hg push")

