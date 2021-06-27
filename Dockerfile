FROM python:3.8-slim-buster
ARG creds
ENV CREDENTIALS=${creds}
WORKDIR /home/ubuntu/app
COPY ./project/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "./project/app.py" , ${CREDENTIALS}]
