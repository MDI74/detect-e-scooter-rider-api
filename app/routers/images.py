from app.utils.files_validator import files_validator_detect
from fastapi import UploadFile, APIRouter, HTTPException
from typing import List
from app.utils.download_zip import download_zip
from app.detection_helpers import *
import os
import shutil
import base64
import cv2
import sys

sys.path.append("..")

router = APIRouter()


@router.post("/images/detect")
def detect(files: List[UploadFile]):
    files_validator_detect(files)
    try:
        detect_results = []

        for file in files:
            with open(f'images/input/{file.filename}', "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

                detector = Detector()
                detector.load_model('./weights/best.pt')

                input_path_to_files = f'images/input/{file.filename}'
                output_path_to_files = f'images/output/{file.filename}'

                detect_result = detector.detect(source=input_path_to_files)

            cv2.imwrite(output_path_to_files, detect_result)

            with open(output_path_to_files, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())

            os.remove(input_path_to_files)

            detect_results.append(encoded_string)

        return detect_results
    except:
        raise HTTPException(status_code=400, detail='Не удалось обработать изображение')


@router.get("/images/download-zip")
def download_images_zip():
    return download_zip('images/output')
