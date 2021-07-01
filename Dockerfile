FROM python:3.8-slim-buster
ARG host_name=test
ARG user_name
ARG user_password
ARG database_name
ENV HOST=${host_name}
ENV NAME=${user_name}
ENV PASSWORD=${user_password}
ENV DATABASE=${database_name}
WORKDIR /home/ubuntu/app
COPY ./project/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT [ "python3", "./project/app.py" ]
CMD [ ${HOST}, ${NAME},  ${PASSWORD}, ${DATABASE} ]
