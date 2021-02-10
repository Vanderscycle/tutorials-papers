# base image
FROM python:slim
# metadata info
LABEL maintainer="Henri Vandersleyen" email="hvandersleyen@gmail.com"
# exposing container port to be the same as streamlit default port
EXPOSE 5000
# set work directly so that paths can be relative
WORKDIR /usr/src/app
# copy to make usage of caching
COPY requirements.txt ./
#install dependencies
RUN pip install -r requirements.txt
# copy code itself from local file to image
COPY . .
RUN chmod +x /usr/src/app/demonstrations/start.sh
# starting it automatically is a bad idea since it will go in a forever loop
# use : # docker run -it data_structure_app:beta-pre-prod /bin/bash
# CMD bash start.sh