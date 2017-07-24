#!/usr/bin/python
import sys
import scripts.lib.repoTools
import scripts.lib.assetTools
import scripts.lib.skinTools
import scripts.lib.buildTools
from scripts.lib.constants import icon, error

# SET UP 
# export PATH=$PATH:$PWD
# type this to get current working directory into the path
# so you can call this script using fun instead of ./fun


def usage():
    print "For more help, try 'fun help'"
    sys.exit(0)

def help():
    print("""Usage:

# getting started, getting up to date
fun pull                     ensures all repos are up to date

# crush assets
fun audio crush apple        create m4a and caf audio from master WAVs 
fun audio crush android      create mp3 audio from master WAVs
fun art crush [VERSION]      create 8bit art and save to VERSION folder 
                             e.g. fun art crush 15.0.1

# link assets
fun assets link master       links master assets (24bit art and WAV audio)
fun assets link [VERSION]    links versioned assets (8bit art and m4a/mp3 audio)

# skins (DK, DTP)
fun skin crush [PRODUCT] [VERSION]  create 8bit art and m4a/mp3 audio 
fun skin link master                links master skin (24bit art and WAV audio)
fun skin link [VERSION]             links versioned skin (8bit art and m4a/mp3 audio)

# build 
fun build fun_english -p apple -t release -d
                                builds the app at the current version number 
                                builds to a build folder
# publish 
fun publish fun_english -p apple -d 
                                builds a release version of the app at current version number
                                copies build to relevant builds/ folder 
                                uploads product config json to Amazon S3
""")
    sys.exit(0)



if __name__ == '__main__':

    argcount = len(sys.argv)

    # print(sys.argv)
    # print(argcount)

    if argcount < 2:
        help()

    command = sys.argv[1]

    if command == "pull":
        scripts.lib.repoTools.updateAll()

    elif command == "help":
        help()


    elif command == "assets":
        if argcount < 3:
            print error + " Missing action for assets."
            usage()
        action = sys.argv[2]
        if action == "link":
            if argcount < 4:
                print error + " Missing version for assets link."
                usage()
            version = sys.argv[3]
            scripts.lib.assetTools.link(version)
        else:
            print error + " Missing action for assets."
            usage()


    elif command == "audio":
        if argcount < 3:
            print error + " Missing action for audio."
            usage()
        action = sys.argv[2]
        if action == "crush":
            if argcount < 4:
                print error + " Missing platform for audio crush."
                usage()
            platform = sys.argv[3]
            scripts.lib.assetTools.crushAudio(platform)
        else:
            print error + " Unknown action for audio."
            usage()


    elif command == "art":
        if argcount < 3:
            print error + " Missing action for art."
            usage()
        action = sys.argv[2]
        if action == "crush":
            if argcount < 4:
                print error + " Missing version for art crush."
                usage()
            version = sys.argv[3]
            scripts.lib.assetTools.crushArt(version)
        else:
            print error + " Unknown action for art."
            usage()

    elif command == "skin":
        if argcount <= 2:
            print error + " Missing action for skin."
            usage()
        action = sys.argv[2]
        if action == "crush":
            if argcount <= 4:
                print error + " Missing product or version for skin crush."
                usage()
            product = sys.argv[3]
            version = sys.argv[4]
            scripts.lib.skinTools.crush(product, version)
        elif action == "link":
            if argcount <=3 :
                print error + " Missing version for skin link."
                usage()
            version = sys.argv[3]
            scripts.lib.skinTools.link(version)
        else:
            print error + " Unknown action for skin."
            usage()

    elif command == "build":
        # pass rest of parameters on to the build script
        if argcount <= 2:
            print error + " Missing product for build."
            usage()
        # product = sys.argv[2]
        scripts.lib.buildTools.build(sys.argv[2:])

    elif command == "publish":
        if argcount <= 2:
            print error + " Missing product for publish."
            usage()
        product = sys.argv[2]
        sys.argv.append("--publish")
        scripts.lib.buildTools.build(sys.argv[2:])
        scripts.lib.buildTools.uploadConfig(product)

    else:
        print error + " Unknown command."
        usage()

