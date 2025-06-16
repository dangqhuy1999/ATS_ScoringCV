## Run MySQL and ubuntu code python 

docker network create my_network


docker rm -f custom_mysql && 
docker run -d --name custom_mysql --network my_network  -e MYSQL_ROOT_PASSWORD=rootpassword123 -e MYSQL_DATABASE=cv  -e MYSQL_USER=user_cv -e MYSQL_PASSWORD=userpass123  -p 3306:3306  lamianguyen99/my_custom_mysql8:v2

docker run -it --rm   --name ubuntu_client   --network my_network  -p 8501:8501   lamianguyen99/my_custom_ubuntu:v2   bash


## After that , run code with 

```python
pip install -r requirements.txt

streamlit run App (1).py

```

## ERROR note:

### **Error 1(Windows):**

`docker: Error response from daemon: Conflict. The container name "/custom_mysql" is already in use by container "435988aa01c5189d2fb5308f5c5e40a716dd505b93cbee8ce0d82ba373c2e745". You have to remove (or rename) that container to be able to reuse that name.`

**Solve:**  
	
  **docker rm -f custom_mysql**

### **Error 2(Windows):**

`docker: Error response from daemon: Ports are not available: exposing port TCP 0.0.0.0:3306 -> 127.0.0.1:0: listen tcp 0.0.0.0:3306: bind: Only one usage of each socket address (protocol/network address/port) is normally permitted.
`

**Solve:**  
	
```

netstat -aon | findstr :3306
tasklist /FI "PID eq <PID>"
sc query type= service state= all | findstr /I "mysql"
net stop MySQL80
```


## Commit docker

Bạn có container tên là `ubuntu_client`, sau khi cài xong Python, spaCy, v.v., bạn muốn lưu lại thành image mới:

```
docker commit ubuntu_client lamianguyen99/my_custom_ubuntu:v4
docker images

```

## Xoa Docker images

```
docker images
docker rmi -f lamianguyen99/my_custom_ubuntu:v2

```

## Push docker images

```
## Login Docker Hub
docker login
docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
## Đổi tag
docker tag lamianguyen99/my_custom_ubuntu:v3 lamianguyen99/my_custom_ubuntu:latest 
or
docker tag lamianguyen99/my_custom_ubuntu:v3 lamianguyen99/my_custom_ubuntu:v4
## Push images
docker push lamianguyen99/my_custom_ubuntu:v3

```

## Clear Docker Overlay Linux
Không nên dùng `docker system prune -a --volumes` trừ khi em chắc chắn các volume/image không còn cần nữa.

Thay vào đó, chỉ dùng:

```
## PreCheck 

docker volume ls
docker image ls
docker system df -v

## Clear not use

docker container prune
docker image prune
docker volume prune
docker network prune

```

