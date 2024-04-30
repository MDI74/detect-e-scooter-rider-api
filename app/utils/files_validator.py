import os
from typing import List
from fastapi import UploadFile, HTTPException


def files_validator_detect(files: List[UploadFile]):
    for file in files:
        _, file_extension = os.path.splitext(file.filename)
        if file_extension != '.jpg' and file_extension != '.png' and file_extension != '.jpeg':
            raise HTTPException(status_code=400, detail="Расширения файлов должно быть PNG или JPG")


def file_validator_tracking(file: UploadFile):
    _, file_extension = os.path.splitext(file.filename)
    if file_extension != '.mp3' and file_extension != '.mp4':
        raise HTTPException(status_code=400, detail="Расширения файла должно быть MP4")
