# JsonAPP

podman build -t jsonapp:v1 .

podman run -it --rm --name jsonapp -p8000:8000 jsonapp:v1

podman run -it --rm --name jsonapp -p8000:8000 quay.io/lagomes/jsonapp:latest

curl -X POST -H "Content-Type: application/json" -d @files/response.example.json 127.0.0.1:8000 | jq

