import gofile as go

def file_upload(file):
    a=1
    cur_server= go.getServer()
    print(f"El servidor es {cur_server}")
    url= go.uploadFile(file)
    print(f"Download file here: \n{url['downloadPage']}")

if __name__=="__main__":
    file_upload('banner.jpg')