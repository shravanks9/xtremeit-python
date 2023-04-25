from fastapi import APIRouter, UploadFile, File
import ftplib
from typing import List

router = APIRouter()

server = "store.xtremeitservices.in"
username = "storextreme@store.xtremeitservices.in"
password = "Zx!as@qw#9"

@router.post("/upload")
async def upload_files(file: UploadFile = File(...)):
    urls = []
    # Connect to the FTP server
    ftp = ftplib.FTP()
    ftp.connect(server, 21)
    ftp.login(user=username, passwd=password)
    ftp.cwd("/images")

   
    # Save the file to the local disk
    with open(file.filename, "wb") as f:
        f.write(await file.read())
    
    # Upload the file to the FTP server
    with open(file.filename, "rb") as f:
        ftp.storbinary(f"STOR {file.filename}", f)
    
    # Generate the URL for the uploaded file
    url = f"https://{server}/images/{file.filename}"
    urls.append(url)

    # Close the FTP connection
    ftp.quit()

    # Return the list of URLs
    return {"urls": urls}
