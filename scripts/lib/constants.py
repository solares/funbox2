coronaPath = "/Applications/Corona/Corona\ Simulator.app/Contents/MacOS/Corona\ Simulator"

# app repos
appRepos = [
    {"base":"apps", "path":"funenglish", "name":"funenglish2", "ver":"git", "branch":"_master"}, 
]

# asset repos
assetRepos = [
    {"base":"assets", "path":"art-funenglish", "name":"art-fejr", "ver":"git", "branch":"master"}, 
    {"base":"assets", "path":"audio-funenglish", "name":"audio-funenglish", "ver":"hg", "branch":"default"}, 
    {"base":"assets", "path":"audio-funsfx", "name":"audio-funsfx", "ver":"hg", "branch":"default"}, 
    {"base":"assets", "path":"audio-funmusic", "name":"audio-funmusic", "ver":"hg", "branch":"default"}, 
    # {"base":"assets", "path":"funenglish-skins", "name":"funenglish-skins", "ver":"git", "branch":"master"}, 

    # {"base":"assets", "path":"audio-fungerman", "name":"audio-fungerman", "ver":"hg", "branch":"default"}, 
    # "audio-funspanish", 
    # "audio-funchinese", 
    # "audio-funfrench", 
    # "audio-fungerman", 

    # "art-stories",
    # "audio-stories",
    # "art-abcgalaxy",
    # "audio-abcgalaxy",
    
]

buildRepos = [

]

displacementFolder = "__displaced__"

requiredFolders = [
    "apps",
    "assets",
    "builds"
]

# icon="\xF0\x9F\x8E\x93 " 
icon =""
tick = "\xE2\x9C\x85"
error="\xE2\x9B\x94"
warn="\xE2\x9C\x8B"
