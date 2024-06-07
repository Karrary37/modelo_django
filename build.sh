aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 381492111037.dkr.ecr.us-east-1.amazonaws.com

docker build -t django-modelo -f Dockerfile .

docker tag django-modelo:latest 381492111037.dkr.ecr.us-east-1.amazonaws.com/django-modelo:latest

docker push 381492111037.dkr.ecr.us-east-1.amazonaws.com/django-modelo:latest