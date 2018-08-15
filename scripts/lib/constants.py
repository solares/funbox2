coronaPath = "/Applications/Corona/Corona\ Simulator.app/Contents/MacOS/Corona\ Simulator"

# app repos
appRepos = [
    {"base":"apps", "path":"funenglish", "name":"funenglish2", "ver":"git", "branch":"_master"}, 
]

# asset repos
assetRepos = [
    # {"base":"assets", "path":"art-funenglish2", "name":"art-funenglish2", "ver":"hg", "branch":"default"}, 

    # {"base":"assets", "path":"art-funenglish", "name":"art-funenglish", "ver":"hg", "branch":"default"}, 
    # {"base":"assets", "path":"audio-funenglish", "name":"audio-funenglish", "ver":"hg", "branch":"default"}, 
    # {"base":"assets", "path":"audio-funsfx", "name":"audio-funsfx", "ver":"hg", "branch":"default"}, 
    # {"base":"assets", "path":"audio-funmusic", "name":"audio-funmusic", "ver":"hg", "branch":"default"}, 
    # {"base":"assets", "path":"funenglish-skins", "name":"funenglish-skins", "ver":"git", "branch":"master"}, 

    # {"base":"assets", "path":"audio-fungerman", "name":"audio-fungerman", "ver":"hg", "branch":"default"}, 
    {"base":"assets", "path":"audio-funspanish", "name":"audio-funspanish", "ver":"hg", "branch":"default"}, 

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
    {"base":"apps/builds", "path":"apple/build-apple-fc", "name":"build-apple-fc", "ver":"hg", "branch":"default"}, 
    {"base":"apps/builds", "path":"apple/build-apple-fs", "name":"build-apple-fs", "ver":"hg", "branch":"default"}, 
    {"base":"apps/builds", "path":"apple/build-apple-fg", "name":"build-apple-fg", "ver":"hg", "branch":"default"}, 
    
    {"base":"apps/builds", "path":"apple/build-apple-fec", "name":"build-apple-fec", "ver":"hg", "branch":"default"}, 
    {"base":"apps/builds", "path":"apple/build-apple-fsc", "name":"build-apple-fsc", "ver":"hg", "branch":"default"}, 
    {"base":"apps/builds", "path":"apple/build-apple-fgc", "name":"build-apple-fgc", "ver":"hg", "branch":"default"}, 
    {"base":"apps/builds", "path":"apple/build-apple-ffc", "name":"build-apple-ffc", "ver":"hg", "branch":"default"}, 
    {"base":"apps/builds", "path":"apple/build-apple-fcc", "name":"build-apple-fcc", "ver":"hg", "branch":"default"}, 

    {"base":"apps/builds", "path":"apple/build-apple-fetv", "name":"build-apple-fetv", "ver":"hg", "branch":"default"}, 

    
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
