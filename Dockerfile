FROM python:3.8-slim-buster
WORKDIR /home/ubuntu/app
COPY ./project/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT [ "python3", "./project/app.py" ]
