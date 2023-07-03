# base image
FROM python:3
# metadata info
LABEL maintainer="Henri Vandersleyen" email="hvandersleyen@gmail.com"
# exposing container port to be the same as streamlit default port
EXPOSE 6023
# set work directly so that paths can be relative
WORKDIR /usr/src/app
# copy to make usage of caching
COPY requirements.txt ./
#install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt
# copy code itself from local file to image
COPY . .
CMD scrapy crawl xkcdDocker