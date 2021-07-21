Quick refresher on docker

start command (assuming you have the image)

sudo docker run -it -v mongodata:/data/db --name mongodb -d mongo
-v (volume) with local data being stored in mongodata
if you want to bind a port add -p {local port}:{container port} (you can bind an ip:port address to a container port as well)
