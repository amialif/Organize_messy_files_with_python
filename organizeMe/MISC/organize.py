import os
from pathlib import Path
SUBDIRECTORIES = {
    "DOCUMENTS":['.pdf','.rtf','.txt'],
    "AUDIO":['.m4a','m4b','.mp3'],
    "VIDEOS":['.mov','.avi','.mp4','.wmv'],
    "IMAGES":['.jpg','.png','.jpeg']
}

def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return "MISC"       

print(pickDirectory('.pdf'))

def orgranizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = pickDirectory(fileType)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

#finally call the function
orgranizeDirectory()

