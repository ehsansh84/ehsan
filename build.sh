docker build -t ehsan .
docker stop ehsan && true
docker rm ehsan && true
#docker rmi ehsan
docker run --name ehsan -p 8100:8080 -d --restart always --network dockers_default -e MONGO=mongodb  ehsan
