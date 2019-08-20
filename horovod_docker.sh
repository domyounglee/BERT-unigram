sudo docker run -u 0 --net=host \
 -v /home/user01/gyun/:/root/workspace/ \
 -v "$HOME/.Xauthority:/root/.Xauthority:rw" \
 -v /tmp/.X11-unix:/tmp/.X11-unix \
 -it -p 8891:8891 -e DISPLAY=$DISPLAY \
 horovod-py3-tensor1.12.0 \
 /bin/bash
