# Mastering Docker after the initial trauma

After a very brief overview and usage during my data science bootcamp at lighthouse lab I was left very confused and not being able to fully grasp how powerful a dockerized application can be. To learn about Docker, we will build our own website using streamlit, and dockerize it. This way I hope that you will be able to showcase your data science skills and past projects to future employers without having to worry about silly things like hardware or OS.

I can't cover all the theory, nor can I cover it better than the references listed in the *Additional ressources and reading* section. Please take this tutorial as a walkthrought where I highly encourage to go off the beaten path, try, fail and learn for it is how I learned.

This tutorial will be done using a Linux distribution(Ubuntu), and Python.
## What is Docker
Docker is a tool created for the sole purpose of packaging a single process into a self enclosed containers, which can be run independent of the host hardware and OS configuration. If the container can run on your local machine, it will run on any machine hosting the container.  

## Docker containers vs Virtual Machine 
One of the main alternative to a Docker is the usage of a Virtual Machine. They are fairly common as you can, for example, run previous version of windows or other distros inside windows. A virtual machine is isolated from the hardware (often server hardware) it is running on meaning that any problems with the virtual machine will not impact the host. Each virtual machine are assigned its own virtual hardware (mapped on the hardware of the server) that is not shared accross multiple virtual machine instances. 

A virtual machine is essentially a virtual computer executed on server hardware and controlled through the server's hypervisor. Each virtual machine have their own isolated OS/distros, binaries and libraires required to run the application.

The life-cyle of a virtual machine is also intended to be longer than that of a container, and building, running, and stopping a virtual machine takes significantly longer than a docker container. 

![img](./images/docker-vm-container.png)

A docker container is not a virtual machine, but as described in Docker up & running, is a lightweight wrapper around a single process (your app). Containers, unlike virtual machines, are not isolated from their hosts as they share their host OS kernel. As the host you can peek inside each running containers and inspect their content.
```
docker exec -it {nameOfContainer} bash
```
Unlike virtual machine, the hypervisor is replaced by the docker engine or daemon which runs in the background and is required for any docker command and operations to work. The docker engine, unlike the hypervisor, can decide the allocation of the host's ressources to individual containers leading to better service. Because virtual machines are virtual abstractions of server hardware, their ressources are set and cannot be easily reallocated. This can lead to an unbalanced load accross all virtual machines meaning that one virtual machine is overloaded while other instances are underutilized.

Essentially virtual machine isolate entire OS/distros while docker isolate only the application leading to greater efficicy in server ressources utilization.

## installing Docker
Docker docs offers a very straightforward [installation](https://docs.docker.com/engine/install/ubuntu/). I highly recommend you follow the installation ste-by-step.

To confirm proper installation type in the terminal
```
docker ps
```
of which you should see the following heading
```
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
```

## Docker images
A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.Container images become containers at runtime and in the case of Docker containers - images become containers when they run on Docker Engine.

The image is layered because its construction follows a chronological order detailed in a Dockerfile. You do not need a Dockerfile to build an image as it can be done through the command line interface.

One of the advantage of a docker image is that each image is a snapshot of your program. So if a container from a newer image doesn't run proprely you can remove the container and recreate it from a previous image.

## Docker containers
A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another. Each containers are run from a docker image.

![Main idea behind](./images/servlet.ImageServer.jpeg)

## Hosting images
Much like Github, you can push and pull images using [Docker hub](https://hub.docker.com/). One of the great thing about Docker hub is that you can have one private container image hosted for free while the rest are publicly hosted.

### Pulling our first image
As the sacred words of hello-world must be enunciated when learning a new language or system, we will pull the hello world container from Docker hub. You can find it [here](https://hub.docker.com/_/hello-world)
```
docker pull hello-world
```
We now need to confirm that the image is available and we can use the following commands for that:
```
docker images
#or
docker image ls
```
We should see something like this in the CLI:
```
REPOSITORY                   TAG                 IMAGE ID            CREATED             SIZE
hello-world                  latest              bf756fb1ae65        11 months ago       13.3kB
```
To run a container from the image we execute the following command
```
#--name allows us to give a meaningful name to our container otherwise a random one will be assigned
docker run --name test hello-world
```
The run command should give you a greeting message from the container. You can however access the logs of a container, whether it is running or stopped, using:
```
# where container id/names is the respective name of the container you want to inspect
docker logs {CONTAINER ID/NAMES}
```

## Installing Streamlit
[Streamlit](https://www.streamlit.io/) allows data scientist who are not yet savvy in front-end devellopment to create beautiful and interactive apps in a short time. 
```
pip install streamlit
```
For a quick introduction on its capabilities:
```
streamlit hello
```
I highly recommend reading the [documentation](https://docs.streamlit.io/en/stable/) while creating your app as it is well written. 

Before moving on, it is important to remember that Streamlit is still in devellopment and you can contribute to the [project](https://github.com/streamlit/streamlit) 

## Creating our website
Navigating to any section of the drive we create the folder which will contain  all the source code.
```
mkdir streamlitWebsite
```
We will organize the website in the following fashion as we want to separate files based on their purpose. This is especially important in the future when we want a separate folder for our data, image, etc.
```
# current structure of our folder
.
└── src
    └── app.py 
```
You use the [tree](https://www.cyberciti.biz/faq/linux-show-directory-structure-command-line/) to obtain the same visualization as above. Inside the app file we will create a very simple hello world message.
```python
import streamlit as st

def helloworld():
    st.title("Henri Vandersleyen's Website")
    st.header("Hello World!")

helloworld()
```
Before packaging this simple app into a container we must confirm that it is working. 
```
# streamlit run {fileLocation}
streamlit run ./src/app.py 
```
You should be greeted with the following message:
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.95:8501
```
After confirming that everything is in order we can package the app into a container. Of note, please change and play with your streamlit app file using the [documentation](https://docs.streamlit.io/en/stable/api.html). Just ensure that prior containerizing the app it is working locally.

## Requirements.txt
the requirements.txt file is a simple text file used by Dockerfile to specify what python packages are required to run the project. You can do so manually by writting each and every indiuvidual module used in your porject or you can use a Pip requirements.txt generator based on imports in project. In our case we will be using [pipreqs](https://pypi.org/project/pipreqs/). 
```
# synthax pipreqs {folderLocation}
pipreqs ./streamlitWebsite/
```
Which should output:
```
INFO: Successfully saved requirements file in ./streamlitWebsite/requirements.txt
```
Peeking inside the file we should see the following:
```
# of note you can remove the version and simply type streamlit
streamlit==0.72.0
```
Also, ensure that you update the requirements file after adding or removing modules in your py file. Otherwise, the app inside the container will not run as it will be missing dependencies.
```
# --force allows you to overwrite the requirement file
pipreqs --force ./streamlitWebsite/
```

if you are having issues please confirm the folder location and the presence of a py file. It is very important to be aware of what version of Python you are using as we will be using the same version for our Dockerfile base image. 
```
python -V
```
In my case I am currently using Python 3.8.5
## Dockerfile 

![xkcd1988](./images/containersxkcd.png)

A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image. To create a Dockerfile we simply type the following in the app folder.
```
# there are no extensions after Dockerfile
touch Dockerfile
```
Our file structure should look like this: 
```
.
├── Dockerfile
├── requirements.txt
└── src
    └── app.py

1 directory, 3 files
```
Looking at the base image of [python](https://hub.docker.com/_/python) in docker hub we are interrested in two section the simple tags (version of the base image), and how to use this image which gives us a template to construct our app from.You should also see different versions using duster, alpine, slim, etc. Please check this [reference](https://medium.com/swlh/alpine-slim-stretch-buster-jessie-bullseye-bookworm-what-are-the-differences-in-docker-62171ed4531d) to learn more about them. 

Looking at the template we will copy the following inside the Dockerfile with slight modification.
```
# base image
FROM python:3
# metadata info
LABEL maintainer="Henri Vandersleyen" email="hvandersleyen@gmail.com"
# exposing container port to be the same as streamlit default port
EXPOSE 8051
# set work directly so that paths can be relative
WORKDIR /usr/src/app
# copy to make usage of caching
COPY requirements.txt ./
#install dependencies
RUN pip install -r requirements.txt
# copy code itself from local file to image
COPY . .
CMD streamlit run ./src/app.py
```
## Our first image
Now that we have the Dockerfile, requirements.txt and the app working locally we are ready to containerize our folder. <span style="color:red">The dot</span> after streamlit reference all files in the folder you are currently on.
```
# while in the streamlitWebsite Folder
# docker build [OPTIONS] PATH | URL | -
docker build -t streamlit . 
```
the -t represent the 'name:tag(optional)' format given to your image. To make version control easier to discern you can use tags in the following format:
```
docker build -t streamlit:beta-pre-prod . 
docker build -t streamlit:latest .
```
<span style="color:red">Before moving forward</span>, if you ran any of the build commands above you were most likely greeted by a confusing error message from Docker. Debugging a Dockerfile can be difficult, since the error message can overflow the CLI terminal so this is why we can have the terminal output saved into a log file.
```
docker build -t streamlit:beta-pre-prod .>./log.txt
```
Analysing the log file we find the following error at line ~145:
```
[91m  ERROR: Command errored out with exit status 1:
   command: /usr/local/bin/python /usr/local/lib/python3.9/site-packages/pip install --ignore-installed --no-user --prefix /tmp/pip-build-env-wggwsz_m/overlay --no-warn-script-location --no-binary :none: --only-binary :none: -i https://pypi.org/simple -- 'cython >= 0.29' 'numpy==1.14.5; python_version<'"'"'3.7'"'"'' 'numpy==1.16.0; python_version>='"'"'3.7'"'"'' setuptools setuptools_scm wheel
       cwd: None
  Complete output (3410 lines):
  Ignoring numpy: markers 'python_version < "3.7"' don't match your environment
```
So the failed build is due to the base image not being compatible with the version listed in the requirements.txt file. In our Dockerfile we listed the base image as python:3 which means that docker will pull the latest version of python for our image which is 3.9 at the time of writting. There are two ways to solve the problem:
* 1. if the specific version doesn't matter you can change from streamlit==0.72.0 to streamlit. which will download the latest version of streamlit for the image.
* 2. use the appropriate base image version for our app.

We will use option 2. Since the current version of python we are using is 3.8.5 we will use 3.8-slim. <span style="color:red">Please, confirm what version of the base image you need.</span>
```
# base image
FROM python:3.8-slim
# metadata info
{...}
```
Running the build command again:
```
docker build -t streamlit:beta-pre-prod .
```
If the build is successfull we should see the following images: 
```
#docker images
REPOSITORY                   TAG                 IMAGE ID            CREATED             SIZE
streamlit                    beta-pre-prod       5512b0cff92c        11 seconds ago      516MB
python                       3.8-slim            2be36bcc692b        5 days ago          113MB
```
Along with the container image we created we see the base image we used to build our container. The next time we build a new version of our image, using the same base image, the process will be much faster since docker will have access to it locally. To run a container from an image we use the run command.
```
# -d to run the container in detached mode otherwise the CLI is used
# -p how we configure the container port{localportFromLocalMachine:theContainerExposedPort}
# --name is self-explanatory
docker run --name personal-website -d -p 3000:8051 streamlit:beta-pre-prod 
```
You should see a single alphanumeral string output that will confirm that the container has been created successfully. 
```
#in our case
03dd6ad6a5edbd894d0c1fb83b2e6e8f4a912d1cff9485d15c4b302603147f50
```
if you forgot -d and do not want to open a new terminal window you can reopen the port.
```
# first exit the terminal
# check the port user
sudo lsof -i :{port of the container}
# terminate it
sudo kill -9 {PID}
```
To confirm that the container is running we run the following command:
```
# command
Docker ps
# output
CONTAINER ID        IMAGE                     COMMAND                  CREATED             STATUS              PORTS                    NAMES
03dd6ad6a5ed        streamlit:beta-pre-prod   "/bin/sh -c 'streaml…"   52 seconds ago      Up 51 seconds       0.0.0.0:3000->8051/tcp   personal-website
```
If the container has encountered an error it will not show in docker ps which is why you need to use the -a option which show all containers. From then on, we will need to access the container logs to investigate the cause of the error.
```
docker logs {container id/name}
```
It so happens that in the current image configuration we cannot access the website using the standard localhost:3000 even with streamlit default port exposed. We can access it by checking the logs.
```
(NNScraper) henri@Vanderscycle:~/Documents/Post Lighthouse-Lab work/DockerKubernetes/streamlitWebsite$ docker logs personal-website 

  You can now view your Streamlit app in your browser.

  Network URL: http://172.17.0.2:8501
  External URL: http://107.190.20.126:8501
```
Using the Network URL we can access the website which should give you something similar to this:
![hello website](./images/res.png)
### A better Dockerfile
With the current configuration we have to check the log files everytime we want to access the container, but this is awkward and not the way a container was meant to be accesssed. We can remedy this by altering the dockerfile so that we can pass the desired port at the moment of the container creation. 
```
{...}
CMD streamlit run ./src/app.py --server.port $PORT
```
We build the image again. You can use a different tag if you'd like.
```
docker build -t streamlit:beta-pre-prod .
```
Do not forget to remove the previous container.
```
docker run --name personal-website -d -p 5000:8000 -e PORT=8000 streamlit:beta-pre-prod 
```
After confirming that everything is working you can access the website at localhost:5000
![hello website](./images/res2.png)
## Usefull commands
Remove every containers regardless whether it is running of not:
```
# -f is for force
# -q is for quiet which only output the CONTAINER ID
docker rm -f $(docker ps -aq)
# if you only want to remove stopped containers
docker rm $(docker ps -aq)
```
removing all none images which have been superseeded by newer version.
```
# the -f in docker images is for filter not force.
docker rmi -f  $(docker images -f "dangling=true" -q)
```
## Saving to docker hub
The first step is to create a repository on Docker hub and create a repository. This is done similarly to how you create a repo on Github. You this example, we named our repo: website-walkthrough.
![empty  docker repo](./images/emptyrepo.png)
The second step is to tag the image, we want to upload, to the format given our repo.
```
docker tag streamlit:beta-pre-prod  vandercycle/website-walkthrough:latest
```
We should see the following images in the repo. I removed all none images.
```
REPOSITORY                        TAG                 IMAGE ID            CREATED             SIZE
vandercycle/website-walkthrough   latest              83d55f6269df        About an hour ago   516MB
streamlit                         beta-pre-prod       83d55f6269df        About an hour ago   516MB
python                            3.8-slim            2be36bcc692b        6 days ago          113MB
```
We are ready to push to the repo.
```
docker push vandercycle/website-walkthrough:latest
```
You should see the following on your repo.
![first push repo img](./images/firstpushrepo.png)
Pulling from any repo is as easy as our first container pull with hello world.
## Example
You can access my dockerized [website](https://hub.docker.com/repository/docker/vandercycle/streamlit-repo) on docker hub.
## Additional ressources and reading
* [Docker up & running](https://github.com/gary136/ebook/blob/master/Docker%20Up%20and%20Running.pdf)
* [Docker and Kubernetes tutorial (amigoscode and TechWorld with Nana)](https://www.youtube.com/watch?v=bhBSlnQcq2k)


## Closing statement

I am a student and future professional who is keen on learning, If you have any questions, or would like to point out any inaccuracies please email me.

Thank you for reading.

[Henri Vandersleyen P.Eng](hvandersleyen@gmail.com)

Future Data Engineer
