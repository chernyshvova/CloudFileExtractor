from os.path import exists, join
import os
from json import dump, load
from fileSorage import StorageFile

def prepareEnvironment(path):
    if not exists(path):
        os.makedirs(join(path, "work_folder"))


def storageFileToJson(storageFile):
        newFile = {"encrypted":storageFile.encrypted,
                          "name":storageFile.name}
        
        if storageFile.encrypted == False:
                        print("save not encrypted")
                        newFile.update({
                        "checkSum":storageFile.checkSum,
                        "time":storageFile.time,
                        "type":storageFile.resolution,
                        "size":storageFile.size,
                        "key":storageFile.source,
                        "downloaded":storageFile.downloaded,
                        })
        return newFile

def saveFilesToJson(storageFiles):
        stFile = {}
        stFile["files"] = []

        for downloadfile in storageFiles:
                stFile["files"].append(storageFileToJson(downloadfile))

        with open('data.json', 'w') as outfile:  
                dump(stFile, outfile)


def saveStorageFiles(storageFiles):
        if not exists("data.json"):
                saveFilesToJson(storageFiles)

        with open('data.json') as f:
                jsonFile = load(f)
        
        for newFile in storageFiles:
                if not is_fileExistsInArray(jsonFile["files"], newFile):
                        jsonFile["files"].append(storageFileToJson(newFile))
        
        with open('data.json', 'w') as outfile:  
                dump(jsonFile, outfile)
                        
def is_fileExistsInArray(fileList, storeageFile):
        for oldFile in fileList:
                if storeageFile.name == oldFile["name"]:#change to checksum
                        return True
        
        return False