docker rm -f timeless-hello-world 
docker build . -t="timeless-hello-world"
docker run -d -p 3000:3000 --name timeless-hello-world timeless-hello-world

# 