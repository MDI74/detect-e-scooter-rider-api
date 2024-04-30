import os
import zipfile
import io
from fastapi import Response


def download_zip(folder_path: str):
    buffer = io.BytesIO()

    with zipfile.ZipFile(buffer, 'w') as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))

    buffer.seek(0)
    content = buffer.getvalue()

    response = Response(content, media_type="application/zip")
    response.headers["Content-Disposition"] = "attachment; filename=results.zip"

    return response
