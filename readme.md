# JsonAPP

Web App for receive json post from clients, this app is using fastapi as core code

## Build App
    podman build -t jsonapp:v1 .

## Run App

### Run localy
    podman run -it --rm --name jsonapp -p8000:8000 jsonapp:v1

### Run from Quay
    podman run -it --rm --name jsonapp -p8000:8000 quay.io/lagomes/jsonapp:latest

## Post json sample
    curl -X POST -H "Content-Type: application/json" -d @files/response.example.json 127.0.0.1:8000 | jq

