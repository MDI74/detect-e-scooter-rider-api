FROM python:3.9

RUN apt-get update \
    && apt-get -y install python3-pip \
    && apt-get install python-is-python3\
    && apt-get install -y --no-install-recommends ffmpeg libsm6 libxext6 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip --no-cache-dir


WORKDIR /code

COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]