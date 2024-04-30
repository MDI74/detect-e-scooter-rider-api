from app.bridge_wrapper import YOLOv7_DeepSORT
from app.utils.download_zip import download_zip
from app.utils.files_validator import file_validator_tracking, HTTPException
from app.detection_helpers import *
from fastapi import UploadFile, APIRouter
import os
import shutil
import base64
import sys

sys.path.append("..")

router = APIRouter()


@router.post("/video/track")
def track(file: UploadFile):
    file_validator_tracking(file)

    try:
        with open(f'video/input/{file.filename}', "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        detector = Detector()
        detector.load_model('./weights/best.pt')

        tracker = YOLOv7_DeepSORT(reID_model_path="./deep_sort/model_weights/mars-small128.pb", detector=detector)

        input_path_to_file = f'video/input/{file.filename}'
        output_path_to_file = f'video/output/{file.filename}'

        tracker.track_video(
            video=input_path_to_file,
            output=f'video/output/{file.filename}',
            show_live=False,
            skip_frames=0,
            count_objects=True,
            verbose=1
        )

        with open(output_path_to_file, "rb") as video_file:
            encoded_string = base64.b64encode(video_file.read())
        os.remove(output_path_to_file)
        os.remove(input_path_to_file)

        return encoded_string
    except:
        raise HTTPException(status_code=400, detail='Не удалось обработать видео')


@router.get("/video/download-zip")
def download_video_zip():
    return download_zip('video/output')
