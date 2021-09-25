import dropbox

class Tranferdata:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_files(self,file_from,file_to):
        # link the our dropbox account to the application
        dbx = dropbox.Dropbox(self.access_token)     
        f = open(file_from,'rb') 
        #upload these contents to the dropbox using the files_upload() method
        dbx.files_upload( f.read() , file_to)

def main():
    access_token= '4xL_15-Tap4AAAAAAAAAAVI_7Ko0iEemn7PxwQ6M_iT8AIfygrI9wM2Nk_LSq4dC'
    #creating object for class
    td = Tranferdata(access_token)
    file_from = input("Enter The File Path To Tranfer : ")
    file_to = input("Enter The Path To Upload To DropBox : ")
    #method in class is called
    td.upload_files(file_from,file_to)
    print('File Has Been Moved !!! ')

main()