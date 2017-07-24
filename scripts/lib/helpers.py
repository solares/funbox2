#!/usr/bin/python
import os
from subprocess import Popen, PIPE, STDOUT

def bash(*args):
	cmd = " ".join(args)
	print cmd
	# p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
	p = Popen(cmd, shell=True, stdin=PIPE, stdout=STDOUT, stderr=STDOUT, close_fds=True)
	output = p.stdout.read()
	print output
	return output

def ensureFolder(*folders):
	f = os.path.join(*folders)
	if not os.path.exists(f):
		os.makedirs(f)
		return f, False
	return f, True

# def ensureHgFolder(*folders):
# 	f = os.path.join(*folders)
# 	existing=True
# 	if not os.path.exists(f):
# 		os.makedirs(f)
# 		existing=False
# 	hgf = os.path.join(f, ".hg")
# 	if not os.path.exists(hgf):
# 		existing=False
# 	return f, existing

def ensureVersionFolder(*folders):
	f = os.path.join(*folders)
	versioning=False
	if not os.path.exists(f):
		os.makedirs(f)
		existing=False
	hgf = os.path.join(f, ".hg")
	if os.path.exists(hgf):
		versioning="hg"
	gitf = os.path.join(f, ".git")
	if os.path.exists(gitf):
		versioning="git"
	return f, versioning
