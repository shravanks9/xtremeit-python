import logging
import os
from typing import List
import ftplib

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile,Form
from sqlmodel import Session

from fastapi.encoders import jsonable_encoder

from lib.database import get_session
from models.product import products

router = APIRouter()

logger = logging.getLogger("infinity-logger")



server = "store.xtremeitservices.in"
username = "storextreme@store.xtremeitservices.in"
password = "Zx!as@qw#9"

@router.post("/upload-file-data")
def create_projectmembers(
    product: products=Form(...),
    files: List[UploadFile] = File(...),
    session: Session = Depends(get_session),
):
    file_data = get_file_data(files)
    print(file_data,"###########")
    print(product,"@@@@@@@@@@")
    product = products.from_orm(product)
    session.add(product)
    session.commit()
    session.refresh(product)

    return jsonable_encoder(product)





def get_file_data(files: List[UploadFile]) -> List[str]:
    urls = []
    ftp = None
    try:
        # Connect to the FTP server
        ftp = ftplib.FTP()
        ftp.connect(server, 21)
        ftp.login(user=username, passwd=password)
        ftp.cwd("/images")

        for file in files:
            # Save the file to the local disk
            file_path = os.path.join(".", file.filename)
            with open(file_path, "wb") as f:
                f.write(file.file.read())

            # Upload the file to the FTP server
            with open(file_path, "rb") as f:
                ftp.storbinary(f"STOR {file.filename}", f)

            # Generate the URL for the uploaded file
            url = f"https://{server}/images/{file.filename}"
            urls.append(url)

    except Exception as e:
        logger.error("Error while uploading files to FTP server")
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal server error")
    finally:
        # Close the FTP connection
        if ftp is not None:
            ftp.quit()

    # Return the list of URLs
    return urls
