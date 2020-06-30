
from Requester import connector
from bs4 import BeautifulSoup
from os.path import join, exists
from os import mkdir, rmdir
from urllib.parse import quote_plus
from connector.HTTPTools import download_file
from shutil import rmtree
from humanfriendly import parse_size
from explorer import saveFilesToJson, saveStorageFiles, readStorageFiles
from SitesInfo import SiteInfo

class StorageFile:
    name = ""
    checkSum = ""
    time = ""
    resolution = ""
    size = 0
    source = ""
    downloaded = False
    encrypted = False

def get_filesList():
    url = SiteInfo.FILELIST_URL
    conx = connector()
    conx.get_http_request(url)
    responsePage = conx.get_body()
    fileList = parseFileList(responsePage)
    return fileListToFiles(fileList)


def parseFileList(page):
    result = []
    soup = BeautifulSoup(page, features="lxml")
    for link in soup.findAll("a"):
        suspect = str(link.get("href"))
        if suspect.startswith("file"):
            result.append(suspect)
    return result


def fileListToFiles(filelist):
    conx = connector()
    storegeFiles = []
    for i in range(0, 7):#filelist
        url = join("http://files.dp.ua/", fileUriEncode(filelist[i]))
        print("saving url {}".format(url))
        conx.get_http_request(url)
        responsePage = conx.get_body()

        if is_encrypted(responsePage):
            metaFile = StorageFile()
            metaFile.encrypted = True
            metaFile.name = parseNameFromFull(filelist[i])
            storegeFiles.append(metaFile)
        else:
            storegeFiles.append(parseFileInfoFromPage(responsePage))
    return storegeFiles

def getCArg(page):
    
    start = page.find("&c=")
    end = page[start:].find("\"")
    return page[start: start +end]

def parseFileInfoFromPage(page):
    metaFile = StorageFile()
    soup = BeautifulSoup(page, features="lxml")
    
    stat = soup.find('div', attrs= {'class': 'stat'})
    metaList = stat.contents
    
    metaFile.name =  parseValueFromSoupStatName(metaList[1])
    metaFile.source =  parseValueFromSoupStat(metaList[3]) + getCArg(str(page))
    metaFile.size =  getSizeBytes(parseValueFromSoupStat(metaList[5]))
    metaFile.time =  parseValueFromSoupStat(metaList[7])
    metaFile.checkSum =  parseValueFromSoupStat(metaList[9])
    metaFile.resolution = metaFile.name[metaFile.name.rfind(".")+1:]
    return metaFile

def fileUriEncode(strFile):
    uri = strFile.find("url=") + len("url=")
    res = strFile[:uri] + quote_plus(strFile[uri:])
    return res

def parseValueFromSoupStatName(stat):
    statStr = str(stat)
    start = statStr.find("<span><b>") + len("<span><b>") -1
    end = statStr.find("</b></span>") 
    
    fullname = statStr[start+1:end]
    return fullname


def parseNameFromFull(full):
    uri = full.find("url=") + len("url=")
    res = full[uri:]
    return res

def parseValueFromSoupStat(stat):
    statStr = str(stat)
    start = statStr.find("<span>") + len("<span>")
    end = statStr.find("</span>") 
    return statStr[start:end]


def parseTypeFromFullName(full):
    name = parseNameFromFull(full)
    return  name[name.rfind("."):]

def is_encrypted(page):
    soup = BeautifulSoup(page, features="lxml")
    stat = soup.find('div', attrs= {'class': 'stat'})
    if stat is None:
        return True
    return False

def downloadFiles(filelist):

    for file in filelist:
        if file["encrypted"] == True:
            continue
        path = preparefolderForFile(file)
        fileUri = SiteInfo.FILE_URL + file["key"]
        print("downloading file:{}".format(file["name"]))
        download_file(fileUri, join(path, file["name"]))
    
def preparefolderForFile(file):
        if not exists("storage"):
                mkdir("storage")
        
        if exists(join("storage", file["name"])):
            rmtree(join("storage", file["name"]))
        mkdir(join("storage", file["name"]))
        return join("storage", file["name"])


def getSizeBytes(sizeStr):
    return parse_size(sizeStr)

def updateInfo():
    filelist = get_filesList()
    saveStorageFiles(filelist)

def run_downloader(filter = False):
    filelist = readStorageFiles()
    downloadFiles(filelist)