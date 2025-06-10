## Run MySQL and ubuntu code python 

docker network create my_network


docker rm -f custom_mysql && 
docker run -d --name custom_mysql --network my_network  -e MYSQL_ROOT_PASSWORD=rootpassword123 -e MYSQL_DATABASE=cv  -e MYSQL_USER=user_cv -e MYSQL_PASSWORD=userpass123  -p 3306:3306  lamianguyen99/my_custom_mysql8:v2

docker run -it --rm   --name ubuntu_client   --network my_network  -p 8501:8501   lamianguyen99/my_custom_ubuntu:v2   bash


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