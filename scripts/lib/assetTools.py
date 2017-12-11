#!/usr/bin/python
import os
from helpers import ensureFolder, ensureVersionFolder, bash
from constants import appRepos, assetRepos, buildRepos, tick, warn, error, displacementFolder

import datetime
now = str(datetime.datetime.now())[:16]
now = now.replace(" ", "-")
now = now.replace(":", "")

# TODO move these to INI
path_to_app = "apps/funenglish"
path_to_assets = "assets"

app_path = os.path.realpath(path_to_app)
assets_path = os.path.realpath(path_to_assets)






def crushArt(version):
    print "Crushing art to %s"%version
    # TODO move to INI
    art_script_path = "assets/art-funenglish/scripts"
    os.chdir(art_script_path)
    bash("./build.sh", version)

def crushAudio(platform, language):
    print "Crushing %s audio for %s"%(language, platform)

    # ensure audio folder is present
    audio = os.path.join(app_path, "audio")
    if not os.path.exists(audio):
        bash("mkdir", audio)

    script_path = os.path.join(assets_path, "audio-funenglish")
    os.chdir(script_path)
    command = "./create_%s_audio.sh"%platform
    bash(command)

    script_path = os.path.join(assets_path, "audio-fungerman")
    os.chdir(script_path)
    command = "./create_%s_audio.sh"%platform
    bash(command)

    script_path = os.path.join(assets_path, "audio-funsfx")
    os.chdir(script_path)
    command = "./create_%s_sfx_audio.sh"%platform
    bash(command)

    script_path = os.path.join(assets_path, "audio-funmusic")
    os.chdir(script_path)
    command = "./create_%s_music_audio.sh"%platform
    bash(command)

# if a folder is in the way, it gets moved to a time-stamped folder in __displaced__ on the app root
def displace(name, target, location):

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
        displaced = os.path.join(app_path, displacementFolder, "%s-%s"%(name, now))
        print warn + "  Moving %s folder to %s"%(location, displaced)
        bash("mv", location, displaced)

    # create the link
    bash("ln -sf", target, location) 


def link(version):
    print "Linking %s version assets"%version

    # art
    versionFolder = "24bit"
    if version != "master":
        versionFolder = os.path.join("8bit", version)
    artLink = os.path.join(assets_path, "art-funenglish", versionFolder)
    artLocation = os.path.join(app_path, "art")
    displace("art", artLink, artLocation)

    # audio
    audioLink = os.path.join(assets_path, "audio-funenglish")
    audioLocation = os.path.join(app_path, "audio", "english")
    displace("english", audioLink, audioLocation)

    # audio
    audioLink = os.path.join(assets_path, "audio-fungerman")
    audioLocation = os.path.join(app_path, "audio", "german")
    displace("german", audioLink, audioLocation)

    # TODO 
    # add spanish, french, chinese

    audioLink = os.path.join(assets_path, "audio-funsfx")
    audioLocation = os.path.join(app_path, "audio", "sfx")
    displace("sfx", audioLink, audioLocation)

    audioLink = os.path.join(assets_path, "audio-funmusic")
    audioLocation = os.path.join(app_path, "audio", "music")
    displace("music", audioLink, audioLocation)
