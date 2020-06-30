from os.path import exists, join
import os
from json import dump, load


def prepareEnvironment(path):
    if not exists(path):
        os.makedirs(join(path, "work_folder"))


def saveFilesToJson(storageFiles):
        stFile = {}
        stFile["files"] = []

        for downloadfile in storageFiles:
                stFile["files"].append(storageFileToJson(downloadfile))

        with open('data.json', 'w') as outfile:  
                dump(stFile, outfile)

