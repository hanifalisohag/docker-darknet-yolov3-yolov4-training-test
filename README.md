# Docker Darknet YOLOv3 YOLOv4 Training and Test (With GPU CUDA support on Linux)

### Build it
```
$ docker build -t docker-darknet_yolo:latest .
```

### Run it

#### without X-server
```
$ docker run -it --gpus all docker-darknet_yolo:latest
```
#### with X-server
```
$ docker run -it --gpus all --net host -e DISPLAY=$DISPLAY -v $HOME/.Xauthority:/root/.Xauthority docker-darknet_yolo:latest
```


### Test it
####YOLOv4
```
$ ./darknet detector test ./cfg/coco.data ./cfg/yolov4.cfg yolov4.weights data/dog.jpg -dont_show
```
####YOLOv3
```
$ ./darknet detector test ./cfg/coco.data ./cfg/yolov3.cfg yolov3.weights data/dog.jpg -dont_show
```

## For training:
  
### On the host machine
1. Clone the repository 
```
$ git clone https://github.com/hanifalisohag/docker-darknet-yolov3-yolov4-training-test.git
```
2. Put all your custom ".jpg" and ".txt" annotations on this folder : `/dataset/data/obj`

3. Generate the **val.txt** and **train.txt** on the **/dataset/data** folder 
``` 
$ cd dataset
$ python train_test_split.py
OR
$ python3 train_test_split.py
```
4. Please change the **yolo-obj.cfg**, **obj.data** and **yolo-obj.names** file according to your custom class numbers and ***YOLOv3 and YOLOv4***. This repo has been configured of **6 classes** for **YOLOv3**
5. The full **dataset** direcotry structures should look like below-
```
├── data
│   ├── obj
│   │   ├── 000000000036.jpg
│   │   ├── 000000000036.txt
│   │   ├── 000000581921.jpg
│   │   ├── 000000581921.txt
│   │   └── ................
│   ├── train.txt
│   ├── val.txt
│   └── yolo-obj.names
├── obj.data
├── train_test_split.py
└── yolo-obj.cfg
```
## Run the following command to start the training (Manually)
```
$ docker run -it --gpus all --name darknet_training\
  -v '${PWD}/dataset/data/obj:/darknet/data/obj' \
  -v '${PWD}/dataset/data/val.txt:/darknet/data/val.txt' \
  -v '${PWD}/dataset/data/train.txt:/darknet/data/train.txt' \
  -v '${PWD}/dataset/data/yolo-obj.names:/darknet/data/yolo-obj.names' \
  -v '${PWD}/dataset/obj.data:/darknet/obj.data' \
  -v '${PWD}/dataset/yolo-obj.cfg:/darknet/yolo-obj.cfg' \
  -v '${PWD}/dataset/backup:/darknet/backup' \
  docker-darknet_yolo:latest /bin/bash
  
```  
### Inside the running container (/darknet#):
####YOLOv3
```
./darknet detector train obj.data yolo-obj.cfg darknet53.conv.74 -map -dont_show
```
####YOLOv4
```
./darknet detector train obj.data yolo-obj.cfg yolov4.conv.137 -map -dont_show
```
##Running the container in detached mode:
####YOLOv3
```
$ docker run -it --gpus all --name darknet_training -d\
  -v '${PWD}/dataset/data/obj:/darknet/data/obj' \
  -v '${PWD}/dataset/data/val.txt:/darknet/data/val.txt' \
  -v '${PWD}/dataset/data/train.txt:/darknet/data/train.txt' \
  -v '${PWD}/dataset/data/yolo-obj.names:/darknet/data/yolo-obj.names' \
  -v '${PWD}/dataset/obj.data:/darknet/obj.data' \
  -v '${PWD}/dataset/yolo-obj.cfg:/darknet/yolo-obj.cfg' \
  -v '${PWD}/dataset/backup:/darknet/backup' \
  docker-darknet_yolo:latest ./darknet detector train obj.data yolo-obj.cfg darknet53.conv.74 -map -dont_show
```

####YOLOv4
```
$ docker run -it --gpus all --name darknet_training -d\
  -v '${PWD}/dataset/data/obj:/darknet/data/obj' \
  -v '${PWD}/dataset/data/val.txt:/darknet/data/val.txt' \
  -v '${PWD}/dataset/data/train.txt:/darknet/data/train.txt' \
  -v '${PWD}/dataset/data/yolo-obj.names:/darknet/data/yolo-obj.names' \
  -v '${PWD}/dataset/obj.data:/darknet/obj.data' \
  -v '${PWD}/dataset/yolo-obj.cfg:/darknet/yolo-obj.cfg' \
  -v '${PWD}/dataset/backup:/darknet/backup' \
  docker-darknet_yolo:latest ./darknet detector train obj.data yolo-obj.cfg yolov4.conv.137 -map -dont_show
```

### To attach to the container
```
$docker attach --detach-keys="ctrl-a,x" darknet_training
```
In order to get out of the container without exiting it **press** `CTRL+A` then **press** `X`. It will get the user out of the running container.

### To delete that container 
```
$ docker rm -f darknet_training
```
