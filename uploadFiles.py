# IMPORT NEEDED LIBRARIES
import dropbox
import os

# CREATE THE TRANSFER DATA CLASS
class TransferData:

    # CREATE THE INIT FUNCTION
    def __init__(self,accessToken):
        self.accessToken = accessToken

    # CREATE A FUNCTION FOR UPLOADING FILE ON DROPBOX
    def UploadFile(self,file_from,file_to,local_path):
        dbx = dropbox.Dropbox(self.accessToken)

        

        for root,dirs,files in os.walk(file_from):
            relativePath = os.path.relpath(local_path,file_from)
            dropbox_path = os.path.join(file_to,relativePath)

        with open(local_path,'rb') as f:
            dbx.files_upload(f.read(),dropbox_path,mode=WriteMode("overwrite"))

    
# CREATE THE MAIN FUNCTION    D:/PythonProjects/PRO_C101/test.txt 
def main():
    accessToken = '3r652F1gy6QAAAAAAAAAAXPSMVagVaDPkYVvDWbjOEJZtuf3P1gZDEfdAPilPTCz'
    transferdata = TransferData(accessToken)

    file_from = input("ENTER THE FILE NAME")
    file_to = input("ENTER THE FULL PATH")
    

    transferdata.UploadFile(file_from,file_to,local_path)



# CALL THE MAIN FUNCTION
main()