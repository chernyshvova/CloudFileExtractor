from Requester import connector
from fileSorage import get_filesList, StorageFile
from explorer import saveFilesToJson, saveStorageFiles



filelist = get_filesList()


saveStorageFiles(filelist)
#saveFileToJson(filelist)