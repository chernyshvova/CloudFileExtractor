
from Requester import connector
from bs4 import BeautifulSoup
from os.path import join
from urllib.parse import quote_plus

class StorageFile:
    name = ""
    checkSum = ""
    time = ""
    resolution = ""
    size = 0
    source = ""
    downloaded = False
    encrypted = False

class StorageFiles:
    files = []

def get_filesList():
    url = "http://files.dp.ua/files_list"
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
        print("url is {}".format(url))
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

def parseFileInfoFromPage(page):
    metaFile = StorageFile()
    soup = BeautifulSoup(page, features="lxml")
    
    stat = soup.find('div', attrs= {'class': 'stat'})
    metaList = stat.contents
    
    metaFile.name =  parseValueFromSoupStatName(metaList[1])
    metaFile.source =  parseValueFromSoupStat(metaList[3])
    metaFile.size =  parseValueFromSoupStat(metaList[5])
    metaFile.time =  parseValueFromSoupStat(metaList[7])
    metaFile.checkSum =  parseValueFromSoupStat(metaList[9])
    return metaFile

def fileUriEncode(strFile):
    uri = strFile.find("url=") + len("url=")
    res = strFile[:uri] + quote_plus(strFile[uri:])
    return res

def parseValueFromSoupStatName(stat):
    statStr = str(stat)
    start = statStr.find("<span><b>") + len("<span><b>")
    end = statStr.find("</b></span>") 
    
    fullname = statStr[start:end]
   
    return parseNameFromFull(fullname)


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