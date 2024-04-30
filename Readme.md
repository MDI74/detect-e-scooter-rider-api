

### Build a docker image
```
docker build -t yolo:7.0 .
```

### Run a service
```
docker run -d --name fastapiyolov7 -p 8000:8000 yolo:7.0 
```

### Remove a service
```
docker rm fastapiyolov7
```

```
 uvicorn main:app --reload
```
