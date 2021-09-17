import dropbox
import os
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
def getAllDirectories(dbx):
    value = {}
    id=1
    result = dbx.files_list_folder(path="")
    for i in result.entries:
        value[id] = i.name
        id+=1
       
    return value
    
    #change code to be called upon user selection, testing with Dropbox Test Folder here

def getSubDirectories(dbx,directory_name):
    value = {}
    id=1
    result = dbx.files_list_folder(path="/"+directory_name)
    for i in result.entries:
        value[id] = i.name
        id+=1
       
    return value

def save_temp_file_to_dropbox(f_name,uploaded_file_url,dir,sub_dir,dbx,file):
    # file_path = os.path.join(settings.MEDIA_ROOT,uploaded_file_url) 
    # temp_file = open(file_path)
    # f = default_storage.open(os.path.join(f_name), 'r')
    # data = f.read()
    
    db_path ="/"+dir+"/"+sub_dir+"/"+f_name
    dbx.files_upload(file.read(),db_path)
#     filename="changethenamelater.pdf"
#     path = "/Dropbox Test Folder/Test1/"+filename

#     SaveFile(dbx,path)

# def SaveFile(dbx,DropboxPath):
      
#     computer_path= "/Users/prateeksrivastava/Documents/glacier_pg1.pdf"

#     dbx.files_upload(open(computer_path, "rb").read(), DropboxPath)

if __name__=='__main__':
    str = 'xyz123'
    dbx = dropbox.Dropbox(str)
    getAllDirectories(dbx)
    
